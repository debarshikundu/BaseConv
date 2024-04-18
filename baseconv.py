class Converter:
    @staticmethod
    def binary_to_decimal(binary):
        decimal = 0
        power = len(binary) - 1
        for digit in binary:
            decimal += int(digit) * (2 ** power)
            power -= 1
        return decimal

    @staticmethod
    def decimal_to_binary(decimal):
        binary = ""
        if decimal == 0:
            return "0"
        while decimal > 0:
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal //= 2
        return binary


# Example usage:
binary_number = "101010"
decimal_number = 42

print("Binary to Decimal:")
print(f"{binary_number} in decimal is: {Converter.binary_to_decimal(binary_number)}")

print("\nDecimal to Binary:")
print(f"{decimal_number} in binary is: {Converter.decimal_to_binary(decimal_number)}")
