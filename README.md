# SDN-Firewall-as-a-service-for-Floodlight-Controller-using-REST

Video Walk through link
# [Imgur](http://i.imgur.com/tblRUxo.gifv)

Firewall as a serviceSDN Firewall as a service for Floodlight Controller using REST

1. 	The main aim of this project was to provide an orchestration software for firewall deployment.
2. 	Developed a restful firewall as a service app which is integrated with SDN controller on north bound interface.
3. 	The orchestration software allows deployment of firewall, installation of policies & fine grain network management with ease. 	Policies could be based on Layer2, layer3 or layer 4 attributes like IPaddress, Mac address, src ports, ether type etc.
4. 	Used the APIs provided by flood light controller to develop the software in Python.
5.	Then the following options are provided:

    **Enable Firewall:**
  Enables firewall & by default blocks everything in the network
  
    **Disable Firewall:**
	Disables firewall
  
    **List all existing rules:**
    Lists all the existing rules.
6.	Once the firewall is enabled the app provides the following options:
•	Add allow rules
-	You can provide a wide variety of matches including port no, MAC address, IP address etc.
-	Action is allow
•	Add block rules
-	You can provide a wide variety of matches including port no, MAC address, IP address etc.
-	Action is deny
•	Delete a rule by ID
-	Takes in a ID and deletes that particular ID
7.	A working demo has been added with this file as a gif file(video) where we explore all the features of the application.
