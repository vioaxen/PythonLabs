x = -123.45678
formatted_x = f"{x:.3e}" if x < 0 else f"{x:.5e}"
print(formatted_x)