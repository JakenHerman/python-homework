from tkinter import *

class MyPaint:

    x1 = 10
    x2 = 10
    y1 = 10
    y2 = 10
    color = "Red"
    fill = False

    def __init__(self):
        window = Tk()
        window.title("MyPaint")

        self.canvas = Canvas(window, width = 750, height = 500, bg = "white")
        self.canvas.pack()



        menubar = Menu(window)
        window.config(menu = menubar)

        operationMenu = Menu(menubar, tearoff = 0)


        filemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "Clear", command = self.clearCanvas)
        filemenu.add_command(label = "Quit", command = window.quit)


        menubar.add_cascade(label = "Shape", menu = operationMenu)
        operationMenu.add_command(label = "Rectangle", command = self.displayRect)
        operationMenu.add_command(label = "Oval", command = self.displayOval)



        #place buttons in frame
        colorFrame = Frame(window)
        colorFrame.pack()

        btOrange = Radiobutton(colorFrame, text = "Orange", bg = "Orange", variable = self.color,
        value = "Orange", command = self.setColor("Orange", self.getColor()))
        
        btPurple = Radiobutton(colorFrame, text = "Purple", bg = "Purple", variable = self.color,
        value = "Purple", command = self.setColor("Purple", self.getColor()))

        btOrange.grid(row = 0, column = 1)
        btPurple.grid(row = 0, column = 2)

        frame = Frame(window)
        frame.pack()

        btRectangle = Button(frame, text = "Rectangle", command = self.displayRect)
        btOval = Button(frame, text = "Oval", command = self.displayOval)
        btClear = Button(frame, text = 'clear', command = self.clearCanvas)

        btRectangle.grid(row=1, column = 1)
        btOval.grid(row=1, column = 2)
        btClear.grid(row=1, column = 3)

        frame2 = Frame(window)
        frame2.pack()

        rbYesFill = Radiobutton(frame2, text = 'Fill', variable=self.fill, value = True, command = self.fillTrue)
        rbNoFill = Radiobutton(frame2, text = 'No Fill', variable=self.fill, value = False, command = self.fillFalse)

        rbYesFill.grid(row = 2, column = 1)
        rbNoFill.grid(row = 2, column = 2)

        window.mainloop()

    #display rectangle
    def displayRect(self):
        self.canvas.create_rectangle(10,10,190,90,tags='rect')
    #display an oval
    def displayOval(self):
        self.canvas.create_oval(self.x1 ,self.y1 ,190,90, fill = self.color, tags = 'oval')

    def clearCanvas(self):
        self.canvas.delete('rect', 'oval')

    def fillTrue(self):
        self.fill = True;
        pass

    def fillFalse(self):
        self.fill = False;
        pass

    def setColor(self, color, oldColor):

        x = self.color.replace(oldColor, color)
        pass

    def getColor(self):
        return self.color


MyPaint() #create gui
