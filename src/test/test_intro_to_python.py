# Tyler Boudreau
# COT 4500
import numpy as np

def Reduced_Row_E():
    arr = np.empty(shape=(3,3))
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if i == j:
                arr[j][i] = 1
            else:
                arr[j][i] = 0
    print(arr, "\n")

def Matrix_of_Three():
    arr = np.empty(shape=(3,3))
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if i != j:
                arr[j][i] = 3
    print(arr,"\n")
    arr = np.delete(arr, 2, 1)
    print(arr)


def main():
    Reduced_Row_E()
    Matrix_of_Three()


if __name__ == "__main__":
    main()
