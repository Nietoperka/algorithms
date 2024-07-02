def solver(first_numbers):
    s=[]
    for i in range(len(first_numbers)):
        if first_numbers[i]==0:
            #x="s"+str(i%4+1)+str(i//4+1)
            #x=[1,2,3,4]
            s.append("1234")   
        else:
            s.append(str(first_numbers[i]))
    print(s)
    for i in range(1,4):
        for j in range(1,5):
            print(i,j,split(i,j,s))
            print(row2(split(i,j,s)))

# def row(inp): #inp - lista z rzędem
#     print(inp)
#     for i in inp:
#         if len(i)!=1:
#             for j in inp:
#                 if len(j)==1 and i.find(j)>=0:
#                     print("i: ",i," j: ",j)
#                     inp[inp.index(i)]=i.replace(j,'')
#                     print("po: ",inp)
#     return(inp)

def row2(inp): #druga metoda
    singles=[]
    for i in inp:
        if len(i)==1:
            singles.append(i)
    #print("singles: ",singles)
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
    #print(sud,ind,inp)
    for i in ind:
        #sud.replace(sud[i],inp[x])
        sud[i]=inp[x]
        x=x+1
    #print(sud)
    return(sud)


b=["1234","2","1234","1234"]
e=["1234","3","1234","1"]
a=[3,0,1,2,0,2,0,0,0,0,0,0,0,3,0,1]
aa=['3', '1234', '1', '2', '1234', '2', '1234', '1234', '1234', '1234', '1234', '1234', '1234', '3', '1234', '1']

#solver(a)
print(aa)
po_podziale=split(1,1,aa)
print(po_podziale)
po_rozwiazaniu=row2(split(1,1,aa)[0])
print(po_rozwiazaniu)
podmianka=replacement(aa,split(1,1,aa)[1],po_rozwiazaniu)
print(podmianka)