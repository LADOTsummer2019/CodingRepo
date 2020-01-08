import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# change directory
desiredpath = 'C:/Users/406822/Desktop/tim_black_mds/'
os.chdir(desiredpath)
print(desiredpath)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

''' # Live API
url = 'https://la-gbfs.getwheelsapp.com/free_bike_status.json'
data = pd.read_json(url)
df = pd.DataFrame(data['data']['bikes'])
'''
# change unix time to readable time
data = 'count_time_1min.csv'
df = pd.read_csv(data)
# print(df.head())
df['new_date'] = pd.to_datetime(df['unixtime'],unit='s') # Check time/date
# print(df.head())


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    dcc.Graph(
        id='MDS',
        figure={
            'data': [
                {'x': df[df['company']=='birdla']['new_date'], 'y': df[df['company']=='birdla']['count'], 'type': 'line', 'name': 'birdla'},
                {'x': df[df['company']=='spin']['new_date'], 'y': df[df['company']=='spin']['count'], 'type': 'line', 'name': 'spin'},
                {'x': df[df['company']=='wheels']['new_date'], 'y': df[df['company']=='wheels']['count'], 'type': 'line', 'name': 'wheels'},
                {'x': df[df['company']=='birdsm']['new_date'], 'y': df[df['company']=='birdsm']['count'], 'type': 'line', 'name': 'birdsm'},
                {'x': df[df['company']=='lime']['new_date'], 'y': df[df['company']=='lime']['count'], 'type': 'line', 'name': 'lime'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
