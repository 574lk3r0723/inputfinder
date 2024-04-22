import requests
from bs4 import BeautifulSoup

def find_input_fields(url):
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all input fields in the HTML form
        input_fields = soup.find_all('input')

        # Extract attributes and location of each input field
        input_details = []
        for field in input_fields:
            field_details = {
                'name': field.get('name', ''),
                'type': field.get('type', ''),
                'value': field.get('value', ''),
                'placeholder': field.get('placeholder', ''),
                'location': str(field.find_parents()[0].name) if field.find_parents() else 'Unknown'
            }
            input_details.append(field_details)

        return input_details

    except Exception as e:
        print("Error:", e)
        return None

# Example usage
url = 'https://crypto.com/trending'  # Replace with the URL of the website you want to inspect
input_fields = find_input_fields(url)

if input_fields:
    print("Input fields found on the website:")
    for field in input_fields:
        print(field)
else:
    print("Failed to retrieve input fields.")