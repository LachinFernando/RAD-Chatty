from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os
import streamlit as st


os.environ["GROQ_API_KEY"] = st.secrets["keys"]["GROQ_API_KEY"]

MODEL_TYPE = "llama-3.1-8b-instant"


COMMON_TEMPLATE = """
"You are Chatty, an highly intelligent and friendly chatbot dedicated to answer user questions."
"Provide clear and consicse answers."
"Do not repeat the history of the conversation. But only the answer is required."
"\n\n"
Question: {question}
"n"
"Helpful answer:   "
"""

def get_groq_model():
    model = ChatGroq(temperature=0, groq_api_key=os.environ["GROQ_API_KEY"], model_name=MODEL_TYPE)
    return model


def streaming_question_answering(query_question: str, template: str = COMMON_TEMPLATE):
    prompt = ChatPromptTemplate.from_template(template)

    # select the model
    model = get_groq_model()

    # output parser
    output_parser = StrOutputParser()

    # create the chain
    chain = prompt | model | output_parser

    # get the answer
    return chain.stream({"question": query_question})