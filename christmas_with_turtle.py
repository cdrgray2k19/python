"""create christmas scene using python turtle
current ideas - snowflake - tree - snowdrops on random places on the screen - presents - text

pseudo code to plan project:

imports here

class Text():
    def __init__(self, message, size, color, font, style, position, x, y):
        #initialise variables

    def draw():
        configure text variables then write them on the screen

class snowflake():

    def __init(x and y position, size, how many times we would like to call our recursive fractal function):
        #initialise variables


    def draw():
        #call recursive methods iterating it 6 times with for loop


    def fractal(number of recursions, size of starting pen):
        if order == 0 then draw a line

        call function again

        this will basically just produce 4 x the number of recursions of a straight line with various angle changes to create a fractal shape

        got the shape idea from online:

        it is called the koch snowflake



        link ---> https://www.google.com/search?q=koch+snowflake&safe=strict&rlz=1C5CHFA_enGB892GB892&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiiz_SFucHtAhWqWhUIHY1ZC3QQ_AUoAXoECB0QAw&biw=1440&bih=821#imgrc=Ffl1AthA6ShQkM


class tree():

    def __init__(x and y position, size, how many times we would like to call our recursive fractal function):

        initialise variables


    def draw():
        call star and then call fractal function for the tree part

    def draw_star():
        draw star on top of christmas tree
    
    def fractal():
        if order == 0:
            return
        else:
            forward(size)
            call function again with order-1 and a 0.8 less size
            right(120)
            call function again with order-3 and a 0.5 less size
            right(120)
            call function again with order-3 and a 0.5 less size
            right(120)
            back(size)

        
        #this goes forwards and then draws smaller branches each going back on each other which will then allow the tree to go onto draw different branches with a main 'trunk' down the middle

class snowball():

    def __init__(random x and y position, size, colour of pen):
        initialise variabels


    def draw():
        draw small ciclical shape

class present():
    def __init__(random x and y position, size, color, fill color):
        initialise variables
    
    def draw():
        reference methods to to draw square, ribbons, then bow

    #extra methods down here




create objects which will then be drawn using methods

mainloop to keep page open
"""


#import libraries

import turtle
import time
from random import randint

#create references to actual turtle and the screen
t = turtle.Turtle()
wn = turtle.Screen() 
#hides the turtle while drawing
t.ht()
#set the fastest speed for turtle to draw at
t.speed(0)

#sets background colour to black which will help us see snow better in image
wn.bgcolor('black')

#set width and height for screen then make variables to reference values easier
wn.setup(width=1500,height=900)

WIDTH = int(wn.window_width())
HEIGHT = int(wn.window_height())


#set title
wn.title("Python Christmas Scene")


#create classses

class Text():
    def __init__(self, message, size, color, font, style, position, x, y):
        #initalise variables
        self.message = message
        self.size = size
        self.color = color
        self.font = font
        self.style = style
        self.position = position
        self.x = x
        self.y = y

    def draw(self):
        #set pen color and change x and y coordinates
        t.color(self.color)
        t.up()
        t.home()
        t.goto(self.x - WIDTH/2, HEIGHT/2-self.y)
        t.down()
        #create template for text and then write the text with a message, font and alignment
        template = (self.font, self.size, self.style)
        t.write(self.message, font = template, align  = self.position)
        

class Snowflake():

    def __init__(self, x, y, size, order):
        #initalise variables
        self.x = x
        self.y = y
        self.size = size
        self.order = order

    def draw(self):
        #set pen color and change x and y coordinates
        t.color('lightblue', 'lightblue')
        t.up()
        t.home()
        t.goto(self.x - WIDTH/2, HEIGHT/2-self.y)
        t.down()
        t.begin_fill()
        #call fractal method 6 times each time turning left 60 degrees to from a snowflake shape with 6 identical sides
        for _ in range(0, 6):
            self.fractal(self.order, self.size)
            t.left(60)
        t.end_fill()

    def fractal(self, order, size):
        #if order of n is 0 then it draws a straight line
        #otherwise it calls itself agian using recursion and adjusts with corresponding angles in array
        if order == 0:
            t.forward(size)
        else:
            for angle in [60, -120, 60, 0]:
                self.fractal(order-1, size/3)
                t.left(angle)

class Tree():
    def __init__(self, x, y, size, order):
        #initalise variables
        self.x = x
        self.y = y
        self.size = size
        self.order = order
    
    def draw(self):
        #set pen color and change x and y coordinates
        t.up()
        t.home()
        t.goto(self.x - WIDTH/2, HEIGHT/2-self.y)
        t.left(90)
        t.color('orange', 'yellow')
        t.forward(self.size * 4.8)
        t.left(126)
        t.down()
        #begin filling turtle color and call star method
        t.begin_fill()
        self.star_draw()
        t.end_fill()
        #change color, position turtle, and then draw tree using fractal method
        t.right(126)
        t.pencolor('green')
        t.back(self.size * 4.8)
        self.fractal(self.order, self.size)


    def star_draw(self):
        #draw pentagon for star
        for _ in range(0,5):
            for angle in [144, -72]:
                t.forward(self.size/5)
                t.right(angle)


    def fractal(self, order, size):
        #draw tree fractal
        if order <= 0:
            return
        t.forward(size)
        self.fractal(order-1, size*0.8)
        t.left(120)
        self.fractal(order-3, size*0.5)
        t.left(120)
        self.fractal(order-3, size*0.5)
        t.left(120)
        t.back(size)

class Snowball():

    def __init__(self, x, y, size) :
        #initalise variables
        self.x = x
        self.y = y
        self.size = size
    
    def draw(self):
        #set pen color and change x and y coordinates
        t.color('white', 'white')
        t.up()
        t.home()
        t.goto(self.x - WIDTH/2, HEIGHT/2-self.y)
        t.down()
        #begin fillinf turtle and draw circle for snowball
        t.begin_fill()
        t.circle(self.size)
        t.end_fill()

class Presents():

    def __init__(self, x, y, size, color, bg_color):
        #initalise variables
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.bg_color = bg_color

    def draw(self):
        #set pen color and change x and y coordinates
        t.color(self.color, self.color)
        t.up()
        t.home()
        t.goto(self.x - WIDTH/2, HEIGHT/2-self.y)
        t.down()
        t.begin_fill()
        self.square()
        t.end_fill()
        t.color(self.color, self.bg_color)
        self.both_ribbbons()
        t.color(self.color, self.color)
        t.begin_fill()
        self.bow()
        t.end_fill()

    def square(self):
        #create base for present
        for _ in range(0, 4):
            t.forward(self.size)
            t.left(90)

    def both_ribbbons(self):
        #draw two ribbons over base square for presents
        self.single_ribbon()
        t.forward(self.size/2 - self.size/20)
        t.left(90)
        self.single_ribbon()

    def single_ribbon(self):
        #draw single ribbon
        t.forward(self.size/2 + self.size/20)
        t.begin_fill()
        for _ in range(0, 2):
            for size in [self.size, self.size/10]:
                t.left(90)
                t.forward(size)
        t.end_fill()

    def bow(self):
        #draw bow at top by drawing two rectangles at angles of top of base shape of present
        #go to top of present sqaure to draw bows
        t.forward(self.size/2 - self.size/20)
        t.left(90)
        t.forward(self.size/2)
        t.right(60)

        #draw one string of the bow
        self.string()
        
        #reconfigure position to draw second string of the bow
        t.left(110)

        #draw one string of the bow
        self.string()

    def string(self):
        #draw rectangle for a bow
        t.forward(self.size/3)
        t.right(90)
        t.forward(self.size/20)
        t.right(90)
        t.forward(self.size/3)


#create objects and then draw them to screen

for _ in range(0, 50):
    S1 = Snowball(randint(50, 1450), randint(50, 850), 10)
    S1.draw()

Title_Text = Text('Christmas Scene', 50, 'gold', 'Courier', 'italic', 'center', 750, 50)
Title_Text.draw()

Credit_Text = Text('By Charlie Gray', 30, 'gold', 'Courier', 'italic', 'center', 750, 100)
Credit_Text.draw()

P1 = Presents(500, 650, 50, 'red', 'blue')
P1.draw()

P2 = Presents(950, 650, 50, 'blue', 'red')
P2.draw()

SF1 = Snowflake(100, 200, 100, 4)
SF1.draw()

SF2 = Snowflake(1250, 200, 100, 4)
SF2.draw()

SF3 = Snowflake(100, 800, 100, 4)
SF3.draw()

SF4 = Snowflake(1250, 800, 100, 4)
SF4.draw()

T1 = Tree(750, 550, 75, 15)
T1.draw()

#carry on a main loop until exit button is pressed
wn.mainloop()