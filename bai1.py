n=int(input())
st1=0
st2=0
if n%2==0:
    st2=n//2
    st1=n//2
if n%2!=0:
    st1=n//2
    st2=n//2+1
print(st1,st2)
    