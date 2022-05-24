import json

def replace():

    with open('package.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    json_object = json.dumps(json_object, indent=4).replace("^","")
    json_object = json.loads(json_object)
    json_object = json.dumps(json_object, indent=4).replace("~","")
    json_object = json.loads(json_object)

    with open("package.json", "w") as outfile:
        json.dump(json_object, outfile, indent=4)


if __name__ == '__main__':
    replace()
