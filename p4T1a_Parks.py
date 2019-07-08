import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
alex = turtle.Turtle()    # Create a turtle, assign to alex

#commands from here to the last line can be replaced 

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(6)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees

t.forward(100)          
t.left(120)            
t.forward(100)
t.left(120)
t.forward(100)
t.forward(50)          # Tell alex to move forward by 50 units
t.left(90)             # Tell alex to turn by 90 degrees
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# end commands
win.mainloop()             # Wait for user to close window
