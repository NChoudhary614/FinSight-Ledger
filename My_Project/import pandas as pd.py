import os
print(os.getcwd())

import pandas as pd

# Step 1: Gather Data
# Example: Load transactions from a CSV file with columns: Date, Category, Amount, Type (Income/Expense)
df = pd.read_csv('transactions.csv')

# Step 2: Organize and Categorize
income = df[df['Type'] == 'Income']['Amount'].sum()
expenses = df[df['Type'] == 'Expense']['Amount'].sum()

# Step 3: Calculate Savings
savings = income - expenses

# Step 4: Prepare Report Data
report = {
    'Total Income': income,
    'Total Expenses': expenses,
    'Savings': savings
}

# Step 5: Generate Financial Statement Table
print("Financial Report")
print("----------------")
for key, value in report.items():
    print(f"{key}: {value:.2f}")

# Step 6: Save Report to Excel
report_df = pd.DataFrame([report])
report_df.to_excel('financial_report.xlsx', index=False)

# Optional: Add notes or explanations
notes = "This report summarizes income, expenses, and savings for the selected period."
with open('financial_report_notes.txt', 'w') as f:
    f.write(notes)
