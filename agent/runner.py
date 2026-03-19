import os
from dotenv import load_dotenv
from smolagents import CodeAgent, LiteLLMModel
from smolagents import DuckDuckGoSearchTool
from agent.tools import run_python, calculate

load_dotenv()

def build_agent():
    """Build and return a smolagents CodeAgent powered by Groq via LiteLLM."""
    model = LiteLLMModel(
        model_id="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )

    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool(), run_python, calculate],
        model=model,
        max_steps=7,
        additional_authorized_imports=["requests", "bs4", "json", "urllib"]
    )
    return agent

def run_task(task: str) -> str:
    """Run a single task through the agent and return the result."""
    agent = build_agent()
    try:
        result = agent.run(task)
        return str(result)
    except Exception as e:
        return f"Agent error: {str(e)}"