from fastapi import FastAPI
from supabase import create_client, Client
import os

# ✅ Fetch Supabase credentials from environment variables (correct way)
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://synvlfkwthbsimipkxne.supabase.co")  
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN5bnZsZmt3dGhic2ltaXBreG5lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5ODgxMjMsImV4cCI6MjA1NzU2NDEyM30.2ptXuZNuQ3Su0aMvEeL931IjPm9t1ruN_iNj7duzvuI")

# Debugging: Print environment variable status (Partially Masked Key for Security)
print(f"DEBUG: SUPABASE_URL = {SUPABASE_URL}")
print(f"DEBUG: SUPABASE_KEY = {'SET' if SUPABASE_KEY else 'NOT SET'}")  

# Validate that environment variables are set
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase environment variables!")

# ✅ Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Create FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "F1 Pool API is running!"}

@app.get("/leaderboard")
def get_leaderboard():
    response = supabase.table("f1_pool").select("*").execute()
    return response.data
