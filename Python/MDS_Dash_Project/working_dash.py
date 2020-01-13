import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# change directory
desiredpath = 'C:/Users/406822/Desktop/MDS_Data/'
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
data = 'clean_count.csv'
df = pd.read_csv(data)
# print(df.head())
#df['new_date'] = pd.to_datetime(df['unixtime'],unit='s') # Check time/date
# print(df.head())


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='MDS Scooter Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Numbers of Scooters Being Used in past 24 Hours', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    
    dcc.Graph(
        id='MDS',
        figure={
            'data': [
                {'x': df[df['company']=='birdla']['date'], 'y': df[df['company']=='birdla']['used'], 'type': 'line', 'name': 'birdla'},
                {'x': df[df['company']=='spin']['date'], 'y': df[df['company']=='spin']['used'], 'type': 'line', 'name': 'spin'},
                {'x': df[df['company']=='wheels']['date'], 'y': df[df['company']=='wheels']['used'], 'type': 'line', 'name': 'wheels'},
                {'x': df[df['company']=='birdsm']['date'], 'y': df[df['company']=='birdsm']['used'], 'type': 'line', 'name': 'birdsm'},
                {'x': df[df['company']=='lime']['date'], 'y': df[df['company']=='lime']['used'], 'type': 'line', 'name': 'lime'},
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
