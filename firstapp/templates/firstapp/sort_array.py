def fun_call(strg):
    if(strg[0]=="#"):
        return 0
    else:
        return 1
def find(new_string,g):
    m=len(new_string)
    for i in range(0,m,2):
        if(new_string[i]==g):
            return 0
    return 1

def count_number(b,g,new_string,z):
    if(find(new_string,g)):
        c=0
        for i in range(0,z):
            if(g==b[i]):
                c=c+1
        return(c)
    else:
        return 0

def i_want_half_sort(new_string):
    q=len(new_string)
    for i in range(0,q,2):
        for j in range(i+2,q,2):
            if(new_string[i] > new_string[j]):
                temp1=new_string[i]
                temp2=new_string[i+1]
                new_string[i]=new_string[j]
                new_string[i+1]=new_string[j+1]
                new_string[j]=temp1
                new_string[j+1]=temp2
    return(new_string)

#main string
n=input()
b=[]
for i in range(0,n):
    strg=raw_input().split()
    l=len(strg)
    for i in range(0,l):
        ret=fun_call(strg[i])
        if(ret == 0):
            b.append(strg[i])

z=len(b)
new_string=[]
for i in range(0,z):
    count=count_number(b,b[i],new_string,z)
    if(count!=0):
        new_string.append(b[i])
        new_string.append(count)
half_sort=i_want_half_sort(new_string)
temp=half_sort[1]
final_output=[]
leng=len(half_sort)
for i in range(1,leng,2):
    if(temp < half_sort[i]):
        temp=half_sort[i]

for i in range(1,leng,2):
    if(temp!=0):
        for j in range(1,leng,2):
            if(half_sort[j]==temp):
                final_output.append(half_sort[j-1])
        temp=temp-1
    else:
        break

for i in range(0,5):
    print(final_output[i])