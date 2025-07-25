# E-mail Sender REST API

#### Emails

| Método | URL                                         | Descrição                                         |
| ------ | ------------------------------------------- | ------------------------------------------------- |
| POST   | `/api/emails/send`                          | Enviar e-mail                                     |
| POST   | `/api/emails/schedule`                      | Agendar envio de e-mail                           |
| GET    | `/api/emails/schedule`                      | Listar e-mails agendados ou enviados              |
| DELETE | `/api/emails/schedule/<string:schedule_id>` | Cancelar envio de e-mail agendado                 |
| GET    | `/api/emails/<string:email_id>`             | Buscar e-mail específico                          |


