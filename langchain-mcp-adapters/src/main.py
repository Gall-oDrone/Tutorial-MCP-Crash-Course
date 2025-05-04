import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters import load_mcp_tools
from langgraph.prebuilt import create_react_agent

llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["/src/servers/math_server.py"]
)
async def main():
    print("Hello world")

if __name__ == "__main__":
    asyncio.run(main())