import random
import re #for better text cleaning

# Predefined responses
responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine, thanks for asking!"],
        "your name": ["I'm ChatBot, your virtual assistant!", "You can call me ChatBot."],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "default": ["I'm not sure I understand. Can you rephrase that?", "Hmm, I don't have an answer for that."]
                            }
# Function to clean user input
def clean_input(user_input):
    user_input = user_input.lower().strip()  # Convert to lowercase & remove spaces
    user_input = re.sub(r"[^a-zA-Z0-9\s]", "", user_input)  # Remove special characters    
    return user_input


# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Chat loop
print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot:", random.choice(responses["bye"]))
        break
    print("ChatBot:", get_response(user_input))
