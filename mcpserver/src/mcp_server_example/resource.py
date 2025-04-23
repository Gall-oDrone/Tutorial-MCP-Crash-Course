from mcp.server.fastmcp import FastMCP
import os
import asyncio
from pathlib import Path

# Create a resource handler
async def register_resources(mcp: FastMCP):
    """
    Register MCP resources to expose files
    """
    # Get the absolute path to the mcpserver directory
    base_dir = Path(__file__).parent.parent.parent
    readme_path = base_dir / "mcpreadme.md"
    
    @mcp.resource("file:///mcpreadme.md")
    async def get_readme():
        """
        Return the contents of mcpreadme.md file
        """
        try:
            if readme_path.exists():
                # Read file using async
                return await asyncio.to_thread(read_file, readme_path)
            else:
                return f"Error: File not found at {readme_path}"
        except Exception as e:
            return f"Error reading file: {str(e)}"

def read_file(file_path):
    """Helper function to read file contents synchronously"""
    with open(file_path, "r") as f:
        return f.read() 