N = 7
S = [1,3,7,0,5,3,2]
D = [2,1,4,8,5,9,0]
F = 0
for i in range (1,N):
    if S[i] == D[i]:
        F = F + 1
print (F)
