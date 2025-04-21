import requests
import tempfile
import os

# URL of the Python script
url = "https://gizmomusk.github.io/calciapp/"

# Security warning
print("WARNING: Executing code from external sources can be dangerous. Ensure you trust the source.")
print("This script downloads and executes a Python script from the provided URL.")
print("Review the downloaded code before proceeding in a production environment.")

try:
    # Download the script
    response = requests.get(url)
    response.raise_for_status()

    # Create a temporary file to store the script
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8") as temp_file:
        temp_file.write(response.text)
        temp_file_path = temp_file.name

    print(f"Script downloaded and saved at: {temp_file_path}")

    # Read and display the script content
    with open(temp_file_path, "r", encoding="utf-8") as f:
        script_content = f.read()
        print("\n=== Downloaded Script Content ===")
        print(script_content)
        print("================================")

    # Prompt user to proceed
    proceed = input("\nDo you want to execute this script? (yes/no): ").strip().lower()
    if proceed != "yes":
        print("Execution aborted by user.")
        os.unlink(temp_file_path)
        exit()

    # Read the file again and execute
    with open(temp_file_path, "r", encoding="utf-8") as f:
        script_content = f.read()
        exec(script_content, {})

    print("Script executed successfully.")

except requests.RequestException as e:
    print(f"Error downloading the script: {e}")
except Exception as e:
    print(f"Error executing the script: {e}")
finally:
    # Clean up
    if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
        os.unlink(temp_file_path)
        print(f"Temporary file {temp_file_path} deleted.")
