# import openai

# openai.api_key = "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"

# # # list models
# # models = openai.Model.list()

# # # print the first model's id
# # print(models.data)

# input_text = "Where is the 2014 World Cup held?"

# # create a chat completion
# # completions = openai.Completion.create(
# #     model="gpt-3.5-turbo",
# #     messages=[{"role": "user", "content": input_text}],
# #     max_tokens=3990,
# #     n=1,
# #     stop=None,
# #     temperature=0.5,
# # )

# completions = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "user", "content": "what can you say about streamlit?"},
#     ],
#     max_tokens=4000,
#     temperature=0.1,
# )

# # print the chat completion
# print(completions["choices"][0]["message"]["content"])


import os

import openai
import streamlit as st

# from dotenv import load_dotenv
from streamlit_chat import message

from PASSWORDS import OPENAI_KEY

# load_dotenv('api_key.env')
openai.api_key = (
    OPENAI_KEY  # os.environ.get('API_KEY')
)


def generate_response(prompt):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.6,
    )
    message = completion.choices[0].text
    return message


st.title("ChatGPT-like Web App")
# storing the chat
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
user_input = st.text_input("You:", key="input")
if user_input:
    output = generate_response(user_input)
    # store the output
    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(output)
if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
