# REDDIT FLAIR
A simple application which allows users to predict the flair of a reddit India posts given its link
Website link: http://webredditflair.herokuapp.com/
## Directory Structure

### data
* data.csv - The flaired posts collected from reddit. The posts are from date 16 July 2018 to 16 July 2019.

### scripts
* data_extraction.py - To scrape the Reddit website and add the data extracted to 'data.csv'
* model.py - It implements Stochastic Gradient Descent algortihm on 'data.csv' to make 'model.pkl' file. The accuracy of the model is 56.023%

### website
* static
  * css 
    * style.css - Cascading Style Sheet to make 'layout.html' look better
  * img
    * background.png - Background of website
    * loading1.gif - Loading gif used in website
  * cpp.png - A line chart of Number of Comments per post for each flair
  * dan.html - To display the data analysis of the reddit posts
  * nocs.png - A bar graph of Number of Comments for each flair
  * nops.png - A bar graph of Number of Posts for each flair
  * npdd.png - A line chart of the numbers of posts across the day
  * scores.png - A bar graph of Scores of each flair
  * spp.png - A line chart of Score per post for each flair
* templates
  * layout.html - The layout of the website
* .gitignore - A part of the website to ignore 'env'
* Procfile - Needed for hosting website on Heroku to specify the commands that are executed by the website on startup.    
* model.pkl - The machine learning model trained by model.py
* reddit_cred.py - Contains ressit credentials
* requirements.txt - Needed for hosting webstie on Heroku to specify the modules needed for the website to run
* views.py - To make the Flask based website






