
import re 
  
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
      

def check(email):  
   
    if(re.search(regex,email)):  
        print(email)  
           
       
if __name__ == '__main__' :  
      
     i=input("enter the value:")
     for n in range(0,i):
        email=raw_input("enter mail:")
        check(email)
