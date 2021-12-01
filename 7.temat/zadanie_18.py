#####
# Stack definition
##

stack = []

# add value at the end of the stack
def push(value):
    stack.append(value)
    
# remove the topmost element of the stack
# and return its value    
def pop():
    if not empty():
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in stack:
        print(i, end=" ")
    print()
number=int(input("natural number: "))
while(number>0):
    push(number%2)
    number=number//2
    
size=len(stack)
n=0
while(size>n):
    print(stack[-1-n],end="")
    n+=1
while(len(stack)>0):
    pop()