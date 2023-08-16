from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import openai
openai.api_key = "Mettez votre clé d'api ici"
app = FastAPI()
conversation_history = []
def get_completion(question,conversation_history, model="gpt-3.5-turbo"):
    cursus="Mettez le texte de référence ici"
    message_base = {"role": "system", "content": "Vous êtes un chatbot sur Achraf, vous donnerez des infos que sur Achraf en se basant sur un texte "}
    message_assistant={"role":"assistant","content": " Le texte aprés les deux points d'explication est le cursus d'Achraf Louzali : "+ cursus}
    messages=[message_base,message_assistant]
    if len(conversation_history)>0:
        for x in conversation_history:
            messages.append(x)
    message_question = {"role": "user", "content": question}
    messages.append(message_question)
    response = openai.ChatCompletion.create(model=model,messages=messages,temperature=0)
    return response.choices[0].message["content"]
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/ask_achraf/")
def modify_text(text: str = Form(...)):
    global conversation_history
    conversation_history.append({"role": "user", "content": text})
    
    modified_text = get_completion(text, conversation_history)
    
    conversation_history.append({"role": "assistant", "content": modified_text})
    return {"modified_text": modified_text}

@app.get("/", response_class=HTMLResponse)
def get_html():
    with open("index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)