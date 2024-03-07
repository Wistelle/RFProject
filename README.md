# 0. Progress

|Item|Progress(%)|Status|
|-|-|-|
|Splunk Setup|100|Complete|
|RF App Setup|100|Complete|
|Pulling Data from API|80|In-Progress|
|Cleaning Data for Splunk Ingestion|10|Planning|
|Field Extraction for Ingested Data|10|Planning|
|Correlations|10|Planning|
|Dashboard Modifications|0|Waiting|
|Risk review|0|Waiting|

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

## 1.4 (DRAFT) Data Cleaning

All 4 of the APIs return data a little differently than each other.
All of them need to be cleaned and the fields extracted in order to be fed into Splunk.  

### IP
For each line in the reply, extract the time, service policy, src IP and dst IP. This should give us some easy correlations to C2 connections.
### Hash
The output is very similar to CSV already; Check if splunk has a way to get headers from fields and delimit on colon.
### Domain
For each line, extract: Time, IP, protocol, HTTP Method, Domain and Application
### Vulnerabilities
For each line extract: Time, Name, CVSS Vector, Hostname, Description, First-Seen, CVE Details

## 1.5 Data Ingestion

To ingest data, navigate to the `RF App`, then `Settings > Add Data`  
[Alternatively click here to go directly to the add data page.](http://127.0.0.1:8000/en-GB/manager/TA-recordedfuture/adddata)

I suggest manually uploading and cleaning the files until such a time when data is verified to be properly ingested with the fields extracted properly.

If ever you need a fresh clean slate to start over, please refer to 
[Managing Indexers and Clusters of Indexers](https://docs.splunk.com/Documentation/Splunk/7.0.1/Indexer/RemovedatafromSplunk#How_to_use_the_clean_command)

Once ready, Navigate to `Data Input` and set up a `Monitor`. Follow the instructions to designate a folder such that it updates near real-time without you having to constantly reupload.

# 2. (Draft) RFProject Usage

> Document the use case of the dashboard for the day to day user here.

# 3. RFProject Customization

## 3.0 How Splunk Charges

Splunk charges the users by how much data is ingested into their system. The more data you ingest, the more you are charged.

To make things more efficient for Searching, as well as cost reduction to the client, it is imperative we trim the data down to only information that we need.

The art of this is balancing what we prune; Too much, and we lose contextual clues. Too little, and we're ingesting data we have no use for resulting in higher costs. A field or two wouldn't add much in the long run, but ingesting data you're never going to use would slow Searches.

## 3.1 (Draft) Data Pruning

Before we start pruning, take some time to figure out what is important, not just to you as a developer, but as a consumer. Threat Intelligence would have wants and needs different to an Intrusion Analyst.

For the sake of this assignment, we will don the hat of an Intel Analyst.

Specifically, the kind that works for a company that has contracted RF's services.  
They will want to know at a glance if the intel given is pertinent to their company.

> Which parts need to be pruned, from IP/Hash/Domains/Vulns

## 3.2 (DRAFT) Correlations

Correlations are similar to alerts in that they are generated when the events are matched with intellgence (correlated).  

From the documentation of the Recorded Future App:
> "Correlations detect malicious events with a low rate of false positives. Dedicated correlation views help shorten the time spent on event triage."

### Basic Correlations

IPs, Hashes, Domains and Vulnerabilities can be easily correlated 1-1 to the existing RF tables.
