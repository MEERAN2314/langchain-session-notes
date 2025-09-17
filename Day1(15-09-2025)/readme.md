# Day1(15-09-2025)

This directory contains the files for Day 1.

## Files

- `prompt.py`: This file generates a short story about a given topic using the Gemini LLM.
    - **Features:**
        - Takes a topic as input.
        - Generates a short story based on the topic.
    - **Concepts Used:**
        - Langchain
        - GoogleGenerativeAI
        - PromptTemplate
        - LLMChain
    - **How to Run:** To run this file, use the following command: `python prompt.py`

- `few_short_prompt.py`: This file generates a short story about a given task using the Gemini LLM with few-shot examples.
    - **Features:**
        - Takes a task as input.
        - Generates a short story based on the task, using few-shot examples to guide the output.
    - **Concepts Used:**
        - Langchain
        - GoogleGenerativeAI
        - PromptTemplate
        - Chain
    - **How to Run:** To run this file, use the following command: `python few_short_prompt.py`

## Instructions

1.  Make sure you have Python installed.
2.  Install the required packages using `pip install -r requirements.txt`.
3.  Set the Gemini API key in the .env file
4.  Run the python files using the commands mentioned above.
