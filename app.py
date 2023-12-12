from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Furniture(db.Model):
    furniture_id = db.Column(db.Integer, primary_key=True)
    furniture_name = db.Column(db.String(200), nullable=False)
    furniture_type = db.Column(db.String(100))
    furniture_weight = db.Column(db.Float)
    furniture_price = db.Column(db.Float)

    def __repr__(self):
        return '<Furniture %r' % self.id
    
class Shoes(db.Model):
    shoes_id = db.Column(db.Integer, primary_key=True)
    shoes_name = db.Column(db.String(200), nullable=False)
    shoes_brand = db.Column(db.String(100))
    shoes_size = db.Column(db.Integer)
    shoes_gender = db.Column(db.String(50))
    shoes_color = db.Column(db.String(50))
    shoes_price = db.Column(db.Float)

    def __repr__(self):
        return '<Shoes %r>' % self.id
    
class Appliances(db.Model):
    appliance_id = db.Column(db.Integer, primary_key=True)
    appliance_name = db.Column(db.String(200), nullable=False)
    appliance_type = db.Column(db.String(100))
    appliance_brand = db.Column(db.String(100))
    appliance_weight = db.Column(db.Float)
    appliance_voltage = db.Column(db.Integer)
    appliance_price = db.Column(db.Float)
    
    def __repr__(self):
        return '<Appliances %r>' % self.id

class Stationery(db.Model):
    stationery_id = db.Column(db.Integer, primary_key=True)
    stationery_name = db.Column(db.String(200), nullable=False)
    stationery_brand = db.Column(db.String(100))
    stationery_type = db.Column(db.String(100))
    stationery_quantity = db.Column(db.Integer)
    stationery_price = db.Column(db.Float)

    def __repr__(self):
        return '<Stationery %r>' % self.id

def create_view(): # VIEW
    with app.app_context():
        view_query = text("""
        CREATE VIEW IF NOT EXISTS category_summary AS 
        SELECT 'Furniture' AS category, COUNT(*) AS count FROM furniture
        UNION ALL
        SELECT 'Shoes', COUNT(*) FROM shoes
        UNION ALL
        SELECT 'Appliances', COUNT(*) FROM appliances
        UNION ALL
        SELECT 'Stationery', COUNT(*) FROM stationery;
        """)
        db.session.execute(view_query)
        db.session.commit()


    
@app.route('/')
def index():
    result = db.session.execute(text('SELECT * FROM category_summary'))
    categories = [{'category': row[0], 'count': row[1]} for row in result]
    return render_template('index.html', categories=categories)
    
@app.route('/furniture', methods=['POST', 'GET'])
def furniture():
    if request.method == 'POST':
        furniture_name = request.form.get('furniture_name')
        furniture_type = request.form.get('furniture_type')
        furniture_weight = request.form.get('furniture_weight')
        furniture_price = request.form.get('furniture_price')
        
        if furniture_name and furniture_type and furniture_weight and furniture_price:
            try:
                new_furniture = Furniture(
                    furniture_name=furniture_name,
                    furniture_type=furniture_type,
                    furniture_weight=float(furniture_weight),
                    furniture_price=float(furniture_price)
                )
                db.session.add(new_furniture)
                db.session.commit()
                return redirect('/furniture')
            except Exception as e:
                return f'An error occurred when adding the furniture: {e}'
    
    furniture_items = Furniture.query.all()
    return render_template('furniture.html', furniture_items=furniture_items)
    
@app.route('/shoes', methods=['POST', 'GET'])
def shoes():
    if request.method == 'POST':
        shoes_name = request.form.get('shoes_name')
        shoes_brand = request.form.get('shoes_brand')
        shoes_size = request.form.get('shoes_size')
        shoes_gender = request.form.get('shoes_gender')
        shoes_color = request.form.get('shoes_color')
        shoes_price = request.form.get('shoes_price')
        
        if shoes_name and shoes_brand and shoes_size and shoes_gender and shoes_color and shoes_price:
            try:
                new_shoes = Shoes(
                    shoes_name=shoes_name,
                    shoes_brand=shoes_brand,
                    shoes_size=int(shoes_size),
                    shoes_gender=shoes_gender,
                    shoes_color=shoes_color,
                    shoes_price=float(shoes_price)
                )
                db.session.add(new_shoes)
                db.session.commit()
                return redirect('/shoes')
            except Exception as e:
                return f'An error occurred when adding the shoes: {e}'
    
    shoes_items = Shoes.query.all()
    return render_template('shoes.html', shoes_items=shoes_items)

    
@app.route('/appliances', methods=['POST', 'GET'])
def appliances():
    if request.method == 'POST':
        appliance_name = request.form.get('appliance_name')
        appliance_type = request.form.get('appliance_type')
        appliance_brand = request.form.get('appliance_brand')
        appliance_weight = request.form.get('appliance_weight')
        appliance_voltage = request.form.get('appliance_voltage')
        appliance_price = request.form.get('appliance_price')
        
        if appliance_name and appliance_type and appliance_brand and appliance_weight and appliance_voltage and appliance_price:
            try:
                new_appliance = Appliances(
                    appliance_name=appliance_name,
                    appliance_type=appliance_type,
                    appliance_brand=appliance_brand,
                    appliance_weight=float(appliance_weight),
                    appliance_voltage=int(appliance_voltage),
                    appliance_price=float(appliance_price)
                )
                db.session.add(new_appliance)
                db.session.commit()
                return redirect('/appliances')
            except Exception as e:
                return f'An error occurred when adding the appliance: {e}'
    
    appliances_items = Appliances.query.all()
    return render_template('appliances.html', appliances_items=appliances_items)

    
@app.route('/stationery', methods=['POST', 'GET'])
def stationery():
    if request.method == 'POST':
        stationery_name = request.form.get('stationery_name')
        stationery_brand = request.form.get('stationery_brand')
        stationery_type = request.form.get('stationery_type')
        stationery_quantity = request.form.get('stationery_quantity')
        stationery_price = request.form.get('stationery_price')
        
        if stationery_name and stationery_brand and stationery_type and stationery_quantity and stationery_price:
            try:
                new_stationery = Stationery(
                    stationery_name=stationery_name,
                    stationery_brand=stationery_brand,
                    stationery_type=stationery_type,
                    stationery_quantity=int(stationery_quantity),
                    stationery_price=float(stationery_price)
                )
                db.session.add(new_stationery)
                db.session.commit()
                return redirect('/stationery')
            except Exception as e:
                return f'An error occurred when adding the stationery: {e}'
    
    stationery_items = Stationery.query.all()
    return render_template('stationery.html', stationery_items=stationery_items)

    
def get_model_by_category(category):
    if category == 'furniture':
        return Furniture
    elif category == 'shoes':
        return Shoes
    elif category == 'appliances':
        return Appliances
    elif category == 'stationery':
        return Stationery
    else:
        return None

@app.route('/delete/<category>/<int:id>')
def delete(category, id):
    model = get_model_by_category(category)
    if model is None:
        return 'Invalid category'

    item_to_delete = model.query.get_or_404(id)
    
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that item'
    
@app.route('/update/furniture/<int:id>', methods=['GET', 'POST'])
def furnitureUpdate(id):
    furniture_item = Furniture.query.get_or_404(id)

    if request.method == 'POST':
        furniture_item.furniture_name = request.form.get('furniture_name')
        furniture_item.furniture_type = request.form.get('furniture_type')
        furniture_item.furniture_weight = float(request.form.get('furniture_weight', 0))
        furniture_item.furniture_price = float(request.form.get('furniture_price', 0))

        try:
            db.session.commit()
            return redirect('/furniture')
        except Exception as e:
            return f'There was an issue updating the furniture item: {e}'

    else:
        return render_template('furnitureupdate.html', item=furniture_item)
    
@app.route('/update/shoes/<int:id>', methods=['GET', 'POST'])
def shoesUpdate(id):
    shoes_item = Shoes.query.get_or_404(id)

    if request.method == 'POST':
        shoes_item.shoes_name = request.form.get('shoes_name')
        shoes_item.shoes_brand = request.form.get('shoes_brand')
        shoes_item.shoes_size = int(request.form.get('shoes_size', 0))
        shoes_item.shoes_gender = request.form.get('shoes_gender')
        shoes_item.shoes_color = request.form.get('shoes_color')
        shoes_item.shoes_price = float(request.form.get('shoes_price', 0))

        try:
            db.session.commit()
            return redirect('/shoes')
        except Exception as e:
            return f'There was an issue updating the shoes item: {e}'

    else:
        return render_template('shoesupdate.html', item=shoes_item)
    
@app.route('/update/appliances/<int:id>', methods=['GET', 'POST'])
def appliancesUpdate(id):
    appliance_item = Appliances.query.get_or_404(id)

    if request.method == 'POST':
        appliance_item.appliance_name = request.form.get('appliance_name')
        appliance_item.appliance_type = request.form.get('appliance_type')
        appliance_item.appliance_brand = request.form.get('appliance_brand')
        appliance_item.appliance_weight = float(request.form.get('appliance_weight', 0))
        appliance_item.appliance_voltage = int(request.form.get('appliance_voltage', 0))
        appliance_item.appliance_price = float(request.form.get('appliance_price', 0))

        try:
            db.session.commit()
            return redirect('/appliances')
        except Exception as e:
            return f'There was an issue updating the appliance item: {e}'

    else:
        return render_template('appliancesupdate.html', item=appliance_item)
    
@app.route('/update/stationery/<int:id>', methods=['GET', 'POST'])
def stationeryUpdate(id):
    stationery_item = Stationery.query.get_or_404(id)

    if request.method == 'POST':
        stationery_item.stationery_name = request.form.get('stationery_name')
        stationery_item.stationery_brand = request.form.get('stationery_brand')
        stationery_item.stationery_type = request.form.get('stationery_type')
        stationery_item.stationery_quantity = int(request.form.get('stationery_quantity', 0))
        stationery_item.stationery_price = float(request.form.get('stationery_price', 0))

        try:
            db.session.commit()
            return redirect('/stationery')
        except Exception as e:
            return f'There was an issue updating the stationery item: {e}'

    else:
        return render_template('stationeryupdate.html', item=stationery_item)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
        create_view()    
    app.run(debug=True)
