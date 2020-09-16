
import requests
import itertools
import flask
from flask import Flask, render_template
from flask import request, jsonify
from GoogleNews import GoogleNews
from datetime import datetime,timedelta
import news
import analysis
from threading import Thread
import numpy

news_dic=dict()
news_dic['news_list']=list()
news_dic['is_completed']=False

def news_get():
    news_dic['news_list']=news.get_news()
    news_dic['is_completed']=True
th=Thread(target=news_get)
th.start()

r2=requests.get('https://api.covid19india.org/data.json')
rit=r2.json()
India_list=rit['statewise']
r=requests.get('https://corona.lmao.ninja/v2/countries')
World_list=r.json()
w_total=requests.get('https://disease.sh/v3/covid-19/all?yesterday=true&twoDaysAgo=true&allowNull=true').json()
for i in World_list:
    if i['country']=='India':
        i_total=i
        break



app = flask.Flask(__name__, template_folder="public_html", static_folder="public_html/static")
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home(India_list= India_list,World_list= World_list,i_total=i_total,w_total=w_total):
    return render_template("India_Covid.html", ilist=India_list,wlist=World_list,i_total=i_total,w_total=w_total)

@app.route('/news', methods=['GET'])
def news_sec():
    th.join()
    return render_template("news.html", newsList= news_dic['news_list'])
    # jsonify(news.get_news())

@app.route('/api',methods=['GET'])
def api_sec():
    return render_template("api_Covid.html")

@app.route('/guidelines',methods=['GET'])
def guidelines_sec():
    return render_template("guidelines.html")

@app.route('/about', methods=['GET'])
def about_sec():
    return render_template("About_covid.html")

@app.route('/analysis', methods=['GET'])
def analysis_sec(dataw=analysis.get_world_daily_data(),datai=analysis.get_india_daily_update(),datawd=analysis.get_world_derrivative(),dataid=analysis.get_india_derrivative()):
    return render_template("Analysis.html",dataw=dataw,datai=datai,datawd=datawd,dataid=dataid,zip=zip)

@app.route('/api/world', methods=['GET'])
def api_world(World_list=World_list):
    return jsonify(World_list)

@app.route('/api/india', methods=['GET'])
def api_india(India_list=India_list):
    return jsonify(India_list)

@app.route('/api/news', methods=['GET'])
def api_news():
    th.join()
    return jsonify(news_dic['news_list'])

if __name__ == "__main__":
    app.run(debug=True)
