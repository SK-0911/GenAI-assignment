import streamlit as st
import pandas as pd
from pymongo import MongoClient, errors
from query_generator import load_llama_model, generate_mongo_query

# MongoDB connection details
mongo_url = "mongodb://localhost:27017/"
database_name = "sample_database"
collection_name = "sample_collection"

# Load Llama model
st.write("Loading Llama model...")
llama_generator = load_llama_model()

# MongoDB connection setup
try:
    client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
    db = client[database_name]
    collection = db[collection_name]
    client.server_info()  # Test connection
except errors.ServerSelectionTimeoutError:
    st.error("Could not connect to MongoDB. Please check your connection.")
    st.stop()

# Streamlit UI
st.title("MongoDB Query Interface with Llama-2")

# Display available columns
try:
    sample_data = pd.DataFrame(list(collection.find().limit(1)))
    available_columns = sample_data.columns.tolist()
    st.write("### Available Columns")
    st.write(", ".join(available_columns))
except Exception as e:
    st.error(f"Could not retrieve columns from MongoDB: {e}")
    st.stop()

# User input for column name
column_name = st.text_input("Enter the column name you want to query:")

if column_name:
    if column_name not in available_columns:
        st.error("Invalid column name. Please enter a valid column.")
    else:
        # Generate and display the query
        try:
            query = generate_mongo_query(llama_generator, column_name)
            st.write("Generated MongoDB Query:", query)
        except Exception as e:
            st.error(f"An error occurred while generating the query: {e}")
            query = {column_name: {"$exists": True, "$ne": None}}  # Default query

        # Retrieve data based on the query
        try:
            results = collection.find(query)
            result_data = pd.DataFrame(list(results))

            # Option to display or save data
            action = st.radio("Choose an action:", ("Display Data", "Save to CSV"))

            if action == "Display Data":
                if result_data.empty:
                    st.warning("No data found for the specified query.")
                else:
                    st.write("### Query Results")
                    st.dataframe(result_data)

            elif action == "Save to CSV":
                test_case = st.text_input("Enter the test case name (e.g., 'test_case1'):")
                if test_case:
                    file_name = f"{test_case}.csv"
                    result_data.to_csv(file_name, index=False)
                    st.success(f"Data saved to {file_name}")
                    st.download_button(
                        label="Download CSV",
                        data=result_data.to_csv(index=False),
                        file_name=file_name,
                        mime="text/csv"
                    )
        except Exception as e:
            st.error(f"An error occurred while processing your request: {e}")
