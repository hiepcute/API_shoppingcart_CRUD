from app import *
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
             # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Users.query.filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})
        returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorator
