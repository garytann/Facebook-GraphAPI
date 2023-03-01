# Facebook GraphAPI
This shows a simple use-case of Facebook's GraphAPI. The API is free to use except with a rate-limit, find out more: https://developers.facebook.com/docs/graph-api/overview/rate-limiting#platform-rate-limits

# Setup
## Register a developer account with Facebook and creating a meta app
- Begin the process by visiting this link: https://developers.facebook.com/docs/development/register/
- Next, register a meta application, this is to get the access token

## Install dependencies
```
pip install -r requirements.txt
```

# Usage
## Obtain a long-lived access token
- A long-lived access token last for 60 days, so you can test your applications without the need to regenerate the access token, more info: https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived/
```
https://graph.facebook.com/v16.0/oauth/access_token?grant_type=fb_exchange_token&client_id=${CLIENT ID}&client_secret=${CLIENT SECRET}&fb_exchange_token=${PAGE/USER ACCESS TOKEN}
```
##  Using the API
- You can use the built-in api explorer: https://developers.facebook.com/tools/explorer/ or in my case I prefer the usage of Postman
-  You need to acquire the **page-id** of your Facebook's page, which could be obtained from the page's url
- You can begin usage of the API now with:
```
https://graph.facebook.com/${PAGE ID}/posts?access_token=${ACCESS TOKEN}
```
## Using app.py
- Create a file secret.py or .env and store your credentials, in app.py import the credentials to be used 
- Retrieve: 
	- Parent post content
	- Child comments' content
	-  Child comments' author
	- Reactions
	- Dates
	- Hyperlinks
	- Most reacted comments


