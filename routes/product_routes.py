from flask import Blueprint, request, jsonify
from extensions import db
from models.product import Product

product_bp = Blueprint("product_bp", __name__)

@product_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])

@product_bp.route("/products", methods=["POST"])
def add_product():
    data = request.json
    new_product = Product(
        name=data.get("name"),
        price=data.get("price"),
        supplier_id=data.get("supplier_id")
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@product_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.supplier_id = data.get("supplier_id", product.supplier_id)
    db.session.commit()
    return jsonify(product.to_dict())

@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": f"Product {product_id} deleted"})