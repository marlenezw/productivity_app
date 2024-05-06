# Productivity App
This is an app that helps you acheieve your goals with llms and python. This app allows a user to input a goal and have an LLM generate a plan for how to achieve the goal..

## Deploy the application with the Azure Developer CLI
Using the Azure Developer CLI, you can deploy the app to Azure Container Instances. Follow these steps to deploy the app:

1) Clone this repository to your local machine.

2) Login to the Azure ising the Azd CLI

```bash
azd auth login
```

3) Create a gpt deployment in Azure OpenAI and get the API key. Once you have all of the credentials needed, create and add them to a `.env` file in the root of the project.

```bash
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_MODEL=""
AZURE_OPENAI_API_VERSION=""
```

4) Deploy the application using the Azure Developer CLI

```bash
azd up
```

5) ⏳ Wait until the deployment has finished and navigate to the URL provided in the output to access the app.

## Running the app locally within a virtual environment
To run this Python app using a virtual environment (venv), follow these steps:

1) Clone this repository to your local machine.

2) Navigate to the directory where your project is located within your terminal.

```bash
cd path/to/your/project
```

3) Create a new virtual environment using the venv module. This will create a new directory named venv (or any name you choose) in your current directory.

```bash
python3 -m venv venv
```

4) Activate the virtual environment. This changes your shell's environment variables so that running Python will get you this environment's Python and pip.

```bash
source .venv/bin/activate
```

5) Install the necessary dependencies using pip. This will install the packages in the virtual environment, isolated from your global Python environment.

```bash
pip install -r requirements.txt
```

6) Create a gpt deployment in Azure OpenAI and get the API key. Once you have all of the credentials needed, create and add them to a `.env` file in the root of the project.

```bash
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_MODEL=""
AZURE_OPENAI_API_VERSION=""
```

7) Run the app using the uvicorn server. This will start the server on port 8080, and you can access the app by navigating to http://localhost:8080 in your browser.

```bash
make run
```

## Example of using the app 

![](https://github.com/marlenezw/galaxy_productivity_app/blob/main/goal_example.png)



