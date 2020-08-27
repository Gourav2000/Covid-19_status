
import requests
import itertools
import flask
from flask import Flask, render_template
from flask import request, jsonify
from GoogleNews import GoogleNews
from datetime import datetime,timedelta
import news
import analysis
import numpy
#import matplotlib.pyplot as plt

'''state_list=[
'Andaman and Nicobar Islands',
'Andhra Pradesh (AP)',
'Arunachal Pradesh (AR)',
'Assam (AS)',
'Bihar (BR)',
'Chandigarh',
'Chhattisgarh (CG)',
'Daman and Diu',
'Delhi',
'Dadra and Nagar Haveli',
'Goa (GA)',
'Gujarat (GJ)',
'Himachal Pradesh (HP)',
'Haryana (HR)',
'Jharkhand (JH)',
'Jammu and Kashmir (JK)',
'Karnataka (KA)',
'Kerala (KL)',
'Lakshadweep',
'Maharashtra (MH)',
'Meghalaya (ML)',
'Manipur (MN)',
'Madhya Pradesh (MP)',
'Mizoram (MZ)',
'Nagaland (NL)',
'Odisha(OR)',
'Punjab (PB)',
'Puducherry',
'Rajasthan (RJ)',
'Sikkim (SK)',
'Telangana (TG)',
'Tamil Nadu (TN)',
'Tripura (TR)',
'Uttar Pradesh (UP)',
'Uttarakhand (UK)',
'West Bengal (WB)',
'Total',
]'''
#r=requests.get('https://api.covid19india.org/states_daily.json')
#ri=r.json()
#India_list_json=jsonify(India_list)

#def create_pie_chart():

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
'''labels='active','recovered','dead'
sizes=[int(i_total['cases'])-int(i_total['deaths'])-int(i_total['recovered']),int(i_total['recovered']),int(i_total['deaths'])]
explode = (0.1, 0.1, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels,
shadow=True, startangle=90)
ax1.axis('equal')
plt.savefig('public_html/static/iplot1.png',transparent=True)
#plt.show()'''


app = flask.Flask(__name__, template_folder="public_html", static_folder="public_html/static")
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home(India_list= India_list,World_list= World_list,i_total=i_total,w_total=w_total):
    return render_template("India_Covid.html", ilist=India_list,wlist=World_list,i_total=i_total,w_total=w_total)

@app.route('/news', methods=['GET'])
def news_sec():
    return jsonify(news.get_news())

@app.route('/guidelines',methods=['GET'])
def guidelines_sec():
    return "<h1>Its already 5 months at minimum and u still don't know guideline u dumb F***</h1>"

@app.route('/about', methods=['GET'])
def about_sec():
    return render_template("About_covid.html")
@app.route('/analysis', methods=['GET'])
def analysis_sec(dataw=analysis.get_world_daily_data(),datai=analysis.get_india_daily_update(),datawd=analysis.get_world_derrivative(),dataid=analysis.get_india_derrivative()):
    return render_template("Analysis.html",dataw=dataw,datai=datai,datawd=datawd,dataid=dataid,zip=zip)

if __name__ == "__main__":
    app.run(debug=True)
