from fastapi import FastAPI
from .server import mcp
app = FastAPI()


def hello():
    print("Hello world")

def running_mcp_server():
    # Don't run mcp server here to avoid conflicts
    # This should only be done in server.py directly
    pass

@app.get("/")
async def root():
    return "Hello world"