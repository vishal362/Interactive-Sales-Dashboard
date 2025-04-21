# import dash
# from dash import html

# #initializing the app

# app = dash.Dash(__name__)

# #defnining layout of the dashboard

# app.layout = html.Div ([html.H1("E-commerce sales dashboard", style = {'textalign':'center'}),
# html.P("Welcome to interactive dashboard!" ,  style = {'textalign':'center'})])

# #run the app

# if __name__ == '__main__':
#     app.run(debug = True)

# import pandas as pd
# import dash
# from dash import dcc,html
# import plotly.graph_objs as go
# import plotly.express as px

# df = pd.DataFrame({
#      'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
#      'Country': ['USA', 'Canada', 'UK', 'India', 'Germany'],
#      'Year': [2021, 2021, 2021, 2021, 2021],
#      'CustomerID': [1, 2, 3, 4, 5],
#      'Sales': [100, 150, 200, 250, 300]
# })

# df = pd.read_csv('./data/ecommerce_data.csv', encoding='latin1')
# print(df.head())
# df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
# df['invoice_month']= df['InvoiceDate'].dt.to_period('M').astype(str)
# df['total_sales'] = df['Quantity'] * df['UnitPrice']
# df['Year'] = df['InvoiceDate'].dt.year


# monthly_sales = df.groupby('invoice_month')['total_sales'].sum()
# top_products = df.groupby('Description')['total_sales'].sum().sort_values(ascending = False).head(10)
# country_sales = df.groupby ('Country')['total_sales'].sum().sort_values(ascending = False).head(10)
# top_customers = df.groupby ('CustomerID')['total_sales'].sum().sort_values(ascending =False).head(10)


# app = dash.Dash(__name__)

# app.layout = html.Div(
#      style = {'backgroundColor' : '#f8f9fa' , 'padding' : '20px' , 'fontFamily' : 'Arial'}, 
#      children= [
#      html.H1("E-commerce sales dashboard: ", style = {'textAlign':'center' , 'color' : '#333'}),

#      #Main filter dropdown
#      dcc.Dropdown(
#           id = 'Filter-Dropdown',
#           options =[
#           {'label' : 'Filter by Country' , 'value' : 'Country'},
#           {'label' : 'Filter by Year' , 'value' : 'Year'},
#           {'label' : 'Filter by CustomerID', 'value' : 'CustomerID'}
#           ],
#      value = 'Country',
#      style = {'width' : '50%', 'padding' : '30px' , 'margin' : '20px auto'}
#      ),
#  # Dropdowns for Country, Year, CustomerID (Initially hidden)

#      dcc.Dropdown(
#           id = 'Country-Dropdown',
#           style = {'display':'none'},
#           options = [{'label': country, 'value': country} for country in df ['Country'].unique()]
#      ),
#      dcc.Dropdown(
#           id = 'Year-Dropdown',
#           style = {'display': 'none'},
#           options = [{'label': year , 'value': year } for year in df ['Year'].unique()]

#      ),

#      dcc.Dropdown(
#           id = 'CustomerID-Dropdown',
#           style = {'label': 'none'},
#           # options = [{'label': CustomerID , 'value' : CustomerID } for CustomerID in df ['Customer'].unique()]
#           options = [{'label': f'CustomerID {CustomerID}', 'value': CustomerID} for CustomerID in df['CustomerID'].unique()]

#      ),



#      html.Div([
#      html.H2("Monthly sales revenue" , style = {'color': '#444'}),
#      dcc.Graph(
#           id = 'Monthly-Sales Graph',
#          figure ={
#              'data':[
#                 go.Bar(
#                     x=monthly_sales.index,
#                     y=monthly_sales.values,
#                      marker_color = 'Maroon'
#                  )
#              ],
#              'layout':{
#                  'title' : 'Monthly sales revenue',
#                  'xaxis' : {'title':'Month'},
#                  'yaxis' : {'title':'Revenue'}
#              }
                  
#          }
#      )
#    ], style = {'marginBottom': '#50px'}),


# html.Div([
# html.H2 ("Top 10 best selling products" , style = {'color' : '#444'}),
# dcc.Graph(
#      id = 'Top products graph',
#      figure ={
#           'data': [
#                go.Bar(
#                     x = df.groupby('Description')['total_sales']
#                     .sum()
#                     .sort_values(ascending = False)
#                     .head(10)
#                     .index,

#                     y = df.groupby('Description')['total_sales']
#                     .sum()
#                     .head(10)
#                     .values,
#                     marker_color= 'Teal'
#                )
#           ],

#           'layout' :{
#                'title' : "Top 10 best selling products",
#                'xaxis' : {'title' : 'product'},
#                'yaxis' : {'title' : 'Total Sales'}
#           }
#      }
# )
# ], style = {'marginBottom' : '#50px'}),
     

# html.Div([
# html.H2("Revenue by countries"),
# dcc.Graph(
#      id = 'Revenue by country graph',
#      figure={
#           'data':[
#                go.Bar(
#                     x = df.groupby('Country')['total_sales']
#                     .sum()
#                     .sort_values(ascending=False)
#                     .head(10)
#                     .index,

#                     y = df.groupby('Country')['total_sales']
#                     .sum()
#                     .sort_values(ascending=False)
#                     .head(10)
#                     .values,
#                )
#           ], 
#           'layout' :{
#                'title' : 'Top 10 countries by revenue',
#                'xaxis' : {'title': 'Country'},
#                'yaxis' : {'title': 'Total Sales'}
#           }
          
#      }
          
# )
# ], style = {'marginBottom' : '#50px' }), 

# html.Div([
# html.H2("Top 10 customers by revenue" , style = {'color':'#444'}),
# dcc.Graph(
#     figure = {
#         'data':[
#             go.Bar(
#                 x = top_customers.index.astype(str),
#                 y = top_customers.values,
#                 marker_color = 'indigo'
#             )

            
#         ],
#         'layout':{
#             'title' : "Top 10 customers by total spend",
#             'xaxis' : {'title':'Customer id'},
#             'yaxis' : {'title': 'Total Revenue'}
#         }
                                          

#     }
    
# )
# ])
#      ]
# )
# from dash.dependencies import Input, Output
# @app.callback(
#       Output('Monthly-Sales Graph', 'figure'),
#       [
#        Input('Filter-Dropdown' ,'value'),
#        Input('Country-Dropdown', 'value'),
#        Input('Year-dropdown', 'value'),
#        Input('CustomerID-Dropdown' , 'value')
       
#      ]
      
# )
# # @app.callback(
# #     Output('Monthly-Sales Graph', 'figure'),
# #     [
# #         Input('Filter-Dropdown', 'value'),
# #         Input('Country-Dropdown', 'value'),
# #         Input('Year-dropdown', 'value'),
# #         Input('CustomerID-Dropdown', 'value')
# #     ]
# # )

# # def update_graph(filter_value, country_value, year_value, customer_value):
# #      pass

# def update_graph (selected_filter, selected_country,selected_year, selected_customer):
#      print("Filter selected:", selected_filter)

#      if selected_filter == 'Country':
#           filtered_df = df[df['Country'] == selected_country]
#           fig = px.bar (filtered_df,x = 'Month' , y ='Sales' , title = f"Monthly sales for {selected_country}")

#      elif selected_filter == 'Year':
#            filtered_df = df[df['Year'] == selected_year]
#            fig = px.bar (filtered_df, x = 'Month' , y ='Sales' , title = f"Monthly sales for{selected_year}")

#      elif selected_filter == 'Customer_ID':
#           filtered_df = df[df['Customer_ID'] == selected_customer]
#           fig = px.bar (filtered_df, x = 'Month' , y ='Sales' , title = f"Monthly sales for{selected_customer}")

#      else:
#         # default fallback
#         fig = px.bar(df, x='Month', y='Sales', title="Monthly Sales Overview")

#      return fig

# # Callback to show/hide the relevant dropdowns based on the filter selection

# @app.callback(
#      [Output('Country-Dropdown', 'style'),
#       Output('Year-dropdown', 'style'),
#       Output('CustomerID-Dropdown', 'style')],
#       [Input('Filter-Dropdown' ,'value')]

# )
# def update_dropdown_visibility(filter_value):
#      pass

# def toggle_dropdown(selected_filter):
#      if selected_filter == 'Country':
#           return{'display':'block'},{'display':'none'},{'display':'none'}
#      elif selected_filter == 'Year':
#           return{'display' : 'none'} ,{'display': 'block'}, {'display':'none'}
#      elif selected_filter == 'CustomerId':
#           return {'display': 'none'} ,{'display':'none'},{'display':'block'}
#      else:
#         return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}
     
# if __name__== '__main__':
#      app.run(debug=True)


#newcode with only one dashboard
# import pandas as pd
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px

# # Load and preprocess data
# df = pd.read_csv('./data/ecommerce_data.csv', encoding='latin1')
# df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
# df['Year'] = df['InvoiceDate'].dt.year
# df['Customer_ID'] = df['CustomerID'].astype(str)
# df['Sales'] = df['Quantity'] * df['UnitPrice']

# # Initialize app
# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1("E-commerce Sales Dashboard", style={'textAlign': 'center'}),

#     html.H3("Filter by"),
#     dcc.Dropdown(
#         id='Filter-Dropdown',
#         options=[
#             {'label': 'Country', 'value': 'Country'},
#             {'label': 'Year', 'value': 'Year'},
#             {'label': 'Customer ID', 'value': 'Customer_ID'},
#         ],
#         value='Country',
#         style={'width': '300px'}
#     ),

#     dcc.Dropdown(id='Country-Dropdown',
#                  options=[{'label': country, 'value': country} for country in df['Country'].unique()],
#                  placeholder="Select Country", style={'display': 'block', 'width': '300px'}),

#     dcc.Dropdown(id='Year-dropdown',
#                  options=[{'label': str(year), 'value': year} for year in sorted(df['Year'].unique())],
#                  placeholder="Select Year", style={'display': 'none', 'width': '300px'}),

#     dcc.Dropdown(id='CustomerID-Dropdown',
#                  options=[{'label': f'Customer {cid}', 'value': cid} for cid in df['Customer_ID'].unique()],
#                  placeholder="Select Customer", style={'display': 'none', 'width': '300px'}),

#     dcc.Graph(id='Monthly-Sales Graph')
# ])

# # Show/hide dropdowns
# @app.callback(
#     [Output('Country-Dropdown', 'style'),
#      Output('Year-dropdown', 'style'),
#      Output('CustomerID-Dropdown', 'style')],
#     [Input('Filter-Dropdown', 'value')]
# )
# def toggle_dropdowns(filter_value):
#     if filter_value == 'Country':
#         return {'display': 'block', 'width': '300px'}, {'display': 'none'}, {'display': 'none'}
#     elif filter_value == 'Year':
#         return {'display': 'none'}, {'display': 'block', 'width': '300px'}, {'display': 'none'}
#     elif filter_value == 'Customer_ID':
#         return {'display': 'none'}, {'display': 'none'}, {'display': 'block', 'width': '300px'}
#     return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}

# # Graph update based on filter
# @app.callback(
#     Output('Monthly-Sales Graph', 'figure'),
#     [Input('Filter-Dropdown', 'value'),
#      Input('Country-Dropdown', 'value'),
#      Input('Year-dropdown', 'value'),
#      Input('CustomerID-Dropdown', 'value')]
# )
# def update_graph(filter_type, country_val, year_val, customer_val):
#     if filter_type == 'Country' and country_val:
#         filtered_df = df[df['Country'] == country_val]
#         title = f"Monthly Sales for {country_val}"
#     elif filter_type == 'Year' and year_val:
#         filtered_df = df[df['Year'] == year_val]
#         title = f"Monthly Sales for Year {year_val}"
#     elif filter_type == 'Customer_ID' and customer_val:
#         filtered_df = df[df['Customer_ID'] == customer_val]
#         title = f"Monthly Sales for Customer {customer_val}"
#     else:
#         filtered_df = df
#         title = "Monthly Sales (All Data)"

#     monthly_sales = filtered_df.groupby('Month')['Sales'].sum().reset_index()
#     fig = px.bar(monthly_sales, x='Month', y='Sales', title=title, color_discrete_sequence=['indigo'])
#     return fig

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

#code for all dashboards

# import pandas as pd
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import plotly.graph_objs as go

# # Load and preprocess data
# df = pd.read_csv('./data/ecommerce_data.csv', encoding='latin1')
# df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
# df['Month'] = df['InvoiceDate'].dt.to_period('M').astype(str)
# df['Year'] = df['InvoiceDate'].dt.year
# df['Customer_ID'] = df['CustomerID'].astype(str)
# df['Sales'] = df['Quantity'] * df['UnitPrice']

# # # Initialize app
# app = dash.Dash(__name__)

# # App Layout
# app.layout = html.Div([
#     html.H1("E-commerce Sales Dashboard", style={'textAlign': 'center'}),

#     # Filter Dropdowns
#     html.H3("Filter by"),
#     dcc.Dropdown(
#         id='Filter-Dropdown',
#         options=[
#             {'label': 'Country', 'value': 'Country'},
#             {'label': 'Year', 'value': 'Year'},
#             {'label': 'Customer ID', 'value': 'Customer_ID'},
#         ],
#         value='Country',
#         style={'width': '300px'}
#     ),

#     dcc.Dropdown(id='Country-Dropdown',
#                  options=[{'label': country, 'value': country} for country in df['Country'].unique()],
#                  placeholder="Select Country", style={'display': 'block', 'width': '300px'}),

#     dcc.Dropdown(id='Year-dropdown',
#                  options=[{'label': str(year), 'value': year} for year in sorted(df['Year'].unique())],
#                  placeholder="Select Year", style={'display': 'none', 'width': '300px'}),

#     dcc.Dropdown(id='CustomerID-Dropdown',
#                  options=[{'label': f'Customer {cid}', 'value': cid} for cid in df['Customer_ID'].unique()],
#                  placeholder="Select Customer", style={'display': 'none', 'width': '300px'}),

#     dcc.Graph(id='Monthly-Sales Graph'),

#     html.H2("Top 10 Best-Selling Products"),
#     dcc.Graph(
#         figure=px.bar(
#             df.groupby('Description')['Sales'].sum().sort_values(ascending=False).head(10).reset_index(),
#             x='Description', y='Sales', title='Top 10 Products by Revenue', color_discrete_sequence=['teal']
#         )
#     ),

#     html.H2("Revenue by Country"),
#     dcc.Graph(
#         figure=px.bar(
#             df.groupby('Country')['Sales'].sum().sort_values(ascending=False).head(10).reset_index(),
#             x='Country', y='Sales', title='Top 10 Countries by Revenue', color_discrete_sequence=['darkorange']
#         )
#     ),

#     html.H2("Top 10 Customers by Revenue"),
#     dcc.Graph(
#         figure=go.Figure(
#             data=[
#                 go.Bar(
#                     x=df.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False).head(10).index,
#                     y=df.groupby('Customer_ID')['Sales'].sum().sort_values(ascending=False).head(10).values,
#                     marker_color='indigo'
#                 )
#             ],
#             layout=go.Layout(
#                 title='Top 10 Customers by Total Spend',
#                 xaxis=dict(title='Customer ID'),
#                 yaxis=dict(title='Total Revenue')
#             )
#         )
#     )
# ])

# # # Show/hide relevant dropdowns
# @app.callback(
#     [Output('Country-Dropdown', 'style'),
#      Output('Year-dropdown', 'style'),
#      Output('CustomerID-Dropdown', 'style')],
#     [Input('Filter-Dropdown', 'value')]
# )
# def toggle_dropdowns(filter_value):
#     if filter_value == 'Country':
#         return {'display': 'block', 'width': '300px'}, {'display': 'none'}, {'display': 'none'}
#     elif filter_value == 'Year':
#         return {'display': 'none'}, {'display': 'block', 'width': '300px'}, {'display': 'none'}
#     elif filter_value == 'Customer_ID':
#         return {'display': 'none'}, {'display': 'none'}, {'display': 'block', 'width': '300px'}
#     return {'display': 'none'}, {'display': 'none'}, {'display': 'none'}

# # Update graph based on filter
# @app.callback(
#     Output('Monthly-Sales Graph', 'figure'),
#     [Input('Filter-Dropdown', 'value'),
#      Input('Country-Dropdown', 'value'),
#      Input('Year-dropdown', 'value'),
#      Input('CustomerID-Dropdown', 'value')]
# )
# def update_graph(filter_type, country_val, year_val, customer_val):
#     if filter_type == 'Country' and country_val:
#         filtered_df = df[df['Country'] == country_val]
#         title = f"Monthly Sales for {country_val}"
#     elif filter_type == 'Year' and year_val:
#         filtered_df = df[df['Year'] == year_val]
#         title = f"Monthly Sales for Year {year_val}"
#     elif filter_type == 'Customer_ID' and customer_val:
#         filtered_df = df[df['Customer_ID'] == customer_val]
#         title = f"Monthly Sales for Customer {customer_val}"
#     else:
#         filtered_df = df
#         title = "Monthly Sales (All Data)"

#     monthly_sales = filtered_df.groupby('Month')['Sales'].sum().reset_index()
#     fig = px.bar(monthly_sales, x='Month', y='Sales', title=title, color_discrete_sequence=['indigo'])
#     return fig

# # Run app
# if __name__ == '__main__':
#     app.run(debug=True)


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
