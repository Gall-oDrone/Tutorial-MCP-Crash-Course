from mcp.server.fastmcp import FastMCP
import subprocess
from typing import Dict, Any, List, Optional

# Create an MCP server
mcp = FastMCP("Terminal Tool Server")

@mcp.tool()
def run_command(command: str) -> Dict[str, Any]:
    """
    Run a terminal command and return its output
    
    Args:
        command: The shell command to execute
        
    Returns:
        Dictionary containing stdout, stderr, and return code
    """
    try:
        # Execute the command and capture output
        process = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30  # Set a timeout to prevent hanging
        )
        
        return {
            "stdout": process.stdout,
            "stderr": process.stderr,
            "return_code": process.returncode
        }
    except subprocess.TimeoutExpired:
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
    mcp.run("stdio")
