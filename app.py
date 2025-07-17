import streamlit as st
from chat import chat_bot 

st.title("Gemini Chat Bot")

if "messages" not in st.session_state:
    st.session_state.messages = [] 

for message in st.session_state.messages : 
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Typing a Message")
if prompt:

    response = chat_bot(prompt)

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.messages.append({
        "role": "user", "content" : prompt
    })

    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({
            "role": "assistant", "content": prompt
        })

        

    #  with st.chat_message("assistant"):
    #     st.markdown(response) 
    #     st.session_state.messages.append({
    #         "role": "assistant", "content": prompt
    #     }) 

       

