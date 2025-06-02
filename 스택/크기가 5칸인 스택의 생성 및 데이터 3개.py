stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = "커마"
top += 1
stack[top] = "녹화"
top += 1
stack[top] = "꿀물"

print("----스택상태----")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])
