#Qno:2
s = input("Enter the Numbers : ")
s=s.split(',')
l1=[]
for i in s:
    for k in range(int(i)):
        if 2**k == int(i):
            l1.append(int(i))
            break;
print(l1)
            
