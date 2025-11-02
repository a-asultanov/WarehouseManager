from extensions import db

class WarehouseStock(db.Model):
    __tablename__ = "warehouse_stocks"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), unique=True, nullable=False)
    quantity = db.Column(db.Integer, default=0)

    product = db.relationship("Product", back_populates="stock")

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity
        }