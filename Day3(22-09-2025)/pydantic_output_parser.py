from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field
import os

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = "Your_api_key"

# Define your desired data structure
class ProgrammingLanguage(BaseModel):
    name: str = Field(description="The name of the programming language")
    year_created: int = Field(description="The year the language was created")
    creator: str = Field(description="The creator(s) of the language")
    paradigm: str = Field(description="The programming paradigm of the language")
    is_compiled: bool = Field(description="Whether the language is compiled")

# Set up a parser
parser = PydanticOutputParser(pydantic_object=ProgrammingLanguage)

# Create a prompt with format instructions
prompt = PromptTemplate(
    template="Provide information about this programming language: {language}.\n{format_instructions}\n",
    input_variables=["language"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=0.3)

# Prepare the query
language = "Python"
_input = prompt.format_prompt(language=language)

# Get output and parse it
output = model.invoke(_input.to_string())
parsed_result = parser.parse(output.content)

print(f"Information about {parsed_result.name}:")
print(f"Year created: {parsed_result.year_created}")
print(f"Creator: {parsed_result.creator}")
print(f"Paradigm: {parsed_result.paradigm}")
print(f"Is compiled: {parsed_result.is_compiled}")