```
  ____  ____  _   _ _____ _____   _____ ___  ____   ____ _____ ____  
 | __ )|  _ \| | | |_   _| ____| |  ___/ _ \|  _ \ / ___| ____|  _ \ 
 |  _ \| |_) | | | | | | |  _|   | |_ | | | | |_) | |   |  _| | |_) |
 | |_) |  _ <| |_| | | | | |___  |  _|| |_| |  _ <| |___| |___|  _ < 
 |____/|_| \_\\___/  |_| |_____| |_|   \___/|_| \_\\____|_____|_| \_\
```
BRUTE-FORCER-ALL-IN-ONE
A powerful Python-based automation wrapper for Ncrack. This tool provides a 
comprehensive menu-driven interface to perform high-speed brute force attacks 
across multiple categories including Remote Access, Databases, Web CMS, 
Email services, and IoT protocols.

**Features**
* **Remote Access:** Brute force SSH, RDP, Telnet, VNC, and WinRM.
* **File Transfer:** Supports FTP, SMB, SFTP/SCP, and TFTP.
* **Database Auditing:** Attack MySQL, PostgreSQL, MSSQL, MongoDB, and Redis.
* **CMS & Web:** Specialized modules for WordPress login and HTTP/HTTPS.
* **Email & Communication:** Supports POP3(S), IMAP(S), and SIP.
* **IoT & Industrial:** Target MQTT and SNMP services.
* **Smart Defaults:** Automatically suggests standard ports (22, 3389, 445, etc.) but allows manual override.

**Prerequisites**
The following tools must be installed for the script to function:
* Python 3.x
* Ncrack: The high-speed network authentication cracking tool.
* Figlet: (The script attempts to install this automatically via apt).

**Installation**

Clone the repository:
   * git clone https://github.com/Tde99/Brute-Forcer.git

Navigate to the directory:
   * cd Brute-Forcer

Make the script executable:
   * chmod +x bruteforce.py

**Usage**
Network-level operations and package installation require root privileges:

sudo python3 bruteforce.py

**Step-by-Step Execution:**
1. **Target Info:** Enter the target IP address and the paths to your Userlist and Passwordlist files.
2. **Category Selection:** Choose from 6 main service categories (Remote Access, Database, etc.).
3. **Service Selection:** Choose the specific protocol (e.g., SSH).
4. **Port Configuration:** Use the default port or specify a custom one.
5. **Execution:** The script generates and executes the optimal Ncrack command for you.

**Important Notes:**
* **Ethics:** Strictly for authorized penetration testing and educational purposes.
* **Performance:** Uses T3/T4 timing templates in Ncrack for a balance between speed and reliability.
