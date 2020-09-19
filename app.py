
import requests
import itertools
import os
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
th_news=Thread(target=news_get)
th_news.start()

detail_dic= dict()
detail_dic['India_list']=list()
detail_dic['World_list']=list()
i_total=dict()
w_total=dict()

def getDetails():
    r2=requests.get('https://api.covid19india.org/data.json')
    rit=r2.json()
    detail_dic['India_list']=rit['statewise']
    r=requests.get('https://corona.lmao.ninja/v2/countries')
    detail_dic['World_list']=r.json()
    w_total.update(requests.get('https://disease.sh/v3/covid-19/all?yesterday=true&twoDaysAgo=true&allowNull=true').json())
    for i in detail_dic['World_list']:
        if i['country']=='India':
            i_total.update(i)
            break
th_details=Thread(target=getDetails)
th_details.start()

dataw=dict()
datai=dict()
datawd=dict()
dataid=dict()
def getAnalysis():
    dataw.update(analysis.get_world_daily_data())
    datai.update(analysis.get_india_daily_update())
    datawd.update(analysis.get_world_derrivative())
    dataid.update(analysis.get_india_derrivative())
th_analysis= Thread(target=getAnalysis)
th_analysis.start()


app = flask.Flask(__name__, template_folder="public_html")
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    th_details.join()
    return render_template("India_Covid.html", ilist=detail_dic['India_list'],wlist=detail_dic['World_list'],i_total=i_total,w_total=w_total)

@app.route('/news', methods=['GET'])
def news_sec():
    th_news.join()
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
    return render_template("About_Covid.html")

@app.route('/analysis', methods=['GET'])
def analysis_sec():
    th_analysis.join()
    return render_template("Analysis.html",dataw=dataw,datai=datai,datawd=datawd,dataid=dataid,zip=zip)

@app.route('/api/world', methods=['GET'])
def api_world():
    th_details.join()
    return jsonify(detail_dic['World_list'])

@app.route('/api/india', methods=['GET'])
def api_india():
    th_details.join()
    return jsonify(detail_dic['India_list'])

@app.route('/api/news', methods=['GET'])
def api_news():
    th_news.join()
    return jsonify(news_dic['news_list'])

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
