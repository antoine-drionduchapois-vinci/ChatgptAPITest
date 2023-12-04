import openai
from config import OPENAI_API_KEY

# Set your OpenAI GPT-3 API key
openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Updated model name
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

user_input = "What is the meaning of life?"
gpt_response = chat_with_gpt(user_input)
print(gpt_response)

