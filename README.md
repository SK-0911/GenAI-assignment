# MongoDB Query Interface with Llama-2
This project provides a simple, interactive web application using Streamlit that allows users to generate MongoDB queries, retrieve data based on column names, and either display or save the results. It uses the Llama-2-7B-GGUF model for natural language query generation, enabling users to generate MongoDB queries by simply entering the column name. The app is designed to be user-friendly, with robust error handling for invalid inputs and connectivity issues.

## Features
- **Natural Language Query Generation**: Uses the Llama-2 model to generate MongoDB queries based on user input.
- **Data Retrieval and Display**: Allows users to retrieve, view, and download data from a MongoDB collection.
- **Error Handling**: Handles invalid inputs, MongoDB connection issues, and model loading errors gracefully.

## Requirements
- **Python**: 3.8 or higher
- **MongoDB**: Ensure a MongoDB instance is running locally or remotely.
- **Llama-2 Model**: This system uses the Llama-2-7B-GGUF model from Hugging Face, which requires installation of the `transformers` and `torch` libraries.
- **Streamlit**: To provide a web-based interface for interaction.

Install the necessary Python libraries with the following command:

```bash
pip install -r requirements.txt
```

## Installation
### Step 1: Clone the Repository
Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

## Step 2: Install Dependencies
Ensure all dependencies are installed by running:
```bash
pip install -r requirements.txt
```

## Step 3: Download and Set Up the Llama-2 Model
To use the Llama-2-7B-GGUF model:
- Download the model locally from Hugging Face.
- Save it in a models/ directory within the project folder.
- Alternatively, if you have the model downloaded elsewhere, update the model path in query_generator.py.

## Step 4: Set Up MongoDB
Make sure MongoDB is installed and running on your local machine or a remote server.
- Update `mongo_url`, `database_name`, and `collection_name` in app.py to match your MongoDB setup.

## Step 5: Run the Application
Use Streamlit to launch the app:
```bash
streamlit run app.py
```

The app should open in a web browser at [http://localhost:8501].

## Project Structure

project_directory/
│
├── app.py                    # Main Streamlit app
├── query_generator.py        # Contains function to load and use Llama model
├── requirements.txt          # Dependencies for the project
└── models/                   # Local model storage (optional)

