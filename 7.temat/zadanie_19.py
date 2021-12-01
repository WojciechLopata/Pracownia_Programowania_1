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
equation=input()
equation_change=""
for char in equation:
    if(char=="+"):
        calc=stack[-2]+stack[-1]
        pop()
        pop()
        push(calc)
    elif(char=="-"):
        calc=stack[-2]-stack[-1]
        pop()
        pop()
        push(calc)
    elif(char=="*"):
        calc=stack[-2]*stack[-1]
        pop()
        pop()
        push(calc)
    elif(char=="/"):
        calc=stack[-2]/stack[-1]
        pop()
        pop()
        push(calc)
    elif(char=="="):
        break
    else:
        try:
            a=int(char)
            push(a)
        except:
            print("podałeś złe znaki")
            break
display()
        
    

    
    