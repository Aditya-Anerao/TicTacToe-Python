#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python Assignment 2: 
Tic-Tac-Toe
Due: Monday, September 13, 11:59pm
https://www.csc2.ncsu.edu/faculty/healey/msa/python/assn-tictactoe/

@author: Aditya Anerao
"""
# Null Value (asthetic)
Blank = " "
Space = "                 "

# Define Valid entries
valid_Entries = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# Nest game in infinite while loop to allow for continuous play
while True:

    # Initialize all positions as blank
    A1 = Blank
    A2 = Blank
    A3 = Blank
    B1 = Blank
    B2 = Blank
    B3 = Blank
    C1 = Blank
    C2 = Blank
    C3 = Blank
    
    #Empy String to record previously selected positions
    entries = []

     # Function to check if a move is valid
    def check_valid(n):
        valid = True #Assume valid
        if n in entries: #if  has already been played then invalid
            valid = False
        if n not in valid_Entries: #if position is not valid
            valid = False
        return valid

    # Function to check if game is over
    def check_win(n):
        #By default game is not over unless condition is met
        win = False
        #Vertical Win
        if A1 != Blank and A1 == B1 and A1 == C1:
            win = True
        elif A2 != Blank and A2 == B2 and A2 == C2:
            win = True
        elif A3 != Blank and A3 == B3 and A3 == C3:
            win = True
        # Vertical win    
        elif A1 != Blank and A1 == A2 and A1 == A3:
            win = True
        elif B1 != Blank and B1 == B2 and B1 == B3:
            win = True
        elif C1 != Blank and C1 == C2 and C1 == C3:
            win = True
        # Diagonal win    
        elif A1 != Blank and A1 == B2 and A1 == C3:
            win = True
        elif A3 != Blank and A3 == B2 and A3 == C1:
            win = True
        # If 9 moves have been played and game has not been won than the game is a draw
        if win == False and len(entries) == 9:
            win = "draw"
        return win

    # Print Board
    def print_board():
        print("")
        print(Space + " ----------- ")
        print(Space + "| " + A1 + " | " + B1 + " | " + C1 + " |")
        print(Space + " ----------- ")
        print(Space + "| " + A2 + " | " + B2 + " | " + C2 + " |")
        print(Space + " ----------- ")
        print(Space + "| " + A3 + " | " + B3 + " | " + C3 + " |")
        print(Space + " ----------- ")
        print("")
            
    print("")
    print("********** Let's Play Tic-Tac-Toe **********")
    
    # win is false by default
    win = False
    #count number of moves
    move = 1
    
    while win == False:
        # print board
        print_board()
        # First player is X, therefore all odd moves are X
        if move%2 == 1:
            player = "X"
        # Second player is O, therefore all even moves are O
        else: 
            player = "O"
        print("Player " + player + "'s turn")
        
        position = input( "Choose a position: " )
        position = str(position).capitalize()
        
        # check valid move
        valid = check_valid(position)
        while valid == False: #while loop will remain false until valid move is selected
            valid = check_valid(position)
            if valid == False:
                if position not in valid_Entries:
                    print("Error: please select a valid position")
                    position = input( "Choose a position: " )
                    position = str(position).capitalize()
                if position in entries:
                    print("Error: This position has been selected.")
                    position = input( "Choose a position: " )
                    position = str(position).capitalize()
        
        # add valid moves to tracker of previous positions
        entries.append(position)
        
        if position == 'A1':
            A1 = player
        elif position == 'A2':
            A2 = player
        elif position == 'A3':
            A3 = player
        elif position == 'B1':
            B1 = player
        elif position == 'B2':
            B2 = player
        elif position == 'B3':
            B3 = player
        elif position == 'C1':
            C1 = player
        elif position == 'C2':
            C2 = player
        else:
            C3 = player
        win = check_win(position)
        move += 1
    
    print_board()
    if win == True:
        print("Player " + player + " Wins!")
    else:
        print("Both players draw!")
    
    # Player option to play again
    # If player answers "Y", then play again, else quit
    end_game = input("Do you want to play again? Y/N: ")
    end_game = str(end_game).capitalize()
    if end_game != "Y":
        print("")
        break