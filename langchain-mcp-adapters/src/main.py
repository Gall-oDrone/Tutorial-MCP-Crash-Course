import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    print("Hello world")

if __name__ == "__main__":
    asyncio.run(main())