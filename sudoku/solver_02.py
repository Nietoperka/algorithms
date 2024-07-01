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
    for x in inp:
        for y in singles:
            if len(x)!=1 and x.find(y)>=0:
                inp[inp.index(x)]=x.replace(y,'')
    return(inp)

b=["1234","2","1234","1234"]
e=["1234","3","1234","1"]
a=[3,0,1,2,0,2,0,0,0,0,0,0,0,3,0,1]
solver(a)

print(e)
print(row2(e))