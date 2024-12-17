import tkinter as tk
from tkinter import Label




# ----------------- Change actions ----------------- #
def change_action_to_x():
    if not player["x"]:
        player['x'] = True
        player['player'] = "X"

def change_action_to_o():
    if player["x"]:
        player['x'] = False
        player['player'] = "O"

# ----------------- Check the winning status ----------------- #
def check_win():
    # Vertical and horizontal win case
    for i in range(3):
        if (buttons[(i, 0)].cget("text") == buttons[(i, 1)].cget("text") == buttons[(i, 2)].cget("text") != "" or
            buttons[(0, i)].cget("text") == buttons[(1, i)].cget("text") == buttons[(2, i)].cget("text") != ""):
            winner.config(text=f"{player['player']} Wins!")
            winner.grid(row=5, column=0, sticky="nsew")
            return True

    # Diagonal win case
    if (buttons[(0, 0)].cget("text") == buttons[(1, 1)].cget("text") == buttons[(2, 2)].cget("text") != "" or
        buttons[(0, 2)].cget("text") == buttons[(1, 1)].cget("text") == buttons[(2, 0)].cget("text") != ""):
        winner.config(text=f"{player['player']} Wins!")
        winner.grid(row=5, column=0, sticky="nsew")
        return True

    # Draw case
    may_draw = None
    for pos in buttons:
        if buttons[pos].cget("text") == "":
            return False
        else:
            may_draw = True

    if may_draw:
        winner.config(text=f"Draw!")
        winner.grid(row=5, column=0, sticky="nsew")
        return True



# ----------------- Disable play when player wins ----------------- #
def disable_play():
    for pos in buttons:
        buttons[pos].config(state="disabled")

# ----------------- Restart game (clear) ----------------- #
def restart_game():
    winner.config(text="")
    for pos in buttons:
        buttons[pos].config(state="normal", text="")


# ----------------- Cross where it is clicked ----------------- #
def cross(r, c):
    buttons[(r, c)].config(text="X")
    check_win()

    if check_win():
        restart_button.config(state="normal")
        disable_play()

    change_action_to_o()

# ----------------- Circle where it is clicked ----------------- #
def circle(r, c):
    buttons[(r, c)].config(text="O")
    check_win()

    if check_win():
        restart_button.config(state="normal")
        disable_play()

    change_action_to_x()


# ---------------------- UI ---------------------- #
# ----------------- TK Root ----------------- #
root = tk.Tk()
root.title("TicTacToe")

# ----------------- Window Scale ----------------- #
root.configure(background='grey', padx=20, pady=20)

# Needed dictionaries
player = {"x": True, "player": "X"}
buttons = {}

# Toolbar
winner = Label(root, text=f"{player['player']} Wins!", bg="grey")
restart_button = tk.Button(root, text="Restart", command=restart_game, padx=5, pady=5)


def set_ui():
    global restart_button
    for row in range(3):
        for col in range(3):
            cell = tk.Button(
                root,
                text="",
                width=10,
                height=5,
                borderwidth=1,
                command=lambda r=row, c=col: cross(r, c) if player['x'] else circle(r, c)
            )
            cell.grid(row=row, column=col)
            buttons[(row, col)] = cell

    action_cross = tk.Button(root, text="I'm 'x'", command=change_action_to_x, padx=5, pady=5)
    action_cross.grid(row=3, column=0, sticky="nsew", pady=5)
    action_circle = tk.Button(root, text="I'm 'o'", command=change_action_to_o, padx=5, pady=5)
    action_circle.grid(row=3, column=1, sticky="nsew", pady=5)


    restart_button.grid(row=4, column=0, pady=5, sticky="nsew")


set_ui()


root.mainloop()





















