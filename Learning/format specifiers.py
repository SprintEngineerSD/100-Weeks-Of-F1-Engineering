# format specifiers = [value : flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places
# :(number) = allocate that many places
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator


price = 8283.1795

print(f"price is ${price:1f}")
print(f"price is ${price:10}")
print(f"price is ${price:010}")
print(f"price is ${price:<10}")
print(f"price is ${price:>10}")
print(f"price is ${price:^10}")
print(f"price is ${price:+}")
print(f"price is ${price:,}")






