totalamount = 50
usbstickamount=6

num_of_sticks = totalamount // usbstickamount
remaining_amount = totalamount % usbstickamount

print("With $50, she can buy", num_of_sticks, "USB sticks.")

print("She will have $", remaining_amount, "left.")

