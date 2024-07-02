def solver(first_numbers):
    s=[]
    copy_s=[]
    for i in range(len(first_numbers)):
        if first_numbers[i]==0:
            #x="s"+str(i%4+1)+str(i//4+1)
            #x=[1,2,3,4]
            s.append("123456789")   
        else:
            s.append(str(first_numbers[i]))
    #print(s)
    copy_s=s.copy()
    #print(copy_s)
    for i in range(1,4): #method
        for j in range(1,10): #nmb of row,col,sqr
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
            for j in range(1,10): #nmb of row,col,sqr
                spliting=split(i,j,changing)
                solving=row2(spliting[0])
                new=replacement(changing,spliting[1],solving)
        cnt=cnt+1
        #changing.clear()
        changing=new.copy()
        print("petla while: ",cnt,"\nprzed: ",copy_s,"\npo: ",changing,"\n")
        draw(copy_s)

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
    doubles=[]
    pair=[]
    for i in inp:
        if len(i)==1:
            singles.append(i)
        if len(i)==2 :
            doubles.append(i)
    #print("singles: ",singles)
    for i in range(len(doubles)-1):
        if doubles[i]==doubles[i+1]:
            pair.append(doubles[i])
    for y in singles:
        for x in inp:
            if len(x)!=1 and x.find(y)>=0:
                inp[inp.index(x)]=x.replace(y,'')
    if len(pair)>=1:
        for y in inp:
            if len(y)>=3 and y.find(pair[0])>=0:
                inp[inp.index(y)]=y.replace(pair[0],'')
    return(inp)

def row3(inp): #advanced SOLVING
    doubles=[]
    for i in inp:
        if len(i)==2 :
            doubles.append(i)
    pair=[]
    for i in range(len(doubles)-1):
        if doubles[i]==doubles[i+1]:
            pair.append(doubles[i])
    #print("singles: ",singles)
    for y in inp:
        if len(y)>=3 and y.find(pair[0])>=0:
            inp[inp.index(y)]=y.replace(pair[0],'')
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
        for i in range((nmb-1)*9,nmb*9):
            inp.append(sud[i])
            indexes.append(i)
    if x==2:        #columns
        for i in range(nmb-1,len(sud),9):
            inp.append(sud[i])
            indexes.append(i)
    if x==3:        #square
        if nmb==1:
            for i in (0,1,2,9,10,11,18,19,20):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==2:
            for i in (3,4,5,12,13,14,21,22,23):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==3:
            for i in (6,7,8,15,16,17,24,25,26):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==4:
            for i in (27,28,29,36,37,38,45,46,47):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==5:
            for i in (30,31,32,39,40,41,48,49,50):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==6:
            for i in (33,34,35,42,43,44,51,52,53):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==7:
            for i in (54,55,56,63,64,65,72,73,74):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==8:
            for i in (57,58,59,66,67,68,75,76,77):
                inp.append(sud[i])
                indexes.append(i)
        if nmb==9:
            for i in (60,61,62,69,70,71,78,79,80):
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

def draw(sud):
    print("\n")
    j=0
    for i in range(0,len(sud),9):
        j=j+1
        print(sud[i],sud[i+1],sud[i+2],"|",sud[i+3],sud[i+4],sud[i+5],"|",sud[i+6],sud[i+7],sud[i+8])
        if j%3==0:
            print("_______________________")
    print("\n")


# 8,7,6,4,9,3,2,5,1,
# 3,4,5,7,1,2,9,6,8,
# 2,9,1,5,6,8,4,7,3,
# 9,8,2,1,3,5,7,4,6,
# 7,5,4,8,2,6,3,1,9,
# 1,6,3,9,4,7,8,2,5,
# 4,1,7,3,5,9,6,8,2,
# 6,3,8,2,7,1,5,9,4,
# 5,2,9,6,8,4,1,3,7,

#sud_nine=[8,7,6,4,9,3,2,5,1,3,4,5,7,1,2,9,6,8,2,9,1,5,6,8,4,7,3,9,8,2,1,3,5,7,4,6,7,5,4,8,2,6,3,1,9,1,6,3,9,4,7,8,2,5,4,1,7,3,5,9,6,8,2,6,3,8,2,7,1,5,9,4,5,2,9,6,8,4,1,3,7]
sud_nine=[8,0,0,4,0,3,2,0,1,0,0,5,7,1,0,0,0,8,0,9,1,5,0,8,0,0,3,9,0,2,1,0,5,7,0,6,7,0,0,8,2,0,0,1,0,0,6,0,9,4,0,0,2,0,0,1,0,0,0,9,0,8,2,0,3,0,0,7,1,0,0,0,5,2,0,6,0,0,0,3,0]


a=[3,0,1,2,0,2,0,0,0,0,2,0,0,3,0,1]
aa=['3', '1234', '1', '2', '1234', '2', '1234', '1234', '1234', '1234', '1234', '1234', '1234', '3', '1234', '1']

solver(sud_nine)
bb=['8', '34', '9', '2', '34','7', '134', '5', '6']
#print(row3(bb))

# print(aa)
# po_podziale=split(1,1,aa)
# print(po_podziale)
# po_rozwiazaniu=row2(split(1,1,aa)[0])
# print(po_rozwiazaniu)
# podmianka=replacement(aa,split(1,1,aa)[1],po_rozwiazaniu)
# print(podmianka)