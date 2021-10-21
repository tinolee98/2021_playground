import sys
input = sys.stdin.readline
pokemon = {}
N,M = list(map(int,input().split()))
targets = []

for i in range(N):
    name = input().rstrip()
    pokemon[str(i+1)] = name
    pokemon[name] = str(i+1)
for i in range(M):
    targets.append(input().rstrip())
#print(pokemon)
#print("---")
#print(targets)

for target in targets:
    print(pokemon[target])