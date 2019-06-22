num=int(input())
num=list(map(int,input().split()))
b=[]
for i in num:
  if(num.count(i)>1):
    b.append(i)
  else:
    print(i)
