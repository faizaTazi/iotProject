#go through the appPermissions
#for each file in appPermissions go through the list of permissions
import json

from pathlib import Path
appsFile = open("apps.txt", 'r')
apps = appsFile.readlines()

out = open("permissionCal1.csv", 'a')
out.write('app,location,contact,content,calendar,network,device Id,phone state,\n')
for app in apps:
    app = app.rstrip()
    data = Path("./appPermissions/"+app+".permission").read_text()

    data = data.replace("permission:","'permission':")
    data = data.replace("type:","'type':")
    location = 0
    contact = 0
    content = 0
    calendar = 0
    dId = 0
    phone = 0
    network = 0
    permissions = eval(data)
    for p in permissions:
        if p['type'] == 'Location' \
                or (p['type'] == 'Other'
                    and ('location' in p['permission']
                         or 'Location' in p['permission']
                         or 'GPS' in p['permission'])):
            location = location + 1

        elif p['type'] == 'Photos/Media/Files':
            content = content + 1
        elif p['type'] == 'Storage':
            content = content + 1
        elif p['type'] == 'Contacts':
            contact = contact + 1

        elif p['type'] == 'Calendar':
            calendar = calendar + 1
        elif p['type'] == 'Device ID & call information':
            dId = dId + 1
        elif p['type'] == 'Phone' \
                or (p['type'] == 'Other' and 'call' in p['permission']):
            phone = phone + 1
            per = p['permission']
        elif (p['type'] == 'Other'
              and ('network' in p['permission']
                   or 'Network' in p['permission']
                   or 'Wi-Fi' in p['permission']))\
                or p['type'] == 'Wi-Fi connection information':
            network = network + 1

    if phone == 1:
        l = per
    else:
        l = phone
    out.write("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7},\n".format(app,location,contact,content,calendar,network,dId,l))

    location = 0
    contact = 0
    content = 0
    calendar = 0
    dId = 0
    phone = 0
    network = 0

out.close()
appsFile.close()

