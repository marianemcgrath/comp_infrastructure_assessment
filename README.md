# FAANG Stock Data Pipeline

This repository completes the Computing Infrastructure module assessment (Winter 25/26) at ATU. It demonstrates:

- Fetching hourly stock data for FAANG companies (META, AAPL, AMZN, NFLX, GOOG) using `yfinance`.
- Saving data to CSV files and plotting closing prices.
- Creating an executable Python script.
- Automating weekly runs via GitHub Actions.

The core work is explained in detail in [`problems.ipynb`](https://github.com/marianemcgrath/comp_infrastructure_assessment/blob/main/problems.ipynb), including code breakdowns, research references, and explanations.

## Setup and Running

1. Clone the repository:

  git clone https://github.com/marianemcgrath/comp_infrastructure_assessment.git
  
  cd comp_infrastructure_assessment

2. Install dependencies:

  pip install -r requirements.txt

3. Run the script (downloads latest data and generates a plot):

  **./faang.py**
  **pyton faang.py**

- Data files are saved in `/data` (CSV format: `YYYYMMDD-HHmmss.csv`).
- Plots are saved in `/plots` (PNG format: `YYYYMMDD-HHmmss.png`).

4. View the latest plot and data in the respective folders.

## Automation

A GitHub Actions workflow (`.github/workflows/faang.yml`) runs `faang.py` every Saturday morning, committing new data and plots automatically.

## Author

Mariane McGrath  
Email: G00473468@atu.ie  
LinkedIn: [marianemcgrath](https://www.linkedin.com/in/marianemcgrath)

This project is for educational purposes. References are included inline in the notebook.
