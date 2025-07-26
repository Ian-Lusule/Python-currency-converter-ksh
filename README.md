# python-currency-converter-ksh

**A real-time currency converter for the Kenyan Shilling (KSH) and major world currencies.**

## Description

This project provides a Python-based currency converter that fetches real-time exchange rates from a public API (exchangerate-api.com) and allows users to convert between the Kenyan Shilling (KSH) and other major currencies.  The application features a user-friendly interface (CLI), handles errors gracefully, and supports batch conversions for efficient multiple currency exchanges.

## Features

* **Real-time exchange rates:** Uses a public API for up-to-date exchange rate data.
* **Kenyan Shilling (KSH) support:**  Includes KSH as a primary currency for conversion.
* **Major currency support:**  Supports conversion to and from a wide range of major world currencies.
* **Batch conversion:** Allows users to convert multiple currency amounts simultaneously.
* **Error handling:** Gracefully handles API errors and invalid inputs.
* **User-friendly CLI:** Provides a simple and intuitive command-line interface.
* **Open-source:**  Available under the MIT License for community contribution and use.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ian-Lusule/python-currency-converter-ksh.git
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
  
## Usage

1. **Run the script:**
   ```bash
   python main.py
   ```
2. **Follow the CLI prompts:** The script will guide you through the conversion process.  You will be asked to specify:
    * The source currency.
    * The target currency.
    * The amount to convert.
    * For batch conversion, provide a list of amounts separated by commas.


**Example CLI interaction:**

```
Welcome to the Currency Converter!

Enter source currency (e.g., USD, KSH): USD
Enter target currency (e.g., KSH, EUR): KSH
Enter amount to convert: 100
100 USD is equivalent to 14000.0 KSH (based on the latest exchange rate).

Do you want to perform another conversion? (y/n): y
... (further interactions) ...
```


## Contributing Guidelines

We welcome contributions to improve this project!  Please follow these guidelines:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Make your changes** and ensure they are well-documented.
4. **Test your changes** thoroughly.
5. **Submit a pull request** with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## API Key (exchangerate-api.com)

You will need to obtain an API key from exchangerate-api.com and set the environment variable `EXCHANGE_RATE_API_KEY` before running the application.  Instructions on how to obtain an API key can be found on their website.  Example (bash):

```bash
export EXCHANGE_RATE_API_KEY="your_api_key_here"
```


## Error Handling

The application includes robust error handling for various scenarios, including:

* **Invalid currency codes:**  The program will inform the user if an invalid currency code is entered.
* **API connection errors:**  If the API is unavailable, a clear error message will be displayed.
* **Invalid input types:** The program will check for non-numeric input for amounts.


This README will be updated as the project evolves.  Please check back for the latest information.
