
# ------------------- Input Values 

L1 = ['PRODUCTION' , 'PROPORTION' , 'RECOMPENSE' , 'REDEMPTION' , 'REPARATION' , 'SETTLEMENT' , 'SOMATOTYPE' , 'SYNCRETISM' , 'TRANSCRIPT' , 'TYPESCRIPT']

L2=['RONDO' , 'SCORE' , 'SCRIP' , 'SETUP' , 'SHAPE' , 'STAMP' , 'STORY' , 'TENOR' , 'THEME' , 'UNION', 'USAGE', 'VALUE' ,'VIRTU','WEAVE','WHOLE']

L3=["abcdefghijklmnopqrst","fffffggg","ttttttttttuuuuuuuuuz","yzzz","qqqqqqqqqqqqqqy","xxxxxxxxxaaaaaaa","aaaaggg","vvvvvvvvvvvvq","mat","mat","make","make","maker","remake","hat"]

L_input= input('please input a list of strings: ')

L1.sort(key=len, reverse=True) #sort the list by len larger to smaller 
L2.sort(key=len, reverse=True)
L3.sort(key=len, reverse=True)
L_input.sort(key=len, reverse=True)

board=[[' ']*20 for i in range(20)]

# ------------------- a function to print the board
def printBoard(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print()

# ------------------- Adds the first word

def addFirstWord(board, word) :
    col = len(board) // 2 - len(word) // 2                  #finds where the letter is going to start to be centered
    row = len(board) // 2 
    if len(word) <= len(board) :
        for i in range(len(word)) :
            board[row-1] [col + i] = word[i]

# ------------------- check vertically for any problem

def checkvertical(board, word, row,col):
    passed=True
    counter=len(word)-1
    for letter in range(len(word)):
        if board[row+letter][col] != word[letter] and board[row+letter][col] != " ": #checks if there is a used space
            passed=False
        if row != 0 and board[row-1][col] != " ":                   #checks for empty space before the word
            passed=False
        if row+len(word) <=19 and board[row+len(word)][col] != " ": #checks for empty space before the word
            passed=False
        if board[row+letter][col] == word[letter]:                  #checks for an identical copy of the word in the empty space
            counter-=1
        if word[letter] != board[row+letter][col]:                  #checks for an empty space around the word
            if col >= 0 and col != 19:
                if board[row+letter][col+1] != " ":
                    passed=False
            if col<=19 and col != 0:
                if board[row+letter][col-1] != " ":
                    passed=False
    if passed and counter != 0:                                     #adds the word after passing the checks
        for w in range(len(word)):
            board[row+w][col] = word[w]
    return passed
# q4
def addvertical(board, word):
    for i in range(len(board)):
        if i+len(word)-1 <= 19:                             #stops running when the word is bigger than the grid
            for j in range(len(board[i])):                  
                for letter in range(len(word)):             
                    if board[i+letter][j] == word[letter]:  #check for a match
                        if checkvertical(board, word, i,j): #if word prints we stop 
                            return True
    return False 


# q5
# ----------------------------------------------checkhorizontal
def checkhorizontal(board, word, row, col):
    counter=len(word)-1
    passed=True
    for letter in range(len(word)):
        if board[row][col+letter] != word[letter] and board[row][col+letter] != " ": #checks if there is a used space
            passed=False
        if col != 0 and board[row][col-1] != " ":                   #checks for empty space before the word
            passed=False
        if col+len(word) <=19 and board[row][col+len(word)] != " ": #checks for empty space before the word
            passed=False
        if board[row][col+letter] == word[letter]:                  #checks for an identical copy of the word in the empty space
            counter-=1
        if word[letter] != board[row][col+letter]:                  #checks for an empty space around the word
            if row >= 0 and row != 19:
                if board[row+1][col+letter] != " ":
                    passed=False
            if row <=19 and row != 0:
                if board[row-1][col+letter] != " ":
                    passed=False
    if passed and counter != 0:                                     #adds the word after passing the checks
        for w in range(len(word)):
            board[row][col+w] = word[w] 
    return passed
    
def addhorizontal(board, word):
    for i in range(len(board)):
            for j in range(len(board[i])):
                if j+len(word)-1 <= 19:                             #stops running when the word is bigger than the grid
                    for letter in range(len(word)):
                        if board[i][j+letter] == word[letter]:      #check for a match
                            if checkhorizontal(board, word, i,j):   #if the word prints we stop 
                                return True 
    return False    

def crossword(L):
    onOff=True                                      #switcher
    addFirstWord(board, L[0])
    extra=[]                                        #words with  no match
    for i in L[1:]:
        if onOff:
            if not addvertical(board, i):
                if not addhorizontal(board, i):     #check if it is possible to go horizontally instead
                    extra.append(i)
            onOff=False
        else:
            if not addhorizontal(board, i):
                if not addvertical(board, i):       #check if it is possible to go vertically instead 
                    extra.append(i)
            onOff=True
    for i in extra:
        print(i,'Does not fit')                     #message if a word does not fit
    print(L)
    printBoard(board)                               #print the board        

# ------------------------- Three different examples 

crossword(L1)                                       #make a crossword using list L1
board=[[' ']*20 for i in range(20)]                 #reset the board
crossword(L2)                                       #make a crossword using list L2
board=[[' ']*20 for i in range(20)]                 #reset the board
crossword(L3)                                       #make a crossword using list L3
board=[[' ']*20 for i in range(20)]                 #reset the board
crossword(L_input)                                  #the customized list

# ---------------------------------------------------
# The End
# ---------------------------------------------------
