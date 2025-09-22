from langchain.prompts import ChatPromptTemplate

# Create a chat prompt with roles
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "Explain {topic} in simple terms."),
    ("ai", "Sure! Here is a simple explanation of {topic}.")
])

# Fill in values
formatted_chat = chat_prompt.format_messages(topic="machine learning")

# Messages are returned as objects
for msg in formatted_chat:
    print(f"{msg.type.upper()}: {msg.content}")

