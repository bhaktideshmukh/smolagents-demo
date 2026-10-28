import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool
from tools import get_word_count

load_dotenv()  # loads HF_TOKEN from .env

model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), get_word_count],
    model=model,
    max_steps=6,
)

if __name__ == "__main__":
    task = input("Enter your task: ")
    print(agent.run(task))