# Import necessary libraries
from fpdf import FPDF # For generating PDF reports
import pandas as pd # For reading and handling CSV data
from datetime import datetime # To add current date and time to the report

# Read the CSV file containing library lending data
df = pd.read_csv("Library_Lending_Data.csv")

# Calculate Summary Statistics
total_books = df["Book ID"].count() # Count total number of books 
returned = df[df["Status"] == "Returned"].shape[0] # Count how many books have been returned
borrowed = df[df["Status"] == "Borrowed"].shape[0] # Count how many books are still borrowed

# Initialize PDF
pdf = FPDF()
pdf.add_page() # Add the first page
pdf.set_auto_page_break(auto=True, margin=15) # Automatically handle page breaks

# Report Title
pdf.set_font("Arial", 'B', 16)  # Set font to Arial Bold, size 16
pdf.set_text_color(0, 70, 140)  # Set text color to blue
pdf.cell(200, 10, "Library Book Lending Report", ln=True, align='C') # Centered title

# Report Date
pdf.set_font("Arial", '', 12) # Normal font for subtitle
pdf.set_text_color(50, 50, 50) # Gray text color

# This line places a centered timestamp in the PDF
pdf.cell(200, 10, f"Report Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
pdf.ln(10)

# Table Headers
pdf.set_font("Arial", 'B', 11) # Bold headers
pdf.set_fill_color (190, 150, 255) # Set header colour to lavender
headers = ['Book ID', 'Title', 'Borrower', 'Borrowed', 'Returned', 'Status']  # Column names
widths = [20, 55, 35, 28, 28, 24] # Custom column widths

# Print each header with formatting
for i in range(len(headers)):
    pdf.cell(widths[i], 10, headers[i], 1, 0, 'C', True)
pdf.ln()

# Table Rows
pdf.set_font("Arial", '', 10) # Regular font for table content

# Loop through each row in the DataFrame and write it to the PDF
for _, row in df.iterrows():  
    pdf.cell(widths[0], 10, str(row['Book ID']), 1)
    pdf.cell(widths[1], 10, str(row['Title'])[:32], 1)  # Limit title to 32 characters
    pdf.cell(widths[2], 10, str(row['Borrower']), 1)
    pdf.cell(widths[3], 10, str(row['Date Borrowed']), 1)
    pdf.cell(widths[4], 10, str(row['Date Returned']) if pd.notna(row['Date Returned']) else '-', 1)
    pdf.cell(widths[5], 10, str(row['Status']), 1)
    pdf.ln()

# Summary Section
pdf.ln(8)  # Add space before summary
pdf.set_font("Arial", 'B', 12)
pdf.set_text_color(0, 70, 140)  # blue for summary heading
pdf.cell(200, 10, "Summary", ln=True)

# Set normal font and black text for summary content
pdf.set_font("Arial", '', 11)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 8, f" Total Books Tracked: {total_books}", ln=True)
pdf.cell(0, 8, f" Books Returned: {returned}", ln=True)
pdf.cell(0, 8, f" Books Still Borrowed: {borrowed}", ln=True)

# Footer
pdf.ln(10)
pdf.set_font("Arial", 'I', 10) # Italic font
pdf.set_text_color(100, 100, 100) # Gray color for footer
pdf.multi_cell(0, 8, "Note: This report was automatically generated for monitoring library book lending activity.")

# Save the PDF
pdf.output("library_book_report.pdf")

# Confirmation in the terminal
print("Report generated as library_book_report.pdf")

