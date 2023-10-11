# https://platform.openai.com/account/api-keys
# https://github.com/amrrs/chatgpt-api-python/blob/main/ChatGPT_API_in_Python.ipynb


import requests

# Define the API URL
URL = "https://api.openai.com/v1/chat/completions"

# Define the API key
#api_key = "sk-"

# Define the user's question
user_question = "What is the first computer in the world?"

# Create the payload
payload = {
    "model": "gpt-3.5-turbo	",
    "messages": [{"role": "user", "content": user_question}],
    "temperature": 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

# Set the request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

# Send the API request
response = requests.post(URL, headers=headers, json=payload)

# Check for a successful response
if response.status_code == 200:
    data = response.json()
    model_reply = data['choices'][0]['message']['content']
    print("Model Reply:", model_reply)
else:
    print("Error:", response.text)



   
   
