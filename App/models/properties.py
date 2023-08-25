from App.database import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2))
    area = db.Column(db.Float)
    beds = db.Column(db.Integer)
    baths = db.Column(db.Integer)
    location = db.Column(db.String(200))
    property_type = db.Column(db.String(100))
    is_for_sale = db.Column(db.Boolean)
    is_for_rent = db.Column(db.Boolean)
    agent_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    photo = db.Column(db.String(255))


    def __init__(self, title, description, price, area, beds, baths, location,
        property_type, is_for_sale, is_for_rent, agent_id, photo):
        self.title = title
        self.description = description
        self.price = price
        self.area = area
        self.beds = beds
        self.baths = baths
        self.location = location
        self.property_type = property_type
        self.is_for_sale = is_for_sale
        self.is_for_rent = is_for_rent
        self.agent_id = agent_id
        self.photo = photo

    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'price': str(self.price),
            'area': self.area,
            'beds': self.beds,
            'baths': self.baths,
            'location': self.location,
            'property_type': self.property_type,
            'is_for_sale': self.is_for_sale,
            'is_for_rent': self.is_for_rent,
            'agent_id': self.agent_id,
            'photo': self.photo
        }