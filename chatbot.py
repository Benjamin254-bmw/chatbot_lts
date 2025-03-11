import random
import re #for better text cleaning
import json

# File to store user data
DATA_FILE = "chatbot_memory.json"

# Predefined responses
responses = {
        "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
        "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm fine, thanks for asking!"],
        "your name": ["I'm ChatBot, your virtual assistant!", "You can call me ChatBot."],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "default": ["I'm not sure I understand. Can you rephrase that?", "Hmm, I don't have an answer for that."]
        }

# Function to load memory from a file
def load_memory():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return empty dictionary if file is missing/corrupt

# Function to save memory to a file
def save_memory(memory):
    with open(DATA_FILE, "w") as file:
        json.dump(memory, file)

# Load user memory
memory = load_memory()

# Function to clean user input
def clean_input(user_input):
    user_input = user_input.lower().strip()  # Convert to lowercase & remove spaces
    user_input = re.sub(r"[^a-zA-Z0-9\s]", "", user_input)  # Remove special characters    
    return user_input

#function to get response with memory
def get_response(user_input):
    user_input = clean_input(user_input)

    #check if user mentioned their name
    if "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        memory["name"] = name.capitalize()
        return f"Nice to meet you, {memory ['name']}!"

    # If user asks for their name
    if "what's my name" in user_input or "what is my name" in user_input:
        if "name" in memory:
            return f"Your name is {memory['name']}!"            
        return "I don't think you've told me your name yet."

    # Standard responses
        for key in responses:
            if key in user_input:
                return random.choice(responses[key])
        return random.choice(responses["default"])  # Default response if no match is found

# Chat loop
print("ChatBot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot:", random.choice(responses["bye"]))
        break
    print("ChatBot:", get_response(user_input))
