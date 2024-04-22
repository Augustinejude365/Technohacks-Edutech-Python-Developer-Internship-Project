#!/usr/bin/env python3
import requests


def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'].get(to_currency)
    else:
        return None


def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is not None:
        converted_amount = amount * rate
        return converted_amount
    else:
        return "Unable to perform conversion. Please check the \
                currencies provided."


if __name__ == "__main__":
    amount = float(input("Enter amount to convert: "))
    from_currency = input("Enter the currency you have (3-lettercode, e.g., USD, EUR, NGN, CAD, CHF, CNY, GBP, INR, AUD, AED): ").upper()
    to_currency = input("Enter the currency you want to convert to (3-letter code, e.g., USD, EUR, NGN, CAD, CHF, CNY, GBP, INR, AUD, AED, CHF): ").upper()
    result = convert_currency(amount, from_currency, to_currency)
    if isinstance(result, float):
        print("{:.2f} {} is equal to {:.2f} {}".format(amount,
              from_currency, result, to_currency))
    else:
        print(result)
