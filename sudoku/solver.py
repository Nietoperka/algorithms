def solver(first_numbers):
    s=[]
    for i in range(len(first_numbers)):
        if first_numbers[i]==0:
            x="s"+str(i%4+1)+str(i//4+1)
            #x=[1,2,3,4]
            s.append(x)           
    print(s)
    for i in s:
        s[i].append("1")
    print(s)
    #print(first_numbers)
#def row_sh(row):

b=[5,5,5]
a=[3,0,1,2,0,2,0,0,0,0,0,0,0,3,0,1]
solver(a)