# CSE 519 - Data Science (Fall 2023)
## Prof. Steven Skiena
### Homework 3: Data Integration and Modeling
#### Due: Thursday, October 19, 2023

---

### Overview

This assignment explores data integration and model building in IPython, based on the Optiver Trading at the Close Kaggle challenge. The goal is to predict stock price changes during the last ten minutes of the Nasdaq trading day.

---

### Files

The training data contains the following fields:

- `row_id`: Unique identifier (format: f"{date_id}_{time_in_bucket}_{row_id}")
- `time_id`: Sequential time bucket indicator
- `stock_id`: Unique stock identifier
- `date_id`: Unique date identifier
- `imbalance_size`: Unmatched amount at current reference price (in USD)
- `imbalance_buy_sell_flag`: Buy-side imbalance (1), sell-side imbalance (-1), or no imbalance (0)
- `reference_price`: Reference price description
- `matched_size`: Amount matched at current reference price (in USD)
- `far_price`: Far price description
- `near_price`: Near price description
- `[bid/ask]_price`: Most competitive buy/sell level
- `[bid/ask]_size`: Dollar amount on most competitive buy/sell level
- `wap`: Weighted average price
- `seconds_in_bucket`: Seconds elapsed since auction start
- `target`: 60-second future wap move, less the synthetic index move (Train set only)

---

### Environment Setup

We recommend installing Anaconda for Python distribution, or using Google Colab for a hassle-free environment.

#### Required Packages

- pandas
- scikit-learn
- numpy
- Matplotlib
- seaborn (optional)

[Google Colab Notebook](#) contains boilerplate code to start the assignment. Use your @cs.stonybrook.edu email to access.

---

### Tasks (100 points)

1. **Data Cleaning (15 points)**
    - Note anomalies in the training data and clean the data accordingly.

2. **Correlation Table (10 points)**
    - Use Pearson correlation to find pairs of highly correlated variables.

3. **Stock-Day Distance (10 points)**
    - Measure the autocorrelation of the average distance between day i and day i+k for each stock.

4. **Stock Similarity (5 points)**
    - Find pairs of stocks that are unusually similar on a consistent basis.

5. **Clustering (10 points)**
    - Use k-means clustering to categorize stocks.

6. **Closing Trajectory Analysis (10 points)**
    - Evaluate if stock closing is highly correlated or random.

7. **Permutation Test (15 points)**
    - Determine the statistical confidence in your answer.

8. **Model Prediction (20 points)**
    - Build the best prediction model for the Kaggle task.

9. **Kaggle Submission (5 points)**
    - Submit your best models on Kaggle and report your rank and score.

---

### Rules

- Individual work only.
- Understand the domain.
- Start early for better iterations.
- Written responses should be in the notebook template provided.
- Public Kaggle discussions are allowed for reference but must be implemented independently.

---

### Additional Resources

- [Anaconda Installation](#)
- [Google Colab](#)
- [Data Download](#)

---