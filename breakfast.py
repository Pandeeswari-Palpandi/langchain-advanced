from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

print("openAI is connected!")

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.8)

prompt = """Give me 5 unique breakfast ideas that are healthy and easy to prepare in south TamilNadu.
    Everytime it should be different and unique menu."""

result = llm.invoke(prompt)
print(result.content)
