def Strlen(l):
    if l=="":
      return 0
    else:
       return 1+Strlen(l[1:])
    
def strrev(l):
   if l=="":
      return ""
   else:
      return l[-1]+strrev(l[:-1])
    
def Smallest(l):
   if len(l)==1:
      return l[0]
   elif l[0]<Smallest(l[1:]):
      return l[0]
   else:
      return Smallest(l[1:])
    
    
st=input("Enter your string:")
print("Length :",Strlen(st))
print("Reverse :",strrev(st))
print("Smallest :",Smallest(st))