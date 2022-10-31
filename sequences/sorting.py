def insertion_sort(A):

    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
          A[j] = A[j-1]
          j -= 1
        A[j] = cur

Data = [4, 3, 2, 1]
print(insertion_sort(Data))
