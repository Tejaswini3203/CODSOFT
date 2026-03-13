print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")
        
    elif user == "how are you":
        print("Bot: I am doing great. How about you?")
        
    elif user == "your name":
        print("Bot: My name is CodSoft Chatbot.")
        
    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence. It allows machines to learn and make decisions.")
        
    elif user == "who created you":
        print("Bot: I was created by Tejaswini for the CodSoft AI Internship.")
        
    elif user == "what can you do":
        print("Bot: I can answer simple questions and chat with you.")
        
    elif user == "thank you":
        print("Bot: You're welcome!")
        
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
        
    else:
        print("Bot: Sorry, I didn't understand that.")
