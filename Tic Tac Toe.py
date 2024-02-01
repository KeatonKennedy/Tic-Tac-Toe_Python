def rowPrint():
    print(row1)
    print(row2)
    print(row3)

row1 = ['','','']
row2 = ['','','']
row3 = ['','','']

turn = 1

print('Welcome to Tic Tac Toe!')
p1 = str(input('Player 1 choose X or O: '))

if p1 == 'x' or 'X':
    p2 = 'O'
else:
    p2 = 'X'

rowPrint()
while True:
    while turn == 1:
        print('\nPlayer 1:')
        rowMove = int(input('Choose which row? 1-3: '))
        colMove = int(input('Choose which column? 1-3: '))
        colMove -= 1
        
        if rowMove == 1:
            if row1[colMove] == '':
                row1[colMove] = p1
                turn += 1
            else:
                print('-----Invalid move-----')
        if rowMove == 2:
            if row2[colMove] == '':
                row2[colMove] = p1
                turn += 1
            else:
                print('-----Invalid move-----')
        if rowMove == 3:
            if row3[colMove] == '':
                row3[colMove] = p1
                turn += 1
            else:
                print('-----Invalid move-----')
        rowPrint()

    if (row1[0] and row1[1] and row1[2] == p1) or (row2[0] and row2[1] and row2[2] == p1) or (row3[0] and row3[1] and row3[2] == p1) or (row1[0] and row2[0] and row3[0] == p1) or (row1[1] and row2[1] and row3[1] == p1) or (row1[2] and row2[2] and row3[2] == p1) or (row1[0] and row2[1] and row3[2] == p1) or (row1[2] and row2[1] and row3[0] == p1):
        print('Player 1 Won the game!')    
        break #not working
    
    while turn == 2:
        print('\nPlayer 2:')
        rowMove = int(input('Choose which row? 1-3: '))
        colMove = int(input('Choose which column? 1-3: '))
        colMove -= 1

        if rowMove == 1:
            if row1[colMove] == '':
                row1[colMove] = p2
                turn -= 1
            else:
                print('-----Invalid move-----')
        if rowMove == 2:
            if row2[colMove] == '':
                row2[colMove] = p2
                turn -= 1
            else:
                print('-----Invalid move-----')
        if rowMove == 3:
            if row3[colMove] == '':
                row3[colMove] = p2
                turn -= 1
            else:
                print('-----Invalid move-----')
        rowPrint()

    if (row1[0] and row1[1] and row1[2] == p2) or (row2[0] and row2[1] and row2[2] == p2) or (row3[0] and row3[1] and row3[2] == p2) or (row1[0] and row2[0] and row3[0] == p2) or (row1[1] and row2[1] and row3[1] == p2) or (row1[2] and row2[2] and row3[2] == p2) or (row1[0] and row2[1] and row3[2] == p2) or (row1[2] and row2[1] and row3[0] == p2):
        print('Player 2 Won the game!')
        break #not working
