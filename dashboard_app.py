import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Load and preprocess data
df = pd.read_csv('./data/ecommerce_data.csv', encoding='latin1')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
df['Year'] = df['InvoiceDate'].dt.year
df['Customer_ID'] = df['CustomerID'].astype(str)
df['Sales'] = df['Quantity'] * df['UnitPrice']

# Initialize app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("E-commerce Sales Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.H4("Filter By:"),
        dcc.Dropdown(
            id='filter-type',
            options=[
                {'label': 'Country', 'value': 'Country'},
                {'label': 'Year', 'value': 'Year'},
                {'label': 'Customer ID', 'value': 'Customer_ID'}
            ],
            value='Country',
            style={'width': '300px'}
        ),
        dcc.Dropdown(id='filter-value', style={'width': '300px', 'marginTop': '10px'})
    ], style={'marginBottom': '30px'}),

    dcc.Graph(id='monthly-sales'),
    dcc.Graph(id='top-products'),
    dcc.Graph(id='revenue-country'),
    dcc.Graph(id='top-customers')
])

# Update second dropdown values based on filter type
@app.callback(
    Output('filter-value', 'options'),
    Input('filter-type', 'value')
)
def update_filter_options(filter_type):
    unique_vals = sorted(df[filter_type].dropna().unique())
    return [{'label': str(val), 'value': val} for val in unique_vals]

# Update all graphs
@app.callback(
    [Output('monthly-sales', 'figure'),
     Output('top-products', 'figure'),
     Output('revenue-country', 'figure'),
     Output('top-customers', 'figure')],
    [Input('filter-type', 'value'),
     Input('filter-value', 'value')]
)
def update_dashboard(filter_type, filter_value):
    filtered_df = df.copy()
    title_suffix = " (All Data)"

    if filter_value:
        filtered_df = filtered_df[filtered_df[filter_type] == filter_value]
        title_suffix = f" ({filter_type}: {filter_value})"

    # Monthly Sales Chart
    monthly_sales = filtered_df.groupby('Month')['Sales'].sum().reset_index()
    fig1 = px.bar(monthly_sales, x='Month', y='Sales',
                  title="Monthly Sales" + title_suffix, color_discrete_sequence=['indigo'])

    # Top 10 Products
    top_products = filtered_df.groupby('Description')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
    fig2 = px.bar(top_products, x='Description', y='Sales',
                  title='Top 10 Best-Selling Products' + title_suffix, color_discrete_sequence=['teal'])

    # Revenue by Country
    revenue_country = filtered_df.groupby('Country')['Sales'].sum().sort_values(ascending=False).head(10).reset_index()
    fig3 = px.bar(revenue_country, x='Country', y='Sales',
                  title='Revenue by Country' + title_suffix, color_discrete_sequence=['darkorange'])

    # Top 10 Customers
    top_customers = filtered_df.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False).head(10)
    fig4 = go.Figure(data=[
        go.Bar(x=top_customers.index, y=top_customers.values, marker_color='indigo')
    ])
    fig4.update_layout(title='Top 10 Customers by Revenue' + title_suffix,
                       xaxis=dict(title='Customer ID'), yaxis=dict(title='Revenue'))

    return fig1, fig2, fig3, fig4

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
