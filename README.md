# EV_Project-Task1
The Task 1 of this project includes steps from dataset loading, cleaning, exploratory analysis, and preparation for machine learning models.
Problem Statement
Objective:
To develop a machine learning model that can predict the cost of an EV based on its specifications and performance metrics.
Use Cases:
Estimating EV prices based on features
Comparing EV efficiency and range across manufacturers
Recommending optimal EVs for specific needs
Dataset Information
File: raw_ev_dataset.csv
Cleaned File: cleaned_ev_data.csv
Rows: 250,000
Columns: 22
Key Columns:
manufacturer, model, type, drive_type, battery_kwh, range_km, charging_time_hr,
release_year, price_usd, efficiency_score, top_speed_kmph, safety_rating, target_high_efficiency
Exploratory Data Analysis (EDA)
Key Findings
EV Price Distribution
Prices are normally distributed; most EVs cost between $25,000–$35,000.
Top 10 Manufacturers
Major brands include Tesla, BMW, Hyundai, Kia, Ford, Nissan, Chevrolet, etc.
Feature Correlation
battery_kwh ↔ range_km: 0.91
battery_kwh ↔ price_usd: 0.83
efficiency_score ↔ target_high_efficiency: 0.82

Battery Capacity vs Range

Linear trend: larger battery → higher range.
