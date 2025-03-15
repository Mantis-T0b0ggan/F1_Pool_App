import requests
from supabase import create_client, Client

# Supabase credentials (Placeholder values)
SUPABASE_URL = "https://synvlfkwthbsimipkxne.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN5bnZsZmt3dGhic2ltaXBreG5lIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE5ODgxMjMsImV4cCI6MjA1NzU2NDEyM30.2ptXuZNuQ3Su0aMvEeL931IjPm9t1ruN_iNj7duzvuI"

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fetch all drivers listed in the current F1 season
ERGAST_DRIVERS_URL = "http://ergast.com/api/f1/current/drivers.json"
ERGAST_RESULTS_URL = "http://ergast.com/api/f1/current/results.json"

drivers_response = requests.get(ERGAST_DRIVERS_URL)
results_response = requests.get(ERGAST_RESULTS_URL)

if drivers_response.status_code == 200 and results_response.status_code == 200:
    all_drivers = drivers_response.json()["MRData"]["DriverTable"]["Drivers"]
    race_results = results_response.json()["MRData"]["RaceTable"]["Races"]

    # Extract drivers who have actually participated in a race
    active_driver_ids = set()
    for race in race_results:
        for result in race["Results"]:
            active_driver_ids.add(result["Driver"]["driverId"])

    # Filter out only active drivers
    active_drivers = [
        driver for driver in all_drivers if driver["driverId"] in active_driver_ids
    ]

    # Format driver data for Supabase
    formatted_drivers = [
        {
            "driver_id": driver["driverId"],
            "first_name": driver["givenName"],
            "last_name": driver["familyName"],
            "nationality": driver["nationality"],
            "code": driver.get("code", ""),  # Some drivers may not have a code
        }
        for driver in active_drivers
    ]

    # Insert or update drivers in Supabase
    response = supabase.table("f1_drivers").upsert(formatted_drivers).execute()

    print(f"✅ Successfully updated {len(formatted_drivers)} active F1 drivers in Supabase!")
else:
    print(f"❌ Failed to fetch data: {drivers_response.status_code}, {results_response.status_code}")
