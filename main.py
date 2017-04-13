import tkinter #for graphics
import csv #to read CSV spreadsheet

#Set up window
window = tkinter.Tk() #generate window
canvas = tkinter.Canvas(window, width=500, height=500) #set up canvas to draw in it
canvas.grid() #set cavnas to grid mode; special tkinter thing.

#Set up walls
f = open("board template.csv") #open spreadsheet csv file
spreadsheet = csv.reader(f, dialect='excel') #interpret file as CSV spreadsheet
spreadsheet = list(spreadsheet) #transform into a 2D list

for x in range(10):
  for y in range(10):
    if spreadsheet[x][y] == 'X':
      x_left = x * 50
      x_right = x_left + 50
      y_top = y * 50
      y_bottom = y_top + 50
      canvas.create_rectangle(x_left, y_top, x_right, y_bottom, fill="pink")

def left(event):
  print(event)
def right(event):
  print(event)
def up(event):
  print(event)
def down(event):
  print(event)
window.bind('<Left>', left)
window.bind('<Right>', right)
window.bind('<Down>', down)
window.bind('<Up>', up)

window.mainloop()
#while True:
#  window.update_idletasks()
#  window.update()
