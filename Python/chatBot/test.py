import google.generativeai as genai
import os
API_KEY = ""

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

terminal_width= os.get_terminal_size().columns
commands =["!Restart","!Stop","!Clear"]


response = model.generate_content("If you recieved this message say:Hi I'm ready, How can I help you today ?")
print(f"{'Gemini :': <30}{response.text:<30}")

prompt  = input("You : ")

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
#Sperator
print("-"*terminal_width)
command = 0
while(not check_commands(prompt)):
    if(prompt in commands):
        command = 1
        prompt = "Bye !"
        response = model.generate_content(prompt)
        #Response
        print(f"\n{'Gemini :': <30}{response.text:<30}")
        #Separator
        print("-"*terminal_width)
    else:
        command = 0
        #input
        prompt = input("You : ")
        #Separator
        print("-"*terminal_width)
        response = model.generate_content(prompt)
        #Response
        print(f"\n{'Gemini :': <30}{response.text:<30}")
        #Separator
        print("-"*terminal_width)
    
if(command==1):
    prompt = "Bye !"
    response = model.generate_content(prompt)
    #Response
    print(f"\n{'Gemini :': <30}{response.text:<30}")
else:
    response = model.generate_content(prompt)
    #Response
    print(f"\n{'Gemini :': <30}{response.text:<30}")