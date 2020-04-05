def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size - 2):
        for j in range(i + 1, arr_size - 1):
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print(A[i]," ", A[j]," ", A[k])
                    # return True
    # return False


# Driver program to test above function
n = int(input())
user_input = input()
A = list(int(i) for i in user_input.strip().split(" "))
sum = int(input())
arr_size = len(A)
find3Numbers(A, arr_size, sum)