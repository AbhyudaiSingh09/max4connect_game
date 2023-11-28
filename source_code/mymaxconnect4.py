
import sys 
from myMaxConnect4Game import * 

def oneMoveGame(currentGame,depth):
    if currentGame.pieceCount == 42:
        print('BOARD FULL\n \n Game Over!\n')
        sys.exit(0)

    currentGame.aiPlay(depth)

    print('Game state after move')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n'%(currentGame.player1Score, currentGame.player2Score))


    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()



def interactiveGame(currentGame,depth):
    while currentGame.pieceCount < 42:
        if currentGame.currentTurn == 1: 
            userMove = int(input("Enter the column number (1-7) to play: "))-1
            if userMove < 0 or userMove > 6 or not currentGame.playPiece(userMove):
                print("Invalid move. Try again.")
                continue
        else: 
            print("\n AI's turn")
            currentGame.aiPlay(depth)

        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player1 = %d, Player 2 = %d \n' %(currentGame.player1Score, currentGame.player2Score))

        currentGame.currentTurn = 1 if currentGame.currentTurn == 2 else 2 


        if currentGame.pieceCount == 42: 
            print("BOARD FULL \n \n Game over :P")
            break



def  main(argv):
    if len(argv) != 5:  
        print("Four command-line arguments are needed:")
        print("Usage: %s interactive [input_file][computer-next/human-next][depth]"% argv[0])
        print('or: %s one-move [input-file][output_file][depth]'%argv[0])
        sys.exit(2)


    game_mode, inFile = argv[1:3]
    depth = int(argv[4])

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecgnized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game()

    try: 
        currentGame.gameFile = open(inFile,'r')
    except IOError: 
        sys.exit("\n Error opening input file. \n Check file name.\n")

    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn= int(file_lines[-1][0])
    currentGame.gameFile.close()



    print('\n MaxConnect-4 game\n')
    print('Game state before move: ')
    currentGame.printGameBoard()


    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n'%(currentGame.player1Score, currentGame.player1Score))

    if game_mode =='interactive':
        interactiveGame(currentGame,depth)
    else: 
        outFile = argv[3]
        try: 
            currentGame.gameFile= open(outFile,'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,depth)


if __name__=='__main__':
    main(sys.argv)

    














