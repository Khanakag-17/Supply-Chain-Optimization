# 🚚 Supply Chain Optimization – Walmart Sparkathon

## 📌 Overview
Developed as part of the **Walmart Sparkathon 2024**, this project focuses on **enhancing supply chain processes in India** through data-driven strategies and AI-powered solutions.

### 🎯 Key Objectives:
1. 💸 **Cost of Transportation** – Minimize logistics expenses.
2. 📦 **Inventory Management** – Predict shelf life & improve demand forecasting.
3. 🗺️ **Route Optimization** – Determine the most efficient delivery paths.
4. 📊 **Apriori Analysis** – Apply association rule mining to boost product bundling and inventory decisions.

🔍 This end-to-end pipeline integrates multiple datasets, machine learning models, and a sleek **Streamlit dashboard** to offer actionable business insights.

---

## ✨ Features

### 🧬 Shelf Life Prediction
- Considers factors like **storage**, **weather**, and **transport conditions**.
- ML models predict product degradation timelines to reduce spoilage.

### 🚗 Route Optimization
- Calculates shortest and **safest delivery paths** using real-world factors like road conditions and weather.
- Solves **Vehicle Routing Problems (VRP)** for efficient delivery planning.

### 💰 Cost Optimization
- Analyzes fuel, vehicle type, toll charges, and package weight to suggest **cost-effective transport strategies**.
- Suggests **efficient return routes** to reduce empty-trip costs.

### 🛒 Apriori Analysis
- Implements **association rule mining** to discover frequently bought product combinations.
- Informs **inventory stocking** and **bundle recommendations** for sales growth.

---

## 🗂️ Project Structure

```
Supply-Chain-Optimization-main
├── Datasets
│ ├── Apriori Association Data.csv
│ ├── Cost of Transportation - Product data.csv
│ ├── Cost of Transportation - Vehicle data.csv
│ ├── Integrated_Dataset - Inventory.csv
│ ├── Integrated_Dataset - Route Opt.csv
│ ├── Inventory Management Data - City_tier.csv
│ └── veh_fuel_type.csv
├── LICENSE
├── README.md
├── Website
│ ├── app.py
│ ├── apriori.py
│ ├── apriori_rules.pkl
│ ├── best_model.pkl
│ ├── job_suggest.py
│ ├── main_dashboard.py
│ ├── new_app.py
│ └── optimal_route.pkl
```

---

## 🧠 Technologies Used

| Category | Tools |
|---------|-------|
| 💻 Programming | Python |
| 🤖 ML Models | Scikit-learn, Apriori Algorithm |
| 📈 Visualization | Matplotlib, Streamlit |
| 📊 Data Handling | Pandas, NumPy |
| 🧩 Dashboard | Streamlit |
| 🔁 Version Control | Git & GitHub |

---

## 🚀 How to Use

1. **Launch the Dashboard**  
   Run the Streamlit app to view live predictions and visual analytics.

2. **Upload Your Data**  
   Use the built-in uploader to input your own datasets for custom analysis.

3. **Explore Insights**  
   Visualize results like:
   - 📦 Shelf life predictions  
   - 🛣️ Optimized delivery routes  
   - 💵 Cost efficiency suggestions  
   - 📊 Association rule findings  

---

## 👩‍💻 Contributors

- 👩‍💼 [Khanak Agrawal](https://github.com/Khanakag-17)
- 👨‍💻 [Ashutosh Singh](https://github.com/ashutosh-singh-03)
- 👩‍🔬 [Abhishree Soni](https://github.com/abhishree045)  
🧠 Team **Necromancers**

---

## 🌱 Future Enhancements

- ⚡ Integrate real-time traffic & weather APIs for dynamic route planning.
- 🧺 Expand support for more SKUs and product categories.
- 📊 Add interactive data exploration & analytics panels in the dashboard.

---

## 🙏 Acknowledgments

Thanks to **Walmart Sparkathon 2024** for presenting this impactful problem statement and opportunity to innovate in real-world supply chain systems.

---


