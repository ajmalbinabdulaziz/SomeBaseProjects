        #Application part 1
        
   #Verifying the input IP address     

while True:
    ip_address=input("Enter an IP address: ")
        
    a=ip_address.split('.')

    if (len(a)==4) and (1<=int(a[0])<=223) and (int(a[0])!=127) and (int(a[0])!=169 or int(a[1])!=254) and (0<=int(a[1])<=255) and (0<=int(a[2])<=255) and (0<=int(a[3])<=255):
        break
    else:
         print("\nThe IP address is INVALID!Please retry!\n")
         continue

mask = [255,254,252,248,240,224,192,128,0]
while True:
    subnet_mask=input("Enter the subnet mask: ")
    b=subnet_mask.split('.')

    if (len(b)==4) and (int(b[0])==255) and (int(b[1]) in mask) and (int(b[2]) in mask) and (int(b[2]) in mask) and (int(b[3]) in mask) and (int(b[0])>=int(b[1])>=int(b[2])>=int(b[3])):
        break
        
    else:
        print("\nThe subnet mask is INVALID! Please retry!\n")
        continue

        #Application part 2

#converting mask to binary
mask_octets_padded = []
mask_octets_decimal = subnet_mask.split(".")
#print(mask_octets_decimal)

for octet_index in range(0,len(mask_octets_decimal)):
        #print(bin(int(mask_octets_decimal[octet_index])))

        binary_octet=bin(int(mask_octets_decimal[octet_index])).split("b")[1]
        #print(binary_octet)

        if len(binary_octet)==8:
            mask_octets_padded.append(binary_octet)
        if len(binary_octet)<8:
            binary_octet_padded=binary_octet.zfill(8)
            mask_octets_padded.append(binary_octet_padded)

#print(mask_octets_padded)

decimal_mask="".join(mask_octets_padded)
#print(decimal_mask)

#calculating the no of hosts per subnet

no_of_zeros=decimal_mask.count("0")
no_of_ones=32-no_of_zeros
no_of_hosts=abs(2**no_of_zeros - 2)
#print(no_of_hosts)

# Obtaining wildcard mask
wildcard_octets=[]

for w_octet in mask_octets_decimal:
        wild_octet=255-int(w_octet)
        wildcard_octets.append(str(wild_octet))
    
#print(wildcard_octets)
wildcard_mask=".".join(wildcard_octets)
#print(wildcard_mask)

            #Application part 3

#converting ip address to binary

ip_octets_padded=[]
ip_octets_decimal=ip_address.split(".")
#print(ip_octets_decimal)

for octet_index in range(0,len(ip_octets_decimal)):
        binary_octet=bin(int(ip_octets_decimal[octet_index])).split("b")[1]

        if len(binary_octet)<8:
            binary_octets_padded=binary_octet.zfill(8)
            ip_octets_padded.append(binary_octets_padded)
            
        else:
            ip_octets_padded.append(binary_octet)
            

binary_ip="".join(ip_octets_padded)    
#print(binary_ip)
        
#getting the network and broadcast address

network_address_binary=binary_ip[:(no_of_ones)] + "0" * no_of_zeros
#print(network_address_binary)

broadcast_address_binary=binary_ip[:(no_of_ones)] + "1" * no_of_zeros
#print(broadcast_address_binary)

net_ip_octets=[]
for octet in range(0,len(network_address_binary),8):
    net_ip_octet=network_address_binary[octet:octet+8]
    net_ip_octets.append(net_ip_octet)  

net_ip_address=[]
for each_octet in net_ip_octets:
    net_ip_address.append(str(int(each_octet,2)))
    #print(net_ip_address)
    
network_address=".".join(net_ip_address)
#print(network_address)

brd_ip_octets=[]
for octet in range(0,len(broadcast_address_binary),8):
    brd_ip_octet=broadcast_address_binary[octet:octet+8]
    brd_ip_octets.append(brd_ip_octet)

brd_ip_address=[]
for each_octet in brd_ip_octets:
    brd_ip_address.append(str(int(each_octet,2)))
    #print(brd_ip_address)

broadcast_address=".".join(brd_ip_address)
#print(broadcast_address)

print("\n")
print("Network address is: %s" % network_address)
print("Broadcast address is: %s" % broadcast_address)
print("No.of valid hosts per subnet: %s" % no_of_hosts)
print("Wildcard mask: %s" % wildcard_mask)
print("Mask bits: %s" % no_of_ones)
print("\n")

#Application part 4

# Random IP generator

import random
#bst_ip_address=['192', '168', '3', '255']
#net_ip_address=['192', '168', '3', '0']

while True:
    generate=input("Generate random ip address from subnet? (y/n)")
    if generate == "y":
        generated_ip=[]
    
        for indexb,oct_bst in enumerate(brd_ip_address):
        #print(indexb,oct_bst)
            for indexn,oct_net in enumerate(net_ip_address):
               #print(indexn,oct_net)
                   if indexb==indexn:
                           if oct_bst==oct_net:
                                generated_ip.append(oct_bst)
                                #print(generated_ip)

                           else:
                                generated_ip.append(str(random.randint(int(oct_net),int(oct_bst))))
                                #print(generated_ip)

        y_iaddr = ".".join(generated_ip)
        #print(y_iaddr)
        print("Random IP address is: %s " % y_iaddr)

    else:
        print("Okay! Bye!!!\n")

        




    

    
            
            
            

        
        
        

                      
    
     

