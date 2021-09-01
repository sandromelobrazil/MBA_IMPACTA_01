#!/usr/bin/python
import json
import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
#shodan_target = '149.56.244.87' 
shodan_target = '179.191.78.194' 
shodan_host = shodan_api.host(shodan_target) 


mydictionary = shodan_host
shodan_json = json.dumps(mydictionary, indent = 6)
print(shodan_json)


