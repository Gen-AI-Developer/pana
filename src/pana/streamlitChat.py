import streamlit as st
def main():
    gemini_api_key = st.sidebar.text_input("Enter Gemini API key", type="password")

    with st.expander("Disclaimer"):
        st.write('''
            This is Simple Chat Bot Don't Expect To much
        ''')

    st.title("Echo Bot")
    # prompt = st.chat_input("Say something")
    # if prompt:
    #     st.write(f"User has sent the following prompt: {prompt}")
# Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

# Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
if __name__ == "__main__":
    main()