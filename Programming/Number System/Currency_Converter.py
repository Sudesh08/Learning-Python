# Currency Converter
# Convert rupees to dollars (or vice versa) using a conversion rate.

print("Currency Converter")
print("Press 1 : Convert Rupees to Dollar")
print("Press 2 : Convert Dollar to Rupees")

value=int(input())


def convert_rupee_to_dollar(r):
    return r/83


def convert_dollar_to_rupee(d):
    return d*83


match value:
    case 1:
        rupee=int(input("Enter amount in rupees: "))
        print(convert_rupee_to_dollar(rupee), " Dollar")
    case 2:
        dollar=input("Enter amount in dollar: ")
        print(convert_dollar_to_rupee(dollar), " Rupees")