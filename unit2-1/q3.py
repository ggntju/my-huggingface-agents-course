# Set up secure code execution environment
from smolagents import CodeAgent, E2BSandbox

sandbox = E2BSandbox()

agent = CodeAgent(
    tools=[],
    model=model,
    # Add security configuration
    sandbox=sandbox,
    additional_authorized_imports = ["numpy"]
)