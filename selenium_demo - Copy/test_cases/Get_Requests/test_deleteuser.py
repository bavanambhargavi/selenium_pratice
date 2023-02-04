import requests
import jsonpath

#API  Url
Url = "https://reqres.in/api/users/2"
def test_sample2():

   response = requests.delete(Url)

# fetch the response code
   print(response.status_code)
   assert response.status_code == 204

