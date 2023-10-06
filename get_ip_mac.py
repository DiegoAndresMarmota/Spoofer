#pip install scapy
import scapy.all as scapy


def check_scan(ip):
    """
    The function `check_scan` uses scapy to send an ARP request to a given IP address and returns a list
    of dictionaries containing the IP and MAC addresses of the devices that responded.
    
    :param ip: The `ip` parameter is the IP address or IP range that you want to scan for. It can be a
    single IP address or a range of IP addresses specified in CIDR notation
    :return: a list of dictionaries, where each dictionary contains the IP address and MAC address of a
    device that responded to the ARP request.
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="aa:bb:cc:dd:ee:ff")
    
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
    
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    checked_list = []
    for ip_mac in answered_list:
        ip_mac_dict = {"ip": ip_mac[1].psrc, "mac": ip_mac[1].hwsrc}
        checked_list.append(ip_mac_dict)
    return checked_list


def verify_scan(checked_scan):
    """
    The function "verify_scan" prints the IP address and MAC address of each scan in the "checked_scan"
    list.
    
    :param checked_scan: A list of dictionaries, where each dictionary represents a scanned device and
    contains the IP address and MAC address of the device
    """
    print("IP Address", "MAC Address \n")
    for scan in checked_scan:
        print(f' scan["ip"]  scan["mac"] \n')


# The code is calling the `check_scan` function with the IP address or IP range "012.345.6.7/89" as
# the argument. This function uses scapy to send an ARP request to the specified IP address or range
# and returns a list of dictionaries containing the IP and MAC addresses of the devices that responded
# to the request.
check_scan("012.345.6.7/89")
