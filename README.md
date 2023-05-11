# my-gpt
code demonstrates how to run nomic-ai gpt4all locally

## Introduction
This code demonstrates how to use the nomic-ai/gpt4all-j model from the Hugging Face transformers library to generate text-based responses to user input in a conversational manner. The program takes user input, passes it to the model, generates a response, and returns it to the user. This process is repeated until the user inputs "bye" or "exit" to end the conversation.

## Installation and Setup
To run this code using Poetry, you will need to have Poetry installed on your system along with Python 3. You can install Poetry by following the instructions in the official [Poetry documentation](https://python-poetry.org/docs/).

- Clone this repository: `git clone git@github.com:Avinava/my-gpt.git`
- Navigate to the project directory: `cd my-gpt`
- Install the required packages using Poetry: `poetry install`
  - Note: When you run for the first time, it might take a while to start, since it's going to download the models locally. The models used in this code are quite large, around 12GB in total, so the download time will depend on the speed of your internet connection.
  - Note: The performance of the code also depends on the machine you are running it on. Running it on a machine with better CPU and more RAM will result in faster response times.

## Running the Program
To run the program, simply execute the following command in a terminal or command prompt from the project directory:
```bash
poetry run python index.py
```

Once the program is running, it will prompt you to enter a message:
```bash
Welcome to 🤖 my-gpt-bot
You can exit the chatbot at any time by typing 'bye' or 'exit'

🤖 ask my-gpt-bot:
```
You can type your message and press enter to see the chatbot's response. To end the conversation, simply type "bye" or "exit".


<img width="858" alt="Screenshot 2023-05-11 at 7 24 58 PM" src="https://github.com/Avinava/my-gpt/assets/1398711/51255bc3-f4cb-4082-8b5f-cc3299fe5bc4">

