# Persona3 User Behavior Analysis
    
This project performs an end-to-end user behavior analysis using pandas.
The dataset represents synthetic user data including country, device type,
gender, age, and spending information.

## Dataset
- Name: persona3.csv
- Number of Records: 1000
- Type: Synthetic user data
- Format: CSV

## Objectives
- Clean and validate user data
- Create new features such as age groups and spending levels
- Analyze user behavior using groupby-based aggregations
- Export analysis results as CSV and Excel files

## Analysis Highlights
- Average spending by country
- Average age by device type
- User counts by gender
- User distribution by country and gender
- Spending statistics by age and age groups
- Identification of the age group with the highest average spending

## Project Structure


## Outputs
- Cleaned dataset: `data/cleaned_persona3.csv`
- Analysis summary: `outputs/summary.xlsx` (multi-sheet Excel file)

## Tools Used
- Python
- Pandas

## Notes
Analysis questions are defined in `questions.md`.
Answers and insights are provided through the analysis code in `analysis.py`
and the exported Excel summary file.
