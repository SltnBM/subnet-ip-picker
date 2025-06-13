from netaddr import IPNetwork

subnet = input("Enter the subnet (e.g., 192.168.0.0/22): ")

try:
    network = IPNetwork(subnet)
except Exception as e:
    print("Invalid subnet:", e)
    exit()

try:
    ip_input = input("Enter the IP position you want (number or type 'last'): ").strip()
except ValueError:
    print("Please enter a valid number!")
    exit()

hosts = list(network.iter_hosts())

if ip_input.lower() == 'last':
    selected_ip = hosts[-1]
    print(f"The LAST usable IP in subnet {network.cidr} is: {selected_ip}")
else:
    try:
        ip_index = int(ip_input)
        if 0 < ip_index <= len(hosts):
            print(f"The {ip_index}th IP in subnet {network.cidr} is: {hosts[ip_index - 1]}")
        else:
            print(f"The {ip_index}th IP does not exist in this subnet. This subnet only has {len(hosts)} usable hosts.")
    except ValueError:
        print("Invalid input. Please enter a number or 'last'.")

