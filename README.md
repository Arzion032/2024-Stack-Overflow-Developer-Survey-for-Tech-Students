# Project: Gear-Up-for-Success

## 1. Overview

The primary goal of this project is to derive valuable insights from the Stack Overflow survey data that can be shared with classmates and peers to prepare for the upcoming school year. The analysis focuses on identifying key trends and patterns in the survey data that will aid in understanding the tech industry and making informed career and learning decisions.

**Disclaimer:**  
While [Stack Overflow](https://stackoverflow.blog/2024/07/24/developers-want-more-more-more-the-2024-results-from-stack-overflow-s-annual-developer-survey/) has already provided a detailed analysis of the survey data, this project tailors the analysis to aspects most relevant to students and early-career professionals. The focus is on providing insights that support understanding the industry and making informed decisions about learning and career paths.

**Key questions this analysis aims to address:**

1. What are the most frequently used tools and technologies in various tech roles (e.g., programming languages, cloud platforms, databases, frameworks)? How do these tools vary by job role and country?
2. How have salaries varied for tech job roles, industries, and educational levels?
3. Where do developers most commonly seek coding resources (e.g., books, online tutorials, technical documentation), and how do these preferences differ based on their years of coding experience?
4. What factors have the most significant impact on job satisfaction among developers?
5. For those who use AI in their development process, what are their views on using AI tools in their work? Which parts of their development workflow are they currently using AI tools for? What are the key benefits and challenges associated with AI tools?
6. Any additional insights discovered during the analysis?

## 2. Projects

### Dashboard

The dashboard project visualizes key insights from the Stack Overflow survey data, enabling users to explore various aspects of the tech industry. This interactive dashboard includes:

- **Languages**: Visualizations showing the popularity of programming languages based on country and job role.
- **Databases**: Insights into the usage of different databases across different countries and job roles.
- **Platforms**: Information on the most commonly used tech platforms.
- **Web Frameworks**: Analysis of the usage of various web frameworks.
- **Development Tools**: Data on the most popular development tools.

#### Code

The dashboard is built using Dash and visualizes data that has been processed and cleaned. The code is organized as follows:

- **Data Loading and Transformation**: The data is either loaded from preprocessed CSV files or cleaned from raw survey data.
- **Chart Creation**: Functions to generate visualizations for languages, databases, platforms, web frameworks, and development tools.
- **Widgets**: Dropdowns to filter data by country and job role.
- **App Layout**: The layout includes tabs for each category of data with interactive graphs and filters.

### Notebook

The notebook, titled `Gear-Up-for-Success-Key-Takeaways-from-the-2024-Stack-Overflow-Developer-Survey-for-Tech-Students`, provides a comprehensive analysis of the Stack Overflow survey data. It includes:

- **Exploratory Data Analysis (EDA)**: Initial findings and visualizations of key trends in the survey data.
- **Detailed Insights**: In-depth exploration of various aspects of the tech industry as per the survey questions.
- **Key Takeaways**: Summarized findings relevant to students and early-career professionals.

## 3. Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the dashboard:
    ```bash
    python app.py
    ```

5. Open the notebook:
    ```bash
    jupyter notebook stack.ipynb
    ```

## 4. Requirements

Ensure you have the following packages installed:

- `dash`
- `numpy`
- `pandas`
- `plotly` (if required by `viz.py`)
- Other dependencies listed in `requirements.txt`
