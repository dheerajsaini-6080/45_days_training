# Day_7_Task

Day 7 self-practice — Intermediate Python, Pandas, NumPy, JSON handling, OOP, Data Analysis, Array Operations, and Similarity Calculations.

## Files

| File                  | What it does                                                                            | How to run                        |
| --------------------- | --------------------------------------------------------------------------------------- | --------------------------------- |
| `student_profile.py`  | Creates a student profile card using dictionaries, type hints, functions, and f-strings | `python student_profile.py`       |
| `json_report.py`      | Reads data from a JSON file and generates a formatted report using list comprehensions  | `python json_report.py`           |
| `profile.json`        | Sample JSON file used by `json_report.py`                                               | Used automatically                |
| `learner_class.py`    | Demonstrates class creation, object instantiation, and method calls                     | `python learner_class.py`         |
| `dataframe_filter.py` | Loads a CSV file, selects columns, and filters rows using Pandas                        | `python dataframe_filter.py`      |
| `sample_data.csv`     | Sample dataset used for Pandas exercises                                                | Used automatically                |
| `loc_iloc_demo.py`    | Demonstrates label-based (`loc`) and position-based (`iloc`) DataFrame selection        | `python loc_iloc_demo.py`         |
| `missing_values.py`   | Identifies and handles missing values using `isnull()`, `fillna()`, and `dropna()`      | `python missing_values.py`        |
| `quick_insights.py`   | Generates dataset insights using `describe()` and `value_counts()`                      | `python quick_insights.py`        |
| `numpy_slicing.py`    | Creates NumPy arrays and demonstrates indexing, slicing, shape, dtype, and dimensions   | `python numpy_slicing.py`         |
| `numpy_similarity.py` | Demonstrates masking, broadcasting, and cosine similarity using NumPy                   | `python numpy_similarity.py`      |
| `requirements.txt`    | Contains project dependencies                                                           | `pip install -r requirements.txt` |

## Setup

```bash
git clone https://github.com/dheerajsaini-6080/45_days_training.git

cd 45_days_training

python -m venv .venv

# Windows
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python --version
```

## Concepts Practiced

* Type Hints
* Dictionaries
* Functions
* F-Strings
* JSON File Handling
* List Comprehensions
* Classes and Objects
* Pandas DataFrames
* Data Filtering
* loc and iloc
* Missing Value Handling
* describe()
* value_counts()
* NumPy Arrays
* Array Slicing
* Boolean Masking
* Broadcasting
* Cosine Similarity

## Explore Tasks Attempted

* Function Type Hints
* JSON Parsing
* List Comprehensions
* Pandas Filtering
* loc vs iloc
* fillna() vs dropna()
* describe()
* value_counts()
* NumPy Broadcasting
* NumPy Masking
* Cosine Similarity using Dot Product and Norm

## Requirements

```text
pandas>=2.0.0
numpy>=1.26.0
```

