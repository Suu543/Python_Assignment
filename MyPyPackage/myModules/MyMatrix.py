def mtrxAdd(A, B):
    result = [len(B[0]) * [0] for i in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

def mtrxSub(A, B):
    result = [len(B[0]) * [0] for i in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            result[i][j] = A[i][j] - B[i][j]
    
    return result

def mtrxMul(A, B):
    result = [len(B[1]) * [1] for i in range(len(A))]
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            result[i][j] = A[i][j] * B[i][j]
    
    return result