from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
def process(srcfname,destfname,msg):
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(10, 100, msg)
    can.save()
    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    path=srcfname+".pdf"
    existing_pdf = PdfFileReader(open(path, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    for page1 in range(0, existing_pdf.numPages):
        page = existing_pdf.getPage(page1)
        output.addPage(page)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    path1=srcfname+"final.pdf"
    # finally, write "output" to a real file
    outputStream = open(path1, "wb")
    output.write(outputStream)
    outputStream.close()

#process("demo","out","hello this is eswaran")
