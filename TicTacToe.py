import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.window, width = 2000, height = 1200, bg = "black")
        self.canvas.pack()

        self.grid_size = 5
        self.cell_size = 160
        self.player = 'X'
        self.grid_index = ['E','E','E','E','E','E',
                           'E','E','E','E','E','E',
                           'E','E','E','E','E','E',
                           'E','E','E','E','E','E',
                           'E','E','E','E','E','E',
                           'E','E','E','E','E','E']
        self.grid_dict = {}

        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.canvas.bind("<Button-1>", self.handle_events)
        self.window.bind("4", self.change_grid)
        self.window.bind("5", self.change_grid)
        self.window.bind("6", self.change_grid)

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
            1500, 200,
            text = "",
            fill = "white",
            font = ("Helvetica", 48)
        )

    def change_grid(self, event):
        if event.char == '4':
            print(self.grid_size)
            self.grid_size = 4
        if event.char == '5':
            print(self.grid_size)
            self.grid_size = 5
        if event.char == '6':
            self.grid_size = 6
            print(self.grid_size)
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
            
            # Draw X or O in the clicked cell
            cell_x = 100 + col * self.cell_size + self.cell_size // 2
            cell_y = 120 + row * self.cell_size + self.cell_size // 2

            if self.grid_index[cell_num] == 'E':
                if self.player == 'X':
                    self.canvas.create_text(
                        cell_x, cell_y,
                        text='X',
                        fill='red',
                        font=('Helvetica', 48),
                        tag = "grid"
                    )

                    self.grid_index[cell_num] = 'X'

                else:
                    self.canvas.create_text(
                        cell_x, cell_y,
                        text='O',
                        fill='blue',
                        font=('Helvetica', 48),
                        tag = "grid"
                    )

                    self.grid_index[cell_num] = 'O'
                    
                # Switch player
                if self.player == 'X':
                    self.player = 'O'
                else:
                    self.player = 'X'


    # def check_win():
        # win_state = [[1,2,3,4],[2,3,4,5],[6,7,8,9],[7,8,9,10],[11,12,13,14],[12,13,14,15],[16,17,18,19],[17,18,19,20],[21,22,23,24],[22,23,24,25]
        #             [1,6,11,16],[2,7,12,17],[7,12,17,22],[3,8,13,18],[8,13,18,23],[4,9,14,19],[9,14,19,24],[5,10,15,20],[10,15,20,25],
        #             [6,12,18,24],[1,7,13,19],[7,13,19,25],[2,8,14,20],[4,8,12,16],[5,9,13,17],[9,13,17,21],[10,14,18,22]                     
        #              ]

            

    def close_window(self):
        self.window.destroy()

    def start(self):
        self.window.mainloop()

        """POROVNAVAT WIN STATY S LISTOM KTORY SA BUDE MENIT NA ZAKLADE INPUTOV"""




game = TicTacToe()
game.start()