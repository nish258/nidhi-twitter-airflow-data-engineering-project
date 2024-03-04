# nidhi-twitter-airflow-data-engineering-project
This repo consists of all the code that pulls data from twitter, schedules script on airflow via EC2 and pushes data to s3 bucket. The code written, specifically pulls `elonmusk` tweets, creates a dataframe and finally pushes the csv to s3 bucket via airflow scheduling.
My goal for this project was to learn and try airflow, understand how dags work, utilize AWS services.

### Steps Involved

* Create a twitter developer account
* Extract the api keys or bearer token based on which twitter api are you using
* Write a python script to extract required data from tweepy api
* Write a python dag script to run the file on airflow 
* Create AWS EC2 intance 
* Connect to AWS EC2 instance via SSH from local terminal 
* Install required python and twitter packages on the instance
* Install apache airflow 
* Run Apache airflow on port 8080
* Create s3 bucket to push the final file that was created
* Move all local files on EC2 instance using `scp` command 
* Run the dag that was created on airflow and fix if there are any errors. 
* Final result: You should be able to see the file with all the required data on s3 bucket

### Architecture Diagram 
![Data Architecture](Twitter-Airflow-ETL-Data-Architecture.png)

### Challenges
Similar to others, I encountered several challenges throughout the project. Below, I've outlined these challenges to provide foresight and preparation for future endeavors.

* <u>Twitter API</u> - Twitter's API has undergone changes and is no longer entirely free. To access its full range of features, upgrading your developer account may be necessary. With this upgrade, OAuth authentication has also evolved, potentially requiring OAuth 2.0 authorization based on your specific use case.

* <u>EC2 Instance Free Tier</u> - I attempted to utilize the free tier to host Apache Airflow on an Amazon EC2 instance. However, I encountered difficulties launching Airflow on the free tier due to limited resources. Upon investigation, I discovered that deploying Airflow on an EC2 instance, especially within the confines of the free tier, can be challenging due to resource constraints. Consequently, I opted to upgrade to a paid instance type, which facilitated a smooth deployment process.

* <u>Security Block Accessing Airflow</u> - By default, Airflow operates over HTTP rather than HTTPS. Consequently, depending on your network configuration, access to the Airflow URL may be restricted for security reasons. I encountered such restrictions, prompting me to explore options for enabling HTTPS with Airflow, such as obtaining an SSL certificate from AWS Certificate Manager. However, since my project was a one-time endeavor, I opted to resolve the issue by connecting to a different network, thereby circumventing the security block and gaining access to the Airflow URL.
