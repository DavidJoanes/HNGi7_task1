import json
data = {}
data = {
    "fullname": "David Kemdirim",
    "HNG ID": "HNG-00819",
    "language": "Python",
}

# Transferring the details in the variable 'data' into a newly created json file
details = json.dump(data, open("data.json", "w"))

# Reading the data in the json file called 'detail' and assigning it to a variable called 'detail_access'
with open("./data.json") as detail:
    detail_access = json.load(detail)

print(type(detail_access))
print("Hello world, this is " + detail_access["fullname"] + " with HNG ID: " + detail_access["HNG ID"] + ", using " + detail_access["language"] + " for stage two task.")