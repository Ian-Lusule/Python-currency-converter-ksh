```python
"""
Utilities for the Python currency converter.

This module provides helper functions for fetching exchange rates,
performing conversions, and handling errors.
"""

import requests
import json
from typing import Dict, List, Tuple

API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key from exchangerate-api.com
BASE_URL = "https://v6.exchangerate-api.com/v6/"


def fetch_exchange_rates(base_currency: str = "USD") -> Dict:
    """
    Fetches exchange rates from the exchangerate-api.com API.

    Args:
        base_currency: The base currency for the exchange rates. Defaults to USD.

    Returns:
        A dictionary containing the exchange rates, or None if an error occurred.
    """
    url = f"{BASE_URL}{API_KEY}/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        if data["result"] == "success":
            return data["conversion_rates"]
        else:
            print(f"API Error: {data.get('error-type', 'Unknown error')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None


def convert_currency(amount: float, from_currency: str, to_currency: str, rates: Dict) -> float:
    """
    Converts an amount from one currency to another.

    Args:
        amount: The amount to convert.
        from_currency: The currency to convert from.
        to_currency: The currency to convert to.
        rates: A dictionary of exchange rates.

    Returns:
        The converted amount, or None if an error occurred.
    """
    try:
        if from_currency not in rates or to_currency not in rates:
            raise ValueError("Invalid currency code.")
        return amount * (rates[to_currency] / rates[from_currency])
    except (KeyError, ValueError) as e:
        print(f"Conversion error: {e}")
        return None


def batch_convert(amounts: List[Tuple[float, str, str]], rates: Dict) -> List[Tuple[float, str, str, float]]:
    """
    Performs batch currency conversions.

    Args:
        amounts: A list of tuples, each containing (amount, from_currency, to_currency).
        rates: A dictionary of exchange rates.

    Returns:
        A list of tuples, each containing (amount, from_currency, to_currency, converted_amount).
    """
    results = []
    for amount, from_currency, to_currency in amounts:
        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        if converted_amount is not None:
            results.append((amount, from_currency, to_currency, converted_amount))
    return results


def format_result(result: Tuple[float, str, str, float]) -> str:
    """Formats a single conversion result for printing."""
    amount, from_currency, to_currency, converted_amount = result
    return f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"


#Example usage (for testing purposes):
if __name__ == "__main__":
    rates = fetch_exchange_rates("KES") #Fetch rates with KES as base
    if rates:
        print(f"Exchange rates (base: KES): {rates}")
        batch_results = batch_convert([(100, "KES", "USD"), (50, "USD", "KES"), (200, "EUR", "KES")], rates)
        for result in batch_results:
            print(format_result(result))

```

Remember to replace `"YOUR_API_KEY_HERE"` with a valid API key from exchangerate-api.com.  This `utils.py` file provides the core functionality for currency conversion.  You would then build a CLI or GUI on top of these functions.  Error handling is included for API requests, JSON decoding, and invalid currency codes.  The batch conversion function efficiently handles multiple conversions.  The `format_result` function improves output readability.  The example usage at the end demonstrates how to utilize the functions.
