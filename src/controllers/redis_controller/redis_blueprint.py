from flask import request, jsonify
from repositories.redis_repository import set_value, get_value

#redis_blueprint = Blueprint('redis', __name__)

'''
@redis_blueprint.route('/set', methods=['POST'])
def set_redis_value():
    key = request.json.get('key')
    value = request.json.get('value')
    if not key or not value:
        return jsonify({'error': 'Both key and value are required'}), 400
    set_value(key, value)
    return jsonify({'message': 'Value set successfully'})

@redis_blueprint.route('/get', methods=['GET'])
def get_redis_value():
    key = request.args.get('key')
    if not key:
        return jsonify({'error': 'Key is required'}), 400
    value = get_value(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    return jsonify({'key': key, 'value': value.decode('utf-8')})
'''

def set_redis_value(key, value):
    if not key or not value:
        return jsonify({'error': 'Both key and value are required'}), 400
    set_value(key, value)
    return jsonify({'message': 'Value set successfully'})


def get_redis_value():
    key = request.args.get('key')
    if not key:
        return jsonify({'error': 'Key is required'}), 400
    value = get_value(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    return jsonify({'key': key, 'value': value.decode('utf-8')})

