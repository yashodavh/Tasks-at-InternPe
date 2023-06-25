from forex python.converter import CurrencyRates

cr=CurrencyRates()
amount=int(input("please enter the amount you want to convert"))
from_currency=input("please enter the currency code that has to be converted:")
to_currency=input("please enter the  currency code to convert: ").upper()
print("you are converting ",amount,from_currency,"to",to_currency,".")
output=cr.convert(from_currency,to_currency,amount)
print("the converted rate is:",output)
