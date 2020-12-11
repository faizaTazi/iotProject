import json

appsFile = open("apps.txt", 'r')
apps = appsFile.readlines()

for app in apps:
    app = app.rstrip()
    with open("./appReviews/" + app + ".json", "r") as f:
        with open("./SecurityReviews/" + app + ".txt", "w") as fw:
            data = json.load(f)
            for i in range(len(data)):
                if ('secur' in data[i]['content'] and 'security cam' not in data[i]['content']) \
                        or 'priva' in data[i]['content']:
                    json.dump(data[i], fw, indent=4)
