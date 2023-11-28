MaxConnect4 Game

Overview

MaxConnect4 is an implementation of a two-player connection game where players alternately drop colored discs into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. This implementation of MaxConnect4 is designed to play the game using a depth-limited version of the minimax algorithm with alpha-beta pruning. It can be played in two modes: interactive and one-move.

Installation

To run this game, you will need Python installed on your system. The game was developed and tested with Python 3.11.

Cloning the Repository
Clone the repository to your local machine:

bash
Copy code
git clone [URL to repository]
cd [repository name]
Usage

The game can be run in two different modes: interactive and one-move.

Interactive Mode
In the interactive mode, the game is played in real-time, with the player making a move followed by the AI. To start the game in interactive mode, use the following command:

bash
Copy code
python3 maxconnect4.py interactive [input file] [computer-next/human-next] [depth]
[input file]: Specify the initial state of the board.
[computer-next/human-next]: Specify who will make the next move.
[depth]: Specify the depth for the minimax algorithm.
Example:

bash
Copy code
python3 maxconnect4.py interactive input1.txt computer-next 7
One-Move Mode
In the one-move mode, the game reads the current state from an input file, makes a single move, and writes the resulting state to an output file. Use the following command for one-move mode:

bash
Copy code
python3 maxconnect4.py one-move [input file] [output file] [depth]
[input file]: The file containing the current game state.
[output file]: The file where the new game state will be saved.
[depth]: The depth for the AI's decision-making process.
Example:

bash
Copy code
python3 maxconnect4.py one-move input1.txt output1.txt 5
Contributing

Contributions to this project are welcome. Please ensure to update tests as appropriate.

License

MIT

Replace [URL to repository] and [repository name] with the actual URL and name of your repository. Also, if you have a different license or additional sections you want to add, feel free to modify the README accordingly.
