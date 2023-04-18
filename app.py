import openai
import streamlit as st
import os

# Load the API key from a separate file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up the OpenAI GPT-3 model
model_engine = "text-davinci-002"
prompt = "Hello, how can I assist you today?"

# Define the Streamlit app
def app():
    st.title("ChatGPT")
    st.write("Ask me anything and I'll do my best to help!")
    user_input = st.text_input("You:")
    if user_input:
        # Generate a response using the OpenAI GPT-3 model
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt + user_input,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        st.text_area("ChatGPT:", response.choices[0].text.strip())

# Run the app
if __name__ == "__main__":
    app()
