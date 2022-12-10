row = input("enter number")
for i in range (0,int(row)):
    t = (int(row)*2)-1
    for j in range(0,t):
        if (j >= (int(row)-(i-1)) or j <=(int(row)-(i+1))):
            print("*")
        
        else:
            print("/")
