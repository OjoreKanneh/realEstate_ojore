from App.database import db  # Make sure to import the db instance from your application

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100))
    sender_email = db.Column(db.String(100))
    message_body = db.Column(db.Text)
    property_id = db.Column(db.Integer, db.ForeignKey('Property.id'))
    created_at = db.Column(db.DateTime)
    
    def __init__(self, sender_name, sender_email, message_body, property_id, created_at=None):
        self.sender_name = sender_name
        self.sender_email = sender_email
        self.message_body = message_body
        self.property_id = property_id
        self.created_at = created_at

    def get_json(self):
        return {
            'id': self.id,
            'sender_name': self.sender_name,
            'sender_email': self.sender_email,
            'message_body': self.message_body,
            'property_id': self.property_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    # Additional methods and properties as needed

    def __repr__(self):
        return f"<Message {self.id}>"






