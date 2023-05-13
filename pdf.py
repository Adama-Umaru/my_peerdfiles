import fpdf
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a new PDF document
pdf = canvas.Canvas("example.pdf", pagesize=letter)

# Request for title
# title = input("Enter title: ")

# Set the background color of the header
header_color = colors.HexColor("#ff0000")
pdf.setFillColor(header_color)
pdf.rect(0, letter[1]-50, letter[0], 50, fill=True, stroke=False)

# Set the background color of the body
body_color = colors.HexColor("#00FF00")
pdf.setFillColor(body_color)
pdf.rect(0, 0, letter[0], letter[1]-50, fill=True, stroke=False)

# Add text to the header
pdf.setFont("Helvetica-Bold", 14)
pdf.setFillColorRGB(0, 0, 0)
pdf.drawString(36, letter[1]-25, "Cohort 5")

# Request for subject
# subject = input("Enter subject: ")

# Add text to the subject
pdf.setFont("Helvetica-Bold", 14)
pdf.setFillColorRGB(0, 0, 0)
pdf.drawString(36, letter[1]-45, "Assignment")

# Add text to the body
pdf.setFont("Helvetica", 12)
pdf.setFillColorRGB(0, 0, 0)
pdf.drawString(36, letter[1]-75, "Body text")

# Save the PDF document
pdf.save()



