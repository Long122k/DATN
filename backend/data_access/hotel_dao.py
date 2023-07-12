import sys
sys.path.append('database')
from cassandra_connector import create_cassandra_session
from datetime import datetime

class HotelDao:
    def __init__(self, session):
        self.session = session

    def fetch_hotels_by_city(self, city_name):
        query = f"SELECT hotel_name, price, review_date, sentiment_score, star, total_hotel_reviews FROM hotel_data WHERE city = '{city_name}' ALLOW FILTERING;"
        result = self.session.execute(query)

        hotels = []
        for row in result:
            hotel = {
                'hotel_name': row['hotel_name'],
                'price': row['price'],
                'review_date': str(row['review_date']),
                'sentiment_score': row['sentiment_score'],
                'star': row['star'],
                'total_hotel_reviews': row['total_hotel_reviews']
            }
            hotels.append(hotel)
        return hotels


    def fetch_top_hotels_by_city(self, city_name, limit=10):
        query = f"SELECT hotel_name, price, review_date, sentiment_score, star, total_hotel_reviews FROM hotel_data WHERE city = '{city_name}' ALLOW FILTERING;"
        result = self.session.execute(query)

        hotels = []
        for row in result:
            hotel = {
                'hotel_name': row['hotel_name'],
                'price': row['price'],
                'review_date': row['review_date'].strftime('%Y-%m-%d'),
                'sentiment_score': row['sentiment_score'],
                'star': row['star'],
                'total_hotel_reviews': row['total_hotel_reviews']
            }
            hotels.append(hotel)

        # Sort hotels based on total_hotel_reviews in descending order
        sorted_hotels = sorted(hotels, key=lambda x: x['total_hotel_reviews'], reverse=True)

        # Return the top N hotels based on total_hotel_reviews
        top_hotels = sorted_hotels[:limit]
        return top_hotels
    


    
# x = create_cassandra_session()
# a = HotelDao(x)
# print(a.fetch_hotels_by_city("Quang Nam"))