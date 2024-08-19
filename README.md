# Debt Payoff Calculator

## Overview

This Python program calculates the time required to pay off debts using different payoff strategies. The program allows the user to enter multiple debts, specifying the debt amount, interest rate, and payment value for each debt. The program then computes the debt payoff timeline using the following methods:

1. **Consolidated Method**
2. **Avalanche Method**
3. **Snowball Method**
4. **Highest Payment First Method**

## How It Works

### 1. **Consolidated Method**
- The program calculates the total debt and divides it by the user's income to estimate the payoff time if all debts were consolidated into a single payment.

### 2. **Avalanche Method**
- Debts are sorted in descending order based on their interest rates.
- The program calculates the time required to pay off the debts, starting with the highest interest rate debt first.

### 3. **Snowball Method**
- Debts are sorted in ascending order based on their payment values.
- The program calculates the time required to pay off the debts, starting with the smallest debt first, then adding the previous payment amount to the next debt in the list.

### 4. **Highest Payment First Method**
- Debts are sorted in descending order based on their payment values.
- The program calculates the time required to pay off the debts, starting with the debt with the highest payment first.

## How to Use

1. **Run the Program:**
   - Execute the script in your preferred Python environment.

2. **Input Salary:**
   - When prompted, enter your monthly salary. This value will be used to calculate how long it will take to pay off your debts.

3. **Enter Debts:**
   - For each debt, input the following details:
     - Debt Value: The total amount owed.
     - Interest Rate: The interest rate of the debt.
     - Payment Value: The monthly payment amount.
   - To stop entering debts, input `0` for the Debt Value.

4. **Review the Results:**
   - The program will display the time it will take to pay off your debts using each of the four methods.


## Dependencies

- This script requires Python 3.x.

## Notes

- The program does not consider the interest accrued over time, meaning the actual time to pay off the debt may be longer.
- The Avalanche Method is typically more efficient as it prioritizes high-interest debts, but the Snowball Method can be more motivating as it focuses on clearing smaller debts first.



