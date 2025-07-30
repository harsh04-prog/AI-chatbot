import google.generativeai as genai

API_KEY = "AIzaSyBEusk1KsZXWtle7FzrxUqO2fUyvwNLLWI"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with Gemini ! Type 'exit' to quite." )
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)