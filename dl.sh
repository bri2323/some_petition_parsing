#!/bin/bash

#python -c "from BeautifulSoup import BeautifulSoup; from urllib2 import urlopen; print BeautifulSoup(urlopen('http://www.ipetitions.com/petition/support-authors/signatures/').read()).find('p', 'pagination')('a')[-3].text"

to=$(python -c "from BeautifulSoup import BeautifulSoup; from urllib2 import urlopen; print BeautifulSoup(urlopen('http://www.ipetitions.com/petition/support-authors/signatures/').read()).find('p', 'pagination')('a')[-3].text,")

for i in $(seq 292 $to)
do
    wget http://www.ipetitions.com/petition/support-authors/signatures/page/$i -O dumps/$i
done

#for i in $(seq 99 $to)
#do
    #python -c "import xmlrpclib
#s = xmlrpclib.ServerProxy('http://localhost:6800/rpc')
#s.aria2.addUri(['http://www.ipetitions.com/petition/support-authors/signatures/page/$i'],{'dir':'dumps'})"
#done
