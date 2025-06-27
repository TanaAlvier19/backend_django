from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from app.models import Assiduidade
from datetime import datetime

def gerar_pdf_assiduidade():
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        p.setFont("Helvetica", 14)
        p.drawString(100, height - 50, "Relatório de Assiduidade Apagada")

        p.setFont("Helvetica", 10)
        y = height - 80

        registros = Assiduidade.objects.all()

        for assiduidade in registros:
            texto = f"Funcionário: {assiduidade.funcionario.nome} | Entrada: {assiduidade.entrada} | Saída: {assiduidade.saida} | Data: {assiduidade.data}"
            p.drawString(50, y, texto)
            y -= 20
        if y < 50:
            p.showPage()
            p.setFont("Helvetica", 10)
            y = height - 50

        p.save()
        buffer.seek(0)
        return buffer

