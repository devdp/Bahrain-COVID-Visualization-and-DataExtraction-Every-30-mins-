from flask import Flask, request, render_template, url_for
import pandas as pd
import plotly.graph_objects as go
import json
import plotly
from apscheduler.schedulers.background import BackgroundScheduler
import os
import pull_data
from apscheduler.schedulers.blocking import BlockingScheduler

def sensor():
    print('in sensor and alive')
    try:
        if os.path.exists('owid-covid-data.xlsx'):
            os.remove('owid-covid-data.xlsx')
        if os.path.exists('owid-covid-data.csv'):
            os.remove('owid-covid-data.csv')
        if os.path.exists('data.csv'):
            os.remove('data.csv')
        if os.path.exists('datawoarea.csv'):
            os.remove('datawoarea.csv')
        if os.path.exists('last.csv'):
            os.remove('last.csv')
    except:
        print('not')
    global actcase
    global sstate
    global cs
    global d
    global de
    actcase,sstate,cs,d,de = pull_data.pull()
    df = pd.read_excel('owid-covid-data.xlsx', sheet_name='Sheet1')
    df.to_csv('owid-covid-data.csv')
    df = df[df['location'].str.contains("Bahrain", na=False)]
    df['date'] = pd.to_datetime(df['date'])
    case = df['total_cases']
    date = df['date']
    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(x=list(date), y=list(case),name='Increment In Case'))
    # Set title
    fig1.update_layout(
        title_text="Time Series Increment In COVID-19 Cases"
    )
    # Add range slider
    fig1.update_layout(
        width=1200,
        height=600,
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="YTD",
                         step="year",
                         stepmode="todate"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    global g1
    g1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)


sched = BackgroundScheduler()
sched.add_job(sensor,'interval',minutes=30)
sched.start()
sensor()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    error = ' '
    if request.method == 'POST':
        if request.form['email'] == 'abc@email.com' and request.form['pss'] == '12345':
            return render_template('dash.html', g1 = g1, activecases = actcase, sstate = sstate, cs = cs, d = d, de = de)
        else:
            error = 'Invalid Credentials!'
            return render_template('login.html', error=error)
    return render_template('login.html', error=error)

@app.route('/ref', methods=['GET','POST'])
def ref():
    return render_template('dash.html', g1 = g1, activecases = actcase, sstate = sstate, cs = cs, d = d, de = de)
if __name__ == '__main__':
    app.run()