from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import PromptTemplate
import os

os.environ["GOOGLE_API_KEY"] = "your_api_key"

# Define the response schema
response_schemas = [
    ResponseSchema(name="title", description="The title of the book"),
    ResponseSchema(name="author", description="The author of the book"),
    ResponseSchema(name="year", description="The year the book was published"),
    ResponseSchema(name="genres", description="List of genres the book belongs to", type="list"),
    ResponseSchema(name="summary", description="A brief summary of the book")
]

# Initialize the parser
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Get format instructions
format_instructions = parser.get_format_instructions()

# Create a prompt
prompt = PromptTemplate(
    template="Provide information about this book: {book_title}.\n{format_instructions}",
    input_variables=["book_title"],
    partial_variables={"format_instructions": format_instructions}
)

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=0.4)

# Prepare the query
book_title = "Dune"
_input = prompt.format(book_title=book_title)

# Get and parse output
output = model.invoke(_input)
parsed_result = parser.parse(output.content)

print(f"Book Information for '{parsed_result['title']}':")
print(f"Author: {parsed_result['author']}")
print(f"Year: {parsed_result['year']}")
print(f"Genres: {', '.join(parsed_result['genres'])}")
print(f"Summary: {parsed_result['summary']}")