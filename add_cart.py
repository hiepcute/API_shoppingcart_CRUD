from app import *
@app.route('/cart', methods=['POST'])
@token_required
def create_cart(current_user):
    data = request.get_json()

    new_cart = cart(name=data['name'], Author=data['Author'], image=data['image'],
                      prize=data['prize'], user_id=current_user.id)
    db.session.add(new_cart)
    db.session.commit()
    return jsonify({'message': 'new cart create in to shopping cart'})