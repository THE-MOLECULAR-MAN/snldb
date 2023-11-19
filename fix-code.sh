#!/bin/bash
# g

find . -type f -iname '*.py' -exec autopep8 --in-place {} \;

find . -type f -iname '*.json' -o -iname '*.csv' -delete
rm -f data/snl.json
mkdir ./db/

python3 -m pip install -r requirements.txt


./crawl_single_episode.sh 19751011


find . -type f -iname '*.json' -o -iname '*.csv'


scrapy runspider ./snlscrape/spiders/snl.py -o ./data/snl.json

ps aux | grep 'snl\|scapy'