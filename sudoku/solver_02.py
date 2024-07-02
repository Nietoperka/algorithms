def solver(first_numbers):
    s=[]
    copy_s=[]
    for i in range(len(first_numbers)):
        if first_numbers[i]==0:
            #x="s"+str(i%4+1)+str(i//4+1)
            #x=[1,2,3,4]
            s.append("1234")   
        else:
            s.append(str(first_numbers[i]))
    #print(s)
    copy_s=s.copy()
    #print(copy_s)
    for i in range(1,4): #indexes
        for j in range(1,5): #nmb of row,col,sqr
            spliting=split(i,j,s)
            solving=row2(spliting[0])
            changing=replacement(s,spliting[1],solving)
            # print(i,j,spliting)
            # print(solving)
            # print(changing)
    #new=changing.copy()
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
        #changing.clear()
        changing=new.copy()
        print("petla while: ",cnt,"\nprzed: ",copy_s,"\npo: ",changing,"\n")

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

# def split(x,nmb,sud): #x - method, nmb - number of row,column,square, sud - whole sudoku list
#     inp=[]
#     indexes=[]
#     if x==1:        #rows
#         for i in range((nmb-1)*4,nmb*4):
#             inp.append(sud[i])
#             indexes.append(i)
#     if x==2:        #columns
#         for i in range(nmb-1,len(sud),4):
#             inp.append(sud[i])
#             indexes.append(i)
#     if x==3:        #square
#         if nmb==1:
#             for i in (0,1,4,5):
#                 inp.append(sud[i])
#                 indexes.append(i)
#         if nmb==2:
#             for i in (2,3,6,7):
#                 inp.append(sud[i])
#                 indexes.append(i)
#         if nmb==3:
#             for i in (8,9,12,13):
#                 inp.append(sud[i])
#                 indexes.append(i)
#         if nmb==4:
#             for i in (10,11,14,15):
#                 inp.append(sud[i])
#                 indexes.append(i)
#     return(inp,indexes)

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


# 8,7,6,4,9,3,2,5,1,
# 3,4,5,7,1,2,9,6,8,
# 2,9,1,5,6,8,4,7,3,
# 9,8,2,1,3,5,7,4,6
# 7,5,4,8,2,6,3,1,9,
# 1,6,3,9,4,7,8,2,5,
# 4,1,7,3,5,9,6,8,2,
# 6,3,8,2,7,1,5,9,4,
# 5,2,9,6,8,4,1,3,7,

sud_nine=[8,7,6,4,9,3,2,5,1,3,4,5,7,1,2,9,6,8,2,9,1,5,6,8,4,7,3,9,8,2,1,3,5,7,4,67,5,4,8,2,6,3,1,9,1,6,3,9,4,7,8,2,5,4,1,7,3,5,9,6,8,2,6,3,8,2,7,1,5,9,4,5,2,9,6,8,4,1,3,7]

a=[3,0,1,2,0,2,0,0,0,0,2,0,0,3,0,1]
f=[3,0,0,0,0,2,0,0,0,0,2,0,0,0,0,1]
aa=['3', '1234', '1', '2', '1234', '2', '1234', '1234', '1234', '1234', '1234', '1234', '1234', '3', '1234', '1']

solver(f)

# print(aa)
# po_podziale=split(1,1,aa)
# print(po_podziale)
# po_rozwiazaniu=row2(split(1,1,aa)[0])
# print(po_rozwiazaniu)
# podmianka=replacement(aa,split(1,1,aa)[1],po_rozwiazaniu)
# print(podmianka)