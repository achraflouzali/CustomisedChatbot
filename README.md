# CustomisedChatbot
Creating a customised chatbot based on a text
## 1) Installation of main packages

```bash
pip install openai
pip install fastapi

```

## 2) Communication avec l'api d'OpenAI
To create the chatbot we need to communicate with the OpenAI api through a key.
```bash
import openai
openai.api_key = "Put your open ai key here"
```
# 3) Build
To build an efficient chatbot, your text should be precise, structured and informative. Then you should make clear the tasks that the customised chatbot should do.
    
```python
  message_base = {"role": "system", "content": "Vous êtes un chatbot sur Achraf, vous donnerez des infos que sur Achraf en se basant sur un texte "}
  message_assistant={"role":"assistant","content": " Le texte aprés les deux points d'explication est le cursus d'Achraf Louzali : "+ cursus}
```
Then to build a conversational chatbot, you should show the conversational history to the model so it can know the context. The conversational history will be structured like this: 

```python
  user_question={"role": "user", "content": question}
  chatbot_response={"role": "assistant", "content": answer}
  conversation_history+=[user_question,chatbot_response]
```
This application relies on an api coded with FastAPI and the page is coded with HTML/JavaScript. And the result is displayed like this 
