a=list;b=sorted
def o(l):
 for(i,j)in zip(l,l[1:]):
  if (d:=i-j)==0 or abs(d)>3:return 0
 return(c:=b(l))==l or c[::-1]==l
n=[a(map(int,l.split()))for l in open("input")];print(len(a(filter(o,n))))
