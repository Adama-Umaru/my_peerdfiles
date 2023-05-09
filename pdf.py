#!/usr/bin/env python

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Request for title
title = input("Enter title: ")

# Create a new PDF document
pdf = canvas.Canvas("document.pdf", pagesize=letter)
pdf.setFillColorRGB(0 ,1, 0)
pdf.rect(5,5,652,792, fill=1)
pdf.setTitle("Background")

# Draw the title with a red background
pdf.setFillColorRGB(1, 0, 0)
pdf.setFont("Helvetica-Bold", 24)
pdf.drawCentredString(300, 750, title)

# Request for subject
subject = input("Enter subject: ")

# Draw the subject with a red background
pdf.setFillColorRGB(1, 0, 0)
pdf.setFont("Helvetica", 18)
pdf.drawCentredString(300, 700, subject)

# Generate the body with a green background
pdf.setFillColorRGB(0, 0, 0)
pdf.setFont("Helvetica", 12)
pdf.drawString(50, 650, "This is the body of the document with a green background.")

# Save the PDF document
pdf.save()
