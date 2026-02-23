import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read CI logs file
try:
    with open("test_output.txt", "r") as f:
        logs = f.read()
except FileNotFoundError:
    logs = "No logs found."

prompt = f"""
You are a senior software engineer.
Analyze the CI failure logs below.
Explain the root cause clearly and suggest a fix.

Logs:
{logs}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)

analysis = response.choices[0].message.content

print("==== AI ANALYSIS ====")
print(analysis)

# Save output for PR comment (optional)
with open("analysis.txt", "w") as f:
    f.write(analysis)