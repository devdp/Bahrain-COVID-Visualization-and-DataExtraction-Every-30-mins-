# Bahrain-COVID-Visualization-and-DataExtraction-Every-30-mins-

### install packages
```python
pip install -r packages.txt
```
### api.py
this file contains all the things like data extraction data tranformation and data updation after every 30 min.
```python
from flask import Flask, request, render_template, url_for
import pandas as pd
import plotly.graph_objects as go
import json
import plotly
from apscheduler.schedulers.background import BackgroundScheduler
import os
import pull_data
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dataextraction import ext
from datatranformation import trans
```
- flask is for creating api and serving html pages
- pandas is for reading, writing and some basic transformation of data
- plotly is for making interactive charts
- json is for converting python plotly to javaScript plotly
- apscheduler is for running a particular function after defined interval of time
- os is for removing previous extracted data
- pull_data package is created by me for gathering data
- re is regex and is for extracting relevant information from data
- selenium is for automating browser for raw data gathering
- Keys is for controling keyboard key like ENTER, UP, DOWN, etc.
- By is for locating element in browser
- time is for making code wait
- dataextraction is created by me where I am processing text and making datasets
- datatransformation is created by me for adding some more things to data so that it can be used further for visualization
### dashboard
it contains dashboards created in tableau and these dashboards are embed in html pages.
### to run this code follow these steps
- open api.py
```python
you can change time for data refresh as per your need
- change username and password as for your need
```
- open pull_data.py
```python
- change dicrectory path in prefs as per your working directory
```
- run api.py
- hit http://localhost:5000/ in your browser.
