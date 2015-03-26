# eggscrape
get egg s3 links


#### up and running
in the repo, edit login.py and add your egg user and password.
then install dependencies, `pip install -r requirements.txt`, and then simply invoke eggscrape.
```
# write all s3 links for react to a file. you could pipe the output to wget later.
./eggscrape react > react_s3_links.txt
```
