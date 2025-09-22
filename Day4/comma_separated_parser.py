from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
import os

os.environ["GOOGLE_API_KEY"] = "your_api_key"

# Initialize the parser
parser = CommaSeparatedListOutputParser()

# Get format instructions
format_instructions = parser.get_format_instructions()

# Create a prompt
prompt = PromptTemplate(
    template="List {count} {items}.\n{format_instructions}",
    input_variables=["count", "items"],
    partial_variables={"format_instructions": format_instructions}
)

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=0.7)

# Prepare the query
_input = prompt.format(count=5, items="popular JavaScript frameworks")

# Get and parse output
output = model.invoke(_input)
parsed_result = parser.parse(output.content)

print(parsed_result)