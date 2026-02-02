class caluclator:
    def add(self):
        a=int(input("enter first no.: "))
        b=int(input("enter second no.:"))
        c=a+b
        print(c)

    def sub(self):
        x=int(input("enter first no.: "))
        y=int(input("enter second no.:"))
        z=x-y
        print(z)

a1= caluclator()
i=int(input("enter 1 for add \nenter 2 for sub\n"))
if i==1:
    a1.add()
elif i==2:
    a1.sub()
else:
    print("invalid entry")
