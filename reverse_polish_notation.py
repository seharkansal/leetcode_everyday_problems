exp="10 6 9 3 + -11 * / * 17 + 5 +"
exp=exp.split()
#print(exp)
stack=[]
#char=['+','-','*','/']
for ele in exp:
    if ele not in '+-/*' :
        stack.append(int(ele))

    else:
        left=stack.pop()
        right=stack.pop()

        if ele=="+":
            stack.append(int(right+left))

        elif ele=="-":
            stack.append(int(right-left))

        elif ele=="/":
            stack.append(int(right/left))

        elif ele=="*":
            stack.append(int(right*left))

print(stack.pop())
