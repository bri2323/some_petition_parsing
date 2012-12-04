#!/bin/bash

for i in $(seq 246); do wget http://www.ipetitions.com/petition/support-authors/signatures/page/$i -O dumps/$i -c; done
