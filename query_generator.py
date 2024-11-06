from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Load Llama model locally
model_name = "models/llama-2-7b.Q4_K_M.gguf"


def load_llama_model():
    # Load model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)
    return generator

# Generate query based on column name using Llama model
def generate_mongo_query(generator, column_name):
    prompt = f"Generate a MongoDB query to fetch all documents where '{column_name}' is not null or empty."
    response = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
    # Extract the MongoDB query from the response
    query_start = response.find("{")
    query_end = response.rfind("}") + 1
    query_str = response[query_start:query_end]
    try:
        query = eval(query_str)  # Convert to dictionary if in valid format
    except Exception:
        query = {column_name: {"$exists": True, "$ne": None}}  # Default query
    return query
