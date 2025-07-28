from marshmallow import Schema, fields
from marshmallow.validate import Length

class EmailBody(Schema):
    """ Schema for the body of an e-mail """
    subject = fields.Str(required=True, validate=Length(min=6, max=40), metadata={"description": "Subject of the e-mail"})
    body = fields.Str(required=True, validate=Length(min=20, max=2000), metadata={"description": "Body content of the e-mail"})
    content_type = fields.Str(required=True, validate=lambda x: x in ["text/plain", "text/html"], metadata={"description": "MIME type of the body: 'text/plain' or 'text/html'"})
    to = fields.Email(required=True, metadata={"description": "Recipient's e-mail address"})

    def to_dict(self):
        """ Convert the schema to a dictionary representation """
        return {
            "subject": self.subject,
            "body": self.body,
            "content_type": self.content_type,
            "to": self.to,
        }