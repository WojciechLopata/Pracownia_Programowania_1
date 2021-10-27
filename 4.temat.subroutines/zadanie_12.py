def sum(N):
    if(N>1):
        return sum(N-1)+N
    else: return 1
print(sum(4))