import numpy as np 
import numpy as random
arr = np.array([2,4,4,21,292,3,42,242,242,21,18,54,3434,3,23])

fitler_ar= [] 


for x in arr:
    if x > 30:
        fitler_ar.append(True)
    else :
        fitler_ar.append(False)


newar = arr[fitler_ar]
print(arr)
print(newar)           



arr  = np.array([1,443,53,263,43,2])
x = random.choice(arr)
print(x)

ar =random.choice([3,4,2,4] , p = [ 0.2, 0.4, 0.15, 0.35] , size=(3,5))
print(ar)
