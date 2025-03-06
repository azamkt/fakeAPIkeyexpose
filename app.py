import openai

API_KEY = "kEK54iThTmPNcMcCDHusuxUXzADA7PGghF0Q8t46rw5m6ESmO6jsfJQQJ99BCACYeBjFXJ3w3AAABACOG9nLO"

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    api_key=API_KEY
)

print(response)
