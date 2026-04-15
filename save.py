import json
#Counter stuff
def getcount():
    global maincounter
    with open("paint/save/counter.save","r") as file:
        data = json.load(file)
        data = list(data)
        return data[0]
def increase():
    with open("paint/save/counter.save","r+") as file:
        data = json.load(file)
        data = list(data)
        data[0] += 1
        file.seek(0)
        json.dump(data,file,indent=1)
        file.truncate()