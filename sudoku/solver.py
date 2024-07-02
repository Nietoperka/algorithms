def solver(first_numbers):
    s=[]
    for i in range(len(first_numbers)):
        if first_numbers[i]==0:
            #x="s"+str(i%4+1)+str(i//4+1)
            #x=[1,2,3,4]
            s.append("1234")   
        else:
            s.append(first_numbers[i])

    print(s)

def row2(inp): #druga metoda
    singles=[]
    for i in inp:
        if len(i)==1:
            singles.append(i)
    for x in inp:
        for y in singles:
            if len(x)!=1 and x.find(y)>=0:
                inp[inp.index(x)]=x.replace(y,'')
    return(inp)

def split(x,nmb,sud): #x - method, nmb - number of row,column,square, sud - whole sudoku list
    inp=[]
    if x==1:        #rows
        for i in range((nmb-1)*4,nmb*4):
            inp.append(sud[i])
    if x==2:        #columns
        for i in range((nmb-1)*4,len(sud),4):
            inp.append(sud[i])
    if x==3:        #square
        if nmb==1:
            for i in (0,1,4,5):
                inp.append(sud[i])
        if nmb==2:
            for i in (2,3,6,7):
                inp.append(sud[i])
        if nmb==3:
            for i in (8,9,12,13):
                inp.append(sud[i])
        if nmb==4:
            for i in (10,11,14,15):
                inp.append(sud[i])
    return(inp)

b=["1234","2","1234","1234"]
e=["1234","3","1234","1"]
a=[3,0,1,2,0,2,0,0,0,0,0,0,0,3,0,1]
solver(a)

split(3,3,a)