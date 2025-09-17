import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = GoogleGenerativeAI(model="gemini-1.5-flash-002", google_api_key=gemini_api_key)

# Create a simple prompt
prompt_template = "Write a short story about {topic}"
prompt = PromptTemplate.from_template(prompt_template)

# Create a chain
chain = prompt | llm

# Run the chain
topic = "a cat who wants to be a dog"
story = chain.invoke({"topic": topic})

# Print the output
print(story)
