# SDN-Firewall-as-a-service-for-Floodlight-Controller-using-REST

Video Walk through link below
[Imgur](http://i.imgur.com/tblRUxo.gifv)

Firewall as a serviceSDN Firewall as a service for Floodlight Controller using REST

Firewall as a Service
1.	I have leveraged the existing firewall supported by floodlight & developed an orchestration software.
2.	The Application asks for the controller IP address in the beginning.
3.	Then the following options are provided:
•	Enable Firewall
-	Enables firewall & by default blocks everything in the network
•	Disable Firewall
-	Disables firewall
•	List all existing rules
-	Lists all the existing rules.
4.	Once the firewall is enabled the app provides the following options:
•	Add allow rules
-	You can provide a wide variety of matches including port no, MAC address, IP address etc.
-	Action is allow
•	Add block rules
-	You can provide a wide variety of matches including port no, MAC address, IP address etc.
-	Action is deny
•	Delete a rule by ID
-	Takes in a ID and deletes that particular ID
5.	A working demo has been added with this file as a gif file(video) where we explore all the features of the application.

