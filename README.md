# Productivity App
This is an app that helps you acheieve your goals with llms and python. This app allows a user to input a goal and have an LLM generate a plan for how to achieve the goal.. 

## Running the app 
- To install the necessary dependencies run `pip install fastapi uvicorn python-multipart aiofiles openai` 
- In order to run the app you'll need to insert an OpenAI API key or use your Azure default credentials to power the LLM. 
- You can then run `uvicorn main:app --reload --port 8080` to get the app running on a local server.

## Example of using the app 

![](https://github.com/marlenezw/galaxy_productivity_app/blob/main/goal_example.png)



