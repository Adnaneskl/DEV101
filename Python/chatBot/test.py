import google.generativeai as genai
import os

API_KEY = "AIzaSyDTaF40r0Zjrqjq-809Ab92hbq9PsB8Epc"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

terminal_width= os.get_terminal_size().columns
commands =["!Stop","!Clear"]

#Return false if prompt wasn't a command
def check_commands(prompt):
    if(prompt in commands and prompt == commands[0]):
        return True
    else: return False

def separator():
    print("\n"+"-"*terminal_width)
#Generate a response for the prompt
def generate_response(prompt):
    if(prompt not in commands):
        response = model.generate_content(prompt)
        separator()
        print("\nGemini : ",response.text)
        separator()
#user prompt
def user_prompt():
    return input("\nYou : ")
#Stop response for !Stop command
def bye(): 
    generate_response("Bye !")
#clear method for !Clear command
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

#Show cammands
print("These are the commands that you can use : ",commands)
#Generate the first response
generate_response("If you recieved this message say:Hi I'm ready, How can I help you today ?")

prompt = user_prompt()

while(not check_commands(prompt)):
    if(prompt in commands):
        if(prompt == commands[1]):
            clear_screen()
    if(prompt != commands[0]):
        generate_response(prompt)
        prompt = user_prompt()

bye()