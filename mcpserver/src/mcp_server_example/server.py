from mcp.server.fastmcp import FastMCP
import subprocess
import asyncio
from typing import Dict, Any, List, Optional
from .resource import register_resources

# Create an MCP server
mcp = FastMCP("Terminal Tool Server")

# Register resources - need to be done at startup
async def setup_server():
    await register_resources(mcp)

# Set up resources asynchronously
asyncio.run(setup_server())

@mcp.tool()
async def run_command(command: str) -> Dict[str, Any]:
    """
    Run a terminal command and return its output
    
    Args:
        command: The shell command to execute
        
    Returns:
        Dictionary containing stdout, stderr, and return code
    """
    try:
        # Execute the command and capture output
        # Use asyncio to run subprocess in a non-blocking way
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            shell=True
        )
        
        # Wait for the process to complete with timeout
        try:
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=30)
            return {
                "stdout": stdout.decode() if stdout else "",
                "stderr": stderr.decode() if stderr else "",
                "return_code": process.returncode
            }
        except asyncio.TimeoutError:
            # Try to terminate the process if it times out
            process.terminate()
            return {
                "stdout": "",
                "stderr": "Command timed out after 30 seconds",
                "return_code": -1
            }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"Error executing command: {str(e)}",
            "return_code": -1
        }

# For running directly
if __name__ == "__main__":
    print("Starting Terminal Tool Server (MCP)...")
    try:
        mcp.run("stdio")
    except Exception as e:
        print(f"Error running MCP server: {e}")
