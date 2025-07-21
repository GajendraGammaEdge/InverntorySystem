

arr = range(1,50)
arrnew = [x for x in arr if x % 2 == 0]
print(arrnew)

arrnew2 =[y for y in range(1,44) if y % 5 ==0]
print(arrnew2)


#lambda
la1 = lambda x : x % 2 == 0
lis = range(10,34)
print(la1(7))


#lambda for loop
las2 = lambda  y : y  %3 ==0
for p in range(1,98):
    print(las2(p))
