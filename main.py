from fastapi import FastAPI
from supabase import create_client, Client
import os

# Fetch from environment variables (DO NOT HARDCODE)
SUPABASE_URL = os.getenv("https://synvlfkwthbsimipkxne.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN5bnZsZmt3dGhic2ltaXBreG5lIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MTk4ODEyMywiZXhwIjoyMDU3NTY0MTIzfQ.W71L51FzPXJ907DfKAqRCc7x1MnhD8HFj3SwvcrZVAE")

# Debugging: Print to logs (partially mask the key for security)
print(f"SUPABASE_URL: {SUPABASE_URL}")
print(f"SUPABASE_KEY: {SUPABASE_KEY[:5]}*****")

# Validate if environment variables are set
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase environment variables")

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "F1 Pool API is running!"}

@app.get("/leaderboard")
def get_leaderboard():
    response = supabase.table("f1_pool").select("*").execute()
    return response.data
