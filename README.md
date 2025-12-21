# FAANG Stock Data

**Computing Infrastructure Module Assessment**

### Problem 1: Data from yfinance

Using the yfinance Python package, write a function called get_data() that downloads all hourly data for the previous five days for the five FAANG stocks:

•	Facebook (META)

•	Apple (AAPL)

•	Amazon (AMZN)

•	Netflix (NFLX)

•	Google (GOOG)

The function should save the data into a folder called data in the root of your repository using a filename with the format YYYYMMDD-HHmmss.csv where YYYYMMDD is the four-digit year (e.g. 2025), followed by the two-digit month (e.g. 09 for September), followed by the two digit day, and HHmmss is hour, minutes, seconds. Create the data folder if you don't already have one.

### Problem 2: Plotting Data

Write a function called plot_data() that opens the latest data file in the data folder and, on one plot, plots the Close prices for each of the five stocks. The plot should include axis labels, a legend, and the date as a title. The function should save the plot into a plots folder in the root of your repository using a filename in the format YYYYMMDD-HHmmss.png. Create the plots folder if you don't already have one.

![plot example](https://github.com/marianemcgrath/comp_infrastructure_assessment/blob/22f2fcca8bbf231807669c4a34c12eb937e01f5f/images/plot_2025-12-20_225527.png)

### Problem 3: Script

Create a Python script called faang.py in the root of your repository. Copy the above functions into it and it so that whenever someone at the terminal types ./faang.py, the script runs, downloading the data and creating the plot. Note that this will require a shebang line and the script to be marked executable. Explain the steps you took in your notebook.

![Script](https://github.com/marianemcgrath/comp_infrastructure_assessment/blob/22f2fcca8bbf231807669c4a34c12eb937e01f5f/images/image-2.png)

### Problem 4: Automation

Create a GitHub Actions workflow to run your script every Saturday morning. The script should be called faang.yml in a .github/workflows/ folder in the root of your repository. In your notebook, explain each of the individual lines in your workflow.

![Workflow](https://github.com/marianemcgrath/comp_infrastructure_assessment/blob/22f2fcca8bbf231807669c4a34c12eb937e01f5f/images/workflow_run.png)

**This repository:**

- Fetching hourly stock data for FAANG companies (META, AAPL, AMZN, NFLX, GOOG) using `yfinance`.
- Saving data to CSV files and plotting closing prices.
- Creating an executable Python script.
- Automating weekly runs via GitHub Actions.

The core work is explained in detail in [`problems.ipynb`](https://github.com/marianemcgrath/comp_infrastructure_assessment/blob/main/problems.ipynb), including code breakdowns, references and explanations.

## Quick Demo

- Latest data: See the most recent CSV in [`data/`](https://github.com/marianemcgrath/comp_infrastructure_assessment/tree/main/data)
- Latest plot: See the most recent PNG in [`plots/`](https://github.com/marianemcgrath/comp_infrastructure_assessment/tree/main/plots)
- Workflow runs: Check [.github/workflows/faang.yml](https://github.com/marianemcgrath/comp_infrastructure_assessment/blob/main/.github/workflows/faang.yml) and commit history for automated updates

The `data/` and `plots/` folders contain historical outputs. The latest files always have the most recent timestamps.

## Setup and Running

1. Clone the repository:

   ```bash
   git clone https://github.com/marianemcgrath/comp_infrastructure_assessment.git
   cd comp_infrastructure_assessment

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Run the script (downloads latest data and generates a plot):

   ```bash
   ./faang.py

   or

   python faang.py

- Data files are saved in `/data` (CSV format: `YYYYMMDD-HHmmss.csv`).
- Plots are saved in `/plots` (PNG format: `YYYYMMDD-HHmmss.png`).


4. New files will appear in data/ and plots/ directories


## Automation

A GitHub Actions workflow (`.github/workflows/faang.yml`) runs `faang.py` every Saturday morning, committing new data and plots automatically.

## Author

Mariane McGrath  
Email: G00473468@atu.ie  
LinkedIn: [marianemcgrath](https://www.linkedin.com/in/marianemcgrath)

This project is for educational purposes. References are included throughout the notebook.
