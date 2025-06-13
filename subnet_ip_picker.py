from netaddr import IPNetwork

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def get_valid_subnet():
    while True:
        subnet = input("Enter the subnet (e.g., 192.168.0.0/22): ").strip()
        if subnet.lower() == 'exit':
            print("Exiting program.  Goodbye!")
            exit()
        if not subnet:
            print("No subnet provided. Please try again.")
            continue
        if '/' not in subnet:
            print("Subnet must include prefix (e.g., /24, /22, etc.). Please try again.")
            continue
        try:
            return IPNetwork(subnet)
        except Exception as e:
            print(f"Invalid subnet format or value: {subnet}\n")

def pick_ip_from_subnet():
    try:
        while True:
            network = get_valid_subnet()
            hosts = list(network.iter_hosts())

            ip_input = input("Enter IP position (number) or type 'last' for the last usable IP: ").strip()
            if ip_input.lower() == 'exit':
                    print("Exiting program.")
                    exit()
            
            if ip_input.lower() == 'last':
                selected_ip = hosts[-1]
                print(f"The LAST usable IP in subnet {network.cidr} is: {selected_ip}")
            else:
                try:
                    ip_index = int(ip_input)
                    if 0 < ip_index <= len(hosts):
                        print(f"The {ordinal(ip_index)} IP in subnet {network.cidr} is: {hosts[ip_index - 1]}\n")
                    else:
                        print(f"The {ordinal(ip_index)} IP does not exist in this subnet. This subnet only has {len(hosts)} usable hosts.\n")
                except ValueError:
                    print("Invalid input. Please enter a number or 'last'.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Exiting gracefully.")
        exit()

if __name__ == "__main__":
    pick_ip_from_subnet()