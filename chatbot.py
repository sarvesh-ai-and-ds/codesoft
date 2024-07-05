def chatbot_response(user_input):

    user_input = user_input.lower()
    
    
    if user_input in ["hi", "hello", "hey","howdy"]:
        return "Hello! Master  in supreme"

   
    elif "whats your name" in user_input:
        return "I am a simple chatbot created to assist you."

   
    elif "what all things can you do" in user_input:
        return "I can respond to your greetings, tell you the time, and have a simple chat with you."

    elif "whats the time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        return f"The current time is {current_time}."

    else:
        return "I'm not sure how to respond to that. Can you ask something else?"


def chat():
    print("Welcome to the simple chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Master in supreme")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

chat()