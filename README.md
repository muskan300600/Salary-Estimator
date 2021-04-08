# Data Science Salary Estimator:
1. Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
2. Scraped over 1000 job descriptions from glassdoor using python and selenium
2. Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
2. Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
2. Built a client facing API using flask
# Code and Resources Used
- Python Version: 3.7
- Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
- For Web Framework Requirements:py -m pip install -r requirements.txt
- Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
- Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
