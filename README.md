# Stack Overflow Survey Analysis
**Note:** GitHub does not support interactive Plotly graphs. To view interactive visualizations and the complete analysis, please visit the DataCamp notebook available at the following link: [DataCamp Notebook](https://www.datacamp.com/datalab/w/8eadb104-1ad8-4f1c-b99c-f43d5ab98978/report)

## 1. Overview

The goal of this project is to extract and present meaningful insights from the Stack Overflow 2024 Developer Survey to help students and early-career professionals better prepare for their future careers. This analysis aims to uncover key trends and patterns in technology use, job satisfaction, and salary variations, focusing on aspects relevant to students' understanding of the industry.

**Key questions this analysis addresses include:**

1. What are the most frequently used tools and technologies in various tech roles (e.g., programming languages, cloud platforms, databases, frameworks)? How do these tools vary by job role and country?
2. How have salaries varied for tech job roles, industries, and educational levels?
3. Where do developers most commonly seek coding resources (e.g., books, online tutorials, technical documentation), and how do these preferences differ based on their years of coding experience?
4. What factors have the most significant impact on job satisfaction among developers?
5. How are AI tools used in development workflows, and what are the associated benefits and challenges?

## 2. Project Components

### a. `stack.ipynb`

A Jupyter Notebook that contains the main analysis of the Stack Overflow survey data. It explores key insights and trends relevant to students and early-career professionals.

### b. `dashboard.py`

Contains the main code for the Dash application, including layout, widgets, and callbacks for interactive visualizations.

### c. `viz.py`

Includes functions for generating visualizations based on the data.

### d. `filter.py`

Contains functions for data cleaning and transformation to prepare the dataset for analysis.

### e. `data/`

Directory containing raw and processed CSV files:
- `survey_results_public.csv`: The raw Stack Overflow survey dataset.
- Additional CSV files for transformed data (if used).

### f. `requirements.txt`

Lists the necessary Python packages required for the project, including:
- `dash`
- `pandas`
- `numpy`
- `plotly`
