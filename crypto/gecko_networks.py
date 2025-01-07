import click
import requests

@click.command()
def get_network_ids():
    """
    Fetch and print network IDs from GeckoTerminal API.
    """
    # Base URL and endpoint
    base_endpoint = "https://api.geckoterminal.com/api/v2"
    request_path = "networks"
    
    # Construct the full URL
    url = f"{base_endpoint}/{request_path}"
    
    # Headers for the request
    headers = {
        "Accept": "application/json;version=20230302"
    }
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()['data']
        
        # Ensure 'data' is a list
        if isinstance(data, list):
            # Extract and print the 'id' from each dictionary in the list
            for network in data:
                if 'id' in network:
                    click.echo(network['id'])
        else:
            click.echo("Unexpected response format: data is not a list.", err=True)
    
    except requests.RequestException as e:
        click.echo(f"An error occurred: {e}", err=True)

if __name__ == '__main__':
    get_network_ids()
