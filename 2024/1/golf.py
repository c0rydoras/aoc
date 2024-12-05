A=[[int(x)for x in open('input').read().split()][i::2]for i in[0,1]]
print(sum(abs(x-y)for x,y in zip(*map(sorted,A))))