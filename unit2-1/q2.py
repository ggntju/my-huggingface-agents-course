# Create web agent and manager agent structure

from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, ToolCallingAgent, VisitWebpageTool

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), VisitWebpageTool()],           # Add required tools
    model=model,         # Add model
    max_steps=10,        # Adjust steps
    name="web-agent",           # Add name
    description="do web related work for me"      # Add description
)

manager_agent = CodeAgent(
  model=HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct"),
  managed_agents=[web_agent],
  additional_authorized_imports = ["time", "numpy", "pandas"]
)