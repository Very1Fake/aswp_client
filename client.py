# ASWP v0.0.1pa1

import modules.connection as connection
import modules.tools as tools
import ipaddress

# Connect to server
## Get server ip

for i in range(3):
    ip = input()

    if ':' in ip:
        port = ip.split(':')[1]
        ip = ip.split(':')[0]

    try:
        ipaddress.ip_address(ip)
        break
    except Exception:
        print('Invaid ip address')
else:
    tools.initExitMsg('Too many invalid attemptions.')

## Trying to connect

