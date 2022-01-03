from tkinter import *
#from tkinter import Tk, Canvas, Frame, BOTH
import tkinter
import  math
import math
import board
import row
import block

def init(data):
    global LC
    global b1
    global x,y,bd,nor

    #bd -> block  dimension
    #nor -> no of  rows
    x=50
    y=400
    bd=30
    nor=10

    # left click
    LC = []
    b1 = board.board(nor, bd)
    b1.boardnooffilledrows()
    data.no=b1.no
#    data.rows=b1.rows
    data.bd=bd
    print("the  no of the  rows  is", len(b1.rows))

# def mousePressed(event, data):
#     b1 = board.board(nor, bd)
#     data.rows=b1.rows
#     print("the  mousepressed has  been called")

def mousePressed(event, data):
    RC=[]
    if event.num == 1:
        LC.clear()
        print("left click")
        x = event.x
        y = event.y
        if 50 <= x <= 50+8*bd and  400-(nor*bd) <= y <= 400:
            t1=[x,y,event.num]
            a=isblockselected(t1)
            LC.append(a[0])
            LC.append(a[1])
            LC.append(a[2])
    elif event.num == 3:
        print("right click")
        x = event.x
        y = event.y
        if 50 <= x <= 50+ 8 * bd and 400 - (nor * bd) <= y <= 400:
            t2=[x,y,event.num]
            a=isblockselected2(t2)
            RC.append(a[0])
            RC.append(a[1])
            RC.append(a[2])
    else:
        print("this  is random event")
        x = event.x
        y = event.y
        print(x,y)
    if len(LC) == 3 and len(RC) == 3:
        if  LC[2] == True  and  RC[2] == False:
            rn=int((400-y)/bd)
            movetheblock1(rn,LC[0],LC[1],RC[0])

def keyPressed(event, data):
    pass
def timerFired(data):
    pass
def drawblocks(size,pos,x,y,canvas):
    i=0
    colours=['cyan','red','cyan','green','yellow','','','','black']
    canvas.create_rectangle(pos * bd + x, y, pos * bd + x + size * bd, y + bd, fill=colours[size])

def rowdraw(canvas,r1,x,y):
    i=0
    a=r1.head
    while a != None:
        drawblocks(a.size,a.pos,x,y,canvas)
        a=a.next
    a=r1.head
    if  a == None:
        drawblocks(8, 0 , x, y, canvas)

def  drawboardbackground(canvas,r1,x,y):
    drawblocks(8, 0, x, y, canvas)

def drawboard(canvas,r,no,x,y):
    n=no
    i=0
    while  i < n:
        r1=r[i]
        y=y-bd
        drawboardbackground(canvas, r1, x, y)
        i+=1
    i=0
    y=y+n*bd
    while  i < n:
        r1=r[i]
        y=y-bd
        rowdraw(canvas, r1, x, y)
        i+=1

def redrawAll(canvas, data):
    drawboard(canvas, b1.rows,data.no,x, y)
    b1.boardsettled()

def isblockselected(t1):
    y=t1[1]
    x=t1[0]
    r=-1
    i=int((400-y)/bd)
    a=b1.rows[i]
    print
    b=a.head
    while b!= None:
        s1=b.pos
        l=b.size
        if 50+s1*bd < x < 50+(s1*bd+l*bd):
            return (s1,l,True)
        else:
            b=b.next
    return (-1,-1,False)

def isblockselected2(t1):
    y = t1[1]
    x = t1[0]
    r = -1
    i = int((400 - y) / bd)
    a = b1.rows[i]
    b = a.head
    print("the value of b is", b)
    while b != None:
        s1 = b.pos
        l = b.size
        if 50 + s1 * bd < x < 50 + (s1 * bd + l * bd):
            return (s1,l,True)
        else:
            b = b.next
    s1=int((x-50)/bd)
    return (s1,-1,False)

def movetheblock(rn,s1,l,s2):
    print("the  function move the block has  been called")
    if  s1 > s2:
        a=b1.rows[rn].row_blockaccept(s2,s1+l)
        if a == True:
            c=b1.rows[rn].row_blockaccept(s2,l)
            if  c == True:
                b1.rows[rn].row_blockdelete1(s1)
                b1.rows[rn].row_insert(s2,l)
                b1.boardsettled()
    else:
        a = b1.rows[rn].row_blockaccept(s1,s2+l)
        if a == True:
            c=b1.rows[rn].row_blockaccept(s2,l)
            if  c == True:
                b1.rows[rn].row_blockdelete1(s1)
                b1.rows[rn].row_insert(s2,l)
                b1.boardsettled()

def movetheblock1(rn,s1,l,s2):
    global  b1
    b1.boardnooffilledrows()
    if s1 > s2:
        a = b1.rows[rn].row_blockaccept(s2,s1-s2)
        if a == True:
            b1.rows[rn].row_blockleftposchange(s1, s2)
            b1.boardsettled()
            b1.boardinsertnewrow()
            b1.boardsettled()
            if b1.boardnooffilledrows() == 10:
                print(b1)
                b1 = board.board(10, bd)
                print(b1)
                b1.boardnooffilledrows()
    else:
        a = b1.rows[rn].row_blockaccept(s1+l,s2-s1-l+1)
        if a == True:
            b1.rows[rn].row_blockrightposchange(s1,s2,l)
            b1.boardsettled()
            b1.boardinsertnewrow()
            print("the value of  length is",len(b1.rows))
            b1.boardsettled()
            if  b1.boardnooffilledrows() == 10:
                print(b1)
                b1 = board.board(10, bd)
                print(b1)
                b1.boardnooffilledrows()

####################################
# use the run function as-is
####################################
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass

    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 500  # milliseconds
    init(data)

    # create the root and the canvas
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root,bg="red",width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Button>", lambda event:
    mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
    keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
#    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(640, 640)









