# Big Mart Sales Data Analysis

This project performs exploratory data analysis (EDA) on Big Mart sales data. It includes data cleaning, visualization, and various analytical techniques to understand the distribution and relationships within the dataset.

## Technologies Used
- Python
- Pandas (Data Manipulation)
- NumPy (Numerical Operations)
- Matplotlib (Data Visualization)
- Seaborn (Statistical Data Visualization)

## Project Overview
The analysis involves several key steps:
1. **Data Loading & Inspection**: Loading the `Test.csv` dataset and understanding its structure.
2. **Data Cleaning**: Handling missing values for attributes like `Item_Weight` and `Outlet_Size`, and standardizing the `Item_Fat_Content` values.
3. **Univariate Analysis**: Exploring distributions of single variables such as `Item_MRP` and `Item_Visibility` using histograms and count plots.
4. **Bivariate Analysis**: Examining relationships between two variables, for instance, comparing `Item_MRP` across different `Outlet_Type`s using boxplots.
5. **Categorical & Time Analysis**: Visualizing counts of categorical features and analyzing trends over `Outlet_Establishment_Year`.
6. **Correlation Analysis**: Generating a correlation heatmap to identify relationships between numerical features.

## Files
- `Test.csv`: The dataset used for analysis.
- `data_analysis_project_fixed.py`: Python script containing the full data analysis and visualization pipeline.
- `data_analysis_project_fixed.ipynb`: Jupyter Notebook version of the analysis.

## How to Run
To run the Python script:
```bash
python data_analysis_project_fixed.py
```
Or open `data_analysis_project_fixed.ipynb` in Jupyter Notebook/JupyterLab.
