import numpy as np

matrix_list = [[0, 1],]

for _ in range(3, 99, 1):
    matrix_list[0].append(0) # finished first row

for i in range(2, 99, 1):
    matrix_entry = []
    for j in range(1, 99, 1):
        if abs(i-j) == 1:
            matrix_entry.append(0.5)
        else:
            matrix_entry.append(0)
    matrix_list.append(matrix_entry)

matrix = np.array(matrix_list) # matrix Q
fundamental_matrix = np.linalg.inv(np.identity(98) - matrix) # this is N = ((I - Q) inverse)


for i in list(fundamental_matrix):
    print(sum(i))
    

# output is 
"""
9604.0
9603.0
9600.0
9595.0
...
...
...
768.0
579.0
388.0
195.0
"""
# therefore sum of values of top row 
# = expected value of floors that must be travelled before reaching top floor for first time 
# = 9604.
