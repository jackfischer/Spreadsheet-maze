import tkinter #for graphics
import csv #to read CSV spreadsheet

#Set up window
window = tkinter.Tk() #generate window
canvas = tkinter.Canvas(window, width=500, height=500) #set up canvas to draw in it
canvas.grid() #set cavnas to grid mode; special tkinter thing.

#Turn spreadsheet into 2D list
f = open("board template.csv") #open spreadsheet csv file
spreadsheet = csv.reader(f, dialect='excel') #interpret file as CSV spreadsheet
spreadsheet = list(spreadsheet) #transform into a 2D list
for line in spreadsheet:
  print(line)

#Traverse 2D list and draw board
for row in range(10): #sheet rows
  for col in range(10): #sheet columns
    if spreadsheet[row][col] == 'X': #check if cell is X
      y0 = row * 50
      x0 = col * 50
      y1 = y0 + 50
      x1 = x0 + 50
      canvas.create_rectangle(x0, y0, x1, y1, fill='pink')

#Set up and draw player
player_row = 0 #we want player oval to be small, so
player_col = 0 #within a cell, from 10,10 to 40,40 instead of 0,0 to 50,50
player_tkinter_id = None #will hold int identifying oval, so we can remove it #TODO try getting rid of
def redraw_player():
  global player_tkinter_id #out of scope
  canvas.delete(player_tkinter_id) #remove old oval
  player_x = player_row * 50 + 10
  player_y = player_col * 50 + 10
  player_tkinter_id = canvas.create_oval(player_x, player_y, player_x+30, player_y+30, fill='blue') #create new oval
  print("Player now at %d,%d" % (player_x, player_y))
redraw_player() #draw player for first time


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
def left(event): #called when a left keypress happens
  global player_col #outside of scope
  future_col = player_col - 1 #where it would go
  if no_wall(player_row, future_col): #wall in the future spot?
    player_col = future_col #if not, change coordinate
  redraw_player() #delete the old player and put a new one with new coordinates

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

#Tell tkinter to call correct functions upon corresponding key presses
window.bind('<Left>', left)
window.bind('<Right>', right)
window.bind('<Down>', down)
window.bind('<Up>', up)

#Tkinter should put the window up and start the event loop waiting for keys
window.mainloop()
