user_input = input("Enter v0, v1, and t: ")
initial_vel, final_vel, time = [float(x) for x in user_input.split(",")]

acceleration = (final_vel - initial_vel) / time

print(f"The average acceleration is {acceleration:.4f}")