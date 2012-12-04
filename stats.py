import json

a = json.load(open("all_signatures.json"))

print "Total:", len(a)
print "Anonymous:", len(filter(lambda x: x['name'] == 'Anonymous', a))
print "Duplications:", len(filter(lambda x: x['name'] != 'Anonymous', a)) - len(set(map(lambda x: x['name'], filter(lambda x: x['name'] != 'Anonymous', a))))
