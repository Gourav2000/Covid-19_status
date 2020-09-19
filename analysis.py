import requests
import calendar
import numpy

def get_world_daily_data():
    r=requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=all")
    w=r.json()
    cases=list()
    recovered=list()
    deaths=list()
    for i in w['cases']:
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=d
        dic['month_word']=calendar.month_abbr[int(m)]  
        dic['month']=int(m) 
        dic['year']=2000+int(y)
        dic['data']=w['cases'][i]
        cases.append(dic)
    for i in w['recovered']:
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=d
        dic['month_word']=calendar.month_abbr[int(m)] 
        dic['month']=int(m)
        dic['year']=2000+int(y)
        dic['data']=w['recovered'][i]
        recovered.append(dic)
    for i in w['deaths']:
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=int(d)
        dic['month_word']=calendar.month_abbr[int(m)]   
        dic['month']=int(m)
        dic['year']=2000+int(y)
        dic['data']=w['deaths'][i]
        deaths.append(dic)
    world_daily_data=dict()
    world_daily_data['cases']=cases
    world_daily_data['deaths']=deaths
    world_daily_data['recovered']=recovered
    #print(world_daily_data)
    return world_daily_data
def get_india_daily_update():
    r=requests.get("https://disease.sh/v3/covid-19/historical/india?lastdays=all")
    ind=r.json()
    cases=list()
    recovered=list()
    deaths=list()
    for i in ind['timeline']['cases']:
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=d
        dic['month_word']=calendar.month_abbr[int(m)]  
        dic['month']=int(m) 
        dic['year']=2000+int(y)
        dic['data']=ind['timeline']['cases'][i]
        cases.append(dic)
    for i in ind['timeline']['recovered']:
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=d
        dic['month_word']=calendar.month_abbr[int(m)] 
        dic['month']=int(m)
        dic['year']=2000+int(y)
        dic['data']=ind['timeline']['recovered'][i]
        recovered.append(dic)
    for i in ind['timeline']['deaths']:
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=int(d)
        dic['month_word']=calendar.month_abbr[int(m)]   
        dic['month']=int(m)
        dic['year']=2000+int(y)
        dic['data']=ind['timeline']['deaths'][i]
        deaths.append(dic)
    india_daily_data=dict()
    india_daily_data['cases']=cases
    india_daily_data['deaths']=deaths
    india_daily_data['recovered']=recovered
    #print(india_daily_data)
    return india_daily_data
def get_world_derrivative():
    r=requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=all")
    w=r.json()
    cases=list()
    recovered=list()
    deaths=list()
    dates=list()
    for i in w['cases']:
        cases.append(w['cases'][i])
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=int(d)
        dic['month_word']=calendar.month_abbr[int(m)]   
        dic['month']=int(m)
        dic['year']=2000+int(y)
        dates.append(dic)
    for i in w['recovered']:
        recovered.append(w['recovered'][i])
    for i in w['deaths']:
        deaths.append(w['deaths'][i])
    
    arr=numpy.array(cases)
    cases=numpy.diff(arr).tolist()
    arr=numpy.array(deaths)
    deaths=numpy.diff(arr).tolist()
    arr=numpy.array(recovered)
    recovered=numpy.diff(arr).tolist()
    
    cases.insert(0,0)
    deaths.insert(0,0)
    recovered.insert(0,0)

    world_daily_data=dict()
    world_daily_data['cases']=cases
    world_daily_data['deaths']=deaths
    world_daily_data['recovered']=recovered
    world_daily_data['dates']=dates
    #print(world_daily_data)
    return world_daily_data
def get_india_derrivative():
    r=requests.get("https://disease.sh/v3/covid-19/historical/india?lastdays=all")
    ind=r.json()
    cases=list()
    recovered=list()
    deaths=list()
    dates=list()
    for i in ind['timeline']['cases']:
        cases.append(ind['timeline']['cases'][i])
        dic=dict()
        m,d,y=i.split('/')
        dic['day']=int(d)
        dic['month_word']=calendar.month_abbr[int(m)]   
        dic['month']=int(m)
        dic['year']=2000+int(y)
        dates.append(dic)
    for i in ind['timeline']['recovered']:
        recovered.append(ind['timeline']['recovered'][i])
    for i in ind['timeline']['deaths']:
        deaths.append(ind['timeline']['deaths'][i])
    
    arr=numpy.array(cases)
    cases=numpy.diff(arr).tolist()
    arr=numpy.array(deaths)
    deaths=numpy.diff(arr).tolist()
    arr=numpy.array(recovered)
    recovered=numpy.diff(arr).tolist()
    
    cases.insert(0,0)
    deaths.insert(0,0)
    recovered.insert(0,0)

    deaths=list(map(abs, deaths))

    India_daily_data=dict()
    India_daily_data['cases']=cases
    India_daily_data['deaths']=deaths
    India_daily_data['recovered']=recovered
    India_daily_data['dates']=dates
    #print(India_daily_data)
    return India_daily_data
