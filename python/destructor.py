class student:
    def __del__(self):
        print("Destructor called,object deleted")
        s=student() 
        del s       
