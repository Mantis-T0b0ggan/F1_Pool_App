import requests
from supabase import create_client, Client

# Supabase credentials
SUPABASE_URL = "https://synvlfkwthbsimipkxne.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN5bnZsZmt3dGhic2ltaXBreG5lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5ODgxMjMsImV4cCI6MjA1NzU2NDEyM30.2ptXuZNuQ3Su0aMvEeL931IjPm9t1ruN_iNj7duzvuI"

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fetch current F1 drivers from Ergast API
ERGAST_API_URL = "http://ergast.com/api/f1/current/drivers.json"
response = requests.get(ERGAST_API_URL)

if response.status_code == 200:
    drivers_data = response.json()["MRData"]["DriverTable"]["Drivers"]

    # Format driver data with a placeholder name
    formatted_drivers = [
        {
            "name": "Auto-Generated",  # Placeholder name
            "driver": f"{driver['givenName']} {driver['familyName']}",
            "points": 0  # Default points
        }
        for driver in drivers_data
    ]

    try:
        # Insert drivers into Supabase
        response = supabase.table("f1_pool").upsert(formatted_drivers).execute()

        # Print response for debugging
        print("Supabase Response:", response)
    
    except Exception as e:
        print("Error inserting/updating data in Supabase:", e)

else:
    print(f"Failed to fetch drivers: {response.status_code}")
