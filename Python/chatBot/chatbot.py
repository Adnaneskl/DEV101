import google.generativeai as genai
import os
import sys
from time import sleep

API_KEY = "AIzaSyDTaF40r0Zjrqjq-809Ab92hbq9PsB8Epc"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

terminal_width= os.get_terminal_size().columns
commands =["!Stop","!Clear","!Prevent","!Help"]
#class for colors
class colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

#Return false if prompt wasn't a command
def check_commands(prompt):
    if(prompt in commands and prompt == commands[0]):
        return True
    else: return False
def helpcommand ():
    string ="Welcome to chatBot version 1.0, a CLI program based on python that uses Google Generative AI api"
    string += " to generate an excellent response to fit your prompt."
    string += "\n\nThis list below displays all the commands available on the first column, explanations are on the nextcolumn:"
    string +="\n\n\t!Stop\t\t\t:stop the execution of the program."
    string +="\n\t!Clear\t\t\t:clear the terminal."
    string +="\n\t!Help\t\t\t:a guide to understand the use of this program and display of commands that can be used."
    string +="\n\t!Prevent\t\t:to prevent Gemini from answering your prompts. Enter for a second time to switch back."
    print(string)

def separator():
    print()
    '''print("-"*terminal_width)'''
#Generate a response for the prompt
def generate_response(prompt):
    if(prompt not in commands and prompt.__len__()>0):
        if(prompt.__len__ == 0):
            prompt = "Hi"
        response = model.generate_content(prompt)
        separator()
        if(prompt.__contains__("ascii")):
            print(f"{colors.GREEN}Gemini : \n",end="")
        else:
            print(f"{colors.GREEN}Gemini : ",end="")
        for response_with_Effect in response.text:
            if(response_with_Effect == response.text[0]):
                if(not prompt.__contains__("ascii")):
                    print()
            sleep(0.009)
            print(f"{colors.YELLOW}"+response_with_Effect,end="")
        print(end=f"{colors.RESET}")
        separator()
        
#user prompt
def user_prompt():
    return input(f"{colors.CYAN}→ {colors.WHITE}")
#Stop response for !Stop command
def bye(): 
    generate_response("Bye !")
#clear method for !Clear command
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


#set to false to generate responses
bool_preventai=False
#true to prevent ai from responding
def preventai(bool):
    if(bool!=False):
        print("\033[3m","Ai now will not generate responses, type the command again to resume.",colors.RESET)
    else:
        print("\033[3m","Ai now will resume responding to your questions :)",colors.RESET)

#Show help
helpcommand()
#Generate the first response
generate_response("If you recieved this message say:Hi I'm ready, How can I help you today ?")
prompt = user_prompt()
while(not check_commands(prompt)):
    #Check for commands and execute their actions
    if(prompt in commands):
        if(prompt == commands[1]):
            clear_screen()
        #Change bool_preventai to true if requested
        elif(prompt == commands[2]):
            if(bool_preventai != False):
                bool_preventai = False
            else:
                bool_preventai = True
            preventai(bool_preventai)
        elif(prompt == commands[3]):
            clear_screen()
            helpcommand()

    #Generate only when bool_preventai is false
    if(prompt != commands[0] and bool_preventai == False):
        if(prompt not in commands and prompt.__len__ () !=0):
            separator()
            print("\033[3m","Waiting for response ..",colors.RESET)
        generate_response(prompt)
        prompt = user_prompt()
    else:
        prompt = user_prompt()

bye()