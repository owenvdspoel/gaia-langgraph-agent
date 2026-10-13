
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0,
)

response = llm.invoke(
    "What is LangGraph? Answer in one sentence."
)

print("Response:", response.content)
print("Token usage:", response.usage_metadata)
