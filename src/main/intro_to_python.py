# Created by Tyler Boudreau, UCF, COT 4500
import numpy as np

arr = np.empty(shape=(3,3))

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if i == j:
            arr[j][i] = 1
        else:
            arr[j][i] = 0

print(arr)
print("\n")
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if i != j:
            arr[j][i] = 3

print(arr)
print("\n")
arr = np.delete(arr, 2, 1)

print(arr)