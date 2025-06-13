from netaddr import IPNetwork

subnet = input("Enter the subnet (e.g., 192.168.0.0/22): ")

try:
    network = IPNetwork(subnet)
except Exception as e:
    print("Invalid subnet:", e)
    exit()

try:
    ip_index = int(input("Enter the IP position you want (e.g., 450): "))
except ValueError:
    print("Please enter a valid number!")
    exit()

hosts = list(network.iter_hosts())

if 0 < ip_index <= len(hosts):
    print(f"The {ip_index}th IP in subnet {network.cidr} is: {hosts[ip_index - 1]}")
else:
    print(f"The {ip_index}th IP does not exist in this subnet. This subnet only has {len(hosts)} usable hosts.")

