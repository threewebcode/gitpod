from pycoingecko import CoinGeckoAPI

# Initialize the CoinGeckoAPI client
cg = CoinGeckoAPI()

# List of tokens by their CoinGecko IDs
token_ids = ['bitcoin', 'ethereum', 'cosmos', 'celestia', 'bitget-token', 'zerebro']

# Currency to compare against
vs_currency = 'usd'

try:
    # Fetch prices for all tokens in one call
    prices = cg.get_price(ids=','.join(token_ids), vs_currencies=vs_currency)
    
    # Print prices
    for token_id, price_data in prices.items():
        print(f"{token_id.capitalize()}: ${price_data[vs_currency]:.6f}")

except Exception as e:
    print(f"An error occurred: {e}")