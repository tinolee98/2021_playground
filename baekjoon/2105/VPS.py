# VPS: 올바른 괄호 문제

n = int(input())
ps = []
for i in range(n):
    ps.append(list(input()))

for ps_ in ps:
    stack = []
    error = False
    for i in ps_:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0: 
                stack.pop()
            else:
                error = True
                break
    if len(stack) != 0:
        error = True
    if error:
        print('NO')
    else:
        print('YES')