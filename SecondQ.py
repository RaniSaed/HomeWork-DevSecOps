count = 0  #
total = 0  #

while True:
    num = int(input(f"Please enter number #{count + 1}: "))

    if num < 0:
        print("Thank you. Goodbye.")
        break

    count += 1
    total += num
    avg = total / count

    print(f"Please enter number #{count + 1} (avg={avg:.1f}, Sum={total}): ", end="")
