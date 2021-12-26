import row
import block

col = 8
class board:
    def __init__(self, noofrows, length):
        self.rows = []
        self.no = noofrows
        self.bd = length
        i = 0
        while i < self.no:
            a = row.row(8)
            if i >= self.no / 2:
                a.head = None
                self.rows.append(a)
                i += 1
            if a.head != None:
                self.rows.append(a)
                i += 1

    #        print("the  size of the list is", len(self.rows))
    #        print("the value  of  I is", i)

    def boardprint(self):
        i = 0
        no = len(self.rows)
        while i < len(self.rows):
            #            print("the  row  position is", i)
            self.rows[i].row_print()
            print()
            i += 1

    def boardrowdelete(self, pos):
        i = pos
        while i < len(self.rows) - 1:
            self.rows[i] = self.rows[i + 1]
            i += 1

    def dropblocks(self):
        i = 0
        L = len(self.rows)
#       print("no of  rows in  dropblocks is",L)
        counter = 0
        while i < len(self.rows) - 1:
            a = self.rows[i + 1].head
            b = self.rows[i].head
            while a != None:
#                print("pos and  length is", a.pos, a.size)
                c = self.rows[i].row_blockaccept(a.pos, a.size)
                if c == True:
                    counter += 1
#                    print("the  function dropblocks  has been called")
                    self.rows[i].row_insert(a.pos, a.size)
                    self.rows[i + 1].row_blockdelete1(a.pos)
                a = a.next
            i += 1

        return counter > 0

    def removefullrows(self):
        i = 0
        counter = 0
        no = len(self.rows)
        while i < len(self.rows):
            #            print(i)
            if self.rows[i].row_isempty() == False:
                self.boardrowdelete(i)
                counter += 1
            i += 1
        return counter > 0

    def boardsettled(self):
        while True:
            while True:
                if self.dropblocks() == False:
                    break
            if self.removefullrows() == False:
                break

    def boardinsertnewrow(self):
        print("the  function  insert row has been called")
        while(True):
            a=row.row(8)
            if a.row_len() != 0 and  a.row_len() != \
                    8:
                break
        i=0
        print("the value  of  head of the class is",a.head,a.row_len())
        a.row_print()
        while i < self.no-1:
            if i == 0:
                tmp = self.rows[i + 1]
                pre = self.rows[i + 1]
                self.rows[i+1] = self.rows[i]
                self.rows[i] = a
            else:
                tmp = self.rows[i+1]
                self.rows[i+1] = pre
                pre=tmp
            i+=1
#        self.insert(0,a)

    def boardclearnewrow(self):
        i=0
        print("the function boardclearnewrow has  been called")
        while i < len(self.rows):
            self.rows[i]=None
            i+=1

    # def boardnooffilledrows(self):
    #     i=0
    #     while self.rows[i] != None:






