import os
import json
import sys
from BeautifulSoup import BeautifulSoup

all_json = []

total_len = len(sorted(os.listdir("dumps"), key=lambda x: int(x)))
for number, fileu in enumerate(sorted(os.listdir("dumps"), key=lambda x: int(x)), 1):
    soup = BeautifulSoup(open("dumps/" + fileu).read())
    for artist in soup.find('ol', id='signatures_list')('li'):
        artist_json = {}
        if artist.find('div', 'sig_info').em:
            artist_json["name"] = artist.find('div', 'sig_info').em.text
        else:
            artist_json["name"] = filter(lambda x: isinstance(x, basestring) and x.strip(), artist.find('div', 'sig_info'))[0].strip().split("\n")[0]
        artist_json["date"] = artist.find('div', 'sig_info').span.text
        artist_json["num"] = int(artist.span.a.text)
        artist_json["comment"] = ''.join(artist.find('div', 'sig_comment').contents[2:]).strip()

        all_json.append(artist_json)

    sys.stdout.write("%s/%s\r" % (number, total_len))
    sys.stdout.flush()

open("all_signatures.json", "w").write(json.dumps(all_json))
