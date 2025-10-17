# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    """Return a predefined response based on user input."""
    user_input = user_input.lower()  # convert to lowercase for easy matching

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks for asking! 😊"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot created by you!"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Sorry, I don't understand that yet. 🤔"

def run_chatbot():
    """Run the chatbot in a loop until user says bye."""
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() in ["bye", "goodbye", "see you"]:
            break

# Start the chatbot
run_chatbot()
