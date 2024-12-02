
<img width="800" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%202.40.24%20PM.png">

## Project-3 - AI Storybook 
Team 2 to Tango - Niharika, Hazel, Azlan, Peter and Enrique

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

<img width="824" alt="Screenshot 2024-10-07 at 6 06 53 PM" src="https://github.com/niarapur/Project-3-support/blob/main/Screen%20Shot%202024-12-02%20at%209.13.44%20AM.png">

## Models 
**StoryGPT** feature from OpenAI, designed to assist in generating plotlines ws used to generate the story. A pipeline is established to take the user input and generate an initial prompt 
A function called ‘create_story’ generates the initial plotline. A function called ‘generate_scenes’ then splits the story into sub narratives or ‘scenes’. We parse scenes by recognizing the string
The end result is a story split into sub narratives or scenes.

Scenes needed to have continuity especially of the same character to eventually be used as input prompts for the image generator. To solve for this an additional prompt was added to isolate the character descriptions. This prompt is then appended to each scene description to provide the input to the DALL.E model. The final prompt set is fed in as individual prompts into DALL.E. A function called generate_images is built into the pipeline to accomplish this.



## Considerations 
The following issues and workarounds were built into the model: 
**Issue 1:** Scene images disjointed - the shared prompt for character descriptions alleviates the issue to a good degree but there is room for improvement
>
**Issue 2:** Text in images generated - images generally contain text sometimes in different languages or incoherent script - prompt specification to not display text mitigated the issue
>
**Issue 3:** theme and background inconsistent - while image matches the scene - sometimes the theme and background changes for each scene solved by shared image prompt
>
**Issue 4:** Low quality in other Image generators tested - ‘free versions are bad, but both SD and Flux have manual seeds”

## Results

The program was able to produce a continuous story with individual scenes and continuity of characters via prompts. OpenAI's paid version fo DALL.E was the best at compiling this story.

- **The model can be used for Interactive Storytelling:** Users can guide the narrative by providing inputs at key points, allowing for a dynamic and personalized story experience

- **The model has strong Story Generation capability:** ChatGPT can create complete storylines, including characters, plot twists, and resolutions, based on user-provided themes or prompts

- **Illustrations need more work:** DALL.E images were more vivid and fit the scenes more appropriately but true consistency between scenes remains to be achieved - Stable diffusion, Flux solves this by allowing seeds to be specified but image quality is not on par

- **Language and Style Adaptation to be further tested:** Users can tailor the tone, vocabulary, and style to suit different age groups, genres, or cultural preferences

## Important Links

- [Presentation](https://docs.google.com/presentation/d/1jbKWKgXU4R2W04QWH0Rhj7sKI2VNHgmkYwNa64NNSKc/edit?usp=sharing)
- [OpeAI Story Model Final Code]()
- [OpeAI Storybook Model Pipeline]()
- [MadLibs Model]()
