x=[int(n) for n in input("Type in elements of a list separated by space \n").split()]
n=len(x)
s=0
if n==0:
    m=-1
    a=-1
else:
    n=0
    m=x[0]
    while x[n]!=-1:
        s=s+x[n]
        if m>x[n] and x[n]!=-1:
            m=x[n]
        n=n+1
    a=s/n
print("Count: ",n,"\nSum: ",s,"\nMinimum: ",m,"\nMean: ",a)
# it looks like I learned how to use git today
