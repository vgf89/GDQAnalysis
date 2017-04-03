#Donations:
scrapy runspider sgdq2011.py -o data/sgdq2011_donations.json
scrapy runspider agdq2012.py -o data/agdq2012_donations.json

#Run Schedules:
scrapy runspider sgdq2011_runs.py -o data/sgdq2011_schedule.json
scrapy runspider agdq2012_runs.py -o data/agdq2012_schedule.json