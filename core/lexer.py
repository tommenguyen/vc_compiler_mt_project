import pandas as pd
import numpy as np
import os
import csv
import sys
os.chdir(os.path.dirname(__file__))
if __name__ == '__main__':
    print("Current directory: ", os.getcwd())
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("No source code path provided.")
        sys.exit(1)
    with open(path, 'r') as file:
        source_code = file.read()
        source_code += '$'
    transtion_table = pd.read_csv("transition_table.csv", index_col=0)
#initialize the state and the token
    char_iterator = 0
    current_char = source_code[char_iterator] 
    current_state = 0
    current_token = ''
    #initialize the line and column for the error message
    current_line = 1
    current_column = 1
    tokens = [

    ]
    def getNextState(transtion_table, current_char, current_state):
        try:
            next_state = transtion_table.loc[current_state,current_char]
        except:
            return np.nan
        return next_state
    def getTokenVerbose(current_state, current_token, current_line, current_column):
        match current_state:
            case 78 | 79:
                current_kind = "<float-literal>"
            case 77:
                current_kind = "<int-literal>"
            case 84:
                current_kind = "<string-literal>"    
            case 6969 | 31 | 1| 12 | 20 | 24 | 34 | 40 | 44 | 48:
                current_kind = "<id>"
            case 60:
                current_kind = "<="
            case 67:
                current_kind = "=="
            case 61:
                current_kind = ">="
            case 64:
                current_kind = "&&"
            case 65:
                current_kind = "||"
            case 60:
                current_kind = "!!"
            case 7:
                current_kind = "boolean"
            case 11:
                current_kind = "break"
            case 19:
                current_kind = "continue"
            case 23:
                current_kind = "else"
            case 28:
                current_kind = "false"
            case 93:
                current_kind = "float"
            case 30:
                current_kind = "for"
            case 33:
                current_kind = "int"
            case 89:
                current_kind = "if"
            case 39:
                current_kind =  "return"
            case 43:
                current_kind =  "true"
            case 47:
                current_kind = "void"
            case 52:
                current_kind =  "while"
            case _:
                current_kind = current_token
        return {
            "state": current_state,
            "type": current_kind,
            "spelling": current_token,
            "line": current_line ,
            "column": current_column - len(current_token)+1
        }
    while current_char != '$':
        #handle the special characters to lookup the table
        if current_char == ' ' or current_char == '\t':
            current_char = 'whitespaces'
        if current_char == '\n':
            current_char = 'newline'
        #skip the whitespaces and newline characters at state 0
        if (current_char == 'whitespaces') and current_state == 0:
            char_iterator += 1
            current_char = source_code[char_iterator]
            continue
        if  current_char =='newline' and current_state == 0:
            char_iterator += 1
            current_char = source_code[char_iterator]
            current_line += 1
            current_column = 1
            continue
        #get the next state
        next_state = getNextState(transtion_table, current_char, current_state)
        if np.isnan(next_state):
            #append the tracked token to the list of tokens, current character does no change
            tokens.append(
                getTokenVerbose(
                    current_state, 
                    current_token, 
                    current_line,
                    current_column))
            current_token = ''
            current_state = 0
        else:
            match next_state:
                case 88: # Inside a comment state
                    current_token = ''
                    char_iterator += 1
                    current_char = source_code[char_iterator]
                    current_state = 0
                case 69420:
                    print("Error: missing terminating at", current_line,":" ,current_column)
                case _:
                    if current_char == 'whitespaces':
                        current_char = ' '
                    current_token += current_char
                    current_state = next_state
                    #get the next character
                    char_iterator += 1
                    current_column += 1
                    current_char = source_code[char_iterator]
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    with open(os.path.join(output_folder, 'output.vctok'), 'w') as file:
        for token in tokens:
            file.write(f"{token['spelling']}\n")
    
    with open(os.path.join(output_folder, 'output.verbose.vctok'), 'w') as file:
        for token in tokens:
            file.write(f"{token}\n")