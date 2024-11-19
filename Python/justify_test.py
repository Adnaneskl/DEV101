import os

def justify_center(string:str,symbol:str):
    terminal_width = os.get_terminal_size().columns
    string_len = len(string)
    new_string_size = int(terminal_width/2) - int(string_len/2) 
    if(new_string_size*2+string_len > terminal_width):
        print("\n",symbol*new_string_size,string,symbol*(new_string_size-1),sep="")
    else:
        print("\n",symbol*new_string_size,string,symbol*new_string_size,sep="")

def justify_left(string:str,symbol:str):
    terminal_width = os.get_terminal_size().columns

    string_len = len(string)



    left_symbol = print(symbol*int(((terminal_width)/2)-(terminal_width*0.2)),sep="",end="")
    right_symbol = print(symbol* int(((terminal_width)/2)-(terminal_width*0.2)),sep="",end="")


    '''while(left_symbol + right_string_length + string_len > terminal_width):
        right_string_length-=1'''

    print(left_symbol,string,right_symbol,sep="",end="\n")


justify_center("Hello","_")

justify_left("11"*10,"-")
