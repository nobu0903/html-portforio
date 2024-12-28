//tictactoe  You can't win version
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

char board[3][3];
const char PLAYER = 'X';
const char COMPUTER = 'O';

void resetBoard();
void printBoard();
int checkFreeSpaces();
void playerMove();
void computerMove();
char checkWinner();
void printWinner(char winner);

int main() 
{
    int again;
    do
    {
        
    
    
        char winner = ' '; // No winner yet

        resetBoard();

        while (winner == ' ' && checkFreeSpaces() != 0)
        {
            printBoard();
            playerMove();
            winner = checkWinner();
            if (winner !=  ' ' || checkFreeSpaces() == 0)
            {
                break;
            }

            computerMove();
            winner = checkWinner(); // Added this to update the winner after computer move
            if (winner !=  ' ' || checkFreeSpaces() == 0)
            {
                break;
            }
        }

        printBoard();
        printWinner(winner); 
        printf("Do you wanna try again?\n"
               "1: Yes\n"
               "2: No\n");
        scanf("%d", &again);
        
    } while (again == 1);  

    return 0;
}

void resetBoard()
{
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++)
        {
            board[i][j] = ' ';
        }
    }
}

void printBoard()
{
    printf(" %c | %c | %c ", board[0][0], board[0][1], board[0][2]);
    printf("\n---|---|---\n");
    printf(" %c | %c | %c ", board[1][0], board[1][1], board[1][2]);
    printf("\n---|---|---\n");
    printf(" %c | %c | %c ", board[2][0], board[2][1], board[2][2]);
    printf("\n");
}

int checkFreeSpaces()
{
    int freeSpaces = 9;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if(board[i][j] != ' ')
            {
                freeSpaces--;
            }
        }
    }
    return freeSpaces;
}

void playerMove()
{
    int x;
    int y;

    do 
    {
        printf("Enter row #(1-3): ");
        scanf("%d", &x);
        x--;
        printf("Enter column #(1-3): ");
        scanf("%d", &y);
        y--;

        if (board[x][y] != ' ')
        {
            printf("Invalid move! Try again!\n");
        }
        else 
        {
            board[x][y] = PLAYER;
            break;
        }
    } while (board[x][y] != ' ');
}

void computerMove()
{
    srand(time(0));
    int x, y;

    //put on the 3rd piece and win the game
    //check row and then computer win the game
    for(int i = 0; i < 3; i++)
    {
        if(board[i][0] == COMPUTER && board[i][0] == board[i][1] && board[i][2] == ' ') {board[i][2] = COMPUTER; return;}
        if(board[i][0] == COMPUTER && board[i][0] == board[i][2] && board[i][1] == ' ') {board[i][1] = COMPUTER; return;}
        if(board[i][1] == COMPUTER && board[i][1] == board[i][2] && board[i][0] == ' ') {board[i][0] = COMPUTER; return;}
    }

    //check column and then computer win the game
    for(int i = 0; i < 3; i++)
    {
        if(board[0][i] == COMPUTER && board[0][i] == board[1][i] && board[2][i] == ' ') {board[2][i] = COMPUTER; return;}
        if(board[0][i] == COMPUTER && board[0][i] == board[2][i] && board[1][i] == ' ') {board[1][i] = COMPUTER; return;}
        if(board[1][i] == COMPUTER && board[1][i] == board[2][i] && board[0][i] == ' ') {board[0][i] = COMPUTER; return;}
    }

    //check diagnols and then computer win the game
    if (board[0][0] == COMPUTER && board[0][0] == board[1][1] && board[2][2] == ' ') {board[2][2] = COMPUTER; return;}
    if (board[0][0] == COMPUTER && board[0][0] == board[2][2] && board[1][1] == ' ') {board[1][1] = COMPUTER; return;}
    if (board[1][1] == COMPUTER && board[1][1] == board[2][2] && board[0][0] == ' ') {board[0][0] = COMPUTER; return;}

    if (board[0][2] == COMPUTER && board[0][2] == board[1][1] && board[2][0] == ' ') {board[2][0] = COMPUTER; return;}
    if (board[0][2] == COMPUTER && board[0][2] == board[2][0] && board[1][1] == ' ') {board[1][1] = COMPUTER; return;}
    if (board[1][1] == COMPUTER && board[1][1] == board[2][0] && board[0][2] == ' ') {board[0][2] = COMPUTER; return;}

    //detect reach and then block win by player
    //check row and then block player's win
    for(int i = 0; i < 3; i++)
    {
        if(board[i][0] == PLAYER && board[i][0] == board[i][1] && board[i][2] == ' ') {board[i][2] = COMPUTER; return;}
        if(board[i][0] == PLAYER && board[i][0] == board[i][2] && board[i][1] == ' ') {board[i][1] = COMPUTER; return;}
        if(board[i][1] == PLAYER && board[i][1] == board[i][2] && board[i][0] == ' ') {board[i][0] = COMPUTER; return;}
    }

    //check column and then block player's win
    for(int i = 0; i < 3; i++)
    {
        if(board[0][i] == PLAYER && board[0][i] == board[1][i] && board[2][i] == ' ') {board[2][i] = COMPUTER; return;}
        if(board[0][i] == PLAYER && board[0][i] == board[2][i] && board[1][i] == ' ') {board[1][i] = COMPUTER; return;}
        if(board[1][i] == PLAYER && board[1][i] == board[2][i] && board[0][i] == ' ') {board[0][i] = COMPUTER; return;}
    }

    //check diagnols and then block player's win
    if (board[0][0] == PLAYER && board[0][0] == board[1][1] && board[2][2] == ' ') {board[2][2] = COMPUTER; return;}
    if (board[0][0] == PLAYER && board[0][0] == board[2][2] && board[1][1] == ' ') {board[1][1] = COMPUTER; return;}
    if (board[1][1] == PLAYER && board[1][1] == board[2][2] && board[0][0] == ' ') {board[0][0] = COMPUTER; return;}

    if (board[0][2] == PLAYER && board[0][2] == board[1][1] && board[2][0] == ' ') {board[2][0] = COMPUTER; return;}
    if (board[0][2] == PLAYER && board[0][2] == board[2][0] && board[1][1] == ' ') {board[1][1] = COMPUTER; return;}
    if (board[1][1] == PLAYER && board[1][1] == board[2][0] && board[0][2] == ' ') {board[0][2] = COMPUTER; return;}
    

    if (checkFreeSpaces() > 0)
    {
        if (board[1][1] == ' ')
        {
            board[1][1] = COMPUTER;
            return;
        }
        
            
        
        
        do
        {
            int corner = rand() % 4; // Randomly choose a corner
            if (corner == 0) { x = 0; y = 0; } // Top-left
            else if (corner == 1) { x = 0; y = 2; } // Top-right
            else if (corner == 2) { x = 2; y = 0; } // Bottom-left
            else { x = 2; y = 2; } // Bottom-right
        } while (board[x][y] != ' '); // Ensure the corner is free

        board[x][y] = COMPUTER;
        
    }   

}

char checkWinner()
{
    // Check vertical
    for (int i = 0; i < 3; i++)
    {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ')
        {
            return board[i][0];
        }
    }

    // Check horizontal
    for (int i = 0; i < 3; i++)
    {
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ')
        {
            return board[0][i];
        }
    }

    // Check diagonal
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ')
    {
        return board[0][0];
    }

    if (board[2][0] == board[1][1] && board[1][1] == board[0][2] && board[2][0] != ' ')
    {
        return board[2][0];
    }

    return ' '; // No winner yet
}

void printWinner(char winner)
{
    if (winner == PLAYER)
    {
        printf("You win!\n");
    }
    else if (winner == COMPUTER)
    {
        printf("You lose!\n");
    }
    else
    {
        printf("It's a tie!\n");
    }
}

