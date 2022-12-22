import requests 

#Scan the website for open ports 

def scan_ports(url): 
  try: 
    #Set all ports to open by default
    open_ports = [] 

    # Loop through 1 - 65535 to check each port
    for i in range(1, 65535): 
      #Set a timeout of 3 seconds  
      result = requests.get(url, timeout=3) 
      
      # If returns 200, then port is open 
      if result.status_code == 200: 
        open_ports.append(i) 
    
    #Return all open ports 
    return open_ports

  except Exception as e: 
    print(str(e))

# Scan for known vulnerabilities on each port

def scan_vulnerabilities(open_ports): 
  for port in open_ports: 
    # Use the common vulnerabilities and exposure database to look for known vulnerabilities 
    response = requests.get('https://cve.mitre.org/data/downloads/allitems.csv') 

    # If a vulnerability is found, alert the user
    if response.status_code == 200 and 'vulnerability' in response.text: 
      print('Vulnerability discovered on port {}'.format(port)) 

#Run the scans 

def run_scans(url): 
  #Scan for open ports 
  open_ports = scan_ports(url) 
  #Scan for known vulnerabilities 
  scan_vulnerabilities(open_ports)

#Run the scripts 

run_scans('url')
