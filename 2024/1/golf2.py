C,D=[[int(A)for A in open('input').read().split()][A::2]for A in[0,1]]
A=0
for B in C:A+=B*D.count(B);print(A)