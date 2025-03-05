# Create a tool-calling agent
from smolagents import ToolCallingAgent, tool, HfApiModel

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

@tool
def custom_tool(input: str) -> str:
    return "custom output"

agent = ToolCallingAgent(
    # Add configuration here
  tools=[custom_tool], model=model,
  max_steps=10, name="tool-calling-agent", description="run tools based on input and generate an output"
)