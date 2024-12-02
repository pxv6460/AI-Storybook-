
<img width="1500" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%203.46.31%20PM.png">

## Project-3 - AI Storytelling
Team 2 to Tango - Azlan, Peter, Hazel, Niharika and Enrique

## Introduction
**Our model empowers users to craft personalized stories by providing input on characters, plot, and theme** - Using advanced AI tools like ChatGPT- we currently limited the model to generate children's storybooks
- **But what’s a storybook without captivating visuals?** To bring these tales to life, we leveraged LLMs (OpenAI ChatGPT,DALL.E, Gemini Stable Diffusion,Flux)to create vivid illustrations for each part of the story
- **The result?** An integrated, AI-generated illustrated storybook — where every sub-narrative is paired with its unique visual sequence

## User Input
3 elements are being requested, we call them ‘vibes’ :
- Characters - general description or names 
- Genre - e.g. kids story, sci fi, superhero
- Theme - fairytale, adventure, moral etc.
Entering these basic elements would help create a prompt that is the starting point for the story. The input is entered in a UI generated using Gradio

<img width="600" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%203.20.11%20PM.png">

## Models 
**StoryGPT feature from OpenAI**, designed to assist in generating plotlines ws used to generate the story. A pipeline is established to take the user input and generate an initial prompt 
- A function called ‘create_story’ generates the initial plotline
- A function called ‘generate_scenes’ then splits the story into sub narratives or ‘scenes’
We parse scenes by recognizing the string. The end result is a story split into sub narratives or scenes.

### Prompt 1: Story Generation
<img width="600" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%202.52.07%20PM.png">

### Prompt 2: Split Story into Scenes

<img width="600" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%202.52.07%20PM.png">

Scenes needed to have continuity especially of the same character to eventually be used as input prompts for the image generator. To solve for this an additional prompt was added to isolate the character descriptions. This prompt is then appended to each scene description to provide the input to the DALL.E model. The final prompt set is fed in as individual prompts into DALL.E. A function called generate_images is built into the pipeline to accomplish this.

<img width="600" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%203.23.36%20PM.png">


## Using an Image Generator
**DALL.E** was used to generate the final set of images based on the individual prompts

<img width="600" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%203.27.47%20PM.png">


## Considerations 
The following issues and workarounds were built into the model: 
>
- **Issue 1:** Scene images disjointed - the shared prompt for character descriptions alleviates the issue to a good degree but there is room for improvement
- **Issue 2:** Text in images generated - images generally contain text sometimes in different languages or incoherent script - prompt specification to not display text mitigated the issue
- **Issue 3:** theme and background inconsistent - while image matches the scene - sometimes the theme and background changes for each scene solved by shared image prompt
- **Issue 4:** Low quality in other Image generators tested - ‘free’ versions are bad, but offer additional features like inserting manual seeds to control uniform character images (**Stable Diffusion and Flux tested here- see code for 'MAdLibs Version in link below for additional details**)

## Results

The program was able to produce a continuous story with individual scenes and continuity of characters via prompts. OpenAI's paid version fo DALL.E was the best at compiling this story.

### Sample Story and Scenes

<img width="600" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%203.12.54%20PM.png">


### Sample Final Output

<img width="700" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%203.15.21%20PM.png">


- **The model can be used for Interactive Storytelling:** Users can guide the narrative by providing inputs at key points, allowing for a dynamic and personalized story experience

- **The model has strong Story Generation capability:** ChatGPT can create complete storylines, including characters, plot twists, and resolutions, based on user-provided themes or prompts

- **Illustrations need more work:** DALL.E images were more vivid and fit the scenes more appropriately but true consistency between scenes remains to be achieved - Stable diffusion, Flux solves this by allowing seeds to be specified but image quality is not on par

- **Language and Style Adaptation to be further tested:** Users can tailor the tone, vocabulary, and style to suit different age groups, genres, or cultural preferences

## Important Links

- [Presentation](https://docs.google.com/presentation/d/1jbKWKgXU4R2W04QWH0Rhj7sKI2VNHgmkYwNa64NNSKc/edit?usp=sharing)
- [OpeAI Story Model Final Code](https://github.com/pxv6460/AI-Storybook-/blob/main/openai.ipynb)
- [OpeAI Storybook Model Pipeline](https://github.com/pxv6460/AI-Storybook-/blob/main/storygpt.py)
- [MadLibs Model](https://github.com/pxv6460/AI-Storybook-/blob/main/storybook.ipynb)
- Cover Image References - [The art and magic of storytelling](https://pxpfoto.com/storytelling/)
