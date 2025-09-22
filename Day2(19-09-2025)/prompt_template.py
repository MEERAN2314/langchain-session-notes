from langchain.prompts import PromptTemplate

# Create a template
template = "What are 3 advantages of using {technology} in {field}?"

# Define a PromptTemplate
prompt = PromptTemplate(
    input_variables=["technology", "field"],
    template=template
)

# Format with actual inputs
formatted_prompt = prompt.format(technology="AI", field="healthcare")
print(formatted_prompt)