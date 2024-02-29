# 1. RFProject Installation & Set Up

## 1.0 Requirements

- Python3
  - Pandas

## 1.1 Install Splunk

To even use the Recorded Future App from Splunk Base, we need a copy of [Splunk Enterprise.](https://www.splunk.com/en_us/download.html)  
I highly recommend to get a [Developer License](https://dev.splunk.com/enterprise/dev_license/) as well. This should help ingesting data.

Once downloaded, install it and should prompt you to open up the Splunk Web interface.  
Alternatively navigate to http://127.0.0.1:8000/

## 1.2 Install Recorded Future App.

Download the [Recorded Future App from Splunk Base.](https://splunkbase.splunk.com/app/4920)  
Click on Manage your apps, and install the app you downloaded from Splunkbase.  
[Alternatively click here to go directly to the local app upload page.](http://127.0.0.1:8000/en-GB/manager/appinstall/_upload?breadcrumbs=Settings%7C%2Fmanager%2Flauncher%2F%09Apps%7C%2Fmanager%2Flauncher%2Fapps%2Flocal)

Install the RF App. It'll ask you to restart.

You will then be asked to set up the App. To do this, go back to Manage Apps, then "Set Up" on the row with the RF app.
Enter in your token from the email and the Recorded Future App is ready to go!

## 1.3 Get Data

While the App is working, it's a blank slate. Now's a good time to see what we're working with. Head over to
https://api.recordedfuture.com/v2/
and key in the token you have in the top right, and start exploring the APIs.

Play around with what they have to offer and how the data, the arguments, as well as the format in which they are returned. For now we should just take the data wholesale and pipe it into Splunk to see what we get.

For the assignment, we'll have to write a script to use the APIs to pull the demo data.

For an example of this, please check `pull_raw_events.py`.

```
Do note that I have not uploaded it to GitHub as I have yet to implement the secret service and uploading the file will result in the leak of the API token.
```

## 1.4 (DRAFT) Data Cleaning

All 4 of the APIs return data a little differently than each other.



## 1.5 Data Ingestion

To ingest data, navigate to the `RF App`, then `Settings > Add Data`  
[Alternatively click here to go directly to the add data page.](http://127.0.0.1:8000/en-GB/manager/TA-recordedfuture/adddata)

I suggest manually uploading and cleaning the files until such a time when data is verified to be properly ingested with the fields extracted properly.

If ever you need a fresh clean slate to start over, please refer to 
[Managing Indexers and Clusters of Indexers](https://docs.splunk.com/Documentation/Splunk/7.0.1/Indexer/RemovedatafromSplunk#How_to_use_the_clean_command)

Once ready, Navigate to `Data Input` and set up a `Monitor`. Follow the instructions to designate a folder such that it updates near real-time without you having to constantly reupload.

# 2. RFProject Usage
??

# 3. RFProject Customization

## 3.0 How Splunk Charges

Splunk charges the users by how much data is ingested into their system. The more data you ingest, the more you are charged.

To make things more efficient for Searching, as well as cost reduction to the client, it is imperative we trim the data down to only information that we need.

The art of this is balancing what we prune; Too much, and we lose contextual clues. Too little, and we're ingesting data we have no use for resulting in higher costs. A field or two wouldn't add much in the long run, but ingesting data you're never going to use would slow Searches.

## 3.1 Data Pruning

Before we start pruning, take some time to figure out what is important, not just to you as a developer, but as a consumer. Threat Intelligence would have wants and needs different to an Intrusion Analyst.

For the sake of this assignment, we will don the hat of an Intel Analyst.

Specifically, the kind that works for a company that has contracted RF's services.  
They will want to know at a glance if the intel given is pertinent to their company.

## 3.2 (DRAFT) Correlations

Correlations are similar to alerts in that they are generated when the events are matched with intellgence (correlated).  

The key difference with alerts is the urgency; Alerts would trigger known threats that have been detected via splunk to an event.

Correlations are *potential* threats that an analyst has to look through to determine if the threats are valid.
To that end it is possible for more indormation to be correlated to give more context regarding the threat to allow for a more informed decision

### IP

Correlation for IP is easy: Simply match them.
A match would mean an IP is correlated

# TO-DO

## ?. Secret Service

Implement Secret Service such that the .py files can be uploaded without exposing the API token.

## ?. Read the  Docs
~~Primarily will be used for Read the Docs.~~

~~[http://rfproject.readthedocs.io/](http://rfproject.readthedocs.io/)~~

Maybe no RTD until the project is done.