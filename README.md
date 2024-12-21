# Supply Chain Optimization for Walmart Sparkathon

## Overview
This project was developed as part of the Walmart Sparkathon, focusing on optimizing supply chain processes in India. The primary objectives of the project were:

1. **Cost of Transportation**: Analyzing and minimizing transportation expenses.
2. **Inventory Management**: Improving shelf life prediction and demand forecasting.
3. **Route Optimization**: Determining the shortest and most efficient delivery routes.
4. **Apriori Analysis**: Leveraging association rule mining to enhance product recommendations and supply chain strategies.

The project integrates multiple datasets and machine learning models to provide actionable insights for supply chain optimization. A user-friendly Streamlit-based dashboard displays the results and recommendations.

---

## Features

### **Shelf Life Prediction**
- Factors like storage conditions, weather, and transportation impact shelf life.
- Predictive models identify optimal inventory strategies.

### **Route Optimization**
- Shortest and safest routes calculated using distance, road conditions, and weather.
- Integration with vehicle routing problems (VRP) for enhanced delivery planning.

### **Cost Optimization**
- Analysis of transportation costs based on vehicle type, fuel consumption, tolls, and package characteristics.
- Recommendations for efficient return trips.

### **Apriori Analysis**
- Implementation of association rule mining to uncover patterns in product relationships.
- Enhanced decision-making for inventory stocking and bundling strategies.

---

## Project Structure

```
Supply-Chain-Optimization-main
├── Datasets
│   ├── Apriori Association Data.csv
│   ├── Cost of Transportation - Product data.csv
│   ├── Cost of Transportation - Vehicle data.csv
│   ├── Integrated_Dataset - Inventory.csv
│   ├── Integrated_Dataset - Route Opt.csv
│   ├── Inventory Management Data - City_tier.csv
│   └── veh_fuel_type.csv
├── LICENSE
├── README.md
├── Website
│   ├── app.py
│   ├── apriori.py
│   ├── apriori_rules.pkl
│   ├── best_model.pkl
│   ├── job_suggest.py
│   ├── main_dashboard.py
│   ├── new_app.py
│   └── optimal_route.pkl
```

### **Key Components**

#### **Datasets**
- Contain data for inventory management, route optimization, and transportation cost analysis.

#### **Website**
- Python scripts and models for implementing the dashboard and functionalities.

#### **Models**
- `best_model.pkl`: Machine learning model for predictions.
- `optimal_route.pkl`: Precomputed optimal routes.
- `apriori_rules.pkl`: Association rules for product recommendations.

---

## Technologies Used

- **Programming Languages**: Python
- **Machine Learning**: Scikit-learn, Apriori Algorithm
- **Data Visualization**: Matplotlib, Streamlit
- **Data Processing**: Pandas, NumPy
- **Frameworks**: Streamlit for interactive dashboards
- **Version Control**: GitHub for collaboration and code management

---

## Usage

1. **Launch the Dashboard**: Open the Streamlit app to view predictions and insights.
2. **Upload Custom Data**: Use the dashboard to analyze your own datasets.
3. **Explore Results**: Visualize optimized routes, shelf life predictions, cost analyses, and apriori insights.

---

## Contributors
- [Khanak Agrawal](https://github.com/Khanakag-17)
- [Ashutosh Singh](https://github.com/ashutosh-singh-03)
- [Abhishree Soni](https://github.com/abhishree045)
- Team Necromancers

---

## Future Enhancements

1. Incorporate real-time data for route and cost optimization.
2. Extend support for additional product categories.
3. Enhance the dashboard with more interactive visualizations.

---

## Acknowledgments
We thank Walmart Sparkathon for providing the opportunity to work on this challenging and impactful problem statement.
