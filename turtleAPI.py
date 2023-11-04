import turtle as tl

class turtle(tl.Pen):
    def __init__(self):
        super().__init__()
    
    def drawRect(self, x, y, width, height, angle=0):
        self.moveTo(x, y)
        
        self.setheading(angle)
        
        for i in range(2):
            self.forward(width)
            self.right(90)
            self.forward(height)
            self.right(90)
    
    def drawGrid(self, x, y, size, width, height):
        self.moveTo(x, y)

        self.s_pos = self.pos()
        self.right(90)
        self.forward(size * height)
        self.moveTo(self.s_pos[0], self.s_pos[1])
        self.left(90)
        for i in range(width - 1):
            self.forward(size)
            self.s_pos = self.pos()
            self.right(90)
            self.forward(size * height)
            self.moveTo(self.s_pos[0], self.s_pos[1])
            self.left(90)
        
        self.forward(size)
        self.s_pos = self.pos()
        self.right(90)
        self.forward(size * height)
        
        self.right(90)
        
        for i in range(height):
            self.s_pos = self.pos()
            self.forward(size * width)
            self.moveTo(self.s_pos[0], self.s_pos[1])
            self.right(90)
            self.forward(size)
            self.left(90)
        
    def moveTo(self, x, y):
        self.up()
        self.goto(x, y)
        self.down()