from dash import dcc, html, Dash, callback, Input, Output
from viz import graph
from pathlib import Path
import numpy as np
import pandas as pd
from filter import cleaners
current_directory = Path.cwd()

################### DATASET ####################################
#---------------------------------------------------------------
# Below are the dataset loading and transformation steps. 
# The first block (commented out) is used when the data has already been transformed
# and saved as CSV files for each technology category.

"""
# Load transformed data (already cleaned and processed)
languages = pd.read_csv(current_directory / 'data' / 'languages.csv')
databases = pd.read_csv(current_directory / 'data' / 'databases.csv')
platforms = pd.read_csv(current_directory / 'data' / 'platform.csv')
web_frameworks = pd.read_csv(current_directory / 'data' / 'web_framework.csv')
dev_tools = pd.read_csv(current_directory / 'data' / 'development_tools.csv')
"""

# Load the raw survey dataset
filename = current_directory / 'data' /'survey_results_public.csv'
df = pd.read_csv(filename) # Read the survey CSV file into a DataFrame

languages = cleaners(df, "LanguageHaveWorkedWith") 
databases = cleaners(df, "DatabaseHaveWorkedWith")
platforms = cleaners(df, "PlatformHaveWorkedWith")
web_frameworks = cleaners(df, "WebframeHaveWorkedWith")
dev_tools = cleaners(df, "ToolsTechHaveWorkedWith")

app = Dash(__name__)


#################### CHARTS #####################################
def create_language_chart(Count="All", Dev="All"):
    fig = graph(languages, country=Count, devtype=Dev, type="language")
    return fig

def create_database_chart(Count="All", Dev="All"):
    fig = graph(databases, country=Count, devtype=Dev,type="database")
    return fig

def create_platform_chart(Count="All", Dev="All"):
    fig = graph(platforms, country=Count, devtype=Dev,type="platform")
    return fig

def create_webframe_chart(Count="All", Dev="All"):
    fig = graph(web_frameworks, country=Count, devtype=Dev,type="webframe")
    return fig

def create_devtools_chart(Count="All", Dev="All"):
    fig = graph(dev_tools, country=Count, devtype=Dev,type="dev_tools")
    return fig


##################### WIDGETS ####################################

lang_country = np.concatenate((["All"], np.sort(languages.Country.unique())))
lang_devtype = np.concatenate((["All"], np.sort(languages.DevType.unique())))
language_country = dcc.Dropdown(id="lang_count", options=lang_country, value="All",clearable=False)
language_devtype = dcc.Dropdown(id="lang_dev", options=lang_devtype, value="All",clearable=False)

data_country = np.concatenate((["All"], np.sort(databases.Country.unique())))
data_devtype = np.concatenate((["All"], np.sort(databases.DevType.unique())))
database_country = dcc.Dropdown(id="data_count", options=data_country, value="All",clearable=False)
database_devtype = dcc.Dropdown(id="data_dev", options=data_devtype, value="All",clearable=False)

plat_country = np.concatenate((["All"], np.sort(platforms.Country.unique())))
plat_devtype = np.concatenate((["All"], np.sort(platforms.DevType.unique())))
platform_country = dcc.Dropdown(id="plat_count", options=plat_country, value="All",clearable=False)
platform_devtype = dcc.Dropdown(id="plat_dev", options=plat_devtype, value="All",clearable=False)

web_country = np.concatenate((["All"], np.sort(web_frameworks.Country.unique())))
web_devtype = np.concatenate((["All"], np.sort(web_frameworks.DevType.unique())))
webframe_country = dcc.Dropdown(id="web_count", options=web_country, value="All",clearable=False)
webframe_devtype = dcc.Dropdown(id="web_devtype", options=web_devtype, value="All",clearable=False)

dev_country = np.concatenate((["All"], np.sort(dev_tools.Country.unique())))
dev_devtype = np.concatenate((["All"], np.sort(dev_tools.DevType.unique())))
devtools_country = dcc.Dropdown(id="dev_count", options=dev_country, value="All",clearable=False)
devtools_devtype = dcc.Dropdown(id="dev_devtype", options=dev_devtype, value="All",clearable=False)

##################### APP LAYOUT ####################################


app.layout = html.Div([
    # Separate container for the title
    html.Div(
        html.H1("Stack Overflow Survey : Most Popular Developer Tools", className="title"),
        className="text-center",  # Center the title
        style={"margin-bottom": "20px", "color":"white"}  # Add margin if needed
    ),
    
    # Main content
    html.Div([
        dcc.Tabs([
            
            #LANGUAGE CHARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            dcc.Tab([
                html.Br(),
                    html.Div([
                        html.Div([
                            html.Span("Country", className="white-text"),
                            language_country
                        ], style={'display': 'inline-block', 'margin-right': '10px', 'width': '33%'}),  

                        html.Div([
                            html.Span("Job Title", className="white-text"),
                            language_devtype
                        ], style={'display': 'inline-block', 'width': '33%'})
                    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '20px'}),  # Para side-by-side aesthetic
                html.Br(),
                html.Div(dcc.Graph(id="language"), className="centered-graph"),
            ], label="Languages"),
            
            #DATABASE CHARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            dcc.Tab([
                html.Br(),
                    html.Div([
                        html.Div([
                            html.Span("Country", className="white-text"),
                            database_country
                        ], style={'display': 'inline-block', 'margin-right': '10px', 'width': '33%'}),  

                        html.Div([
                            html.Span("Job Title", className="white-text"),
                            database_devtype
                        ], style={'display': 'inline-block', 'width': '33%'})
                    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '20px'}),  
                html.Br(),
                html.Div(dcc.Graph(id="database"), className="centered-graph"),
            ], label="Databases"),
            
            #PLATFORM CHARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            dcc.Tab([
                html.Br(),
                    html.Div([
                        html.Div([
                            html.Span("Country", className="white-text"),
                            platform_country
                        ], style={'display': 'inline-block', 'margin-right': '10px', 'width': '33%'}),  

                        html.Div([
                            html.Span("Job Title", className="white-text"),
                            platform_devtype
                        ], style={'display': 'inline-block', 'width': '33%'})
                    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '20px'}),  
                html.Br(),
                html.Div(dcc.Graph(id="platform"), className="centered-graph"),
            ], label="Platforms"),
            
            #WEB FRAMEWORKS CHARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            dcc.Tab([
                html.Br(),
                    html.Div([
                        html.Div([
                            html.Span("Country", className="white-text"),
                            webframe_country
                        ], style={'display': 'inline-block', 'margin-right': '10px', 'width': '33%'}),  

                        html.Div([
                            html.Span("Job Title", className="white-text"),
                            webframe_devtype
                        ], style={'display': 'inline-block', 'width': '33%'})
                    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '20px'}),  # Flexbox container for side-by-side layout
                html.Br(),
                html.Div(dcc.Graph(id="webframe"), className="centered-graph"),
            ], label="Webframeworks"),
            
            #DEVELOPMENT TOOLS CHARTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            dcc.Tab([
                html.Br(),
                    html.Div([
                        html.Div([
                            html.Span("Country", className="white-text"),
                            devtools_country
                        ], style={'display': 'inline-block', 'margin-right': '10px', 'width': '33%'}),  # Adjust spacing as needed

                        html.Div([
                            html.Span("Job Title", className="white-text"),
                            devtools_devtype
                        ], style={'display': 'inline-block', 'width': '33%'})
                    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'gap': '20px'}),  # Flexbox container for side-by-side layout
                html.Br(),
                html.Div(dcc.Graph(id="devtools"), className="centered-graph"),
            ], label="Development Tools"),
        ])
    ], className="Maangas"),
])


##################### CALLBACKS ####################################
@callback(Output("language", "figure"), [Input("lang_count", "value"), Input("lang_dev", "value"),])
def update_language_chart(count, dev):
    return create_language_chart(count, dev)

@callback(Output("database", "figure"), [Input("data_count", "value"), Input("data_dev", "value"),])
def update_database_chart(count, dev):
    return create_database_chart(count, dev)

@callback(Output("platform", "figure"), [Input("plat_count", "value"), Input("plat_dev", "value"),])
def update_platform_chart(count, dev):
    return create_platform_chart(count, dev)

@callback(Output("webframe", "figure"), [Input("web_count", "value"), Input("web_devtype", "value"),])
def update_webframe_chart(count, dev):
    return create_webframe_chart(count, dev)

@callback(Output("devtools", "figure"), [Input("dev_count", "value"), Input("dev_devtype", "value"),])
def update_webframe_chart(count, dev):
    return create_devtools_chart(count, dev)

if __name__ == "__main__":
    app.run(debug=True)