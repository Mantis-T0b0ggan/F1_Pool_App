from supabase import create_client, Client

# Replace with your Supabase Project URL & API Key
SUPABASE_URL = "https://synvlfkwthbsimipkxne.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN5bnZsZmt3dGhic2ltaXBreG5lIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MTk4ODEyMywiZXhwIjoyMDU3NTY0MTIzfQ.W71L51FzPXJ907DfKAqRCc7x1MnhD8HFj3SwvcrZVAE"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Insert a test user
response = supabase.table("f1_pool").insert({"name": "Test User", "driver": "VER", "points": 0}).execute()
print("Insert Response:", response)

# Fetch all users
users = supabase.table("f1_pool").select("*").execute()
print("Users in Database:", users)
