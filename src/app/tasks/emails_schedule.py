from src.app import celery_app as app
from datetime import datetime

@app.task
def send_email_task(subject, to, body, content_type):
    # Lógica simplificada de envio
    print(f"[{datetime.now()}] Enviando e-mail para {to} com assunto '{subject}'")
    # Aqui você pode usar smtplib ou outro serviço
    return {"success": True, "to": to}