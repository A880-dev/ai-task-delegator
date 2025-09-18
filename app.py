import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key="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")

# Streamlit UI
st.set_page_config(page_title="AI Task Delegator", page_icon="🧠")
st.title("🧠 AI Task Delegator")
st.markdown("Break big goals into smart, actionable steps.")

task = st.text_area("Enter your main task or goal", height=150)

if st.button("Delegate it!"):
    with st.spinner("Thinking like a productivity ninja..."):
        prompt = f"""
You are a helpful and intelligent AI task delegator.

Break the following task into 5–7 clear, actionable subtasks. Assign each subtask:
- A short title
- A priority level (High / Medium / Low)
- A 1–2 sentence description

Task: "{task}"

Return the result in neat bullet points like this:
[Priority] Title: Description
"""

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            breakdown = response.choices[0].message.content
            st.success("Here’s your delegated task plan:")
            st.markdown(f"```markdown\n{breakdown}\n```")
        except Exception as e:
            st.error(f"Error: {e}")
