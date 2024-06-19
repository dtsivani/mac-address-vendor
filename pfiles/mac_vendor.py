from scapy.all import*
import requests

def download_oui_database(file_path):
     url = "http://standards-oui.ieee.org/oui/oui.txt"
     if not os.path.exists(file_path):
         response = requests.get(url)
         with open(file_path, 'wb') as file:
             file.write(response.content)

def load_oui_database(file_path):
     oui_dict = {}
     with open(file_path, 'r') as file:
         for line in file:
             if '(hex)' in line:
                 parts = line.split('(hex)')
                 oui = parts[0].strip().replace("-", ":")
                 vendor = parts[1].strip()
                 oui_dict[oui] = vendor
     return oui_dict

def get_vendor_by_mac_local(mac_address, oui_dict):
    
     oui = ":".join(mac_address.split(":")[:3]).upper()
     return oui_dict.get(oui, "Unknown Vendor")

if __name__ == "__main__":
    ip_address=input("enter the ip range ")
    ip_address=ip_address+'/24'
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address), timeout=10,verbose=False)
    ip,mac=[],[] 
    for send, receive in ans:
         mac.append(receive[Ether].src)
    for send, receive in ans:
         ip.append(receive[ARP].psrc)
    oui_database_path = "oui.txt"   
    download_oui_database(oui_database_path)
    oui_dict = load_oui_database(oui_database_path)
    for i in range(len(mac)):
        vendor = get_vendor_by_mac_local(mac[i], oui_dict)
        print(f"{ip[i]}",'    ',f"{mac[i]}",'     ',f'{vendor}')
 
