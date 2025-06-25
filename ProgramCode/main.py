
import numpy as np 
arr = np.array([1, 2,3,4,5,65,34,43,34])
print(arr[5:8])
# arr1 = np.array([1, 2,3,4,3,4,2132,4,234,2] ,[3434,54,64,476,5,456,44,54,54,356,76,5])
# print(arr1[2:6,2])
arr1 = np.array([1.2,43.23,43,2])
arrint = arr1.astype(int)
print(arrint)

#copy and view 

arr2 = [23,42,4234,523]
#copying 
co= arr2.copy()
print(co)
#viewing
vir = arr2.copy()
arr2[0] = 343
print(arr2)

#shaping 
arr3 = np.array([423,53,4,64,32,542,42,4] , ndmin=5)
print(arr3,"shap of the array" ,arr3.shape)

#reshaping 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2,6)

print(newarr)


for x in arr:
    print(x)
    
arr4 = np.array([[1,3],[4,5]])    
arr5 = np.array([[6,7],[8,9]])
print("satck",np.stack((arr4, arr5),axis=1))   
print("vstack" ,np.vstack((arr4, arr5)))
print("dstack" ,np.dstack((arr4, arr5)))
print("hstack" ,np.hstack((arr4, arr5)))
      
print("Getting the even element ")
x = np.where(arr%2 == 0)
print(x)

print(np.sort(arr))
      




