class  block:
    def __init__(self,pos,size):
        self.pos=pos
        self.size=size
        self.colour=0
        self.next=None
        self.pre=None
    def print(self):
        b=self
        if  b != None:
            print(b.pos,b.size)
