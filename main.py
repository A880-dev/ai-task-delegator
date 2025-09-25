import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

def delegate_task(task):
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

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print("🧠 Welcome to the AI Task Delegator")
    user_task = input("Enter your task or goal: ")
    print("\n🔍 Delegating and planning...\n")
    breakdown = delegate_task(user_task)
    print(breakdown)
