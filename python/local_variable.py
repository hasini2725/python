class test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        #print(a) #nameerror:name'a' is not defined
        print(b)
t=test()
t.m1()
t.m2()
