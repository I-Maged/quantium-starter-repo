import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

DATA_PATH = "formatted_data.csv"
df = pd.read_csv(DATA_PATH)

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

app = dash.Dash(__name__)

df_daily = df.groupby('Date', as_index=False)['Sales'].sum()

fig = px.line(
    df_daily, 
    x='Date', 
    y='Sales', 
    title='Total Sales of Pink Morsel (All Regions)'
)

fig.add_vline(x='2021-01-15', line_width=2, line_dash="dash", line_color="red")

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", id="header", style={'textAlign': 'center', 'fontFamily': 'sans-serif'}),
    dcc.Graph(
        id="sales-chart",
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
