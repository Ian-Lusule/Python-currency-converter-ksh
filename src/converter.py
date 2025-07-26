```python
# src/converter.py

import requests
import argparse
import json
from datetime import datetime

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key from exchangerate-api.com
BASE_URL = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY_HERE/" # Replace with your actual API key


def get_exchange_rates(base_currency="USD"):
    """
    Retrieves exchange rates from the exchangerate-api.com API.

    Args:
        base_currency: The base currency for the exchange rates (default: USD).

    Returns:
        A dictionary containing exchange rates, or None if an error occurs.  
        Includes a 'timestamp' key with the last updated time.
    """
    try:
        response = requests.get(f"{BASE_URL}/latest/{base_currency}")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        if data["result"] == "success":
            rates = data["conversion_rates"]
            rates['timestamp'] = data['time_last_update_utc']
            return rates
        else:
            print(f"API Error: {data.get('error-type', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None


def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another.

    Args:
        amount: The amount to convert.
        from_currency: The currency to convert from.
        to_currency: The currency to convert to.
        rates: A dictionary of exchange rates.

    Returns:
        The converted amount, or None if an error occurs.
    """
    try:
        if from_currency not in rates or to_currency not in rates:
            raise ValueError("Invalid currency code.")
        
        if amount <=0:
            raise ValueError("Amount must be positive.")

        return amount * (rates[to_currency] / rates[from_currency])
    except ValueError as e:
        print(f"Conversion error: {e}")
        return None
    except KeyError as e:
        print(f"Currency not found in exchange rates: {e}")
        return None


def main():
    """Main function to handle command-line arguments and currency conversion."""
    parser = argparse.ArgumentParser(description="Currency Converter")
    parser.add_argument("amount", type=float, help="Amount to convert")
    parser.add_argument("from_currency", help="Currency to convert from (e.g., USD)")
    parser.add_argument("to_currency", help="Currency to convert to (e.g., KSH)")
    args = parser.parse_args()

    rates = get_exchange_rates()
    if rates:
        converted_amount = convert_currency(args.amount, args.from_currency.upper(), args.to_currency.upper(), rates)
        if converted_amount is not None:
            print(f"{args.amount} {args.from_currency.upper()} = {converted_amount:.2f} {args.to_currency.upper()}")
            print(f"Rates last updated: {datetime.utcfromtimestamp(rates['timestamp']).strftime('%Y-%m-%d %H:%M:%S UTC')}")

if __name__ == "__main__":
    main()

```

**To use this code:**

1.  **Replace `YOUR_API_KEY_HERE`** with your actual API key from exchangerate-api.com.  You'll need to sign up for a free account to get one.
2.  **Save the code** as `src/converter.py`.
3.  **Run from your terminal:**  `python src/converter.py 100 USD KSH` (This converts 100 USD to KSH).


This improved version includes:

*   **Error Handling:**  Robust error handling for API requests, JSON decoding, and invalid currency codes.
*   **Clearer Function Separation:**  The code is broken down into well-defined functions for better readability and maintainability.
*   **Command-Line Interface (CLI):** Uses `argparse` for a user-friendly command-line interface.
*   **Currency Code Handling:** Accepts currency codes in upper or lower case.
*   **Timestamp:** Displays the last updated time of the exchange rates.
*   **Input Validation:** Checks for positive amounts.


Remember to install the `requests` library if you haven't already: `pip install requests`


This provides a solid foundation for a currency converter.  For a GUI, you could integrate this with a library like Tkinter, PyQt, or a web framework like Flask or Django.  Batch conversion could be added by modifying the `main` function to accept multiple conversions from a file or other input.
