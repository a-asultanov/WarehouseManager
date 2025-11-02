from extensions import db

class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(200))

    products = db.relationship("Product", backref="supplier", cascade="all, delete")
    orders = db.relationship("PurchaseOrder", backref="supplier", cascade="all, delete")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "contact_info": self.contact_info
        }

    