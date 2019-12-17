#A4-Q1
import re
from scapy.all import *
from scapy.utils import PcapReader
#input file directory and name
s=input('Enter a file:')
packets=rdpcap(s)
for data in packets:
    s = repr(data)
    #regular expression
    p=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    List=p.findall(s)
    if len(List)>0:
        #sort the result
        List.sort()
        print(List)
        print('\n')
