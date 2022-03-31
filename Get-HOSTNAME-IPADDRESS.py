import socket    
host_name = socket.gethostname()    
IPAddress = socket.gethostbyname(host_name)    
print("Your Computer Name is:" + host_name)    
print("Your Computer IP Address is:" + IPAddress) 
#How to get the IP address of a client using socket module