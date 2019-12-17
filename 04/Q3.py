#A4-Q3
import re
from scapy.all import *
from scapy.utils import PcapReader
#input the file directory and name
f=input('Enter a file:')
#input the words which we want to find
users=input("Enter a string or more strings(seperated by space):")
userlist=users.split(' ')
for i in userlist:
    packets=rdpcap(f)
    for data in packets:
        if IP in data:
            if data.payload:
                payload_str=repr(data.payload)
                #remove the unprintable letter
                s=re.sub(r'\\x..',r'',payload_str)
                w=s.find(i)
                if w>0:
                    #print the source IP and destination IP
                    print(data[IP].src,'  ',data[IP].dst)
                    #print the search word and 20 characters on each side
                    print(s[w-20:w],s[w:w+len(users)],s[w+len(users):w+len(users)+20])           
    print('\n') 
