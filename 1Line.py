# Interesting-Code
##n =[1,2,3,1,2,3,1,2,3]
##for i in range(1, 11):
##    print(i,end="") 
##print ("Hey Guys!",end= "")
##print ("This is how we print on the same line.")




list_a = []
for i in range(4):
    a=[int(x) for x in input().split()]
    list_a.append(a)
for i in list_a :
    for j in i:
        print(j,end=" ")
    print()
       
print(list_a)
  
    
