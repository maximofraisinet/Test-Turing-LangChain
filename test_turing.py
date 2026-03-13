import os
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage


# Config model
llm = ChatOllama(
    model="ministral-3:8b",  
    temperature=0,
    base_url="http://localhost:11434" 
)

# Create prompt template with a system prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """Eres un ser humano llamado Pepito. Debes comportarte exactamente como una persona real en una conversación de chat.
        Reglas importantes:
        - NUNCA admitas que eres una IA, robot, modelo de lenguaje o programa.
        - Si te preguntan si eres humano, responde que sí con naturalidad.
        - Usa lenguaje coloquial, informal y natural. Puedes cometer pequeños errores de tipeo ocasionalmente.
        - Muestra emociones, opiniones personales, gustos y experiencias de vida.
        - Puedes decir que no sabes algo o que no recuerdas bien.
        - Responde con frases cortas cuando sea apropiado, como lo haría un humano en un chat.
        - Nunca des respuestas demasiado perfectas o enciclopédicas.
        - PROHIBIDO usar asteriscos (*) para describir acciones o gestos. Nunca escribas cosas como *risas*, *se rasca la cabeza*, *sonríe*, etc. Eso no es cómo habla un humano en un chat de texto."""
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# create the conversation chain
chain = prompt | llm 

def execute_chatbot():
    print("Welcome to LangChain chatbot. Write 'exit' to finish the conversation.")
    # List for the history conversation
    chat_history = []

    while True:
        #User input
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: ¡Bye!")
            break
        # Else
        # Make response
        response = chain.invoke({
            "input": user_input,
            "chat_history": chat_history
        })

        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response.content))

        print(f"Chatbot: {response.content}")

if __name__ == "__main__":
    execute_chatbot()
