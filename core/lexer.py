import pandas as pd
import numpy as np
import os
os.chdir(os.path.dirname(__file__))
with open('example_fib.vc', 'r') as file:
    source_code = file.read()
transtion_table = pd.read_csv('transition_table.dat', index_col=0)
state_list = transtion_table.index.tolist()
symbol_list = transtion_table.columns.tolist()


#initialize the state and the token
char_iterator = 0
current_char = source_code[char_iterator] 
current_state = 0
current_token = ''
tokens = []
no_next_state = False
while current_char != '$':

    #if the state is inside comment, reset current_token to empty string
    if current_state == 86 or current_state == 87 or current_state ==88:
        current_token = ''
        

    #get the next state
    try:
        next_state = transtion_table.loc[current_state,current_char]
        if next_state == 69420:
            print('Lexical Error')
    except:
        no_next_state = True
    #if the next state is nan, then accept the current token

    if np.isnan(next_state) or no_next_state == True:
        if len(current_token) > 0:

            #append the tracked token to the list of tokens
            tokens.append(current_token)
        if current_char == "whitespaces" or current_char == "newline":
            None
        else:
            #append the current character as current token when the next state is nan
            tokens.append(current_char)
        current_token = ''
        current_state = 0
        no_next_state = False
    else:
        if current_char == 'whitespaces':
            current_char = ' '
            
        current_token += current_char
        current_state = next_state
    #accept and print the token

    #get the next state

    
    #get the next character
    char_iterator += 1
    current_char = source_code[char_iterator]

    #handle the special characters
    if current_char == ' ' or current_char == '\t' or current_char == '\r':
        current_char = 'whitespaces'
    if current_char == '\n':
        current_char = 'newline'
with open('output/tokens.txt', 'w') as file:
    for token in tokens:
        file.write(token+'\n')