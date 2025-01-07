import click
import requests

@click.command()
def get_networks():
    # Base URL for the API
    base_endpoint = "https://api.geckoterminal.com/api/v2"
    
    # Request path
    path = "networks"
    
    # Construct the full URL
    url = f"{base_endpoint}/{path}"
    
    # Headers for the request
    headers = {
        "Accept": "application/json;version=20230302"
    }
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse and print the JSON response
        data = response.json()
        click.echo(click.style(f"API Response:", fg='green'))
        click.echo(click.style(data, fg='blue'))
    
    except requests.exceptions.RequestException as e:
        click.echo(click.style(f"An error occurred: {e}", fg='red'))

if __name__ == '__main__':
    get_networks()
