import requests,uuid,webbrowser
webbrowser.open('https://www.facebook.com/profile.php?id=100063307807505&mibextid=ZbWKwL')

user = input('Enter Gmail : ')
password = input('password Mushq G: ')

def login():
	
	url = "https://i.instagram.com/api/v1/accounts/login/"
	
	data = {
	  'username': user,
	  'password': password,
	  'device_id': str(uuid.uuid4()),
	}
	
	headers = {
	  'User-Agent': "Instagram 100.0.0.17.129 Android (31/12; 280dpi; 720x1471; samsung; SM-A025F; a02q; qcom; en_US; 161478664)",
	  'Accept-Encoding': "gzip, deflate",
	  'X-Pigeon-Session-Id': "7440c656-3571-4da1-a39b-0ba705d4fa65",
	  'X-Pigeon-Rawclienttime': "1722648011.442",
	  'X-IG-Connection-Speed': "-1kbps",
	  'X-IG-Bandwidth-Speed-KBPS': "-1.000",
	  'X-IG-Bandwidth-TotalBytes-B': "0",
	  'X-IG-Bandwidth-TotalTime-MS': "0",
	  'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
	  'X-IG-Connection-Type': "WIFI",
	  'X-IG-Capabilities': "3brTvw==",
	  'X-IG-App-ID': "567067343352427",
	  'Accept-Language': "en-US",
	  'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
	  'X-FB-HTTP-Engine': "Liger",
	  'Cookie': "mid=Zq2FmwABAAFSB7rkvqnTqHq91P-0; csrftoken=RJ3FIu1MclvJw5zGPlkFbgiN8GKt5wnS"
	}
	
	response = requests.post(url, data=data, headers=headers)
	
	#print(response.text)
	if 'logged_in_user' in response.text:
		print('𝗚σσ𝗗 𝗟σgιи ✅ '+user+' | '+password)
		
	elif 'The password you entered is incorrect. Please try again.' in response.text:
		print('𝗕α𝗗 𝗟σgιи ❌ '+user+' | '+password)
		
	elif 'Invalid Parameters' in response.text:
		print('𝗕α𝗗 𝗟σgιи ❌ '+user+' | '+password)
		
	elif "invalid_user" in response.text:
		print('𝗕α𝗗 𝗟σgιи ❌ '+user+' | '+password)
		
	else:
		print('Mushq g apki IP block hai ❌ '+user+' | '+password)
login()