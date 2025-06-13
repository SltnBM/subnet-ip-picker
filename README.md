# Subnet IP Picker
A simple command-line tool to pick specific IP addresses from a given subnet. Supports selecting IPs by position number or retrieving the last usable IP. Built for educational and practical network addressing purposes.

## Features
- Retrieve specific IP by position number
- Retrieve the last usable IP in the subnet
- Validates subnet format (requires CIDR prefix)
- Graceful exit on Ctrl+C or typing `exit`
- Looping mode for continuous usage

## Requirements
1. Python 3.6 or higher
2. netaddr

Install dependencies by running:
```bash
pip install -r requirements.txt
```

or

```bash
pip install netaddr
```

## How to Use
1. Make sure you have Python installed (Python 3.6 or higher). Download it from [python.org](https://www.python.org/downloads/).
2. Clone the repository:
```bash
git clone https://github.com/SltnBM/subnet-ip-picker.git
```
3. Navigate to the project directory:
```bash
cd subnet-ip-picker
```
4. Run the script:

```bash
python subnet_ip_picker.py
```

## Usage
Example interaction:
```plaintext
Enter the subnet (e.g., 192.168.0.0/22): 192.168.1.0/24
Enter IP position (number) or type 'last' for the last usable IP: 5
The 1st IP in subnet 192.168.1.0/24 is: 192.168.1.5

Enter the subnet (e.g., 192.168.0.0/22): 192.168.1.0/24
Enter IP position (number) or type 'last' for the last usable IP: last
The LAST usable IP in subnet 192.168.1.0/24 is: 192.168.1.254
```

To exit the program, press `Ctrl+C` or type `exit` when prompted.

## Contributing
Contributions are welcome. Feel free to open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.