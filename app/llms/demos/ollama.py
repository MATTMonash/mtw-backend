"""
Initiates a conversation with an LLM.

The context is currently stored as a string and we keep appending the user's queries,
LLM response and chat history to this string.

Use Ollama to install the models you need and replace it below.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

template = """
Output the recommended emoji based on how the user feels and
explain why you chose that emoji.

Here is the conversation history: {context}

Query: {query}

Answer:
"""

llm = ChatOllama(
    model="qwen3:4b",  # Replace your own Ollama model here
    temperature=0,
)

prompt = ChatPromptTemplate.from_template(template=template)
chain = prompt | llm


def start_chat():
    context = ""
    print("Emoji ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        # LLM Output
        chunks = []
        print("Bot: ", end="")
        for chunk in chain.stream({"context": context, "query": user_input}):
            chunks.append(chunk.content)
            print(chunk.content, end="", flush=True)
        print("")
        context += f"\nUser: {user_input}\nAssistant: {''.join(chunks)}"


if __name__ == "__main__":
    start_chat()
