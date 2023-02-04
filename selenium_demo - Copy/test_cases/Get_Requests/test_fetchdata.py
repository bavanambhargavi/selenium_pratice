import requests
import json
import jsonpath
#API 
Url = 'https://reqres.in/api/users?page=2'

#sent Get request
def test_sample():
    requests.get(Url)
    Response = requests.get(Url)
    print(Response)

#display response content
    print(Response.content)
    print(Response.headers) 

# parse response json format
    json_Response = json.loads(Response.text)
    print(json_Response)

#fetch value using jsonpath
    pages = jsonpath.jsonpath(json_Response,'total_pages')
    print (pages[0])
    assert pages[0] == 2

