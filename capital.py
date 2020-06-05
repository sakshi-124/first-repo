fname=input("enter file name")
f=open(fname,"r")
#for line in f:
cap=f.read()
print(cap.upper())

f.close()    
    
