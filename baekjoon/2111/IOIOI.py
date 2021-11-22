N = int(input())
M = int(input())
S = input()

result = 0
i = 0
while i < M-2:
    if S[i+1] == 'O' and S[i+2]=='I':
        O = 0
        while i < M-2 and S[i] == 'I' and S[i+1] == 'O':
            i += 2
            O += 1
            if S[i] == 'I' and O == N:
                O -= 1
                result += 1
    i += 1
print(result)