from tkinter import *

class MyPaint:

    root = Tk()
    x1 = 10
    x2 = 10
    y1 = 10
    y2 = 10
    colorVar = StringVar()
    color = "Black"
    fill = False
    currentShape = "line"

    if fill == False:
        color = 'white'
        pass

    def __init__(self):

        self.root.title("MyPaint")

        self.canvas = Canvas(self.root, width = 750, height = 500, bg = "white")
        self.canvas.pack()



        menubar = Menu(self.root)
        self.root.config(menu = menubar)

        operationMenu = Menu(menubar, tearoff = 0)


        filemenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "Clear", command = self.clearCanvas)
        filemenu.add_command(label = "Quit", command = self.root.quit)


        menubar.add_cascade(label = "Shape", menu = operationMenu)
        operationMenu.add_command(label = "Rectangle", command = self.shapeRectangle)
        operationMenu.add_command(label = "Oval", command = self.shapeOval)
        operationMenu.add_command(label = "Line", command = self.shapeLine)
        operationMenu.add_command(label = "Arc", command = self.shapeArc)

        colormenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Color", menu = colormenu)
        colormenu.add_command(label = "Red", command = self.setRed)
        colormenu.add_command(label = "Orange", command = self.setOrange)
        colormenu.add_command(label = "Yellow", command = self.setYellow)
        colormenu.add_command(label = "Green", command = self.setGreen)
        colormenu.add_command(label = "Blue", command = self.setBlue)
        colormenu.add_command(label = "Purple", command = self.setPurple)
        colormenu.add_command(label = "Brown", command = self.setBrown)
        colormenu.add_command(label = "Black", command = self.setBlack)

        #place buttons in frame
        colorFrame = Frame(self.root)
        colorFrame.pack()

        btRed = Radiobutton(colorFrame, text = "Red", bg = "Red", variable = self.colorVar, value = "Red", command = self.setRed)
        btOrange = Radiobutton(colorFrame, text = "Orange", bg = "Orange", variable = self.colorVar, value = "Orange", command = self.setOrange)
        btYellow = Radiobutton(colorFrame, text = "Yellow", bg = "Yellow", variable = self.colorVar, value = "Yellow", command = self.setYellow)
        btGreen = Radiobutton(colorFrame, text = "Green", bg = "Green", variable = self.colorVar, value = "Green", command = self.setGreen)
        btBlue = Radiobutton(colorFrame, text = "Blue", bg = "Blue", variable = self.colorVar, value = "Blue", command = self.setBlue)
        btPurple = Radiobutton(colorFrame, text = "Purple", bg = "Purple", variable = self.colorVar, value = "Purple", command = self.setPurple)
        btBrown = Radiobutton(colorFrame, text = "Brown", bg = "Brown", variable = self.colorVar, value = "Brown", command = self.setBrown)
        btBlack = Radiobutton(colorFrame, text = "Black", bg = "Black", variable = self.colorVar, value = "Black", command = self.setBlack)

        btRed.grid(row = 0, column = 0)
        btOrange.grid(row = 0, column = 1)
        btYellow.grid(row = 0, column = 2)
        btGreen.grid(row = 0, column = 3)
        btBlue.grid(row = 0, column = 4)
        btPurple.grid(row = 0, column = 5)
        btBrown.grid(row = 0, column = 6)
        btBlack.grid(row = 0, column = 7)

        frame = Frame(self.root)
        frame.pack()

        btRectangle = Button(frame, text = "Rectangle", command = self.shapeRectangle)
        btOval = Button(frame, text = "Oval", command = self.shapeOval)
        btLine = Button(frame, text = "Line", command = self.shapeLine)
        btArc = Button(frame, text = "Arc", command = self.shapeArc)
        btClear = Button(frame, text = 'clear', command = self.clearCanvas)

        btRectangle.grid(row = 1, column = 1)
        btOval.grid(row = 1, column = 2)
        btLine.grid(row = 1, column = 3)
        btArc.grid(row = 1, column = 4)
        btClear.grid(row = 1, column = 5)

        frame2 = Frame(self.root)
        frame2.pack()

        rbYesFill = Radiobutton(frame2, text = 'Fill', variable = self.fill, value = True, command = self.fillTrue)
        rbNoFill = Radiobutton(frame2, text = 'No Fill', variable = self.fill, value = False, command = self.fillFalse)

        rbYesFill.grid(row = 2, column = 1)
        rbNoFill.grid(row = 2, column = 2)

        self.canvas.bind('<Button-1>', self.startShape)
        self.canvas.bind('<B1-Motion>', self.drawShape)
        self.canvas.bind('<ButtonRelease-1>', self.drawShape)

        self.root.mainloop()

    #display rectangle
    def shapeRectangle(self):
        self.currentShape = 'rectangle'

    #display an oval
    def shapeOval(self):
        self.currentShape = 'oval'

    #display a line
    def shapeLine(self):
        self.currentShape = 'line'

    def shapeArc(self):
        self.currentShape = 'arc'

    def clearCanvas(self):
        self.canvas.delete('rectanglered', 'rectangleorange', 'rectangleyellow', \
        'rectanglegreen', 'rectangleblue', 'rectanglepurple', 'rectanglebrown', \
        'rectangleblack', 'ovalred', 'ovalorange', 'ovalyellow', 'ovalgreen', \
        'ovalblue', 'ovalpurple', 'ovalbrown', 'ovalblack', 'linered', 'lineorange', \
        'lineyellow', 'linegreen', 'lineblue', 'linepurple', 'linebrown', 'lineblack', \
        'arcred', 'arcorange', 'arcyellow', 'arcgreen', 'arcblue', 'arcpurple', 'arcbrown', \
        'arcblack')

    def fillTrue(self):
        self.fill = True;
        pass

    def fillFalse(self):
        self.fill = False;
        self.color = 'white'
        pass

    #set color to Red
    def setRed(self):
        self.color = 'red'
        pass

    #set color to orange
    def setOrange(self):
        self.color = 'orange'
        pass

    #set color to Yellow
    def setYellow(self):
        self.color = 'yellow'
        pass

    #set color to Green
    def setGreen(self):
        self.color = 'green'
        pass

    #set color to Blue
    def setBlue(self):
        self.color = 'blue'
        pass

    #set color to Purple
    def setPurple(self):
        self.color = 'purple'
        pass

    #set color to Brown
    def setBrown(self):
        self.color = 'brown'
        pass

    #set color to Black
    def setBlack(self):
        self.color = 'black'
        pass

    def startShape(self, event):
        self.x1 = event.x
        self.y1 = event.y
        pass

    def drawShape(self, event):
        self.x2 = event.x
        self.y2 = event.y

        if self.currentShape == 'arc':

            if self.color == 'red':
                self.canvas.delete('arcred')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcred')

            elif self.color == 'orange':
                self.canvas.delete('arcorange')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcorange')

            elif self.color == 'yellow':
                self.canvas.delete('arcyellow')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcyellow')

            elif self.color == 'green':
                self.canvas.delete('arcgreen')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcgreen')

            elif self.color == 'blue':
                self.canvas.delete('arcblue')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcblue')

            elif self.color == 'purple':
                self.canvas.delete('arcpurple')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcpurple')

            elif self.color == 'brown':
                self.canvas.delete('arcbrown')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcbrown')

            elif self.color == 'black':
                self.canvas.delete('arcblack')
                self.canvas.create_arc(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'arcblack')

        if self.currentShape == 'line':

            if self.color == 'red':
                self.canvas.delete('linered')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'linered')

            elif self.color == 'orange':
                self.canvas.delete('lineorange')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'lineorange')

            elif self.color == 'yellow':
                self.canvas.delete('lineyellow')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'lineyellow')

            elif self.color == 'green':
                self.canvas.delete('linegreen')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'linegreen')

            elif self.color == 'blue':
                self.canvas.delete('lineblue')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'lineblue')

            elif self.color == 'purple':
                self.canvas.delete('linepurple')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'linepurple')

            elif self.color == 'brown':
                self.canvas.delete('linebrown')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'linebrown')

            elif self.color == 'black':
                self.canvas.delete('lineblack')
                self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'lineblack')

        elif self.currentShape == 'rectangle':

            if self.color == 'red':
                self.canvas.delete('rectanglered')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectanglered'))

            elif self.color == 'orange':
                self.canvas.delete('rectangleorange')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectangle' + 'orange'))

            elif self.color == 'yellow':
                self.canvas.delete('rectangleyellow')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectangle' + 'yellow'))

            elif self.color == 'green':
                self.canvas.delete('rectanglegreen')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectangle' + 'green'))

            elif self.color == 'blue':
                self.canvas.delete('rectangleblue')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectangle' + 'blue'))

            elif self.color == 'purple':
                self.canvas.delete('rectanglepurple')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectangle' + 'purple'))

            elif self.color == 'brown':
                self.canvas.delete('rectanglebrown')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectangle' + 'brown'))

            elif self.color == 'black':
                self.canvas.delete('rectangleblack')
                self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = str('rectangle' + 'black'))

        elif self.currentShape == 'oval':

            if self.color == 'red':
                self.canvas.delete('ovalred')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalred')

            elif self.color == 'orange':
                self.canvas.delete('ovalorange')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalorange')

            elif self.color == 'yellow':
                self.canvas.delete('ovalyellow')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalyellow')

            elif self.color == 'green':
                self.canvas.delete('ovalgreen')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalgreen')

            elif self.color == 'blue':
                self.canvas.delete('ovalblue')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalblue')

            elif self.color == 'purple':
                self.canvas.delete('ovalpurple')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalpurple')

            elif self.color == 'brown':
                self.canvas.delete('ovalbrown')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalbrown')

            elif self.color == 'black':
                self.canvas.delete('ovalblack')
                self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, \
                fill = self.color, tags = 'ovalblack')

        pass



MyPaint() #create gui
