#base cases
x1=[1,1]
x0=[0,0]
#calc nth
def calc(x):
    #if ix is equal to previous num or one less it returns directly but if it is different it calculates base on being bigger or smaller:
    if  x==x0[0]:
        return x0[1]
    #if it is bigger than x1 (our previous  num) it uses x0+x1=x2 ==> xn-1 + xn= xn+1
    elif  x>x1[0]:
        while x1[0]<x:
            x1[0]+=1
            x0[0]+=1
            x1[1],x0[1]=x0[1]+x1[1],x1[1]
    #if it is smaller than x0 (our previous  num-1) it uses x0=x2-x1 ==> xn-1  = xn+1 - xn
    elif x<x0[0]:
        while x0[0]>x:
            x1[0]-=1
            x0[0]-=1
            x1[1],x0[1]=x0[1],x1[1]-x0[1]
        
    return x1[1]
#program ruxing on a loop        
while True:
    i=input("enter a number :\n (enter x to exit) ")
    #break case
    if i=='x':
        break
    #handle wrong entries
    try:
        x=int(i)
        print(calc(x))
    except ValueError:
        print("not valid")

        

