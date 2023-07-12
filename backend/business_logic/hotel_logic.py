import sys
sys.path.append('data_access')
from hotel_dao import HotelDao
# sys.path.append('database')
# from cassandra_connector import create_cassandra_session

class HotelLogic:
    def __init__(self, session):
        self.hotel_dao = HotelDao(session)

    def get_hotels_in_city(self, city_name):
        hotels = self.hotel_dao.fetch_hotels_by_city(city_name)
        processed_hotels = self.process_hotels(hotels)
        return processed_hotels

    def process_hotels(self, hotels):
        # Perform any additional processing or transformations on the retrieved hotel data
        # You can apply business logic, calculations, or formatting specific to your requirements

        # Return the processed hotel data
        return hotels


# x = create_cassandra_session()
# a = HotelLogic(x)
# print(a.get_hotels_in_city("Quang Nam"))