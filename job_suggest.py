import streamlit as st
import pickle
import pandas as pd
import openrouteservice
import folium
from streamlit_folium import folium_static
from geopy.distance import geodesic, great_circle

# Load the pickle file and dataset
with open('optimal_route.pkl', 'rb') as file:
    optimal_route_model = pickle.load(file)

data = pd.read_csv('Integrated_Dataset - Route Opt.csv')

# Input for ORS API Key
api_key = '5b3ce3597851110001cf6248f8f22c8e56fe4055a20d5ac026485fed'

# Function to get coordinates for a given city
def get_coordinates(city):
    row = data[data['city'] == city]
    if not row.empty:
        return row.iloc[0]['Latitude'], row.iloc[0]['Longitude']
    else:
        st.error("City not found in the dataset.")
        return None, None

# Function to find nearby cities within a given radius of a route
def find_nearby_cities_along_route(route_coords, radius_km):
    nearby_cities = set()  # Use a set to avoid duplicates
    for _, row in data.iterrows():  # Iterating over dataset
        city_coords = (row['Latitude'], row['Longitude'])
        for coord in route_coords:
            if great_circle(coord, city_coords).km <= radius_km:
                nearby_cities.add(row['city'])  # Add city to set
                break  # No need to check further points for this city
    return list(nearby_cities)  # Convert set back to list for Streamlit

# Streamlit app layout
st.title("Intermediate Job Suggestions")

start_city = st.selectbox("Select the start city:", data['city'].unique())
end_city = st.selectbox("Select the end city:", data['city'].unique())

if start_city and end_city and api_key:
    start_coords = get_coordinates(start_city)
    end_coords = get_coordinates(end_city)

    if start_coords and end_coords:
        # Reverse coordinates for ORS (convert to (longitude, latitude))
        ors_start_coords = (start_coords[1], start_coords[0])
        ors_end_coords = (end_coords[1], end_coords[0])

        # Create ORS client with the API key
        client = openrouteservice.Client(key=api_key)

        # Fetch the route from start to end city
        try:
            route = client.directions(
                coordinates=[ors_start_coords, ors_end_coords],
                profile='driving-car',
                format='geojson'
            )
            route_coords = [(step[1], step[0]) for step in route['features'][0]['geometry']['coordinates']]

            # Find nearby cities within a 100-150 km radius along the route
            nearby_cities = find_nearby_cities_along_route(route_coords, 150)

            if nearby_cities:
                st.write("Nearby cities found along the route:")
                # Limit the number of intermediate stops to prevent exceeding the free API limit
                max_intermediate_stops = 5
                selected_cities = st.multiselect(f"Select up to {max_intermediate_stops} cities to include in your route:", nearby_cities)

                if len(selected_cities) > max_intermediate_stops:
                    st.error(f"You can only select up to {max_intermediate_stops} cities.")
                elif selected_cities:
                    # Get coordinates for selected cities
                    intermediate_coords = [get_coordinates(city) for city in selected_cities]

                    # Construct the full route with selected intermediate cities
                    full_route_coords = [ors_start_coords] + [(lon, lat) for lat, lon in intermediate_coords] + [ors_end_coords]

                    # Fetch the optimal route including intermediate stops
                    routes = client.directions(
                        coordinates=full_route_coords,
                        profile='driving-car',
                        format='geojson'
                    )

                    # Display the route on the map
                    m = folium.Map(location=start_coords, zoom_start=6)
                    folium.GeoJson(routes).add_to(m)
                    folium.Marker(location=start_coords, popup=start_city).add_to(m)
                    for city, coords in zip(selected_cities, intermediate_coords):
                        folium.Marker(location=coords, popup=city).add_to(m)
                    folium.Marker(location=end_coords, popup=end_city).add_to(m)
                    folium_static(m)

                else:
                    st.write("No intermediate cities selected.")
            else:
                st.write("No nearby cities found along the route.")
        except openrouteservice.exceptions.ApiError as e:
            # Display the error message
            st.error(f"Error fetching route: {e}")