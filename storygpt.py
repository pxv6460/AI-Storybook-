from openai import OpenAI
import re
import json
import matplotlib.pyplot as plt
import requests
from PIL import Image
from io import BytesIO

class StoryGPT:
    def __init__(self, api_key, project_id, vibes):
        self.client = OpenAI(
            api_key=api_key,
            project=project_id,
        )
        self.vibes = vibes
        self.messages = []
        self.verbose = False

    def create_story(self, verbose=False):
        self.verbose = verbose

        print("Generating Story")
        scenes = self.generate_scenes()

        print("Generating Image Prompts")
        image_prompts = self.generate_image_prompts()

        print("Generating Images")
        image_urls = self.generate_images(image_prompts)

        self.show_images(image_urls, scenes)

    def generate_scenes(self):
        self.messages.append({
            "role": "user",
            "content": f"Please generate a children's story. Make sure the story is no more than 300 words. Give your output in plain text, without markdown. Add markers in the LLM’s output to indicate scene transitions (e.g., Scene 1:, Scene 2:). The story should include: {json.dumps(self.vibes)}"
        })

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a creative writer of children's stories. You write succinctly. You write stories that have clear scenes, and vivid imagery that can pair easily with drawings/ illustrations."
                },
                self.messages[0]
            ]
        )
        story = completion.choices[0].message.content

        if self.verbose:
            print("\n-------STORY GENERATED-------\n")
            print(story)
            print("\n-----------------------------\n")

        self.messages.append({
            "role": "assistant",
            "content": [{ "type": "text", "text": story }]
        })

        pattern = r"Scene \d+:"
        scenes = re.split(pattern, story)
        scenes = [scene.replace("\n", "") for scene in scenes]
        scenes = [scene.replace(":", "") for scene in scenes]
        scenes = [scene.replace("*", "") for scene in scenes]
        scenes = [s for s in scenes if s]
        
        return scenes

    def generate_image_prompts(self):
        self.messages.append({
            "role": "user",
            "content": [{ "type": "text", "text": "Create seperate DALL-E image generation prompts for every scene. Describe the characters without using their names and the the character description to every prompt." }]
        })

        if self.verbose:
            print("\n-------MESSAGES SO FAR-------\n")
            print(json.dumps(self.messages, indent=4))
            print("\n-----------------------------\n")

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages
        )

        image_prompts = completion.choices[0].message.content

        if self.verbose:
            print("\n-------IMAGE PROMPTS GENERATED-------\n")
            print(image_prompts)
            print("\n-------------------------------------\n")

        self.messages.append({
            "role": "assistant",
            "content": [{ "type": "text", "text": image_prompts }]
        })

        self.messages.append({
            "role": "user",
            "content": [{ "type": "text", "text": "Give me a shared description that I can include in the prompts so that the settings and characters remain the same." }]
        })

        if self.verbose:
            print("\n-------MESSAGES SO FAR-------\n")
            print(json.dumps(self.messages, indent=4))
            print("\n-----------------------------\n")

        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages
        )

        shared_prompt = completion.choices[0].message.content

        if self.verbose:
            print("\n-------SHARED IMAGE PROMPT-------\n")
            print(shared_prompt)
            print("\n---------------------------------\n")

        pattern = r"Scene \d+"
        prompts = re.split(pattern, image_prompts)
        prompts = [prompt.replace("\n", "") for prompt in prompts]
        prompts = [prompt.replace(":", "") for prompt in prompts]
        prompts = [prompt.replace("*", "") for prompt in prompts]
        prompts = [s for s in prompts if len(s) > 10]

        if self.verbose:
            print(f"\n-------IMAGE PROMPTS-------\n")
            for prompt in prompts:
                print(prompt)
            print("\n---------------------------\n")

        return {"shared_prompt": shared_prompt, "prompts": prompts}

    def generate_images(self, image_prompts):
        image_urls = []
        for i in range(len(image_prompts["prompts"])): 
            response = self.client.images.generate(
                model="dall-e-3",
                prompt="Make sure no text is in the image. Generate the image in the art style of a cartoon. " + image_prompts["shared_prompt"] + image_prompts["prompts"][i],
                quality="standard",
                n=1,
                size="1024x1024"
            )
            image_url = response.data[0].url
            image_urls.append(image_url)

            if self.verbose:
                print(f"\n-------IMAGE URL {i+1}-------\n")
                print(image_url)
                print("\n-----------------------\n")
        
        return image_urls

    def show_images(self, image_urls, scenes):
        fig, axes = plt.subplots(len(image_urls), 1, figsize=(5, len(image_urls) * 5))
        # Loop through the images and display them on the grid
        for i, ax in enumerate(axes.flat):
            image_response = requests.get(image_urls[i])
            img = Image.open(BytesIO(image_response.content))
            ax.imshow(img)
            ax.axis("off")
            ax.set_xlabel(scenes[i], fontsize=12, color="black", labelpad=10)
                
        plt.show()