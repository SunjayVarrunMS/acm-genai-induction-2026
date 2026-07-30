# Contestant Profile: India's Got Latent (Chatbot Act)

**Name:** the bot doesn't have one yet; you name it after picking an act.

**The act:** five personas on tap, locked in before the show starts, no do-overs once the lights come up:

- **RoastBot**: fires back witty, sarcastic comebacks at whatever the judges throw at it.
- **ShakespeareBot**: answers everything in full Shakespearean prose, thee's and thou's included.
- **Emoji Translator Bot**: converts its entire response into emoji-speak.
- **Bollywood Villain Bot**: dramatic, menacing, always one line from a plot twist.
- **No persona**: the plain, no-frills version, for judges who don't want the theatrics.

**Why it'll win the panel over:** most bots on this stage say "Hi, how can I help you?" and mean it literally. This one stays in character across the whole set. It remembers what a judge said three questions ago and can call back to it mid-roast, mid-sonnet, or mid-villain-monologue. Pick an act, hit "Start the show," and it doesn't break character until you reset it.

**How memory works:** every message in the current performance is kept in `st.session_state` and replayed to the model on each turn, so the bot can reference something said earlier in the same conversation, with no need to re-run the file between messages.

## Running it

```bash
pip install -r requirements.txt
streamlit run app.py
```

Get a free Groq API key at [console.groq.com](https://console.groq.com), then either:
- paste it into the sidebar's "Groq API key" field, or
- set it as an environment variable before launching: `export GROQ_API_KEY=...` (or `set` on Windows).

Pick a persona in the sidebar, hit **Start the show**, and start talking in the chat box. **Reset performance** clears the conversation and unlocks the persona picker for a new act.
