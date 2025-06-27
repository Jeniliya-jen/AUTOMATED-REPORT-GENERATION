# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: JENILIYA J

*INTERN ID*: CT04DG574

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*:  NEELA SANTHOSH

# AUTOMATED-REPORT-GENERATION - Codtech Internship Task 2
This project is part of Task 1 for the CodTech Python Internship. This project demonstrates how to create an automated PDF report using Python and the FPDF library. The goal of the task is to read structured data from a CSV file, analyze it, and generate a well-formatted and professional-looking PDF report without manual effort. For this task, we chose a real-world use case — a Library Book Lending Report that summarizes borrowing activity in a fictional programming library.

## Project Overview
Task 2 focuses on building an automated system in Python to read structured data from a CSV file and generate a clean, professional PDF report. For this task, a fictional **Library Book Lending Report system** was created using a dataset of programming-themed books. The Python script uses pandas to analyze book borrowing records—such as borrower's name, date borrowed, date returned, and current status—and then uses the fpdf library to produce a formatted, printable report. The final PDF includes a title, timestamp, lending data table, summary statistics, and a closing note—all automatically generated without manual intervention.

This project showcases real-world applications of automation, such as managing lending systems in libraries. The report layout includes styled headers, pastel coloring, aligned content, and statistical summaries for readability and professionalism. All data used is **fictional**. This task has been an excellent opportunity to learn about integrating data analysis and document generation, and I sincerely thank CodTech IT Solutions for this enriching experience.

## Dataset: Library Book Lending
The CSV file used in this project simulates lending activity in a programming-themed library. It contains fictional records of book lending, including book IDs, book titles (fictional programming books), borrower names, dates of borrowing and returning, and current lending status.

**CSV Columns:**
- **Book ID**: Unique identifier for each book.
- **Title**: Title of the programming-themed book.
- **Borrower**: Name of the person who borrowed the book.
- **Date Borrowed**: The date when the book was borrowed.
- **Date Returned**: The date when the book was returned (if returned).
- **Status**: Current status of the book (Returned or Borrowed).

This structured format allows to create informative tables and summaries in the report.

## Tools & Libraries Used:
- **Python**: Programming language used to implement the script.
- **Pandas**: For reading and processing CSV data.
- **FPDF**: A lightweight Python library to generate PDF documents.
- **datetime**: To include dynamic timestamps in the report.

## About the Auto-Generated PDF Report
This project automatically generates a clean, professional, and informative PDF report from a CSV file. The resulting file is called:
It is created using the Python fpdf library and includes neatly formatted tables, summaries, and report metadata without any manual effort. The report is suitable for academic, library, or internal documentation purposes.
**Report Features**:
1. **Report Title & Timestamp**: The top section of the PDF displays a bold and centered title, **"Library Book Lending Report"**. Immediately below the title, the report shows the timestamp when the report was generated. This adds credibility and helps track the freshness of the data
2. **Lending Data Table**: The core of the report is a tabular representation of the lending records. It displays the following columns for each book:
   - Book ID: Unique identifier of the book.
   - Title: Name of the book.
   - Borrower: Name of the person who borrowed the book.
   - Date Borrowed: The borrowing date.
   - Date Returned: The return date, or a dash if the book is still borrowed.
   - Status: Either Returned or Borrowed.

  The table is formatted with borders, aligned cells, and light-colored headers for better readability.
3. **Summary Section**: After the table, the report includes a summary section that provides quick statistical insights:
   - Total Books Tracked: Number of entries in the CSV.
   - Books Returned: Count of books with status Returned.
   - Books Still Borrowed: Count of books with status Borrowed.
    
  This section is helpful for instantly understanding the lending activity without manually scanning the data.
4. **Footer**: At the end of the report, a footer message is included, **"Note: This report was automatically generated for monitoring library book lending activity."**
  This communicates that the report is produced by a system and helps reinforce the professionalism and consistency of the document.

## Conclusion:
This task was a rewarding experience in automating documentation with Python. It enhanced my understanding of how data can be turned into useful, presentable information through code. I’m grateful to CodTech IT Solutions for assigning such a practical and industry-relevant problem. It encouraged hands-on learning and helped solidify my confidence in Python scripting for data handling and reporting.













