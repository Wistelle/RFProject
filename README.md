# 1. RFProject Installation & Set Up

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

## 1.3 Data Ingestion

Before we move into data ingestion, it's a good idea to see what we're working with. Head over to
https://api.recordedfuture.com/v2/

Key in the token you have in the top right, and start exploring the APIs and what they have to offer and how they return data.

For now we should just take the data wholesale and pipe it into Splunk to see what we get.

# 2. RFProject Usage

# 3. RFProject Customization

## 3.1 Data Pruning

Before we start pruning, take some time to figure out what is important, not just to you as a developer, but as a consumer. Threat Intelligence would have wants and needs different to an Intrusion Analyst.

For the sake of this assignment, we will don the hat of an Intel Analyst.

Specifically, the kind that works for a company that has contracted RF's services.  
They will want to know at a glance if the intel given is pertinent to their company.



Correlation. Affected Versions, IOCs, Devices.

# TO-DO

## ?. Read the  Docs
~~Primarily will be used for Read the Docs.~~

~~[http://rfproject.readthedocs.io/](http://rfproject.readthedocs.io/)~~

Maybe no RTD until the project is done.