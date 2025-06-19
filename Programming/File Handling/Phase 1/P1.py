# 🗂️ File Handling Questions (QA Focused)
# ✅ 1. Read test data from a CSV file and print only failed test cases.
# ✅ 2. Write a script to log test case results into a text file in this format:
# TestCaseID | Status | TimeStamp
#
# ✅ 3. Append new bug IDs to an existing bug log file without overwriting previous data.
# ✅ 4. Write test steps and results to an Excel file using openpyxl or pandas.
# ✅ 5. Scan all .log files in a directory and report the number of errors in each file.
# ✅ 6. Parse a JSON file containing test configuration, and extract environment and browser info.
# ✅ 7. Read credentials from a .env or .json config file and use them to simulate login.
# ✅ 8. Create a function that backs up a test results file by copying it with a timestamp.
# ✅ 9. Verify if a test result file exists before writing; if not, create it.
# ✅ 10. Read a large log file and extract only lines containing "Timeout" errors.
# 🚨 Exception Handling Questions (QA Focused)
# ✅ 11. Wrap a file read operation with exception handling to catch FileNotFoundError and log the issue.
# ✅ 12. Simulate a test execution where a step might fail due to a division by zero; handle it gracefully.
# ✅ 13. Write a function that reads a test data file, and if the format is wrong, raises a custom InvalidDataFormat exception.
# ✅ 14. Use try/except/finally to ensure test result files are always closed after writing, even if an error occurs.
# ✅ 15. Create a log file for exception handling: any error that occurs during test case execution should be written to a separate error log.