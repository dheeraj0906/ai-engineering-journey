import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def classify_log_error(log_line):
    response =client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role":"system", "content":"You classify application log errors. Reply with exactly one word: TIMEOUT, DATA, or UPSTREAM"},
            {"role":"user","content":log_line}
        ]
    )
    return response.choices[0].message.content


with open("sample.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            clean_line = line.strip()
            label = classify_log_error(clean_line)
            print(f"{label} | {clean_line}")


