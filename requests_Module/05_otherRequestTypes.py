import requests

r = requests.put("https://httpbin.org/put" , data={"a":1, "b":3}) # PUT request is used to send data to the server to update an existing resource
print(r.text)
r = requests.delete("https://httpbin.org/delete") # delete request is used to delete a resource
print(r.text)
r = requests.head("https://httpbin.org/get") # head request is used to get the only the header information about the requested resource
print(r.text)
r = requests.options("https://httpbin.org/get") # OPTIONS request is an HTTP method used primarily to describe the communication options for the target resource.
print(r.text)