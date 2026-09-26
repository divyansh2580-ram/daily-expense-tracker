# Daily Expense Tracker

This is a Python-based Daily Expense Tracker created for the CSE1021 mini-project. It uses basic data structures like parallel lists and iterative loops to record and summarize everyday expenses.

**Name:** Divyansh Agarwal
**Registration No.:** 26BCE10443

## Overview and Features
This tool provides a lightweight, terminal-based solution for tracking money. 
* **Data Input:** Users can log expenses by category, amount, and date.
* **Reporting:** Users can view all expenses or see a consolidated category-wise summary.
* **Analytics:** Calculates total overall expenditure.

## Technologies Used
* Python 3.x
* Built-in functions (No external libraries required)

## How to Set Up and Run the Project
**1. Prerequisites**
* You must have Python installed on your system. 

**2. Downloading the Project**
* Clone this repository to your local machine using the command terminal:
  `git clone <paste-your-new-college-repository-url-here>`
* Navigate into the project folder:
  `cd daily_expense_tracker`

**3. Execution**
* Open your command line terminal (CMD, PowerShell, or macOS Terminal).
* Run the following command to start the application:
  `python expense_tracker.py`

## Instructions for Testing
1. Run the script and press `1` to add an expense. Enter "Food", "150", and today's date.
2. Press `1` again and enter "Travel", "50", and today's date.
3. Press `1` again and enter "Food", "100", and today's date.
4. Press `3` to view the Category Summary. Ensure "Food" correctly shows a total of 250, and "Travel" shows 50.
5. Press `4` to ensure the total expense correctly displays 300.
