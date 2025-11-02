from flask import Blueprint, request, jsonify
from extensions import db
from models.supplier import Supplier

supplier_bp = Blueprint("supplier_bp", __name__)

# GET all suppliers
@supplier_bp.route("/suppliers", methods=["GET"])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([s.to_dict() for s in suppliers])

# POST new supplier
@supplier_bp.route("/suppliers", methods=["POST"])
def add_supplier():
    data = request.json
    new_supplier = Supplier(
        name=data.get("name"),
        contact_info=data.get("contact_info")
    )
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify(new_supplier.to_dict()), 201

# PUT update supplier
@supplier_bp.route("/suppliers/<int:supplier_id>", methods=["PUT"])
def update_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    data = request.json
    supplier.name = data.get("name", supplier.name)
    supplier.contact_info = data.get("contact_info", supplier.contact_info)
    db.session.commit()
    return jsonify(supplier.to_dict())

# DELETE supplier
@supplier_bp.route("/suppliers/<int:supplier_id>", methods=["DELETE"])
def delete_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({"message": f"Supplier {supplier_id} deleted"})