import os

# Load from environment or set your Google API key directly
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "xxxx") # API key

# You might add a check to ensure it's loaded
if GOOGLE_API_KEY is None:
    print("Warning: GOOGLE_API_KEY environment variable not set!")
    # Optionally, raise an error to stop execution if the key is mandatory
    # raise ValueError("GOOGLE_API_KEY environment variable must be set.")