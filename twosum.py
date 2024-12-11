a=[1,2,4,6,8,10,11]
l=0
r=len(a)-1
target=10
steps=0 
#to know no of steps taken
while(l<=r):
    steps=steps+1
    if(a[l]+a[r]>target):
        r=r-1
    elif(a[l]+a[r]<target):
        l=l+1
    else:
        print(a[l],a[r])
        r=r-1
        l=l+1
print(steps)
