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
for y in range(10): #sheet rows
  for x in range(10): #sheet columns
    if spreadsheet[y][x] == 'X': #check if cell is X
      x_left = x * 50 #calculate x/y pixels for wall block
      x_right = x_left + 50
      y_top = y * 50
      y_bottom = y_top + 50
      canvas.create_rectangle(x_left, y_top, x_right, y_bottom, fill='pink') #draw wall block

#Set up and draw player
player_x = 10 #we want player oval to be small, so
player_y = 10 #within a cell, from 10,10 to 40,40 instead of 0,0 to 50,50
player_tkinter_id = None #will hold int identifying oval, so we can remove it
def redraw_player():
  global player_tkinter_id #out of scope
  canvas.delete(player_tkinter_id) #remove old oval
  player_tkinter_id = canvas.create_oval(player_x, player_y, player_x+30, player_y+30, fill='blue') #create new oval
  print("Player now at %d,%d" % (player_x, player_y))
redraw_player() #draw player for first time


def no_wall(x_pixels: int, y_pixels: int) -> bool:
  """
  Function called after a keypress to check theoretical new location against
  spreadsheet. Returns boolean indicating whether there's a wall
  """
  row = x_pixels // 50
  if row < 0 or row > 9: #going outside the board horizontally
    return False
  col = y_pixels // 50
  if row < 0 or row > 9: #going outside the board vertically
    return False
  return spreadsheet[y][x] == 'O' #inside board, check exact cell


#Functions called after keypresses
def left(event): #called when a left keypress happens
  global player_x #outside of scope
  future_x = player_x - 50 #where it would go
  if no_wall(future_x, player_y): #wall in the future spot?
    player_x = future_x #if not, change coordinate
  redraw_player() #delete the old player and put a new one with new coordinates

def right(event): #comments above apply
  global player_x
  future_x = player_x + 50
  if no_wall(future_x, player_y):
    player_x = future_x
  redraw_player()

def up(event):
  global player_y
  future_y = player_y - 50
  if no_wall(player_x, future_y):
    player_y = future_y
  redraw_player()

def down(event):
  global player_y
  future_y = player_y + 50
  if no_wall(player_x, future_y):
    player_y = future_y
  redraw_player()

#Tell tkinter to call correct functions upon corresponding key presses
window.bind('<Left>', left)
window.bind('<Right>', right)
window.bind('<Down>', down)
window.bind('<Up>', up)

#Tkinter should put the window up and start the event loop waiting for keys
window.mainloop()
