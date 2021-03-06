Installation
------------
Install following packages with pip:
scrapy
scrapyd
scrapyd-deploy
boto
twisted


Scrapyd Config
--------------
Run scrapyd at input file directory.

Create .scrapyd.conf at home directory ~ with following contents:

[scrapyd]
eggs_dir    = eggs
logs_dir    = logs
items_dir   = 
jobs_to_keep = 5
dbs_dir     = dbs
max_proc    = 0
max_proc_per_cpu = 4
finished_to_keep = 100
poll_interval = 5
http_port   = 6800
debug       = off
runner      = scrapyd.runner
application = scrapyd.app.application
launcher    = scrapyd.launcher.Launcher

[services]
schedule.json     = scrapyd.webservice.Schedule
cancel.json       = scrapyd.webservice.Cancel
addversion.json   = scrapyd.webservice.AddVersion
listprojects.json = scrapyd.webservice.ListProjects
listversions.json = scrapyd.webservice.ListVersions
listspiders.json  = scrapyd.webservice.ListSpiders
delproject.json   = scrapyd.webservice.DeleteProject
delversion.json   = scrapyd.webservice.DeleteVersion
listjobs.json     = scrapyd.webservice.ListJobs


Deploy locally
--------------
scrapy crawl spider1 -a urls_file=urls2.csv


Deploying to Scrapyd
--------------------
To deploy project egg file to scrapyd server:
scrapyd-deploy
scrapyd-deploy default -p crawler

Scrapyd API urls:
curl http://localhost:6800/schedule.json -d project=crawler -d spider=spider1
curl http://localhost:6800/listversions.json -d project=crawler
curl http://localhost:6800/delversion.json -d project=crawler -d version=123
curl http://localhost:6800/delproject.json -d project=crawler
curl http://localhost:6800/cancel.json -d project=crawler -d job=6487ec79947edab326d6db28a2d86511e8247444

EC2:
curl http://ec2-52-3-193-218.compute-1.amazonaws.com:6800/schedule.json -d project=crawler -d spider=spider1
curl http://ec2-52-3-193-218.compute-1.amazonaws.com:6800/listversions.json -d project=crawler
curl http://ec2-52-3-193-218.compute-1.amazonaws.com:6800/delversion.json -d project=crawler -d version=123
curl http://ec2-52-3-193-218.compute-1.amazonaws.com:6800/delproject.json -d project=crawler
curl http://ec2-52-7-199-212.compute-1.amazonaws.com:6800/cancel.json -d project=crawler -d job=5d14cb4a2b6111e5896e12e5826186bf

Pass arguments to spider:
scrapy crawl myspider -a category=electronics
curl http://localhost:6800/schedule.json -d project=crawler -d spider=spider1 -d spider_id=id1 -d urls_file=urls.txt
curl http://ec2-52-3-193-218.compute-1.amazonaws.com:6800/schedule.json -d project=crawler -d spider=spider1 -d spider_id=id1 -d urls_file=urls.txt
curl http://ec2-52-3-193-218.compute-1.amazonaws.com:6800/schedule.json -d project=crawler -d spider=spider1 -d spider_id=id1 -d urls_file=output_1_storyitems.csv
curl http://ec2-52-7-199-212.compute-1.amazonaws.com:6800/schedule.json -d project=crawler -d spider=spider1 -d spider_id=id1 -d urls_file=output_6_storyitems.csv

List all projects:
scrapyd-deploy -l

Status 