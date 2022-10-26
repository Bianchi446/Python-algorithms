from time import time
def compute_average(n):

    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n


print(compute_average(10000))   # Average time for 1000 append operations : 9 seconds
print(compute_average(1000))     
print(compute_average(100)) 
