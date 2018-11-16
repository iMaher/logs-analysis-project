# Log Analysis Project
Log Analysis Project is the first project in Udacity Full Stack Nanodegree
witch analyze the log file that provide it by Udacity into three questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?   

---

# System Requirement and Configuration
You need to install the following applications
* Install [Vagrant](https://www.vagrantup.com/)
* Install [VirtualBox](https://www.virtualbox.org/)
* Install [Postgresql](https://www.postgresql.org/download/)
* Clone [FSND VM](https://github.com/udacity/fullstack-nanodegree-vm)
* Download the database file [newsdata](https://github.com/iMaher/logs-analysis-project/blob/master/newsdata.zip)
* Add this project inside vagrant folder
* Open Terminal
* Run vagrant 'vagrant up'
* Enter remote to vagrant as ssh 'vagrant ssh'
* Load the data using the following command: 'psql -d news -f newsdata.sql;'
* Go to the python file directory
* Run the Python file 'python filename.py'

# ِExpected Output:

' What are the most popular three articles of all time?  
"Candidate is jerk, alleges rival" _ 338647 views  
"Bears love berries, alleges bear" _ 253801 views  
"Bad things gone, say good people" _ 170098 views  
Who are the most popular article authors of all time?  
Ursula La Multa _ 507594 views  
Rudolf von Treppenwitz _ 423457 views  
Anonymous Contributor _ 170098 views  
Markoff Chaney _ 84557 views  
On which days did more than 1% of requests lead to errors?  
July 17, 2016 _ 2.3 % errors  '
