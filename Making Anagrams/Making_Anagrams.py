a = input()
b = input()

delete=0

for i in range(len(a)):
    c=a[i]
    if (a.count(a[i])) == (b.count(a[i])):
        a = a.replace(a[i]," ")
        b = b.replace(c," ")
   
    elif (a.count(a[i]))>(b.count(a[i])) and a[i]!=" ":
        delete+=(a.count(a[i]))-(b.count(a[i]))
        a = a.replace(a[i]," ")
        b = b.replace(c," ")
        
    
    elif (a.count(a[i]))<(b.count(a[i])) and a[i]!=" ":
        delete+=(b.count(a[i]))-(a.count(a[i]))
        a = a.replace(a[i]," ")
        b = b.replace(c," ")
        
    
    elif a[i]==" ":
        pass         

for i in range(len(b)):
    if b[i]!=" ":
        delete+=1  

print(delete)      
