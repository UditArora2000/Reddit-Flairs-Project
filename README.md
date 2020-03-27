# REDDIT FLAIR

### WEBSITE NAME - http://webredditflair.herokuapp.com/

## File Description

* env - A virtual environment created to upload the website on Heroku

### static

* css
* style.css - Cascading Style Sheet to make 'layout.html' look better
* dan.html - To display the data analysis of the reddit posts
* cpp.png - A line chart of Number of Comments per post for each flair
* nocs.png - A bar graph of Number of Comments for each flair
* nops.png - A bar graph of Number of Posts for each flair
* npdd.png - A line chart of the numbers of posts across the day
* scores.png - A bar graph of Scores of each flair
* spp.png - A line chart of Score per post for each flair
* templates
* layout.html - The layout of the website

### Misc

* data.csv - The flaired posts collected from reddit. The posts are from date 16 July 2018 to 16 July 2019.

* model.pkl - The machine learning model trained by 'model.py'

* .gitignore - A part of the website to ignore 'env'

* Procfile - Needed for hosting website on Heroku to specify the commands that are executed by the website on startup.

* requirements.txt - Needed for hosting webstie on Heroku to specify the modules needed for the website to run

* model.py - It implements Stochastic Gradient Descent algortihm on 'data.csv' to make 'model.pkl' file. The accuracy of the model is 56.023%

* data_extraction.py - To scrape the Reddit website and add the data extracted to 'data.csv'

* data_analysis.py - To do data analysis so as to make the png files mentioned above

* views.py - To make the Flask based website






