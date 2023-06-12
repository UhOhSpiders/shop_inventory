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

@products_blueprint.route("/new_product")
def new_product():
    merchants = merchant_repository.select_all()
    return render_template("/products/new.html", merchants = merchants)

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form ['buying_cost']
    selling_cost = request.form ['selling_cost']
    category = request.form ['category']
    min_stock_level = request.form ['min_stock_level']
    merchant_id = request.form ['merchant_id']
    merchant = merchant_repository.select(merchant_id)
    product = Product(product_name, product_description, stock_quantity, buying_cost, selling_cost, category, min_stock_level, merchant)
    product_repository.save(product)
    return redirect("/")

@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('product_details.html', product = product)

@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    merchants = merchant_repository.select_all()
    return render_template('products/edit.html', product = product, merchants = merchants)

@products_blueprint.route("/products/update/<id>", methods=['POST'])
def update_product(id):
    # pdb.set_trace()
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form ['buying_cost']
    selling_cost = request.form ['selling_cost']
    category = request.form ['category']
    min_stock_level = request.form ['min_stock_level']
    merchant = merchant_repository.select(request.form ['merchant_id']) 
    product = Product(product_name, product_description, stock_quantity, buying_cost, selling_cost, category, min_stock_level, merchant, id)
    product_repository.update(product)
    return redirect("/")

@products_blueprint.route("/products/delete/<id>", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/")

@products_blueprint.route("/merchants", methods=['POST'])
def create_merchant():
    # pdb.set_trace()
    merchant_name = request.form['merchant_name']
    ethics = request.form['ethics']
    morals = request.form['morals']
    merchant = Merchant(merchant_name, ethics, morals)
    merchant_repository.save(merchant)
    return redirect("/")

@products_blueprint.route("/new_merchant")
def new_merchant():
    return render_template("merchants/new.html")

@products_blueprint.route("/merchants/<id>", methods=['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchant_details.html', merchant = merchant)

@products_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant = merchant)

@products_blueprint.route("/merchants/update/<id>", methods=['POST'])
def update_merchant(id):
    # pdb.set_trace()
    merchant_name = request.form['merchant_name']
    ethics = request.form['ethics']
    morals = request.form['morals'] 
    merchant = Merchant(merchant_name, morals, ethics, id)
    product_repository.update(merchant)
    return redirect("/")