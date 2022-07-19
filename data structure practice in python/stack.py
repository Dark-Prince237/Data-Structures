stack=[]

def push():

    value=int(input("enter a number to push "))
    stack.append(value)
    print(str(value) +" is pushed to stack")
    print(stack)

def pop():
    if not stack:
        print("stack is empty")

    else:

        print(str(stack[-1])+" is pop out of stack")
        stack.pop()


def peek():
    print("the top of the stack is "+str(stack[-1]))


def display():
    print(stack)



while(True):
    choice=int(input("enter your choice:- {1:push,2:pop,3:peek,4:display}  "))
    if choice==1:
        push()

    elif choice==2:
        pop()

    elif choice==3:
        peek()

    elif choice==4:
        display()

    elif choice==0:
        exit(1)
    
    else:
        print("invalid choice")



    

