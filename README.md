#Port Scanner Script

**Introduction
This script is a basic port scanner that checks the open ports on a given host within a specified range. It uses Python's socket library to establish a connection to each port and identify if it's open.


**Requirements

Python 3.x
Basic understanding of networking concepts
Installation
No additional libraries are required as the script uses the built-in socket module of Python.

**Usage

Run the script using a Python interpreter.
Enter the target hostname or IP address when prompted.
Specify the start and end port numbers for the scan range.

**Example:

  ```python
  
  python port_scanner.py
  Enter the host to be scanned: example.com
  Start port: 50
  End port: 500
```

**Output

The script will output the status of each port within the specified range, indicating whether a port is open.


**Disclaimer

Port scanning can be seen as a hostile activity by network administrators. Always have explicit permission before scanning a network that you do not own or have explicit authorization to test.
