import asyncio
import os
from browser_use import Agent
from browser_use.llm import ChatGroq

async def main():
    os.environ["ANONYMIZED_TELEMETRY"] = "false"
    os.environ["BROWSER_USE_CLOUD_SYNC"] = "false"
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=ChatGroq(model="gpt-4o"),
    )
    await agent.run()

asyncio.run(main())