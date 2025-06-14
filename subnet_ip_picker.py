import argparse
from netaddr import IPNetwork
from rich import print

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def validate_subnet(subnet):
    try:
        network = IPNetwork(subnet)
        hosts = list(network.iter_hosts())
    
        if network.prefixlen == 31:
            print(f"[cyan]Note:[/] Subnet [bold]{network.cidr}[/] is a /31, used for point-to-point links. Both [bold]{hosts[0]}[/] and [bold]{hosts[1]}[/] are usable.\n")
        elif network.prefixlen == 32:
            print(f"[cyan]Note:[/] Subnet [bold]{network.cidr}[/] is a /32, representing a single host address: [bold]{hosts[0]}[/]\n")
        elif len(hosts) < 2:
            print(f"[yellow]Warning:[/] Subnet [bold]{network.cidr}[/] has [bold]{len(hosts)}[/] usable host(s).\n")
        
        return network
        
    except Exception:
        print(f"[red]Error:[/] Invalid subnet format or value: [bold]{subnet}[/]\n")
        return None

def get_hosts(network):
    return list(network.iter_hosts())

def display_ip(network, hosts, position):
    if not hosts:
        if network.prefixlen == 32:
            print(f"[green]Subnet {network.cidr} represents a single host:[/] [bold]{network.ip}[/]\n")
        else:
            print(f"[yellow]Subnet {network.cidr} has no usable hosts.[/]\n")
        return
    if position.lower() == 'last':
        selected_ip = hosts[-1]
        print(f"The [bold]LAST[/] usable IP in subnet [bold]{network.cidr}[/] is: [green]{selected_ip}[/]\n")
    else:
        try:
            index = int(position)
            if 0 < index <= len(hosts):
                print(f"The [bold]{ordinal(index)}[/] IP in subnet [bold]{network.cidr}[/] is: [green]{hosts[index - 1]}[/]\n")
            else:
                print(f"[yellow]The {ordinal(index)} IP does not exist in this subnet.[/] This subnet only has [bold]{len(hosts)}[/] usable hosts.\n")
        except ValueError:
                print("[red]Invalid input.[/] Please enter a number or 'last'.")

def run_interactive():
    print("[bold cyan]" + "="*50 + "[/]")
    print("[bold]Subnet IP Picker[/] — [dim]Type 'exit' anytime to quit.[/]")
    print("[bold cyan]" + "="*50 + "[/]")
    
    try:
        while True:
            while True:
                print("\n[cyan]--- Subnet Input ---[/]")
                subnet = input("Enter the subnet (e.g., 192.168.0.0/22): ").replace(" ", "").strip()
                if subnet.lower() == 'exit':
                    print("[green]Exiting program. Goodbye![/]")
                    exit(0)
                if not subnet or '/' not in subnet:
                    print("[red]Invalid format.[/] Example: 192.168.0.0/24\n")
                    continue
                network = validate_subnet(subnet)
                if network:
                    break
            
            hosts = get_hosts(network)

            print("\n[cyan]--- IP Position Input ---[/]")
            ip_input = input("Enter IP position (number) or type 'last' for the last usable IP: ").strip()
            if ip_input.lower() == 'exit':
                print("[green]Exiting program. Goodbye![/]")
                exit(0)

            display_ip(network, hosts, ip_input)
            print("[dim]" + "-"*50 + "[/]")
    except KeyboardInterrupt:
        print("\n[red]Program interrupted.[/] Exiting.")
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
        print("[red]Both --subnet and --position must be provided together.[/]\n")
        parser.print_help()
    else:
        run_interactive()