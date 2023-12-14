import os
import asyncio
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['OPENAI_API_KEY']


async def callchat(message):
  async with openai.AsyncClient(api_key=api_key) as client:
    assistant_id="asst_FPg6Rlt9WKrgjROV07Du4joO",
    thread={
    "messages":[
    {"role":"user","content":message},
    ]
    }
    )


await asyncio.sleep(5)

run_steps = await client.beta.threads.runs.steps.list(
  thread_id=run.thread_id,
