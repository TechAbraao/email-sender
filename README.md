# E-mail Sender REST API
### Technologies
<section align="left">
    <img alt="Static Badge" src="https://img.shields.io/badge/Python-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Flask-grey?style=flat&logo=Flask">
    <img alt="Static Badge" src="https://img.shields.io/badge/Smtplib-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Celery-grey?style=flat&logo=Celery">
    <img alt="Static Badge" src="https://img.shields.io/badge/Pytest-grey?style=flat&logo=PyTest">
    <img alt="Static Badge" src="https://img.shields.io/badge/Marshmallow-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/SQLALchemy-grey?style=flat&logo=SQLAlchemy">
    <img alt="Static Badge" src="https://img.shields.io/badge/Docker-grey?style=flat&logo=Docker">
    <img alt="Static Badge" src="https://img.shields.io/badge/Redis-grey?style=flat&logo=Redis">
    <img alt="Static Badge" src="https://img.shields.io/badge/PostgreSQL-grey?style=flat&logo=PostgreSQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/PgAdmin-grey?style=flat&logo=PostgreSQL">
    <img alt="Static Badge" src="https://img.shields.io/badge/RabbitMQ-grey?style=flat&logo=RabbitMQ">
    <img alt="Static Badge" src="https://img.shields.io/badge/Postman-grey?style=flat&logo=Postman">
</section>

#### Emails

| Método | URL                                         | Descrição                                         |
| ------ | ------------------------------------------- | ------------------------------------------------- |
| POST   | `/api/emails/send`                          | Enviar e-mail                                     |
| POST   | `/api/emails/schedule`                      | Agendar envio de e-mail                           |
| GET    | `/api/emails/schedule`                      | Listar e-mails agendados ou enviados              |
| DELETE | `/api/emails/schedule/<string:schedule_id>` | Cancelar envio de e-mail agendado                 |
| GET    | `/api/emails/<string:email_id>`             | Buscar e-mail específico                          |


