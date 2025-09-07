import  whois
domain = input("Enter the domain name: ")

info = whois.whois(domain)

def safe_get(value):
    if not value:
        return defult
    if isinstance(value, list):
        return value[0] 
    return value

print("OUTPUT")
print(f" Domain Name     : {safe_get(info.domain_name)}")
print(f" Regestrar Name  : {safe_get(info.registrar)}")
print(f" Creation Date   : {safe_get(info.creation_date)}")
print(f" Update Date     : {safe_get(info.updated_date)}")
print(f" Expiration Date : {safe_get(info.expiration_date)}")