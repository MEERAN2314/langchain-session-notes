import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import chain

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = GoogleGenerativeAI(model="gemini-1.5-flash-002", google_api_key=gemini_api_key)

# Example 1: Code Generation Prompt with Few-Shot Examples
prompt_template_code = """
Write a short story about a cat who goes on an adventure:
```
The cat, Whiskers, stepped outside. He walked down the street, past the bakery, and into the park.
```

Write a short story about a dog who learns a new trick:
```
The dog, Buddy, was sitting. His owner said "Dance!". Buddy tilted his head, then stood on his hind legs and started spinning.
```

Write a short story about {task}:
"""
prompt_code = PromptTemplate.from_template(prompt_template_code)
chain_code = prompt_code | llm

# Example Usage
language = "Python"
task = "a robot who falls in love with a human"
code = chain_code.invoke({"language": language, "task": task})
print("Code:", code)
