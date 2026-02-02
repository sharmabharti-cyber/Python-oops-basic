class college:
    def student(self):
        n=input("enter your name: \n")
        p=input("enter your phone no.: \n")
        e=input("enter yor email: \n")
        print( n,"|",p,"|",e)
    def marks(self):
        a=int(input("enter your maths marks: \n"))
        b=int(input("enter your C marks: \n"))
        c=int(input("enter your C++ marks: \n"))
        d=int(input("enter your python marks: \n"))
        e=int(input("enter your english marks: \n"))
        total=a+b+c+d+e
        percentage=(total/500)*100
        print("total marks is: ", total)
        print("total percentage is: ", percentage)
s1=college()
s1.student()
s1.marks()
