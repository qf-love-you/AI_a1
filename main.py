import os
import random
import time
import turtle as tl
import turtleAPI as tla
import math

def top(x, y):
    global mine
    if mine:
        x_, x__, y_, y__ = -200, -1, 205, -1
        k, l = -1, -1
        for i in range(9):
            if max(x, x_) - min(x_, x) <= 10:
                x__ = x_
                k = i
                break
            x_ += 50
        
        for i in range(9):
            if max(y, y_) - min(y_, y) <= 20:
                y__ = y_
                l = i
                break
            y_ -= 50
        
        if chessman[l][k] == 0 and (x__ != -1 and y__ != -1 and k != -1 and l != -1):
            # print(x__, y__, k, l)
            chessman[l][k] = 1
            
            pen.moveTo(x__, y__)
            pen.color('black')
            pen.dot(30)
            
            screen.update()
            
            x, y = AI(k, l)
            
            pen.moveTo(x, y)
            pen.color('white')
            pen.dot(30)
    # print(chessman, '\n')

def AI(x__, y__):
    x, y, w, black, g, p = 0, 5, False, 0, -1, -1
    
    for i in chessman:
        p, black = -1, 0
        black = 0
        g += 1
        for j in i:
            p += 1
            if j == 1:
                try:
                    black += 1
                    
                    if black >= 5:
                        time.sleep(5)
                        os._exit(0)
                    
                    if black == 1 and chessman[g][p - 1] == 0 and chessman[g][p - 2] == 1:
                        y = 205 - g * 50
                        x = -200 + (p - 1) * 50
                        chessman[g][p - 1] = 2
                        return x, y
                    
                    elif black == 1 and chessman[g - 1][p] == 0 and chessman[g - 1][p - 1] == 1 \
                            and (chessman[g + 1][p] == 1 or chessman[g - 1][p - 2] == 1):
                        y = 205 - (g - 1) * 50
                        x = -200 + p * 50
                        chessman[g - 1][p] = 2
                        return x, y
                    
                    elif black == 2 and chessman[g][p + 1] == 0 and chessman[g][p + 2] == 1:
                        y = 205 - g * 50
                        x = -200 + (p + 1) * 50
                        chessman[g][p + 1] = 2
                        return x, y
                    
                    if p < 4:
                        if black == 3 and chessman[g][p + 1] == 0:
                            y = 205 - g * 50
                            x = -200 + (p + 1) * 50
                            chessman[g][p + 1] = 2
                            return x, y
                        elif black == 3 and chessman[g][p - 3] == 0 and p - 3 >= 0:
                            y = 205 - g * 50
                            x = -200 + (p - 3) * 50
                            chessman[g][p - 3] = 2
                            return x, y
                    else:
                        if black == 3 and chessman[g][p - 3] == 0 and p - 3 >= 0:
                            y = 205 - g * 50
                            x = -200 + (p - 3) * 50
                            chessman[g][p - 3] = 2
                            return x, y
                        elif black == 3 and chessman[g][p + 1] == 0:
                            y = 205 - g * 50
                            x = -200 + (p + 1) * 50
                            chessman[g][p + 1] = 2
                            return x, y
                    
                    if black == 4:
                        if chessman[g][p - 4] == 0 and p - 4 >= 0:
                            y = 205 - g * 50
                            x = -200 + (p - 4) * 50
                            chessman[g][p - 4] = 2
                            return x, y
                        elif chessman[g][p + 1] == 0:
                            y = 205 - g * 50
                            x = -200 + (p + 1) * 50
                            chessman[g][p + 1] = 2
                            return x, y
                        else:
                            print('does not!')
                    
                    # print(black, chessman, '\n')
                except:
                    pass
            else:
                try:
                    black = 0
                except:
                    pass
    
    for i in range(0, 9):
        black = 0
        for j in range(0, 9):
            if chessman[j][i] == 1:
                black += 1
                
                if black >= 5:
                    time.sleep(5)
                    os._exit(0)
                elif black == 3 and chessman[j + 1][i] == 0:
                    y = 205 - (j + 1) * 50
                    x = -200 + i * 50
                    chessman[j + 1][i] = 2
                    return x, y
                elif black == 4:
                    if chessman[j - 4][i] == 0 and j - 4 >= 0:
                        y = 205 - (j - 4) * 50
                        x = -200 + i * 50
                        chessman[j - 4][i] = 2
                        return x, y
                    elif chessman[j + 1][i] == 0:
                        y = 205 - (j + 1) * 50
                        x = -200 + i * 50
                        chessman[j + 1][i] = 2
                        return x, y
            else:
                black = 0
    
    return x, y

mine = True

chessman = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

pen = tla.turtle()
screen = tl.Screen()

screen.screensize(500, 300)
screen.bgcolor('#da7e00')
screen.tracer(0)
pen.hideturtle()

pen.drawGrid(-200, 205, 50, 8, 8)

screen.update()

screen.listen()
screen.onclick(top, 1)

tl.done()