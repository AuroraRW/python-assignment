#A3-Q1
#find i,j,k, and the sum of i,j,k is not N.
#(0 ≤ i ≤ x, 0 ≤ j ≤ y, 0 ≤ k ≤ z)
def cube_not_equal(x,y,z,N):
    s=set()
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                if i+j+k != N:
                    s.add((i,j,k))
    return s  
