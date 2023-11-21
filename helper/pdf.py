from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image

def create_real_estate_pdf(file_name,info):
    # Create a PDF document
    pdf_filename = f"{file_name}.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Define styles for the document
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['BodyText'],
        spaceAfter=12,
    )

    # Create content for the PDF
    content = []

    # Title
    # title_text = f"Ficha - {info['property_type']}"
    title_text = f"Ficha - {info['address']}"
    content.append(Paragraph(title_text, title_style))

    #Add agency info
    content.append(Paragraph(f"Erlich propiedades", body_style))
    img = Image('logo.png', width=75, height=100)
    img.hAlign = 'LEFT'
    content.append(img)
    # Price, Address, Area
    content.append(Paragraph(f"Precio: U$D{info['price']}", body_style))
    content.append(Paragraph(f"Tipo de propiedad: {info['property_type']}", body_style))
    content.append(Paragraph(f"Metros: {info['meters']}", body_style))

    # Images
    for img_url in info['imgs']:
        img = Image(img_url, width=300, height=200)
        content.append(img)

    # Extra Information
    content.append(Paragraph("Informacion basica:", title_style))
    for extra_info in info['Extra_information']:
        content.append(Paragraph(f"- {extra_info}", body_style))

    # Description
    content.append(Paragraph("Descripcion:", title_style))
    content.append(Paragraph(info['description'], body_style))

    # Location
    content.append(Paragraph("Ubicacion:", title_style))
    location_img = Image(info['location'], width=400, height=300)
    content.append(location_img)

    # Build the PDF document
    document.build(content)

    print(f"PDF created successfully: {pdf_filename}")