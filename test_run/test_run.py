import pytest 
import os
import sys


endpoint1 = 'login/ep1_login.txt'
endpoint2 = 'login/ep2_update_user.txt'
class TestClass:
    def test_host(self):
        with open(endpoint1,'r') as ep1,  open(endpoint2, 'r') as ep2:
            for line in ep1:
               if (line.startswith('Host:')):
                   host1 = line[5:]
        
            for line in ep2:
               if (line.startswith('Host:') ):
                   host2 = line[5:]
          
        assert  host1 == host2     
    
    def test_role(self):
        with open(endpoint2, 'r') as ep2:
            
        
            for line in ep2:
               if (line.startswith('\"role\": ') ):
                   role = line[8:-2]
                   
                   
        assert  (role == '\"admin\"') or (role == '\"executor\"') or (role == '\"reporter\"')
    
    def test_active(self):
        with open(endpoint2, 'r') as ep2:
            
        
            for line in ep2:
               if (line.startswith('\"active\":') ):
                   active = line
                   
                   
        assert active.find('true') or active.find('false')
    
    
def main():
   t1 = TestClass()
   t1.test_host()
   t1.test_role()
   t1.test_active()
   
if __name__ == "__main__":
    main()

