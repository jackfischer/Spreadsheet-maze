import tkinter
import csv

#Set up window
window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=500, height=500)
canvas.grid()

#Turn spreadsheet into 2D list
f = open("board template.csv")
spreadsheet = csv.reader(f, dialect='excel')
spreadsheet = list(spreadsheet)
for line in spreadsheet:
  print(line)

#Traverse 2D list and draw board
for row in range(10):
  for col in range(10):
    if spreadsheet[row][col] == 'X':
      y0 = row * 50
      x0 = col * 50
      y1 = y0 + 50
      x1 = x0 + 50
      canvas.create_rectangle(x0, y0, x1, y1, fill='pink')

#Set up and draw player
player_row = 0
player_col = 0
player_tkinter_id = None #hold int identifying oval
def redraw_player():
  global player_tkinter_id
  canvas.delete(player_tkinter_id)
  player_x = player_col * 50 + 10
  player_y = player_row * 50 + 10
  player_tkinter_id = canvas.create_oval(player_x, player_y, player_x+30, player_y+30, fill='blue') #create new oval
  print("Player now at %d,%d" % (player_x, player_y))
redraw_player() #draw intial player


def no_wall(row: int, col: int) -> bool:
  """
  Function called after a keypress to check theoretical new location against
  spreadsheet. Returns boolean indicating whether there's a wall
  """
  if col < 0 or col > 9: #going outside the board horizontally
    return False
  if row < 0 or row > 9: #going outside the board vertically
    return False
  return spreadsheet[row][col] == 'O'


#Functions called after keypresses
def left(event):
  global player_col
  future_col = player_col - 1
  if no_wall(player_row, future_col):
    player_col = future_col
  redraw_player()

def right(event):
  global player_col
  future_col = player_col + 1
  if no_wall(player_row, future_col):
    player_col = future_col
  redraw_player()

def up(event):
  global player_row
  future_row = player_row - 1
  if no_wall(future_row, player_col):
    player_row = future_row
  redraw_player()

def down(event):
  global player_row
  future_row = player_row + 1
  if no_wall(future_row, player_col):
    player_row = future_row
  redraw_player()

window.bind('<Left>', left)
window.bind('<Right>', right)
window.bind('<Down>', down)
window.bind('<Up>', up)

window.mainloop()
