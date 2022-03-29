import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name" : "How to...", "views" : 100000, "likes" : 1234},
    {"name" : "Create a ....", "views" : 123425, "likes" : 45426},
    {"name" : "Play like...", "views" : 34462, "likes" : 5422}
]



# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input() 

# response = requests.delete(BASE + "video/0")
# print(response)

response = requests.put(BASE + "video/1", {"name" : "How to...", "views" : 100000, "likes" : 1234})
print(response.json())

input()

response = requests.get(BASE + "video/1")
print(response.json())

input()

response = requests.delete(BASE + "video/1")
print(response.json())
