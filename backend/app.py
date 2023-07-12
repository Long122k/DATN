import sys
from flask import Flask
from routes.city_route import search_route
from routes.hotel_route import hotel_route
from database.cassandra_connector import create_cassandra_session
# import sys
# sys.path.append('database')
# from cassandra_connector import create_cassandra_session

app = Flask(__name__)

# Register the search API route
app.register_blueprint(search_route)

# Create Cassandra session
session = create_cassandra_session()

# Register the hotel API route with the session
app.register_blueprint(hotel_route, session=session)

if __name__ == '__main__':
    app.run(debug=True)
# if session:
#     print(session)
