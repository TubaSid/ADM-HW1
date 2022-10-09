# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
if __name__=='__main__':
    n, m=list(map(int,raw_input().split()))
    array=[]
    for i in range (n):
        array.append(raw_input())
        array[i]=list(map(int,array[i].split()))
    array= np.array(array)
    print(np.prod((np.sum(array, axis=0)),axis=0))

