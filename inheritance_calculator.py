class Caluclator:
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
        
class Manage(Caluclator):
    def multiply(self):
        i=int(input("enter first no.: "))
        j=int(input("enter second no.:"))
        k=i*j
        print(k)

m=Manage()
m.add()
m.sub()
m.multiply()
