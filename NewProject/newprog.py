import json
import requests

# Get dummy data using an API
res = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?count=10&screen_name=Rbloggers")

# Convert data to dict
data = json.loads(res.text)
print(data)
print(type(data))
# Convert dict to string
data = json.dumps(data)

print(data)
print(type(data))
