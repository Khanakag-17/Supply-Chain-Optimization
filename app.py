import streamlit as st
import pandas as pd
from geopy.distance import geodesic
import openrouteservice
import folium
from streamlit_folium import folium_static
import pickle

# Load the pickle file and dataset
with open('optimal_route.pkl', 'rb') as file:
    optimal_route_model = pickle.load(file)

data = pd.read_csv('Integrated_Dataset - Route Opt.csv')
vehicle_fuel_data = pd.read_csv('veh_fuel_type.csv')
city_tier_data = pd.read_csv('Inventory Management Data - City_tier.csv')

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

# Function to calculate the straight-line distance between two cities
def calculate_distance(start_coords, end_coords):
    return geodesic(start_coords, end_coords).kilometers

# Function to get the state of the start city
def get_state(city):
    row = city_tier_data[city_tier_data['city'] == city]
    if not row.empty:
        return row.iloc[0]['State']
    else:
        st.error("City not found in the city-tier dataset.")
        return None

# Function to find the most cost-optimal vehicle and fuel type based on total cost
def find_optimal_vehicle(distance, state, vehicle_fuel_data):
    # Filter the vehicle fuel data based on the state
    state_vehicle_fuel_data = vehicle_fuel_data[vehicle_fuel_data['State'] == state]
    if state_vehicle_fuel_data.empty:
        st.error("No vehicle fuel data found for the selected state.")
        return None
    
    # Calculate the total cost for each vehicle
    state_vehicle_fuel_data['Total Cost'] = state_vehicle_fuel_data['Cost'] * distance
    # Find the vehicle with the minimum total cost
    optimal_vehicle = state_vehicle_fuel_data.loc[state_vehicle_fuel_data['Total Cost'].idxmin()]
    return optimal_vehicle

# Streamlit app layout
st.title("Optimal Route Finder and Cost Analysis")

start_city = st.selectbox("Select the start city:", data['city'].unique())
end_city = st.selectbox("Select the end city:", data['city'].unique())

if start_city and end_city and api_key:
    start_coords = get_coordinates(start_city)
    end_coords = get_coordinates(end_city)
    start_state = get_state(start_city)

    if start_coords and end_coords and start_state:
        # Reverse coordinates for ORS (convert to (longitude, latitude))
        ors_start_coords = (start_coords[1], start_coords[0])
        ors_end_coords = (end_coords[1], end_coords[0])

        # Calculate the distance and add 150 km
        distance = calculate_distance(start_coords, end_coords) + 250

        # Find the most cost-optimal vehicle
        optimal_vehicle = find_optimal_vehicle(distance, start_state, vehicle_fuel_data)

        if optimal_vehicle is not None:
            # Display the calculated distance and optimal vehicle
            st.subheader("Distance Calculation")
            st.write(f"The distance between {start_city} and {end_city} is approximately {distance:.2f} km.")

            st.subheader("Optimal Vehicle Recommendation")
            st.write(f"**Vehicle Type**: {optimal_vehicle['Truck Type']}")
            st.write(f"**Fuel Type**: {optimal_vehicle['Fuel Type']}")
            st.write(f"**Cost per km**: {optimal_vehicle['Cost']}")
            st.write(f"**Total Cost**: {optimal_vehicle['Total Cost'].round(2)}")

            # Create ORS client with the API key directly passed
            client = openrouteservice.Client(key=api_key)

            # Define the parameters
            coordinates = [ors_start_coords, ors_end_coords]
            radius = [1000, 1000]

            # Fetch the optimal route
            try:
                routes = client.directions(
                    coordinates=coordinates,
                    profile='driving-car',
                    radiuses=radius,
                    format='geojson'
                )

                # Display the route on the map (convert back to (latitude, longitude))
                m = folium.Map(location=start_coords, zoom_start=6)
                folium.GeoJson(routes).add_to(m)
                folium.Marker(location=start_coords, popup=start_city).add_to(m)
                folium.Marker(location=end_coords, popup=end_city).add_to(m)
                folium_static(m)

            except openrouteservice.exceptions.ApiError as e:
                # Display the error message
                st.error(f"Error fetching route: {e}")
