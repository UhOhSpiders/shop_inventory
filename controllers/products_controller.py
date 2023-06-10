from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.product import Product
import repositories.merchant_repository as merchant_repository
import repositories.product_repository as product_repository
import pdb

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/")
def products():
    # pdb.set_trace()
    products = product_repository.select_all()
    # merchants = merchant_repository.select_all()
    return render_template("/index.html", products = products)