import json
appsFile = open("apps.txt", 'r')
apps = appsFile.readlines()
numReviews = 0
for app in apps:
    app = app.rstrip()
    with open("./appReviews/" + app + ".json", "r") as f:
        data = json.load(f)
        numReviews += len(data)
print(numReviews)