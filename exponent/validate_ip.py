# validate IP address
def validateIP(ip: str) -> bool:
    ip = ip.split(".")
    if len(ip) != 4:
        return False
    
    for num in ip:
        if not num.isdigit() or (int(num) < 0 or int(num) > 255):
            return False
        elif len(num) > 1 and num[0] == "0":
            return False
    return True
	
# debug your code below
print(validateIP('192.168.0.1')) # true
print(validateIP('0.0.0.0')) # true
print(validateIP('123.24.59.99')) # true
print(validateIP('192.168.123.456')) # false
print(validateIP('12.34.56.oops')) # false
print(validateIP('1.2.3.4.5')) # false
