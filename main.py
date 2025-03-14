from fastapi import FastAPI
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase credentials
SUPABASE_URL = os.getenv("https://synvlfkwthbsimipkxne.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN5bnZsZmt3dGhic2ltaXBreG5lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5ODgxMjMsImV4cCI6MjA1NzU2NDEyM30.2ptXuZNuQ3Su0aMvEeL931IjPm9t1ruN_iNj7duzvuI")

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "F1 Pool API is running!"}

# Leaderboard endpoint
@app.get("/leaderboard")
def get_leaderboard():
    response = supabase.table("f1_pool").select("*").execute()
    return response.data
