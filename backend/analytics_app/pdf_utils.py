from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def generate_pdf(dataset):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Chemical Equipment Report", styles['Title']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>Dataset Name:</b> {dataset.name}", styles['Normal']))
    elements.append(Paragraph(f"<b>Uploaded At:</b> {dataset.uploaded_at}", styles['Normal']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Summary</b>", styles['Heading2']))
    elements.append(Spacer(1, 8))

    summary = dataset.summary
    elements.append(Paragraph(f"Total Equipment Count: {summary['total_count']}", styles['Normal']))
    elements.append(Paragraph(f"Average Flowrate: {summary['average_flowrate']}", styles['Normal']))
    elements.append(Paragraph(f"Average Pressure: {summary['average_pressure']}", styles['Normal']))
    elements.append(Paragraph(f"Average Temperature: {summary['average_temperature']}", styles['Normal']))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph("<b>Equipment Type Distribution</b>", styles['Heading3']))
    for k, v in summary['type_distribution'].items():
        elements.append(Paragraph(f"{k}: {v}", styles['Normal']))

    doc.build(elements)
    buffer.seek(0)
    return buffer
