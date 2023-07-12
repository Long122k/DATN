import sys
from flask import Blueprint, jsonify
# from business_logic.hotel_logic import HotelLogic
from data_access.hotel_dao import HotelDao

sys.path.append('database')
from cassandra_connector import create_cassandra_session

sys.path.append('business_logic')
from hotel_logic import HotelLogic


hotel_route = Blueprint('hotel', __name__)

@hotel_route.route('/api/dashboard/hotels/<city_name>', methods=['GET'])
def get_hotels(city_name):
    session = create_cassandra_session()
    hotel_dao = HotelDao(session)
    hotels = hotel_dao.fetch_hotels_by_city(city_name)
    return jsonify(hotels)

# x = create_cassandra_session()
# # a = HotelLogic(x)
# print(get_hotels("Quang Nam"))