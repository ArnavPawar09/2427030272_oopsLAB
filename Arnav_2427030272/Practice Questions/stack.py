stack=[]
max=3
print("push\npop\ndisplay\npeek\nsize\nexit\n")
while(True):
    c=int(input("enter choice : "))
    if c==1:
        if len(stack)==max:
            print("overflow")
        else:
            n=int(input("push element : "))
            stack.append(n)
    elif c==2:
        if not stack:
            print("underflow")
        else:
            stack.pop()
    elif c==3:
        if not stack:
            print("empty")
        else:
            for i in stack:
                print(f"{i}  ")
    elif c==4:
        if not stack:
            print("empty")
        else:
            print("peek :",stack[-1])
    elif c==5:
        print(len(stack))
    elif c==6:
        print("exiting...")
        break
    else:
        print("invalid input")
