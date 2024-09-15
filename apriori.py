import streamlit as st
import pandas as pd
import pickle

# Load the pickle file containing the association rules
@st.cache_data
def load_rules():
    with open('apriori_rules.pkl', 'rb') as file:
        rules = pickle.load(file)
    return rules

# Function to extract unique products from the rules
def get_unique_products(rules):
    products = set()
    for antecedents in rules['antecedents']:
        products.update(antecedents)
    for consequents in rules['consequents']:
        products.update(consequents)
    return sorted(list(products))

rules = load_rules()

# Extract unique products for the dropdown
unique_products = get_unique_products(rules)

# Initialize session state for dynamic selection boxes
if 'selection_boxes' not in st.session_state:
    st.session_state.selection_boxes = 1

if 'selected_products' not in st.session_state:
    st.session_state.selected_products = []


# Function to add a new selection box
def add_selection_box():
    if st.session_state.selection_boxes < 5:
        st.session_state.selection_boxes += 1
    else:
        st.warning("Selection Limit Reached")

# Function to remove the last selection box
def remove_selection_box():
    if st.session_state.selection_boxes > 1:
        st.session_state.selection_boxes -= 1
        # Remove the last selected product if it exists
        if len(st.session_state.selected_products) > st.session_state.selection_boxes:
            st.session_state.selected_products.pop()

# Display product selection boxes with add and remove buttons
for i in range(st.session_state.selection_boxes):
    selected_product = st.selectbox(
        f"Select product {i + 1}:", 
        unique_products, 
        key=f"product_select_{i}"
    )
    if selected_product:
        # Store selected products in a session state list
        if len(st.session_state.selected_products) > i:
            st.session_state.selected_products[i] = selected_product
        else:
            st.session_state.selected_products.append(selected_product)

# Buttons for adding and removing selection boxes
if st.session_state.selection_boxes < 5:
    st.button("Add another product", on_click=add_selection_box)
else:
    st.warning("Selection Limit Reached")

if st.session_state.selection_boxes > 1:
    st.button("Remove last product", on_click=remove_selection_box)

# Ensure no repetitions in the selected products
st.session_state.selected_products = list(set(st.session_state.selected_products[:st.session_state.selection_boxes]))

if st.session_state.selected_products:
    # Find rules where any of the selected products are in the antecedents
    associated_rules = rules[rules['antecedents'].apply(lambda x: any(product in x for product in st.session_state.selected_products))]
    
    if not associated_rules.empty:
        # Sort by confidence and then lift to find the top associations
        top_associations = associated_rules.sort_values(by=['confidence', 'lift'], ascending=False)
        
        # Extract and display the top 5 unique associated products without repetition
        associated_products = set()
        st.write("Top 5 products frequently bought with the selected products:")
        for _, row in top_associations.iterrows():
            for consequent in row['consequents']:
                if consequent not in st.session_state.selected_products and consequent not in associated_products:
                    associated_products.add(consequent)
                    st.write(f"- **{consequent}**")
                if len(associated_products) >= 5:
                    break
            if len(associated_products) >= 5:
                break
    else:
        st.write("No associations found for the selected products.")
