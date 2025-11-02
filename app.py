from flask import Flask, jsonify
from config import Config
from extensions import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from routes.supplier_routes import supplier_bp
app.register_blueprint(supplier_bp, url_prefix="/api")

from routes.product_routes import product_bp
app.register_blueprint(product_bp, url_prefix="/api")

from routes.order_routes import order_bp
app.register_blueprint(order_bp, url_prefix="/api")

from routes.stock_routes import stock_bp
app.register_blueprint(stock_bp, url_prefix="/api")


@app.route("/api/status", methods=["GET"])
def status():
    """Простой health-check эндпоинт"""
    return jsonify({"status": "ok", "message": "Warehouse API is running"})


#Админка дашборд
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms import SelectField
from models.supplier import Supplier
from models.product import Product
from models.purchase_order import PurchaseOrder
from models.warehouse_stock import WarehouseStock

class PurchaseOrderAdmin(ModelView):
    form_columns = ["supplier_id", "product_id", "quantity", "status"]

    def scaffold_form(self):
        form_class = super(PurchaseOrderAdmin, self).scaffold_form()
        form_class.status = SelectField(
            "Статус",
            choices=[
                ("pending", "Ожидается"),
                ("received", "Получен"),
                ("canceled", "Отменён")
            ]
        )
        return form_class

    def on_model_change(self, form, model, is_created):
        if model.status == "received":
            stock = WarehouseStock.query.filter_by(product_id=model.product_id).first()
            if not stock:
                stock = WarehouseStock(product_id=model.product_id, quantity=0)
                self.session.add(stock)
            stock.quantity += model.quantity
            self.session.commit()

admin = Admin()
admin.init_app(app)
admin.name = "Warehouse Manager"
admin.template_mode = "bootstrap4"

admin.add_view(ModelView(Supplier, db.session, name="Поставщики"))
admin.add_view(ModelView(Product, db.session, name="Товары"))
admin.add_view(PurchaseOrderAdmin(PurchaseOrder, db.session, name="Заказы"))
admin.add_view(ModelView(WarehouseStock, db.session, name="Остатки"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)