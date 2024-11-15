import re #for regex later
import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')  # word tokenizer
nltk.download('averaged_perceptron_tagger')


# to activate virtual environment: source venv/bin/activate
# to run the python script: python chatbot.py
# to deactivate venv : deactivate


# this checks the user's input and returns an appropriate response based on rules
def get_response(user_input):
    #rules on left, responses on right
    #regex goes here (?)
    
    responses = {
        'hi': "How can I assist you?",
        'hello': "How can I assist you?",
        'bye': "Goodbye!", #exit
        'how are you': "I'm just a chatbot, but I'm doing great! How about you?",
        'what is your name': "I'm a simple rule-based chatbot.",
        'who made you' : 'Yarmi is my maker...This is all I know.',
        'tell me a joke': '[Insert cheesy joke here]...Hilarious, I know.',
        'tell me a scary story': 'You forgot the semicolon.... OOOOOOOOH!'
    }

    # convert input to lowercase to make the matching easier
    user_input = user_input.lower()

    # check if the user input matches any rule (keyword)
    for key in responses:
        if key in user_input: #if the key is present in the input
            return responses[key]

    # no matches
    return "I'm sorry, I didn't understand that."

# starts the conversation
def chat():
    print("\nInitializing Chatbot... type 'bye' to end the conversation\n")
    print("Chatbot: Hi!")
    while(True): #run until a break
        user_input = input("You: ")
        if user_input.lower() == 'bye': #this ends the conversation, break
            print("Chatbot: Goodbye!")
            break

        # get the chatbot's response based on the user input
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# run 
if __name__ == "__main__":
    chat()
