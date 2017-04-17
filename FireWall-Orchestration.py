import requests,json,unicodedata
import json


def addFireWallRule(ruleSelect,cntrlIP):
	rule={}
	print("Enter Values for the fields, Enter return to skip the field")
	
	print("Switch ID: <xx:xx:xx:xx:xx:xx:xx:xx> ")
	switchId=raw_input()
	if switchId!="":
		rule["switchid"]=switchId
		
	print("Source Inport: ")
	src_input=raw_input()
	if src_input!="":
		rule["src-inport"]=src_input
		
	print("Source MAC: <xx:xx:xx:xx:xx:xx>")
	src_mac=raw_input()
	if src_mac!="":
		rule["src-mac"]=src_mac
		
	print("Destination MAC: <xx:xx:xx:xx:xx:xx>")
	dst_mac=raw_input()
	if dst_mac!="":
		rule["dst-mac"]=dst_mac
	
	
	print("dl-Type: <ARP or IPV4>")
	dl_type=raw_input()
	if dl_type!="":
		rule["dl-type"]=dl_type
	
	
	
	print("Source IP:<x.x.x.x/x>")
	src_ip=raw_input()
	if src_ip!="":
		rule["src-ip"]=src_ip
	
	print("Destination IP:<x.x.x.x/x>")
	dst_ip=raw_input()
	if dst_ip!="":
		rule["dst-ip"]=dst_ip
	
	
	print("Network Protocol:<TCP or UDP or ICMP>")
	nw_proto=raw_input()
	if nw_proto!="":
		rule["nw-proto"]=nw_proto
	
	print("Priority: ")
	pr=int(raw_input())
	rule["priority"]=pr
	if ruleSelect=="1":
		action="ALLOW"
		rule["action"]=action
	elif ruleSelect=="2":
		action="BLOCK"
		rule["action"]=action
	else:
		return
	print requests.post(url="http://"+cntrlIP+":8080/wm/firewall/rules/json",data=json.dumps(rule))

def deleteRule(cntrlIp):
	print("Enter Rule ID: ")
	ruleId=int(raw_input())
	if ruleId!="":
		rID={"ruleid":ruleId}
		print requests.delete(url="http://"+cntrlIp+":8080/wm/firewall/rules/json",data=json.dumps(rID))
	
	
print ("*****************************Fire-Wall As A Service*************************************")
print("")
print("Enter the controller's IP address: ")
cntrlIp=raw_input()

while(True):
	try:
		fStatusResponse=requests.get("http://"+cntrlIp+":8080/wm/firewall/module/status/json")
		fStatusObj=json.loads(fStatusResponse.content)
		fStatus=fStatusObj["result"]
		print "Firewall Current Status: ",fStatus
		print("Choose for the below options for your network")
		print("1. Enable Fire-Wall")
		print("2. Disable Fire-Wall")
		print("3. List all Existing Rules")
		selection= raw_input()
		if selection=="1":
			if fStatus!="firewall enabled":
				requests.put("http://"+cntrlIp+":8080/wm/firewall/module/enable/json")
				print("Firewall Enabled")
			else:
				print("Firewall Already Enabled")
			print("1. Add Allow Rules")
			print("2. Add Block Rules")
			print("3. Delete a Rule")
			ruleSelect=str(raw_input())
			if ruleSelect=="1" or ruleSelect=="2":
				addFireWallRule(ruleSelect,cntrlIp)
			elif ruleSelect=="3":
				deleteRule(cntrlIp)
		elif  selection=="2":
			if fStatus=="firewall enabled":
				requests.put("http://"+cntrlIp+":8080/wm/firewall/module/disable/json")
				print("FireWall Disabled")
			else:
				print("FireWall Already Disabled")  
		elif selection=="3":
			fRulesList=requests.get("http://"+cntrlIp+":8080/wm/firewall/rules/json")
			rulesList=json.loads(fRulesList.content)
			if len(rulesList)== 0:
				print ("No Firewall Rules Installed")
			else:
				for curRule in rulesList:
					keys=curRule.keys()
					for curItem in keys:
						print curItem," : ",curRule[curItem]
					print(" ")	
	except KeyboardInterrupt:
		break
exit()
    
