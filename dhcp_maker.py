from dataclasses import dataclass
import csv
import os

def print_header():
    print("""\
#
# DHCP Server Configuration file.
# see /usr/share/doc/dhcp*/dhcpd.conf.sample
# see 'man 5 dhcpd.conf'
#\
""")

def print_subnet(device):
    print(f"""\
subnet {device.subnet} netmask {device.netmask} {{
option domain-name "{device.domain_name}";
}}\
""")

def print_device(device):
    print(f"""\
host {device.host_name} {{
option dhcp-client-identifier {device.mac_address};
fixed-address {device.IP_address};
option bootfile-name "{device.bootfile_name}";
}}\
""")

@dataclass
class device_data:
    subnet: str
    netmask: str
    domain_name: str
    host_name: str
    mac_address: str
    IP_address: str
    bootfile_name: str

def main():
    file_name = "example.csv"
    devices_list = []
    current_subnet = None

    with open(os.path.join("csv", file_name), 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            device = device_data(*row)
            devices_list.append(device)
    
    print_header()
    for device in devices_list:
        if current_subnet != device.subnet:
            current_subnet = device.subnet
            print_subnet(device)
        print_device(device)

if __name__ == "__main__":
    main()