import urllib, json

url = "http://ocalhost:8000/sm/sl/json/22/"
try:
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	myResult = data['links']

	for rs in myResult:
		print rs['position'], rs['sl_link__url'], rs['display_time']
		#pass the above to <selenium>
except: 
	print "Failed to get json"

