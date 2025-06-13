from netaddr import IPNetwork

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def pick_ip_from_subnet():
    subnet = input("Enter the subnet (e.g., 192.168.0.0/22): ")

    if not subnet:
        print("No subnet provided.")
        exit()

    try:
        network = IPNetwork(subnet)
    except Exception as e:
        print("Invalid subnet:", e)
        exit()

    ip_input = input("Enter IP position (number) or type 'last' for the last usable IP: ").strip()

    hosts = list(network.iter_hosts())

    if ip_input.lower() == 'last':
        selected_ip = hosts[-1]
        print(f"The LAST usable IP in subnet {network.cidr} is: {selected_ip}")
    else:
        try:
            ip_index = int(ip_input)
            if 0 < ip_index <= len(hosts):
                print(f"The {ordinal(ip_index)} IP in subnet {network.cidr} is: {hosts[ip_index - 1]}")
            else:
                print(f"The {ordinal(ip_index)} IP does not exist in this subnet. This subnet only has {len(hosts)} usable hosts.")
        except ValueError:
            print("Invalid input. Please enter a number or 'last'.")

if __name__ == "__main__":
    pick_ip_from_subnet()