import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.window, width = 2000, height = 1200, bg = "black")
        self.canvas.pack()

        self.grid_size = 4
        self.cell_size = 160
        self.player = 'X'
        self.grid_index_4 = [
            ['E','E','E','E',],
            ['E','E','E','E',],
            ['E','E','E','E',],
            ['E','E','E','E' ]
        ]
        self.grid_index_5 = [
            ['E','E','E','E','E',],
            ['E','E','E','E','E',],
            ['E','E','E','E','E',],
            ['E','E','E','E','E',],
            ['E','E','E','E','E' ]
        ]
        self.grid_index_6 = [
            ['E','E','E','E','E','E',],
            ['E','E','E','E','E','E',],
            ['E','E','E','E','E','E',],
            ['E','E','E','E','E','E',],
            ['E','E','E','E','E','E',],
            ['E','E','E','E','E','E' ]
        ]
        self.grid_index = self.grid_index_4

        self.window.protocol("WM_DELETE_WINDOW", self.close_window)

        self.canvas.bind("<Button-1>", self.handle_events)
        self.window.bind("4", self.change_grid)
        self.window.bind("5", self.change_grid)
        self.window.bind("6", self.change_grid)
        self.window.bind("k", self.reset)

        self.draw_grid()
        self.write_text()
        

    def write_text(self):
        self.canvas.create_text(
            1500, 200,
            text = "Tic Tac Toe",
            fill = "white",
            font = ("Helvetica", 48)
        )

        self.canvas.create_text(
            1500, 500,
            text = f"Vyhrava ten, co ma 4 znaky vedla seba v hociktorom smere \n    Hraci sa po kzdom tahu striedaju\n Na vyber su 3 hracie polia:\n      4x4 = tlacitko 4\n      5x5 = tlacitko 5\n      6x6 = tlacitko 6\n k = reset",
            fill = "white",
            font = ("Helvetica", 10)
        )


    def change_grid(self, event):
        if event.char == '4':
            print(self.grid_size)
            self.grid_size = 4
            self.grid_index = self.grid_index_4

        if event.char == '5':
            print(self.grid_size)
            self.grid_size = 5
            self.grid_index = self.grid_index_5

        if event.char == '6':
            print(self.grid_size)
            self.grid_size = 6
            self.grid_index = self.grid_index_6

            
        self.canvas.delete("grid")
        self.draw_grid()
            
        

    def draw_grid(self):
        for i in range(1, self.grid_size):
            x = 100 + i * self.cell_size

            self.canvas.create_line(
                x, 100,
                x, 100 + self.cell_size * self.grid_size,
                fill='white',
                width=5,
                tag="grid")

        for i in range(1, self.grid_size):
            y = 100 + i * self.cell_size
            
            self.canvas.create_line(
                100, y,
                100 + self.cell_size * self.grid_size, y,
                fill="white", 
                width=5,
                tag="grid")

        # Draw borders
        self.canvas.create_rectangle(
            100, 100,
            100 + self.cell_size * self.grid_size,
            100 + self.cell_size * self.grid_size,
            outline="white",
            width=5,
            tag="grid"
        )


    def handle_events(self, event):
        # Get the x and y coordinates of the click
        x, y = event.x, event.y
        print(f"Clicked at: ({x}, {y})")
        
        # Calculate the cell number
        if 100 <= x <= 100 + self.cell_size * self.grid_size and 100 <= y <= 100 + self.cell_size * self.grid_size:
            col = (x - 100) // self.cell_size
            row = (y - 100) // self.cell_size
            cell_num = row * self.grid_size + col
            print(f"Clicked in cell: {cell_num}")
            print(f"Row: {row}, Col: {col}")

            
            # Draw X or O in the clicked cell
            cell_x = 100 + col * self.cell_size + self.cell_size // 2
            cell_y = 120 + row * self.cell_size + self.cell_size // 2

            if self.grid_index[row][col] == 'E':
                if self.player == 'X':
                    self.canvas.create_text(
                        cell_x, cell_y,
                        text='X',
                        fill='red',
                        font=('Helvetica', 48),
                        tag = "grid"
                    )

                    self.grid_index[row][col] = 'X'

                else:
                    self.canvas.create_text(
                        cell_x, cell_y,
                        text='O',
                        fill='blue',
                        font=('Helvetica', 48),
                        tag = "grid"
                    )

                    self.grid_index[row][col] = 'O'
                    
                # Switch player
                if self.player == 'X':
                    self.player = 'O'
                else:
                    self.player = 'X'

                self.check_win()


    def check_win(self):
        board = self.grid_index
        size = self.grid_size

        for row in range(size):
            for col in range(size - 3):
                if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] and board[row][col] != 'E':
                    self.canvas.create_text(1000,600,text = f"{board [row][col]} wins!",fill = "white", font = ("Helvetica", 48),tag = "grid")
                    
        for col in range(size):
            for row in range(size - 3):
                if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] and board[row][col] != 'E':
                    self.canvas.create_text(1000,600,text = f"{board [row][col]} wins!",fill = "white", font = ("Helvetica", 48), tag = "grid")

        for row in range(size - 3):
            for col in range(size - 3):
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] and board[row][col] != 'E':
                    self.canvas.create_text(1000,600,text = f"{board [row][col]} wins!",fill = "white", font = ("Helvetica", 48), tag = "grid")
                    
        for row in range(3, size):
            for col in range(size - 3):
                if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] and board[row][col] != 'E':
                    self.canvas.create_text(1000,600,text = f"{board [row][col]} wins!",fill = "white", font = ("Helvetica", 48), tag = "grid")
                    

        
        
   
  

    def reset(self, event=None):
        self.player = 'X'
        if self.grid_size == 4:
            self.grid_index = self.grid_index_4
        elif self.grid_size == 5:
            self.grid_index = self.grid_index_5
        elif self.grid_size == 6:
            self.grid_index = self.grid_index_6

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.grid_index[row][col] = 'E'

        self.canvas.delete("grid")
        self.draw_grid()

    
                    
        

    

    def close_window(self):
        self.window.destroy()

    def start(self):
        self.window.mainloop()

        """POROVNAVAT WIN STATY S LISTOM KTORY SA BUDE MENIT NA ZAKLADE INPUTOV"""



game = TicTacToe()
game.start()