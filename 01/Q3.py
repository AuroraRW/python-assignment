#input two IP addresses and a subnet mask
Ips=input('Enter the source IP:')
Ipd=input('Enter the destination IP:')
Ipm=input('Enter the subnet mask of the source:')
List_ip=[]
List_final=[]

#List_ip is a list that include three IP address which has been splited
List_ip.append(Ips.split('.'))
List_ip.append(Ipd.split('.'))
List_ip.append(Ipm.split('.'))

#Convert the IP address into the binary format
for temp_1 in List_ip:
    i=List_ip.index(temp_1)
    for temp_2 in temp_1:
        temp_3='{:08b}'.format(int(temp_2))
        List_final.append(str(temp_3))
    if i==0:
        print('The Source IP is:', '.'.join(List_final))
    elif i==1:
        print('The Destination IP is:', '.'.join(List_final))
    elif i==2:
        print('The Subnet Mask is:', '.'.join(List_final))
    List_final=[]
