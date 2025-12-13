Tri=[0,0,0]
Check=1
while check==1:
    flag=0
    for x in range(0,3):
        tri[x]=(int(input(f"enter angle {x+1}:")))
        total_sum=0
    for x in range(0,3):
        total_sum=total_sum+tri[x]
    if(total_sum==180):
        flag=1
        if(tri[0]==tri[1]==tri[2]):
        print("Its a equilateral triangle")
        elif(tri[0]==tri[1] or tri[0]==tri[2] or tri[1]==tri[2]):
        pritn("Its a isosceles triangle")
        else:
        print("its a scalene triangle")
        else: print("its not a triangle")
    if(flag==1):
        for x in tri:
        if(x<90):
        print(x,"is acute angle") 
        elif(x==90):

        print(x,"is a right angle")

        else:
        print(x,"is a obtuse angle")
    che=input("Do u want to check another triangle(y/n):")
    if(che=="y"):
    check=1
    else:
        check=0