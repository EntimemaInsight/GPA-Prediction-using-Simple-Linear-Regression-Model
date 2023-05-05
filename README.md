# GPA-Prediction-using-Simple-Linear-Regression-Python-Model
This project uses a simple linear regression model to predict a student's GPA based on their SAT score and attendance rate. 
The project is implemented in Python using various libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Statsmodels.

## Data
The project uses two datasets: 1.01. Simple linear regression.csv and 1.03. Dummies.csv. The 1.01. Simple linear regression.csv file contains data on 84 students, including their SAT scores and GPAs. The 1.03. Dummies.csv file contains similar data but also includes a binary variable indicating whether a student attended more than 75% of their lectures.

## Dependencies
This project requires the following libraries to be installed:

NumPy
Pandas
Matplotlib
Statsmodels
Seaborn
These libraries can be installed using pip by running the following command:
pip install numpy pandas matplotlib statsmodels seaborn

## Usage
To use this project, simply run the GPAPrediction.ipynb Jupyter Notebook file. The file contains code for data exploration, regression analysis, and predictions.

## Regression Analysis
The regression analysis shows that there is a positive correlation between a student's SAT score and their GPA. The coefficient for SAT is positive and statistically significant (t=7.487, p<0.001), indicating that for every one-point increase in SAT score, we can expect to see a 0.0017 point increase in GPA.

The analysis also shows that attendance rate is a significant factor in predicting a student's GPA. The coefficient for attendance is also positive and statistically significant (t=5.451, p<0.001), indicating that students who attend more lectures can be expected to have a higher GPA, holding their SAT score constant.

## Predictions
Based on the predictions made by the model, it can be inferred that a student who attended most of their lectures is likely to have a higher GPA than a student who did not attend as many lectures, even if they scored higher on the SAT.

## Key Insights

1. The simple linear regression model shows that there is a positive correlation between a student's SAT score and their GPA, which is consistent with previous research in the field.

2. Attendance rate is also a significant factor in predicting a student's GPA, indicating that students who attend more lectures are likely to perform better academically.

3. The predictions made by the model suggest that attendance rate is a more important factor than SAT score in determining a student's GPA. This highlights the importance of attending lectures regularly, even if a student has a high SAT score.

4. The model's limitations should also be considered. For example, the dataset used in this project is relatively small and may not be representative of the entire student population. Additionally, the model only considers two variables (SAT score and attendance rate) and does not take into account other factors that may influence a student's academic performance.


## Credits
This project was created by Aleksandar Dimitrov. 
If you have any questions or comments, feel free to contact me at alexi.zein@gmail.com.
