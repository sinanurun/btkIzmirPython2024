import json

# some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])
# print(type(y["age"]))

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)

class Ogrenci():
    # def __init__(self,name, age, city):
    def __init__(self,kwargs):
        self.ad = kwargs["name"]
        self.age = kwargs["age"]
        self.city = kwargs["city"]

# ogr = Ogrenci('ali', 20, 'New York')
# print(vars(ogr))
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
ogr = Ogrenci(x)
print(vars(ogr))