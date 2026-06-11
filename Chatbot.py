import streamlit as st
import requests
st.header("ChatBot")
def Chat_Ai(User_Chat):
  api_url="https://openrouter.ai/api/v1/chat/completions"
  api_key=st.secrets["ChatBot"]
  headers={
       "Authorization":f"Bearer {api_key}",
       "Content-Type":"application/json"
  }
  payload={
      "model":"openrouter/free",
      "messages":[{"role":"system","content":"You are the user friend you chat with him like a real friend"},
                  {"role":"user","content":User_Chat}]
  }
  response=requests.post(api_url,headers=headers,json=payload)
  result=response.json()
  if "choices" in result:
    return result["choices"][0]["message"]["content"]
User_Chat=st.chat_input("Chat with your friend")
if User_Chat is not None:
  with st.chat_message("user"):
    st.markdown(User_Chat)
  with st.spinner("Replying"):
    answer=Chat_Ai(User_Chat)
    with st.chat_message("Assistant"):
      st.markdown(answer)
    
