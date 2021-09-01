#!/usr/bin/python

import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
#shodan_target = '149.56.244.87' 
shodan_target = '179.191.78.194' 
shodan_host = shodan_api.host(shodan_target) 

def shodan_portscan(shodan_host):
    for _ports in shodan_host['data']:
        print("[+] - Portas Abertas:", _ports['port'])

shodan_portscan(shodan_host)


