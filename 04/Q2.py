#A4-Q2
import re
from scapy.all import *
from scapy.utils import PcapReader
#input the directory and name of the file
s=input('Enter a file:')
packets=rdpcap(s)
for data in packets:
    if IP in data:
        #get the source IP
        print(data[IP].src)
        if data.payload:
            payload_str=repr(data.payload)
            #remove the unprintable letter
            temp=re.sub(r'\\x..',r'',payload_str)
            print(temp)
            print('///')
