from flask import Blueprint, jsonify
from models.warehouse_stock import WarehouseStock

stock_bp = Blueprint("stock_bp", __name__)

@stock_bp.route("/stocks", methods=["GET"])
def get_stocks():
    stocks = WarehouseStock.query.all()
    return jsonify([s.to_dict() for s in stocks])