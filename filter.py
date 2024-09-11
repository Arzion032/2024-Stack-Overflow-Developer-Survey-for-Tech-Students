import pandas as pd
import numpy as np

jobs = {
    'Developer, full-stack': 'Full-Stack Developer',
    'Developer, back-end': 'Back-End Developer',
    'Developer, front-end': 'Front-End Developer',
    'Developer, desktop or enterprise applications': 'Software Engineer',
    'Developer, embedded applications or devices': 'Software Engineer',
    'Developer, mobile': 'Mobile App Developer',
    'Developer, game or graphics': 'Game Developer',
    'Developer, QA or test': 'QA Engineer',
    'Developer, AI': 'ML Engineer',
    'Blockchain': 'Blockchain Developer',
    'Cloud infrastructure engineer': 'Cloud Engineer',
    'DevOps specialist': 'DevOps Engineer',
    'System administrator': 'System Administrator',
    'Engineer, site reliability': 'Hardware Engineer',
    'Hardware Engineer': 'Hardware Engineer',
    'Data scientist or machine learning specialist': 'Data Science/ML',
    'Data or business analyst': 'Data Analyst',
    'Data engineer': 'Data Engineer',
    'Database administrator': 'Databases Administrator',
    'Academic researcher': 'Academic Researcher',
    'Research & Development role': 'Professional Researcher',
    'Scientist': 'Professional Researcher',
    'Educator': 'Professional Researcher',
    'Student': 'Academic Researcher',
    'Project manager': 'Project Manager',
    'Engineering manager': 'Project Manager',
    'Senior Executive (C-Suite, VP, etc.)': 'Project Manager',
    'Product manager': 'Project Manager',
    'Designer': 'UI/UX Designer',
    'Security professional': 'Cyber Security',
    'Developer Advocate': 'Software Engineer',
    'Developer Experience': 'Software Engineer',
    'Marketing or sales professional': 'Sales Professional',
    'Other (please specify):': 'Others',
    'nan': 'Others'
}

countries = {
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
    'United States of America': 'United States',
    'Iran, Islamic Republic of...': 'Iran',
    'Republic of Korea': 'South Korea',
    'Russian Federation': 'Russia',
    'Venezuela, Bolivarian Republic of...': 'Venezuela',
    'Lao People\'s Democratic Republic': 'Laos',
    'Syrian Arab Republic': 'Syria',
    'Democratic Republic of the Congo': 'Congo',
    'Hong Kong (S.A.R.)': 'Hong Kong',
    'Micronesia, Federated States of...': 'Micronesia',
    'North Korea': 'North Korea',
    "Democratic People's Republic of Korea": 'North Korea',
    'Côte d\'Ivoire': 'Ivory Coast',
    'Congo, Republic of the...' : 'Congo',
    'Republic of North Macedonia': 'North Macedonia',
    'United Republic of Tanzania': 'Tanzania',
    'Dominican Republic': 'Dominican Rep.',
    'Bosnia and Herzegovina': 'Bosnia & Herzegovina',
    'Republic of Moldova': 'Moldova',
    'Micronesia, Federated States of...': 'Micronesia',
    'Syrian Arab Republic': 'Syria',
    'Libyan Arab Jamahiriya': 'Libya',
    'Brunei Darussalam': 'Brunei',
    'Antigua and Barbuda': 'Antigua & Barbuda',
    'Trinidad and Tobago': 'Trinidad & Tobago',
    'Solomon Islands': 'Solomon Is.',
    'Saint Kitts and Nevis': 'St. Kitts & Nevis',
    'Papua New Guinea': 'Papua N.G.',
    'Lao People\'s Democratic Republic': 'Laos',
    'Isle of Man': 'Isle of Man',
    'Federated States of Micronesia': 'Micronesia',
    'Saint Vincent and the Grenadines': 'St. Vincent & Gren.',
    'Democratic People\'s Republic of Korea': 'North Korea',
    'Congo, Republic of the...': 'Congo',
    'Guinea-Bissau': 'Guinea-Bissau',
    'South Sudan': 'S. Sudan',
    'Viet Nam': 'Vietnam',
    'Timor-Leste': 'Timor-Leste',
    'United Arab Emirates' : 'Emirates',
    'Central African Republic' : 'Central Africa' 
}

tools = {
    'Bash/Shell (all shells)' : 'Bash/Shell',
    'Visual Basic (.Net)' : 'Visual Basic',
    'Firebase Realtime Database' : 'Firebase RTDB',
    'Microsoft Access' : 'MS Acsess',
    'Microsoft SQL Server' : 'MS SQL Server',
    "Amazon Web Services (AWS)": "Amazon Web Services",
    "Oracle Cloud Infrastructure (OCI)": "Oracle Cloud",
    "PythonAnywhere": "PythonAnywhere",
    "Managed Hosting": "Managed Hosting",
    "IBM Cloud Or Watson": "IBM Cloud",
    "Alibaba Cloud": "Alibaba Cloud",
    "Linode, now Akamai": "Linode/Akamai",
    'Maven (build tool)' : 'Maven',
    'Visual Studio Solution' : 'VS Solution',
    'Technical documentation': 'Technical Documentation',
    'Blogs': 'Blogs',
    'Books': 'Books',
    'Written Tutorials': 'Written Tutorials',
    'Stack Overflow': 'Stack Overflow',
    'Coding sessions (live or recorded)': 'Coding Sessions',
    'Social Media': 'Social Media',
    'How-to videos': 'How-to Videos',
    'Interactive tutorial': 'Interactive Tutorials',
    'Video-based Online Courses': 'Video-Based Courses',
    'Written-based Online Courses': 'Written-Based Courses',
    'AI': 'AI Tools',
    'Certification videos': 'Certification Videos',
    'Online challenges (e.g., daily or weekly coding challenges)': 'Online Challenges',
    'Programming Games': 'Programming Games',
    'Other (Please specify):': 'Other',
    'Auditory material (e.g., podcasts)': 'Auditory Material'
    }

def  filter_tools(df):
    df = df.rename(columns=tools)
    return df

def filter_jobs(df, column):
    df[column] = df[column].replace(jobs)
    df.fillna({column: "Others"}, inplace=True)
    return df

def filter_country(df, column):
    df[column] = df[column].replace(countries)
    df.fillna({column: "Others"}, inplace=True)
    return df

def cleaners(df,column,dash=True):
    """
    Transforms a DataFrame by processing a specified column containing semicolon-delimited strings and converts it into a one-hot encoded format.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data to be processed.
    column (str): The name of the column to process. This column should contain semicolon-delimited strings representing various tools or categories.
    dash (bool, optional): A flag indicating whether the DataFrame is for use in a dashboard. If True, additional columns are kept and specific filtering   functions are applied. Default is True.

    Returns:
    pd.DataFrame: A new DataFrame where each unique value from the specified column becomes a separate column with binary indicators (1 or 0) for presence.

    Example:
    If the input DataFrame `df` has the following "Tools" column values:
    
    | Tools                          |
    |--------------------------------|
    | Python; SQL; Pandas             |
    | SQL; NumPy                      |
    | Python; NumPy; Pandas; Scikit-Learn|

    After applying the `cleaners` function:

    | ResponseId | DevType | Country | ConvertedCompYearly | Python | SQL | Pandas | NumPy | Scikit-Learn |
    |------------|---------|---------|----------------------|--------|-----|--------|-------|--------------|
    | ...        | ...     | ...     | ...                  | 1      | 1   | 1      | 0     | 0            |
    | ...        | ...     | ...     | ...                  | 0      | 1   | 0      | 1     | 0            |
    | ...        | ...     | ...     | ...                  | 1      | 0   | 1      | 1     | 1            |

    Notes:
    - **Column Processing**: Splits the values in the specified column based on semicolons (`;`) and creates one column per unique value found.
    - **Column Filtering**: Keeps specific columns based on the `dash` flag:
        - If `dash` is True, additional columns (`ResponseId`, `DevType`, `Country`, and `ConvertedCompYearly`) are kept.
        - If `dash` is False, only the specified column is kept.
    - **One-Hot Encoding**: Adds binary columns for each unique value found in the specified column and populates them with `1` for presence and `0` for absence.
    - **Filtering**: Applies additional filtering functions (`filter_jobs`, `filter_country`, `filter_tools`) based on the `dash` flag to further refine the DataFrame.
    """ 
    
    if dash == True:
        cols_to_keep = ["ResponseId", "DevType", "Country", column]
    else:
        cols_to_keep = ["ResponseId","DevType","Country","ConvertedCompYearly", "YearsCode", column]
        
    df = df[df.columns.intersection(cols_to_keep)]
    df = df[df[column].notnull()]
    
    tools = [] 
    
    for line in df[column]:
        for tool in line.split(";"):
            if tool not in tools:
                tools.append(tool.strip())
      
    cleaned_df = df.loc[:,df.columns.intersection(cols_to_keep[:-1])]
    
    for item in tools:
        cleaned_df[item] = np.nan
          
    for (index1, row1), (index2, row2) in zip(df.iterrows(), cleaned_df.iterrows()):
        for lang in row1[column].split(";"):
            lang = lang.strip()
            cleaned_df.at[index2, lang] = 1
            
    cleaned_df = filter_jobs(cleaned_df, "DevType")
    cleaned_df = filter_country(cleaned_df, "Country") 
    cleaned_df= filter_tools(cleaned_df)    
       
    return cleaned_df
        
