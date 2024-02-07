![Canvas Notifier](public/banner.png)

# About  

- Program that checks Github to make sure you get that sweet sweet green commit chart.  

- Sends a text message if you haven't pushed to Github in the past day  

## Sample Text Notifications (can be edited):

**You coded**  
![good text](public/good.png)  

**You didn't code :/**  
![bad text](public/bad.png)

# Why  

![Meme](public/about.png)  

- establish your superiority over other programmers
- place all of your self worth onto a contribution graph
- more green in the world  
  
# Setup

## Gmail Texting Setup

**Follow [this guide](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637700239874464736-1954441174&rd=1) to get your credentials for texting via Gmail servers.**

#### ENV Method

add this .env file to ``src/util``:

```text
EMAIL=INSERT_YOUR_EMAIL 
PASSWORD=INSERT_YOUR_PASSWORD
PHONE_NUMBER=PHONE_NUMBER_TO_SEND_ALERTS_TO
```  

#### Edit Code Variables Method

edit these variables found in ``src/util/sms.py``:

```python
EMAIL = 'PUT YOUR EMAIL HERE'  # email to send via
PASSWORD = 'PUT YOUR PASSWORD HERE'  # special auth password for email above
PHONE_NUMBER = 'PUT YOUR PHONE NUMBER HERE'  # phone number to send texts to
```

## Hosting

I used a [cron job](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) on an [ec2 instance](https://www.techtarget.com/searchaws/definition/Amazon-EC2-instances) that just checks Github every day at 10pm.  

**[Get 1 year free of AWS](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)** (not sponsored)  

### NOTE: You could also run this locally

#### The following commands are only UNIX based machines (sorry windows users)  

**1.**  ``cd`` into /src:

```bash
cd did-you-code-today/src/
```

**2.** install needed packages:

```bash
pip install -r requirements.txt
```

**3.** adjust permissions of python file with ``chmod``:

```bash
chmod +x github_scraper.py
```

**4.** edit crontab:

```bash
crontab -e
```

**5.** put this in your crontab thing (with respective paths):

```text
0 22 * * * /usr/bin/python3 /home/ec2-user/did-you-code-today/src/
```

**6.** enjoy!

## What I learned  

- webscraping with BeautifulSoup (python library)
- don't waste your time with the Github API (haha)  
- green graph == good  

# FAQ

**Q: Why AWS?**  
A: Beacuse it was free (thanks bezos)

**Q: Is this practical?**  
A: Yes  

**Q: Does this use AI?**  
A: unfortunately, no.
