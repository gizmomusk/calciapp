import requests

# URL of the raw mainapp.py file from the GitHub repository
url = "https://raw.githubusercontent.com/gizmomusk/calciapp/main/mainapp.py"

try:
    # Fetch the content of mainapp.py
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    
    # Get the text content of the script
    script_content = response.text
    
    # Execute the script
    exec(script_content)

except requests.RequestException as e:
    print(f"Error fetching the script: {e}")
except Exception as e:
    print(f"Error executing the script: {e}")
