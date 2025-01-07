import click
import requests

@click.command()
@click.option('--version', default='20230302', help='Version of the API to use')
def get_networks(version):
    """
    Fetch network data from GeckoTerminal API.
    
    This command sends a GET request to the GeckoTerminal API to retrieve network information.
    """
    base_endpoint = "https://api.geckoterminal.com/api/v2"
    request_path = "networks"
    
    # Construct the URL
    url = f"{base_endpoint}/{request_path}"

    # Headers for the request
    headers = {
        "Accept": f"application/json;version={version}"
    }

    try:
        # Make the GET request
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            click.echo(f"Successfully fetched data. Here's a sample:")
            # Print only a sample of the data to avoid overwhelming the console
            click.echo(data['data'][:5])  # Assuming 'data' is the key for network list
        else:
            click.echo(f"Failed to retrieve data: Status code {response.status_code}")
            click.echo(response.text)
    except requests.RequestException as e:
        click.echo(f"An error occurred: {e}")

if __name__ == '__main__':
    get_networks()
