#!/usr/bin/python3 
import subprocess
import os
    
def exec_ftp_auto():
    subprocess.run(["sudo", "python3", "ftp_auto.py"])

def exec_ftps_auto():
    subprocess.run(["sudo", "python3", "ftps_auto.py"])

if __name__ == "__main__":
    print("--Executing ftp_auto.py script--")
    exec_ftp_auto()
    
    print("--Executing ftps_auto.py script--")
    exec_ftps_auto()
  
       
   
    
   
    
    
