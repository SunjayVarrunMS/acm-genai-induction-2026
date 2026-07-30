"""India's Got Latent, a persona chatbot with an unmistakable act and a memory for callbacks.

Run with: streamlit run app.py
"""

import os

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

PERSONAS = {
    "No persona (plain chatbot)": (
        "You are a helpful, friendly chatbot. Answer clearly and stay on topic."
    ),
    "RoastBot": (
        "You are RoastBot, a stand-up comic on India's Got Latent. Fire back witty, "
        "sarcastic roasts at whatever the judges say, no matter the topic. Stay clever "
        "and playful, never genuinely mean or offensive; the panel should laugh, not "
        "wince. Keep responses short and punchy, like a real comeback."
    ),
    "ShakespeareBot": (
        "You are ShakespeareBot. Answer every question in old-English, Shakespearean "
        "prose, thee's and thou's included, no matter how modern or mundane the "
        "question is. Stay fully in character."
    ),
    "Emoji Translator Bot": (
        "You are Emoji Translator Bot. Convert your entire response into emoji-speak: "
        "reply almost entirely in emoji sequences, with only the bare minimum text "
        "needed to keep the meaning clear."
    ),
    "Bollywood Villain Bot": (
        "You are a classic over-the-top Bollywood movie villain. Respond to everything "
        "dramatically and menacingly, refer to your grand evil plans and henchmen, and "
        "deliver every line like it belongs right before an interval twist. Stay campy "
        "and theatrical, never genuinely threatening."
    ),
}

st.set_page_config(page_title="India's Got Latent (Chatbot Act)", page_icon="🎤")


def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "show_started" not in st.session_state:
        st.session_state.show_started = False
    if "persona" not in st.session_state:
        st.session_state.persona = "No persona (plain chatbot)"


def get_llm(api_key, model_name):
    return ChatGroq(api_key=api_key, model=model_name, temperature=0.8)


def build_prompt_messages():
    system_prompt = PERSONAS[st.session_state.persona]
    prompt_messages = [SystemMessage(content=system_prompt)]
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            prompt_messages.append(HumanMessage(content=msg["content"]))
        else:
            prompt_messages.append(AIMessage(content=msg["content"]))
    return prompt_messages


def render_sidebar():
    with st.sidebar:
        st.header("Backstage")

        api_key = st.text_input(
            "Groq API key",
            value=os.environ.get("GROQ_API_KEY", ""),
            type="password",
            help="Get one free at console.groq.com, or set GROQ_API_KEY as an env var instead.",
        )
        model_name = st.selectbox(
            "Model",
            ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"],
            help="8b is faster, 70b stays in character a bit better.",
        )

        st.divider()
        st.subheader("Pick your act")
        st.selectbox(
            "Persona",
            list(PERSONAS.keys()),
            key="persona",
            disabled=st.session_state.show_started,
            help="Locks in once the show starts, no do-overs, remember?",
        )

        if not st.session_state.show_started:
            if st.button("🎬 Start the show", type="primary", use_container_width=True):
                st.session_state.show_started = True
                st.rerun()
        else:
            st.success(f"On stage as: {st.session_state.persona}")

        if st.button("🔁 Reset performance", use_container_width=True):
            st.session_state.messages = []
            st.session_state.show_started = False
            st.rerun()

        return api_key, model_name


def main():
    init_state()
    st.title("🎤 India's Got Latent (Chatbot Act)")
    st.caption(
        "No script, no re-runs. Pick a persona, start the show, and talk to the bot live."
    )

    api_key, model_name = render_sidebar()

    if not st.session_state.show_started:
        st.info("Pick your act in the sidebar and hit **Start the show** to begin.")
        return

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Say something to the panel...")
    if user_input is None:
        return

    if not api_key:
        st.error("Add a Groq API key in the sidebar before performing.")
        return

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    llm = get_llm(api_key, model_name)
    prompt_messages = build_prompt_messages()

    with st.chat_message("assistant"):
        with st.spinner("..."):
            response = llm.invoke(prompt_messages)
        st.markdown(response.content)

    st.session_state.messages.append({"role": "assistant", "content": response.content})


if __name__ == "__main__":
    main()
