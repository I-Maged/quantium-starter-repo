import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

DATA_PATH = "formatted_data.csv"
df = pd.read_csv(DATA_PATH)

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

app = dash.Dash(__name__)

# CSS styling
colors = {
    'background': '#cacadc',
    'text': '#ffffff',
    'accent': '#ff4b4b',
    'dashText': '#7f4bc4',
    'font': 'sans-serif'
}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'minHeight': '100vh', 'padding': '20px', 'fontFamily': colors['font']}, children=[
    html.H1(
        "Pink Morsel Sales Visualiser", 
        id="header", 
        style={
            'textAlign': 'center', 
            'color': colors['text'],
            'marginBottom': '30px',
            'fontWeight': 'bold'
        }
    ),
    
    html.Div(
        [
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': 'North ', 'value': 'north'},
                    {'label': 'East ', 'value': 'east'},
                    {'label': 'South ', 'value': 'south'},
                    {'label': 'West ', 'value': 'west'},
                    {'label': 'All ', 'value': 'all'}
                ],
                value='all',
                inline=True,
                style={
                    'color': colors['text'], 
                    'textAlign': 'center',
                    'fontSize': '18px',
                    'marginBottom': '20px'
                },
                labelStyle={
                    'display': 'inline-block', 
                    'marginRight': '20px', 
                    'cursor': 'pointer'
                }
            )
        ]
    ),

    dcc.Graph(
        id="sales-chart"
    )
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
        title = 'Total Sales of Pink Morsel (All Regions)'
    else:
        filtered_df = df[df['Region'] == selected_region]
        title = f'Total Sales of Pink Morsel ({selected_region.capitalize()} Region)'
        
    df_daily = filtered_df.groupby('Date', as_index=False)['Sales'].sum()
    
    fig = px.line(
        df_daily, 
        x='Date', 
        y='Sales', 
        title=title
    )
    
    fig.add_vline(x='2021-01-15', line_width=2, line_dash="dash", line_color=colors['dashText'])
    
    fig.update_layout(
        plot_bgcolor=colors['text'],
        paper_bgcolor=colors['text'],
        font_color=colors['dashText'],
        title_x=0.5,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#33334d')
    )
    
    fig.update_traces(line_color=colors['accent'])
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
