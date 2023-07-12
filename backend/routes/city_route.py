import sys
sys.path.append('data_access')
from flask import Blueprint, jsonify
from city_dao import fetch_city_info

search_route = Blueprint('search', __name__)

@search_route.route('/api/search/<city_name>', methods=['GET'])
def search_city(city_name):
    city_data = fetch_city_info(city_name)
    return jsonify(city_data)
