import random
import time

greetings =["hello , hope you doing well how can i help you today ",
            "Good day , hope you doing well how can i help you today ",
            "Hello there,hope you doing well how can i help you today"]
music = ["RNB","POP","HIP-HOP","Jazz"]
print("Hi there my name is Home assistant chatbot, how may i assist you today?")


def curtains():
     print("Chatbot: closing curtains")
def house_lights():
    print("Chatbot: turning off lights")
def musicc():
    print("Chatbot: playing music",random.choice(music))
while True:
    user_input = input("you:")

    if user_input.lower()=="hello":
        print("Chatbot:",random.choice(greetings))

    elif user_input.lower()=="close curtains":

        curtains()
    elif user_input.lower()=="turn off the lights":
        house_lights()
    elif user_input.lower()=="play music":
        musicc()
    elif user_input.lower()=="exit":
        print("chatbot: Bye! have an awesome day")
        time.sleep(2)
        break

    else:
        print("I don't understand you")



        







