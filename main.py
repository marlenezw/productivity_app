from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI

from fastapi import Form
import uvicorn

# Initialize your OpenAI API key
openai_api_key = "api_key"
client = OpenAI(api_key=openai_api_key)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", context={"request":request})

@app.post("/", response_class=RedirectResponse)
async def create_plan(request: Request, goal_input: str = Form(...)):

    goal = goal_input

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"I want to achieve the following goal: {goal}. Can you create a simple plan to achieve this? Return the results in HTML format, but do not include the html and body tags."}
        ],
        temperature=0,
    )

    plan = response.choices[0].message.content
    print(plan)
    return templates.TemplateResponse("index.html", context={"request":request, "plan": f"{response.choices[0].message.content}", "goal":goal})



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
