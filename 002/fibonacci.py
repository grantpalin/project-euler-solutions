cap = 3999999
total = 0

# set out starting values in the Fibonacci sequence
previous = 0
current = 1
upcoming = 2

while current < cap:
    # only consider even Fibonacci values under the limit
    if current % 2 == 0 and current < cap:
        total += current
        print(current)

    # shuffle values down
    previous = current
    current = upcoming
    upcoming = previous + current

print(total)