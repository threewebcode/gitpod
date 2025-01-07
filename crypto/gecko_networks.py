import requests
import click

@click.command()
def get_networks():
    # Base URL for the API endpoint
    base_url = "https://api.geckoterminal.com/api/v2"
    
    # Construct the full URL
    url = f"{base_url}/networks"
    
    # Headers for the request
    headers = {
        "Accept": "application/json;version=20230302"
    }

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the 'data' field from the response JSON
        networks = response.json()['data']
        
        # Extract 'id' from each network dictionary
        network_ids = [network['id'] for network in networks]
        
        # Output with pretty formatting and color using click.echo
        click.secho("Network IDs:", fg='green', bold=True)
        click.echo(click.style(str(network_ids), fg='blue'))
    else:
        click.secho(f"Error: {response.status_code}", fg='red')

if __name__ == '__main__':
    get_networks()
