q=[]
def display():
    for i in q:
       print(i,end=" ")
    print()
def push(x):
    q.append(x)
def pop():
    reverse()
    del q[-1]
    reverse()
# może być też del q[0]
def reverse():
    global q
    reversed=[]
    a=len(q)
    for i in range(a):
        reversed.append(q[-1-i])
    q=reversed
