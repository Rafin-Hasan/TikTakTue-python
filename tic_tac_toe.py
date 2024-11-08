import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]  # 3x3 grid
        self.current_player = "X"  # X always goes first
        
        # Create buttons for the 3x3 grid
        self.buttons = [[tk.Button(root, text=" ", font=('normal', 40), width=5, height=2, command=lambda row=row, col=col: self.make_move(row, col)) 
                         for col in range(3)] for row in range(3)]
        
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == " " and not self.check_win():  # Check if cell is empty and game is not over
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win():
                self.display_winner()
            elif self.check_full():
                self.display_draw()
            else:
                self.switch_player()

    def check_win(self):
        # Check rows, columns, and diagonals
        for row in self.board:
            if row.count(self.current_player) == 3:
                return True
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        if self.board[0][0] == self.current_player and self.board[1][1] == self.current_player and self.board[2][2] == self.current_player:
            return True
        if self.board[0][2] == self.current_player and self.board[1][1] == self.current_player and self.board[2][0] == self.current_player:
            return True
        return False

    def check_full(self):
        return all(self.board[row][col] != " " for row in range(3) for col in range(3))

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        
    def display_winner(self):
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.reset_game()

    def display_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")

# Create the main window
root = tk.Tk()

# Initialize the game
game = TicTacToe(root)

# Run the Tkinter event loop
root.mainloop()
