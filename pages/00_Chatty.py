import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from llm import streaming_question_answering


def message_creator(list_of_messages: list) -> list:
    prompt_messages = []
    for message in list_of_messages:
        if message["role"] == "user":
            prompt_messages.append(HumanMessage(content = message["content"]))
        else:
            prompt_messages.append(AIMessage(content = message["content"]))

    return prompt_messages


if not st.experimental_user.is_logged_in:
    st.error("Please log in to access the chatbot")
    st.stop()

st.title("Chatty 🤖")
st.subheader("Your personal assistant")
st.write("Chatty is a personal assistant that can help you with a variety of tasks.")
st.image("https://www.kommunicate.io/blog/wp-content/uploads/2023/07/Personalization-at-Scale-How-Chatbots-Drive-Customized-Customer-Experiences-1.png", caption="Chatty")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_list = message_creator(st.session_state.messages)
        response = st.write_stream(streaming_question_answering(message_list))
    st.session_state.messages.append({"role": "assistant", "content": response})