import argparse
from netaddr import IPNetwork

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def validate_subnet(subnet):
    try:
        return IPNetwork(subnet)
    except Exception:
        print(f"Invalid subnet format or value: {subnet}\n")
        return None

def get_hosts(network):
    return list(network.iter_hosts())

def display_ip(network, hosts, position):
    if position.lower() == 'last':
        selected_ip = hosts[-1]
        print(f"The LAST usable IP in subnet {network.cidr} is: {selected_ip}\n")
    else:
        try:
            index = int(position)
            if 0 < index <= len(hosts):
                print(f"The {ordinal(index)} IP in subnet {network.cidr} is: {hosts[index - 1]}\n")
            else:
                print(f"The {ordinal(index)} IP does not exist in this subnet. This subnet only has {len(hosts)} usable hosts.\n")
        except ValueError:
            print("Invalid input. Please enter a number or 'last'.")

def run_interactive():
    try:
        while True:
            while True:
                subnet = input("Enter the subnet (e.g., 192.168.0.0/22): ").replace(" ", "").strip()
                if subnet.lower() == 'exit':
                    print("Exiting program. Goodbye!")
                    exit(0)
                if not subnet or '/' not in subnet:
                    print("Invalid format. Example: 192.168.0.0/24\n")
                    continue
                network = validate_subnet(subnet)
                if network:
                    break
            
            hosts = get_hosts(network)

            ip_input = input("Enter IP position (number) or type 'last' for the last usable IP: ").strip()
            if ip_input.lower() == 'exit':
                print("Exiting program. Goodbye!")
                exit(0)

            display_ip(network, hosts, ip_input)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        exit(0)

def run_cli(subnet, position):
    network = validate_subnet(subnet)
    hosts = get_hosts(network)
    display_ip(network, hosts, position)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pick an IP address from a subnet.",
        epilog="Example usage:\n  python ip_picker.py --subnet 192.168.1.0/24 --position 5\n  python ip_picker.py --subnet 192.168.1.0/24 --position last",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("--subnet", "-s", help="Subnet in CIDR notation (e.g., 192.168.1.0/24)")
    parser.add_argument("--position", "-p", help="IP position number (1-based) or 'last' for last usable IP")

    args = parser.parse_args()

    if args.subnet and args.position:
        run_cli(args.subnet.replace(" ", "").strip(), args.position.strip())
    elif args.subnet or args.position:
        print("Both --subnet and --position must be provided together for non-interactive mode.\n")
        parser.print_help()
    else:
        run_interactive()