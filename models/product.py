from extensions import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"), nullable=False)

    orders = db.relationship("PurchaseOrder", backref="product", cascade="all, delete")
    stock = db.relationship("WarehouseStock", uselist=False, back_populates="product", cascade="all, delete")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "supplier_id": self.supplier_id
        }