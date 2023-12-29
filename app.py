# Import necessary modules and functions from FastAPI
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import openai

# Set OpenAI API key (Replace "Mettez votre clé d'api ici" with your actual API key)
openai.api_key = "Mettez votre clé d'api ici"

# Create a FastAPI app
app = FastAPI()

# Define a list to store conversation history
conversation_history = []

# Function to get completion from OpenAI Chat API
def get_completion(question, conversation_history, model="gpt-3.5-turbo"):
    # Placeholder for the text of reference
    cursus = "Mettez le texte de référence ici"
    
    # Base message for the assistant role
    message_base = {"role": "system", "content": "Vous êtes un chatbot sur Achraf, vous donnerez des infos que sur Achraf en se basant sur un texte "}
    
    # Assistant's message including the reference text
    message_assistant = {"role": "assistant", "content": " Le texte aprés les deux points d'explication est le cursus d'Achraf Louzali : " + cursus}
    
    # Combine system message, assistant message, and existing conversation history
    messages = [message_base, message_assistant]
    
    if len(conversation_history) > 0:
        for x in conversation_history:
            messages.append(x)
    
    # User's question message
    message_question = {"role": "user", "content": question}
    messages.append(message_question)
    
    # Call OpenAI Chat API for completion
    response = openai.ChatCompletion.create(model=model, messages=messages, temperature=0)
    
    # Return the completed content from the API response
    return response.choices[0].message["content"]

# Mount a static directory for serving static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define a POST endpoint for handling user input and generating responses
@app.post("/ask_achraf/")
def modify_text(text: str = Form(...)):
    global conversation_history
    
    # Append user's question to conversation history
    conversation_history.append({"role": "user", "content": text})
    
    # Get completion from OpenAI based on the conversation history
    modified_text = get_completion(text, conversation_history)
    
    # Append assistant's response to conversation history
    conversation_history.append({"role": "assistant", "content": modified_text})
    
    # Return the modified text as JSON response
    return {"modified_text": modified_text}

# Define a GET endpoint for serving an HTML page
@app.get("/", response_class=HTMLResponse)
def get_html():
    # Read the content of the index.html file
    with open("index.html", "r") as file:
        html_content = file.read()
    
    # Return the HTML content as a response
    return HTMLResponse(content=html_content)
