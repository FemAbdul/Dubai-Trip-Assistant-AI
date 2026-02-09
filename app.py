import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("Dubai Trip Planning Assistant App")

initial_message = [{"role":"system", "content":"You are a Dubai Trip Planner expert, specializing in crafting personalized itineraries. You provide concise, engaging, and informative trip plans in 200 words or less. Your recommendations consider top attractions, cultural experiences, dining, shopping, adventure, accomodation and relaxation, ensuring a well-balanced itinerary. You are knowledgeable, friendly, and professional. Focus on clear, actionable suggestions while keeping responses engaging and tailored to travelers' interests. Ask questions to user."},
                   {"role":"assistant", "content":"Hi, Iam Dubai Genie, your expert Trip Planner. How can i help you today?"}]

def get_response_from_llm(message):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages= message
    )

    return(completion.choices[0].message.content)


if "messages" not in st.session_state:
        st.session_state.messages = initial_message

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_message = st.chat_input("Enter your message")
if user_message:
    new_message = {"role":"user", "content":user_message}
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
            st.markdown(new_message["content"])
    response = get_response_from_llm(st.session_state.messages)
    if response:
        llm_response = {
            "role":"assistant",
            "content":response
        }
        st.session_state.messages.append(llm_response)
        with st.chat_message(llm_response["role"]):
                st.markdown(llm_response["content"])
