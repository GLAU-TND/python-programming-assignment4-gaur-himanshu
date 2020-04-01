ls=eval(input("enter a list"))
st=aval(iput("enter the query string"))
z=[]
for i in ls:
    if i.startswith(st)==True:
      z.append(i)
print(z)