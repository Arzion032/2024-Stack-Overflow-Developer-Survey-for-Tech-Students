import plotly.express as px
def modify_language(df, Country, DevType):
    
    if Country != "All":
        df = df[df["Country"] == Country]
    
    if DevType != "All":
        df = df[df["DevType"] == DevType]
    
    if Country != "All" and DevType != "All":
        text = f"Top Programming Languages in {Country} for {DevType}"
        
    if Country != "All" and DevType == "All":
        text = f"Top Programming Languages in {Country}"
        
    if Country == "All" and DevType != "All":
        text = f"Top Programming Languages for {DevType}"
        
    if Country == "All" and DevType == "All":
        text = f"Top Programming Languages"
    return df, text

def modify_database(df, Country, DevType):
    
    if Country != "All":
        df = df[df["Country"] == Country]
    
    if DevType != "All":
        df = df[df["DevType"] == DevType]
    
    if Country != "All" and DevType != "All":
        text = f"Top Databases in {Country} for {DevType}"
        
    if Country != "All" and DevType == "All":
        text = f"Top Databases in {Country}"
        
    if Country == "All" and DevType != "All":
        text = f"Top Databases for {DevType}"
        
    if Country == "All" and DevType == "All":
        text = f"Top Databases"
    return df, text

def modify_Plaform(df, Country, DevType):
    
    if Country != "All":
        df = df[df["Country"] == Country]
    
    if DevType != "All":
        df = df[df["DevType"] == DevType]
    
    if Country != "All" and DevType != "All":
        text = f"Top Platforms in {Country} for {DevType}"
        
    if Country != "All" and DevType == "All":
        text = f"Top Platforms in {Country}"
        
    if Country == "All" and DevType != "All":
        text = f"Top Platforms for {DevType}"
        
    if Country == "All" and DevType == "All":
        text = f"Top Platforms"
    return df, text

def modify_webframe(df, Country, DevType):
    
    if Country != "All":
        df = df[df["Country"] == Country]
    
    if DevType != "All":
        df = df[df["DevType"] == DevType]
    
    if Country != "All" and DevType != "All":
        text = f"Top Web Frameworks in {Country} for {DevType}"
        
    if Country != "All" and DevType == "All":
        text = f"Top Web Frameworks in {Country}"
        
    if Country == "All" and DevType != "All":
        text = f"Top Web Frameworks for {DevType}"
        
    if Country == "All" and DevType == "All":
        text = f"Top Web Frameworks"
    return df, text

def modify_dev_tools(df, Country, DevType):
    
    if Country != "All":
        df = df[df["Country"] == Country]
    
    if DevType != "All":
        df = df[df["DevType"] == DevType]
    
    if Country != "All" and DevType != "All":
        text = f"Top Development Tools in {Country} for {DevType}"
        
    if Country != "All" and DevType == "All":
        text = f"Top Development Tools in {Country}"
        
    if Country == "All" and DevType != "All":
        text = f"Top Development Tools for {DevType}"
        
    if Country == "All" and DevType == "All":
        text = f"Top Development Tools"
    return df, text


def graph(df, country= "All", devtype = 'All', type=None,n="All"):
    
    bar_graph = df.copy()
    Country = country
    DevType = devtype

    if type == 'language':   
        bar_graph, text = modify_language(bar_graph, Country, DevType)
    elif type == 'database':
        bar_graph, text = modify_database(bar_graph, Country, DevType)
    elif type == 'platform':
        bar_graph, text = modify_Plaform(bar_graph, Country, DevType)
    elif type == 'webframe':
        bar_graph, text = modify_webframe(bar_graph, Country, DevType)
    elif type == 'dev_tools':
        bar_graph, text = modify_dev_tools(bar_graph, Country, DevType)

    num_records = bar_graph.shape[0]
    columns_to_drop = ["Unnamed: 0", "ResponseId", "DevType", "Country"]
    bar_graph = bar_graph.drop(columns = bar_graph.columns.intersection(columns_to_drop))
    bar_graph = bar_graph.count().reset_index()
    bar_graph.columns = ['Language', 'Value']
    bar_graph["Avg"] = round((bar_graph["Value"] / num_records) * 100, 2)


    if isinstance(n, int):
        bar_graph = bar_graph.head(n)
        height = 750
    else:
        height = 2000
    
        
    bar_graph = bar_graph.sort_values(by="Value",ascending=True)
    
    
    # Create the Plotly bar plot
    fig = px.bar(bar_graph,
                y='Language',
                x='Value',
                title=' ',
                labels={'Language': 'Category', 'Value': ''},
                color='Value',  
                color_continuous_scale='OrRd',
                template='plotly_dark',
                text='Value',
                hover_data={'Language': True, 'Value': True, 'Avg': True}
                )  
    fig.update_traces(textposition='outside', 
                    textfont_size=14, 
                    textfont_color='black',
                    hovertemplate='<span style="font-size:18px;">%{y}</span><br>Count : %{x}<br>Avg : %{customdata[0]}%',
                    customdata=bar_graph[['Avg']],
                    hoverlabel=dict(
                        font_size=16,    
                        font_family="Amsterdam",
                                    )
                    )
    # Maangas na Layout
    fig.update_layout(
        title={
            'text': text,
            'font_size': 32,  
            'font_family': 'Amsterdam',  
            'font_color': 'black',  
            'font_weight': 'normal'  
        },
        xaxis_title='',         
        yaxis_title='',  
        xaxis=dict(
            tickvals=[],       
            ticktext=[],       
            showgrid=False,    
            zeroline=False    
        ),
        yaxis=dict(
            tickfont=dict(size=20, color='black', family = 'Amsterdam'),
            ),
    
        plot_bgcolor='white', 
        paper_bgcolor='white', 
        title_x=0.5,
        width=1250,  
        height=height,
        coloraxis_colorbar=dict(
            tickfont=dict(
                size=15,        
                color='Black', 
                family='Amsterdam',
                weight = "normal"
            )

        )
    )

    return fig
    