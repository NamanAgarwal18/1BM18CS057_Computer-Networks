# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 11:58:37 2020

@author: Naman
"""

def main():
 size=int(input("Enter the Bucket Size : "))
 output=int(input("Enter the output rate: "))
 n=int(input("Enter the  number of inputs : "))
 for x in range (n):
     Input=int(input("Enter the input number of packets : "))
     if(Input > size):
       print("Number of packets exceeded th Buffer size!!...")
       return
     if( Input < output):
       print("last " + str(Input) + " Bytes were send")
     elif (Input > output):
       a=abs(output-Input)
       print(str(output) + " bytes outputted")
       print("Last" + str(a) + " bytes send")
      

main()