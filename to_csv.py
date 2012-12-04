import csv
import json
from datetime import datetime

with open('all_signatures-%s.csv' % datetime.now().strftime('%F-%H-%M'), 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
    spamwriter.writerow(['num', 'name', 'date', 'comment'])
    for i in json.load(open("all_signatures.json")):
        spamwriter.writerow([i['num'], i['name'].encode("Utf-8"), i['date'], i['comment'].encode("Utf-8")])
