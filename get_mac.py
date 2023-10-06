#!/usr/bin/...

import re
import subprocess
import optparse


def get_arguments():
    """
    The function `get_arguments()` takes user input for an interface and a new MAC address, and returns
    the output of the `ifconfig` command for the specified interface.
    :return: the output of the `ifconfig` command for the specified interface.
    """
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options


# The lines `interface = optparse.OptionParser.interface` and `new_mac =
# optparse.OptionParser.new_mac` are attempting to assign values to the variables `interface` and
# `new_mac` using the `optparse` module.
interface = optparse.OptionParser.interface
new_mac = optparse.OptionParser.new_mac


def change_mac(interface, new_mac):
    """
    The function `change_mac` is used to change the MAC address of a network interface in Python.
    
    :param interface: The interface parameter is the name of the network interface that you want to
    change the MAC address for. This could be something like "eth0" or "wlan0" depending on your system
    :param new_mac: The `new_mac` parameter is the new MAC address that you want to assign to the
    specified network interface
    """
    try:
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether0", new_mac])
        subprocess.call(["ifconfig", interface, "up"])
    except subprocess.SubprocessError:
        subprocess.SubprocessError.args("[-] Could not change MAC address", interface, new_mac)
    except:
        subprocess.SubprocessError.__call__("[-] Could not change MAC address", change_mac)
    else:
        print("[+] Changing MAC address for " + interface + " to " + new_mac)
    finally:
        print("Done")


def get_alternative_mac(interface):
    """
    The function `get_alternative_mac` retrieves the MAC address of a given network interface.
    
    :param interface: The "interface" parameter is the name of the network interface for which you want
    to retrieve the MAC address
    :return: the MAC address of the specified interface.
    """
    results_arguments = subprocess.check_output(
        ["ifconfig", options.interface])
    mac_address_search = re.search(r"[...]", str(options), re.I)
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[-] Could not read MAC address.")



options = get_arguments()

alternative_mac = get_alternative_mac(options.interface)
print("Current MAC = " + str(alternative_mac))

change_mac(interface, new_mac)
if alternative_mac == new_mac:
    print("[+] MAC address was successfully changed to " + new_mac)
else:
    print("[-] MAC address did not get changed.")
