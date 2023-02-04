#from json import JSONDecoder
import json
import requests
import jsonpath

#ApI users
Url = 'https://reqres.in/api/users'

#Read input json file
def test_resources():
   file = open('D:\\pratice_pytest\\bhargavi_pytests\\Get_requests\\sample.json','r')
   json_input = file.read()

   requests_json = json.loads(json_input)
   print(requests_json)

#make post using input body
   Response = requests.post(Url,requests_json)
   print(Response.content)

#validating response
   assert Response.status_code == 201

#fetch header from response

   print(Response.headers.get('content-length'))


#parse response grom json format

   Response_json = json.loads(Response.text)

#pick id using jsonpath

   id= jsonpath.jsonpath(Response_json,'id')
   print(id[0])
