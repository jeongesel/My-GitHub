import os
import json
import time
from openai import OpenAI
from dotenv import load_dotenv
from collection import OrderedDict

def callchat(message):
  load_dotenv()
  client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
  )
  #스레드 생성, 연결(runs)
  run = client.beta.threads.create_and_run(
  assistant_id="asst_FPg6Rlt9WKrgjROV07Du4joO",
  thread=(
  "messages":[
  {"rloe":"user", "content":message},
    ]
    }
  )
  #5초대기
