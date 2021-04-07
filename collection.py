import Glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/mini9/Desktop/Data Analysis/chromedriver"
df =gs.get_jobs("data scientist",1000, False,path,15)
df.to_csv('glassdoor_jobs.csv', index = False)