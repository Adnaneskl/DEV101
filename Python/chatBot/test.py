import google.generativeai as genai
import os
API_KEY = "AIzaSyDTaF40r0Zjrqjq-809Ab92hbq9PsB8Epc"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

terminal_width= os.get_terminal_size().columns
commands =["!Restart","!Stop","!Clear"]


response = model.generate_content("If you recieved this message say:Hi I'm ready, How can I help you today ?")
print(f"{'Gemini :': <30}{response.text:<30}")

def check_commands(prompt):
    if(prompt in commands):
        match prompt:
            case "!Restart":
                print("A restart method was called")
                return False
            case "!Stop":
                print("A stop method was called")
                return True
            case "!Clear":
                print("A clear method was called")
                return False
            case _:
                return False
def generate_response(prompt):
    #Generate response
    response = model.generate_content(prompt)
    #Response
    print(f"\n{'Gemini :': <30}{response.text:<30}")
def user_prompt():
    return input("You : ")
def bye(): 
    generate_response("Bye !")
    print("-"*terminal_width)

prompt = user_prompt()
command = 0
while(not check_commands(prompt)):
    if(prompt in commands):
        command = 1
        bye()
    else:
        if(command==1):
            command = 0
        user_prompt()
        print("-"*terminal_width)
        generate_response(prompt)
        print("-"*terminal_width)
    
if(command!=1):
    generate_response(prompt)
else:
   bye()