# Salary Prediction Using Linear Regression

This project demonstrates a simple linear regression model to predict the salary of a candidate based on their experience, test score, and interview score.

---

## Overview

The goal is to build a machine learning model that predicts an employee's salary using their:

- **Years of experience** (converted from words to numbers)
- **Test score** (out of 10)
- **Interview score** (out of 10)

The data is preprocessed to handle missing values and convert text-based experience into numerical form. A linear regression model is then trained on this cleaned data.

---

## Dataset

- The dataset is loaded from a CSV file named `hiring.csv`.
- Columns used:
  - `experience` (in words, e.g., "five", "two")
  - `test_score(out of 10)`
  - `interview_score(out of 10)`
  - `salary($)`

---

## Key Steps

1. **Importing Libraries**

   - `pandas` and `numpy` for data handling
   - `word2number` to convert word numbers to integers
   - `math` for numerical operations
   - `scikit-learn` for building the linear regression model

2. **Data Cleaning and Preprocessing**

   - Convert experience values from words to numbers using `word2number`
   - Handle missing values in `test_score(out of 10)` by filling with the median score
   - Convert all values to appropriate data types

3. **Model Training**

   - Train a linear regression model using:
     - `experience`
     - `test_score(out of 10)`
     - `interview_score(out of 10)`
   - Target variable: `salary($)`

4. **Prediction**

   - Example prediction made for a candidate with:
     - 5 years experience
     - Test score of 9
     - Interview score of 9

---

## Linear Regression Formula

The trained model estimates salary using the formula:

```

salary = (coef\_exp \* experience) + (coef\_test \* test\_score) + (coef\_interview \* interview\_score) + intercept

```

For example:

```

salary = 2812.95 \* experience + 1845.71 \* test\_score + 2205.24 \* interview\_score + 17737.26

````

---

## Installation

Make sure you have Python 3.x installed. Then install the required libraries using pip:

```bash
pip install pandas numpy scikit-learn word2number
````

---

## How to Use

1. Place the `hiring.csv` file in the same directory as your script.
2. Run your Python script to train the model.
3. Use the trained model to predict salaries by providing experience (years), test score, and interview score.

---

## License

This project is open-source and free to use for educational purposes.

---

## Author

Your Name
Date: 2025-06-12

---

Feel free to contribute or raise issues!

```

If you want, I can help customize it more!
```
