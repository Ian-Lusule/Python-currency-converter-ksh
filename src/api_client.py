```python
# src/api_client.py

import requests
import json
from typing import Dict, List, Tuple

class ApiClient:
    """
    A client for fetching real-time exchange rates from a public API.  Currently uses exchangerate-api.com.  
    Remember to replace 'YOUR_API_KEY' with your actual API key.
    """

    def __init__(self, api_key: str = "YOUR_API_KEY"):  # Replace with your API key
        self.base_url = "https://v6.exchangerate-api.com/v6/"
        self.api_key = api_key
        self.headers = {"apikey": self.api_key}

    def _make_request(self, endpoint: str, params: Dict = None) -> Dict:
        """Makes a request to the exchangerate-api.com API."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            raise ApiClientError(f"API request failed: {e}") from e
        except json.JSONDecodeError as e:
            raise ApiClientError(f"Invalid JSON response: {e}") from e


    def get_latest_rates(self, base_currency: str = "USD") -> Dict:
        """
        Fetches the latest exchange rates for all currencies relative to a base currency.

        Args:
            base_currency: The base currency (e.g., "USD", "EUR", "KES"). Defaults to "USD".

        Returns:
            A dictionary containing exchange rates.  Keys are currency codes, values are exchange rates.
            Returns an empty dictionary if an error occurs.

        Raises:
            ApiClientError: If there's an issue with the API request or response.
        """
        try:
            data = self._make_request(f"latest/{base_currency}")
            if data['result'] == 'success':
                return data['conversion_rates']
            else:
                raise ApiClientError(f"API request failed: {data['message']}")

        except ApiClientError as e:
            print(f"Error fetching exchange rates: {e}")
            return {}


    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Converts an amount from one currency to another."""
        rates = self.get_latest_rates()
        if not rates:
            return 0  # Handle case where rate fetching failed

        if from_currency not in rates or to_currency not in rates:
            raise ApiClientError(f"One or both currencies ({from_currency}, {to_currency}) not found.")

        try:
            return amount * (rates[to_currency] / rates[from_currency])
        except KeyError as e:
            raise ApiClientError(f"Error during conversion: {e}") from e


    def convert_batch(self, conversions: List[Tuple[float, str, str]]) -> List[Tuple[float, str, str, float]]:
        """
        Performs batch currency conversions.

        Args:
            conversions: A list of tuples, each containing (amount, from_currency, to_currency).

        Returns:
            A list of tuples, each containing (amount, from_currency, to_currency, converted_amount).
            Returns an empty list if an error occurs during rate fetching.
        """
        rates = self.get_latest_rates()
        if not rates:
            return []

        results = []
        for amount, from_curr, to_curr in conversions:
            try:
                converted_amount = self.convert_currency(amount, from_curr, to_curr)
                results.append((amount, from_curr, to_curr, converted_amount))
            except ApiClientError as e:
                print(f"Error converting {amount} {from_curr} to {to_curr}: {e}")
                results.append((amount, from_curr, to_curr, 0)) #Append with 0 on error

        return results


class ApiClientError(Exception):
    """Custom exception for API client errors."""
    pass

```