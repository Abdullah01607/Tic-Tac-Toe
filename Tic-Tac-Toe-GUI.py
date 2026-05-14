import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("350x450")
        self.root.configure(bg="#2b2b2b")
        
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        
        # Title/Status Label
        self.status_label = tk.Label(
            self.root, 
            text=f"Player {self.current_player}'s Turn", 
            font=("Helvetica", 16, "bold"),
            bg="#2b2b2b", 
            fg="white"
        )
        self.status_label.pack(pady=15)
        
        # Frame for the grid
        self.grid_frame = tk.Frame(self.root, bg="#2b2b2b")
        self.grid_frame.pack()
        
        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                self.grid_frame, 
                text=" ", 
                font=("Helvetica", 24, "bold"),
                width=5, 
                height=2,
                bg="#3b3b3b",
                fg="white",
                activebackground="#4b4b4b",
                activeforeground="white",
                command=lambda i=i: self.make_move(i)
            )
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)
            
        # Restart Button
        self.restart_btn = tk.Button(
            self.root, 
            text="Restart Game", 
            font=("Helvetica", 14),
            bg="#007acc",
            fg="white",
            activebackground="#005f9e",
            activeforeground="white",
            command=self.reset_game
        )
        self.restart_btn.pack(pady=20)

    def check_winner(self):
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # cols
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]
        
        for combo in win_positions:
            if (self.board[combo[0]] == self.current_player and
                self.board[combo[1]] == self.current_player and
                self.board[combo[2]] == self.current_player):
                
                # Highlight winning combination
                for idx in combo:
                    self.buttons[idx].config(bg="#4caf50")
                return True
        return False

    def is_draw(self):
        return " " not in self.board

    def make_move(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            
            color = "#ff5555" if self.current_player == "X" else "#5555ff"
            self.buttons[index].config(text=self.current_player, fg=color)
            
            if self.check_winner():
                self.status_label.config(text=f"🎉 Player {self.current_player} wins!", fg="#4caf50")
                self.disable_buttons()
            elif self.is_draw():
                self.status_label.config(text="It's a draw!", fg="yellow")
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s Turn")

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.status_label.config(text=f"Player {self.current_player}'s Turn", fg="white")
        
        for btn in self.buttons:
            btn.config(
                text=" ", 
                state="normal",
                bg="#3b3b3b",
                fg="white"
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
