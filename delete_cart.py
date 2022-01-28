from app import *
@app.route('/carts/<cart_id>', methods=['DELETE'])
@token_required
def delete_cart(current_user, cart_id):
    cart = cart.query.filter_by(id=cart_id, user_id=current_user.id).first()
    if not cart:
        return jsonify({'message': 'cart does not exist'})

    db.session.delete(cart)
    db.session.commit()
    return jsonify({'message': 'cart deleted'})


if __name__ == '__main__':
    app.run(debug=True)