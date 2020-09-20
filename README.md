# Covid-19_status


The COVID-19-status Project collects information from all the countries of the world and all the states of india, to provide the most comprehensive testing data we can collect for the novel coronavirus, SARS-CoV-2.

This repository is for the project's **website**: https://covid-tracker-status.web.app/.

## Development

The website is built on popular Python webbased framework [Flask](https://palletsprojects.com/p/flask/). If you are not familiar with Flask, we suggest checking out their [excellent documentation](https://flask.palletsprojects.com/en/1.1.x/).

### Install and Run

First, you'll need the Python 3.7 or a higher version to run this project:

You can check your python version with:

```shell
python --version
```
Additionally you will need a few dependencies in python,all the dependencies has been listed in requirements.txt
You can simply install all dependencies at a go by running:

```shell
pip install -r requirements.txt
```

To run the website locally,In the root directory use:
(also in app.py erase the '#' from app.run(debug=True) and comment out the other app.run to run it locally)
```shell
python app.py
```
The site is now running at `http://127.0.0.1:5000`. Any changes you make to code is live-updated as soon as you save the changes in app.py. 



Alternatively you can also deploy it in heroku or firebase hosting(with google cloud run). the respective requirements.txt and dockerfile required are already provided.
For help on heroku go to the official documentations page-https://devcenter.heroku.com/articles/getting-started-with-python
For firebase hosting u can look at this for reference- https://medium.com/firebase-developers/hosting-flask-servers-on-firebase-from-scratch-c97cfb204579

### Organization

Components of the project are organized as follows:

- `/home` - This is main all the data is Visualised and shown of both world and india separately.
- `/analyis` - Here all the data is annalyzed and future trends are predicted with graphical analysis and corresponding line charts are shown
- `/News` - Here the latest covid-19 news from whole world is listed
- `/guidelines` - This one lists the guidelines to follow durring the pandemic
- `/api` - Here all our data is listed  and u can access with the listed api calls shown there. 

## Screenshots
<p float="left">
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/1.png" width=30% height=30%>
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/2.png" width=30% height=30%>
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/3.png" width=30% height=30%>
</p>
<p float="left">
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/4.png" width=30% height=33%>
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/5.png" width=30% height=33%>
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/6.png" width=30% height=33%>
</p>
<p float="left">
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/7.png" width=33% height=33%>
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/8.png" width=33% height=33%>
<img src="https://github.com/Gourav2000/Covid-19_status/blob/master/screenshots/9.png" width=33% height=33%>
</p>
<h2><b>How to contribute</b></h2>

No matter how you choose to help, we would love to have you as part of the project. 
You can just fork the repository add your ideas and send us a pull request and we will look through it.. ;-)
