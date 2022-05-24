from tkinter import *
import random
import time



def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")

   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")
      


window_size = 20
rain_rate = 0.1
drop_increase = 5
reset_size = 20


window = Tk()
window.geometry("1000x1000")
window.title("My first GUI")
##window.configure(background="grey")

canvas_width = 1000
canvas_height = 1000

canvas = Canvas(window , width=1000, height=1000 , bg="blue")
canvas.pack()






row = 20
column = 20
axis = [0] * row
for i in range(row):
    axis[i] = [0] * column
    ##print("i is " + str(i) + " colum is "  + str(column))
    
    ##print(axis[i])
    
    ##a.append([0]*m)
    
xaxis = canvas_width/column
yaxis = canvas_height/row
##size = 2
count= 0
def drawCanvas():
   
   canvas.delete("all")
   checkered(canvas, 50)
   
   for i, e in enumerate(axis):
       ##canvas.create_oval(((canvas_width/column)*i)-10,(canvas_height/row)-10,((canvas_width/column)*i)+10,(canvas_height/row)+10, fill="cyan" , tags=('drop'))
       for val, size in enumerate(e): ## Grid Intersection Loop
         ## print(val)
         ## print(i)
          ##count= count + 1
          drop = canvas.create_oval((xaxis*i)-(2+size),yaxis*val-(2+size),(xaxis*i)+(2+size),yaxis*val+(2+size), fill="cyan" , tags=('drop'))
          ##print("Created drop" + str(count))
          ranVal = random.uniform(0,1)
         ## print(ranVal)
          if ranVal < rain_rate:
             ## use taged
             ## oval plus drop size in both directions
             canvas.delete(drop)
             if size >= reset_size:
                size = size - size
                underneathDrop = column-val
                toDrop = val
                while toDrop < column:
                   print("toDrop : " + str(toDrop) + " i is " + str(i) + "val is " + str(val))
                   axis[i][toDrop] = size
                   toDrop = toDrop + 1
                   
             else:
                size = size + drop_increase
                drop = canvas.create_oval((xaxis*i)-(2+size),yaxis*val-(2+size),(xaxis*i)+(2+size),yaxis*val+(2+size), fill="cyan" , tags=('drop'))
                axis[i][val] = size
                print(size)
                print("i is " + str(i) + " val is " + str(val))
                ##print("true move")
   ##canvas.pack()
   window.update()
   time.sleep(0.1)
   

   
    
    ##canvas.create_oval(240, 240, 260, 260, fill="cyan")

##for i in axis:
##    row = 2
##    for col in row:
##        row[col].append(row)
##        print(axis)
        
   ##canvas.create_oval(canvas_width/column*a,,,, fill="cyan")


##axis = [[1, 2], [1, 2]]

drawCanvas()

while count < 100:
  
   drawCanvas()
  
   count = count +1
   ##print(count)
   print(axis)

window.mainloop()




