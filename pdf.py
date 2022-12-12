import pdfkit
from datetime import datetime
import jinja2

data = {}
data['nombre'] = 'Milca Toledo'
data['hora'] = '60'
data['fecha'] = datetime.now().strftime('%m/%d/%Y')

contex = {'data': data}
templade_loader = jinja2.FileSystemLoader('D:/Dennisse/pythonProject')
templade_env = jinja2.Environment(loader=templade_loader)

html_templade = 'certificado.html'
templade = templade_env.get_templade(html_templade)
output_text = templade.render(contex)
path_wkthmltopdf = b'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

conifg = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
output_pdf = 'certificado.pdf'
pdfkit.from_string(output_text, configuration=conifg)