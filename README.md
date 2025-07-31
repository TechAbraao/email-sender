# E-mail Sender REST API
### Technologies
<section align="left">
    <img alt="Static Badge" src="https://img.shields.io/badge/Python-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/Flask-grey?style=flat&logo=Flask">
    <img alt="Static Badge" src="https://img.shields.io/badge/Celery-grey?style=flat&logo=Celery">
    <img alt="Static Badge" src="https://img.shields.io/badge/smtplib-grey?style=flat&logo=Python">
    <img alt="Static Badge" src="https://img.shields.io/badge/kombu-grey?style=flat&logo=Python">
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

| Method | URL                                          |     Description                |
| ------ | -------------------------------------------- | ------------------------------ |
| GET    | `/api/emails`                                | Get all emails                 |
| GET    | `/api/emails?status=<status>`                | Get all emails with status     |
| GET    | `/api/emails/<string:uuid_email>`            | Retrieve specific email        |
| POST   | `/api/emails/send`                           | Send email                     |
| POST   | `/api/emails/schedule`                       | Schedule email sending         |
| DELETE | `/api/emails/schedule/<string:uuid_schedule>`| Cancel scheduled email sending |

#### To start Celery with the Flower UI:
```bash
# Start the Celery App
celery -A src.app.celery_app:celery_app worker --loglevel=info
```
In another terminal, I also ran:
```bash
# Now, start the Flower UI
celery -A src.app.celery_app.celery_app flower
```
Consume the message and send the emailThis messaging architecture uses Flask as the application framework, RabbitMQ as the message broker, and Celery as the worker queue for processing asynchronous tasks like sending emails and schedules.
#### About messaging architecture

```mermaid
graph LR
  Producer["Producer:<br><b>Flask Application</b>"] -->|Message| Exchange["Exchange:<br><b>RabbitMQ</b>"]
  Exchange -->|Route the message| Queue["Queue:<br><b>RabbitMQ</b>"]
  Queue -->|Message| Worker["Worker:<br><b>Celery Application</b>"]

```
