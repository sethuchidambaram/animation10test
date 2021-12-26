import block
import random

class row:
    def __init__(self,coloum):
        self.head=None
        self.tail=None
        self.len=coloum
        self.row_generator()

    def row_generator(self):
        L = 0
        s=0
        while L < 8:
            if L <= 4:
                out = random.randint(1, 4)
                L = L + out
            else:
                out = random.randint(1, 8-L)
                L = L + out
#            print("the value of S  and  L  and  out are",s,out,L)
            if random.randint(1,10) < 6:
                self.row_insert(s,out)

            s=s+out

    def row_insert(self,s,l):
        p=block.block(s,l)
        if self.head==None:
            self.head=p
            self.tail=p
            p.pre=None
            p.next=None
        else:
            p.pre=self.tail
            self.tail.next=p
            self.tail=p

    def row_print(self):
        a=self.head
        while a!= None:
            print("(",a.pos,a.size,")",end=",")
            a=a.next

    def row_len(self):
        a=self.head
        b=0
        while a!= None:
            b=a.size+b
            a=a.next
        return  b


    def row_isempty(self):
        return self.row_len() < self.len

    def row_blockdelete1(self,pos):
#        print("the value of position is",pos)
#        print("the  function row_blockdelete1 has  been called")
        p=self.head
        while p !=None:
            if p.pos  == pos:
                break
            else:
                p=p.next
#       print("I am  in ifelse  loop")
#        if p != None:
#        print("I am  in ifelse  loop")
        if p.pre == None and p.next == None:
            self.head=None
        elif  p.pre == None:
            self.head=p.next
            p.next.pre = None
        elif  p.next == None:
            self.tail=p.pre
            p.pre.next = None
        else:
            p.pre.next=p.next
            p.next.pre=p.pre
        del p

    def row_blockaccept(self,st,len):
        S=st
        L=S+len-1
        a=self.head
        while a!= None:
            if S > a.pos and S > (a.pos+a.size-1):
                a=a.next
            elif L < a.pos and L < (a.pos+a.size-1):
                a=a.next
            else:
                return  False
        return True

    def row_blockleftposchange(self,bpos,cpos):
        a=self.head
        while a!= None:
            if  a.pos==bpos:
                a.pos=cpos
            else:
                a=a.next

    def row_blockrightposchange(self,bpos,cpos,len):
        a=self.head
        while a!= None:
            if  a.pos==bpos:
                a.pos=cpos-len+1
            else:
                a=a.next


