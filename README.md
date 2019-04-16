# Project Title 

Sparkify user & song data ingestion using star schema. 

### Introduction : 

This etl project for a Music app Sparkify that wants to analyze the data they've been collecting on songs and user activity on a music streaming app. The analytics team is particularly interested in understanding what song users are listening to. Data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

Fact and dimension tables are in star schema for a particular analytic focus.

Project contains ETL pipeline that transfers data from files in two local directories into these tables is in Postgres using Python and SQL. 

### Getting started: 

Download the project repositories and execute the following python scripts: 

'''
C:\Users\aryaveer>python create_tables.py
C:\Users\aryaveer>python etl.py
'''

### Test the data is successfully loaded using test.ipynb or type the following queries in a local python notebook 

%load_ext sql

%sql postgresql://student:student@127.0.0.1/sparkifydb

%sql SELECT * FROM songplays LIMIT 5;

%sql SELECT * FROM users LIMIT 5;

%sql SELECT * FROM songs LIMIT 5;

%sql SELECT * FROM time LIMIT 5;

