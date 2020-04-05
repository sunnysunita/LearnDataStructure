def find3Numbers(A, arr_size, sum):
    for i in range(0, arr_size - 1):
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                list0=[A[i],curr_sum - A[j],A[j]]
                print(min(list0),end=" ")
                list0.remove(min(list0))
                print(min(list0),end=" ")
                print(max(list0))

                #return True
            s.add(A[j])

    return False
n=int(input())
user_input=input()
A = list(int(i) for i in user_input.strip().split(" "))
sum =int(input())
arr_size = len(A)
find3Numbers(A, arr_size, sum)