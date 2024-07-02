
# FOR SUDOKU 4X4    

def solver(first_numbers):
    s=[]
    copy_s=[]
    for i in range(len(first_numbers)):
        if first_numbers[i]==0:
            s.append("1234")   
        else:
            s.append(str(first_numbers[i]))
    copy_s=s.copy()
    for i in range(1,4): #method
        for j in range(1,5): #nmb of row,col,sqr
            spliting=split(i,j,s)
            solving=row2(spliting[0])
            changing=replacement(s,spliting[1],solving)    
    print("piersze rozwiazanie: ",copy_s,"\n",changing)
    cnt=0
    while copy_s!=changing:
        copy_s.clear()
        copy_s=changing.copy()
        for i in range(1,4): #method
            for j in range(1,5): #nmb of row,col,sqr
                spliting=split(i,j,changing)
                solving=row2(spliting[0])
                new=replacement(changing,spliting[1],solving)
        cnt=cnt+1
        changing=new.copy()
        print("petla while: ",cnt,"\nprzed: ",copy_s,"\npo: ",changing,"\n")


def row2(inp): #druga metoda
    singles=[]
    for i in inp:
        if len(i)==1:
            singles.append(i)
    for y in singles:
        for x in inp:
            if len(x)!=1 and x.find(y)>=0:
                inp[inp.index(x)]=x.replace(y,'')
    return(inp)

def split(x,nmb,sud): #x - method, nmb - number of row,column,square, sud - whole sudoku list
    inp=[]
    indexes=[]
    if x==1:        #rows
        for i in range((nmb-1)*4,nmb*4):
            inp.append(sud[i])
            indexes.append(i)
    if x==2:        #columns
        for i in range(nmb-1,len(sud),4):
            inp.append(sud[i])
            indexes.append(i)
    if x==3:        #square
        if nmb==1:
            for i in (0,1,4,5):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==2:
            for i in (2,3,6,7):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==3:
            for i in (8,9,12,13):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==4:
            for i in (10,11,14,15):
                inp.append(sud[i])
                indexes.append(i)
    return(inp,indexes)

def replacement(sud,ind,inp):   #sud - whole sudoku list, ind - indexes, inp - row, column or square
    x=0
    for i in ind:
        sud[i]=inp[x]
        x=x+1
    return(sud)

a=[3,0,1,2,0,2,0,0,0,0,2,0,0,3,0,1]

solver(a)