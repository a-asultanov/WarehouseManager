from flask import Blueprint, request, jsonify
from extensions import db
from models.purchase_order import PurchaseOrder
from models.warehouse_stock import WarehouseStock

order_bp = Blueprint("order_bp", __name__)

# GET all orders
@order_bp.route("/orders", methods=["GET"])
def get_orders():
    orders = PurchaseOrder.query.all()
    return jsonify([o.to_dict() for o in orders])

# POST new order
@order_bp.route("/orders", methods=["POST"])
def add_order():
    data = request.json
    new_order = PurchaseOrder(
        supplier_id=data.get("supplier_id"),
        product_id=data.get("product_id"),
        quantity=data.get("quantity"),
        status=data.get("status", "pending")
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

# PUT update order
@order_bp.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    order = PurchaseOrder.query.get_or_404(order_id)
    data = request.json
    old_status = order.status

    order.status = data.get("status", order.status)
    order.quantity = data.get("quantity", order.quantity)
    db.session.commit()

    # Обновляем склад
    if order.status == "received" and old_status != "received":
        stock = WarehouseStock.query.filter_by(product_id=order.product_id).first()
        if not stock:
            stock = WarehouseStock(product_id=order.product_id, quantity=0)
            db.session.add(stock)
        stock.quantity += order.quantity
        db.session.commit()

    return jsonify(order.to_dict())

# DELETE order
@order_bp.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = PurchaseOrder.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": f"Order {order_id} deleted"})