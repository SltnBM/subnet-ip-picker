# Subnet IP Picker
A simple command-line tool to pick specific IP addresses from a given subnet. Supports selecting IPs by position number or retrieving the last usable IP. Built for educational and practical network addressing purposes.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Requirements](https://img.shields.io/badge/requirements.txt-up%20to%20date-brightgreen)

---

## Features
- Retrieve specific IP by position number
- Retrieve the last usable IP in the subnet
- CLI argument support
- Validates subnet format (requires CIDR prefix)
- Graceful exit on Ctrl+C or typing `exit`
- Looping mode for continuous usage

---

## Requirements
1. Python 3.6 or higher
2. netaddr
3. rich

Install dependencies by running:
```bash
pip install -r requirements.txt
```

or manually:
```bash
pip install netaddr rich
```

---

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

---

## Usage
#### Option 1: With CLI arguments
```bash
python subnet_ip_picker.py -s <subnet> -p <position>
```

Example:
```bash
python subnet_ip_picker.py -s 192.168.1.0/24 -p 5
```
or

```bash
python subnet_ip_picker.py -s 192.168.1.0/24 -p last
```

#### Option 2: Interactive mode
If no arguments are provided, the script will ask for input
```bash
python subnet_ip_picker.py
```

Example:
```plaintext
==================================================
Subnet IP Picker — Type 'exit' anytime to quit.
==================================================

--- Subnet Input ---
Enter the subnet (e.g., 192.168.0.0/22): 110.71.0.0/18

--- IP Position Input ---
Enter IP position (number) or type 'last' for the last usable IP: 9000
The 9000th IP in subnet 110.71.0.0/18 is: 110.71.35.40

--------------------------------------------------

--- Subnet Input ---
Enter the subnet (e.g., 192.168.0.0/22): 110.71.0.0/18

--- IP Position Input ---
Enter IP position (number) or type 'last' for the last usable IP: last
The LAST usable IP in subnet 110.71.0.0/18 is: 110.71.63.254

--------------------------------------------------
```

To exit the program, press `Ctrl+C` or type `exit` when prompted.

---

## Contributing
Contributions are welcome. Feel free to open issues or submit pull requests for improvements.

---

## Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sultan%20Badra-blue?logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/sultan-badra)

---

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
