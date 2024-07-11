class game:
    game_no=0
    def __init__(self):
        game.game_no+=1
        self.p1='X'
        self.p2='O'
        self.char='E'
        self.arr=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        print("Welcome to Tic Tac Toe" )
        print("\t\t\tGame-",game.game_no)
    def disp(self):
        for r in self.arr:
            for m in r:
                print(m,end='|')
            print("--------")
        return
    def fill1(self):
        print("Player-1:Enter the row and column:")
        i,j=int(input()),int(input())
        while self.arr[i][j]==self.p1 or self.arr[i][j]==self.p2 :
            print('Sorry.Enter the correct row and column:')
            i,j=int(input()),int(input())
        self.arr[i-1][j-1]=self.p1
        return
    def fill2(self):
        print('Player-2:Enter the row and column:')
        i,j=int(input()),int(input())
        while self.arr[i][j]==self.p1 or self.arr[i][j]==self.p2 :
            print('Sorry.Enter the correct row and column:')
            i,j=int(input()),int(input())
        self.arr[i-1][j-1]=self.p2
        return
    def condchk_res(self) :
        m=0
        while m<=3 :
            if self.arr[m][0]==self.arr[m][1] and self.arr[m][1]==self.arr[m][2] :
                self.char=self.arr[m][0]
                break
            if self.arr[0][m]==self.arr[1][m] and self.arr[1][m]==self.arr[2][m] :
                self.char=self.arr[0][m]
                break
        if self.arr[0][0]==self.arr[1][1] and self.arr[1][1]==self.arr[2][2] :
            self.char=self.arr[0][0]
        if self.arr[0][2]==self.arr[1][1] and self.arr[1][1]==self.arr[2][0] :
            self.char=self.arr[1][1]
        if self.char=='E' :
            pass
        else :
            if self.char==self.p1 :
                print('Player-1 won the game')
            else :
                print('Player-2 won the game')
        return
chk='y'
while chk=='y' or chk=='Y' :
    ob=game()
    while ob.char=='E' :
        if ob.char==ob.p1 or ob.char==ob.p2 :
            break
        ob.fill1()
        ob.disp()
        ob.condchk_res()
        if ob.char==ob.p1 or ob.char==ob.p2 :
            break
        ob.fill2()
        ob.disp()
        ob.condchk_res()
    del ob
    chk=input('Do you want to continue:(y/n):')