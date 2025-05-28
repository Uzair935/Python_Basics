def walk(steps):
    if steps == 0:
        return
    walk(steps-1)
    print(f"You take step {steps}")
walk(1000)