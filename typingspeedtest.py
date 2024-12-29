from time import time
import random as r

def mistake(partest, usertest):
    """Calculate the number of mistakes in the user's input."""
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except IndexError:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    """Calculate the typing speed in characters per second."""
    timedelay = time_e - time_s
    speed = len(userinput) / timedelay
    return round(speed, 2)

test = [
    "The sun rose above the horizon, casting a warm glow over the quiet town. "]

# Select a random test sentence
tes1 = r.choice(test)

print("************** Typing Speed Test ******************")
print("\nYour task is to type the following text as quickly and accurately as possible:\n")
print(tes1)
print()

# Start timing
time1 = time()
testinput = input("Enter the text above: ")
# End timing
time2 = time()

# Calculate results
errors = mistake(tes1, testinput)
speed = speed_time(time1, time2, testinput)

print("\n****************** Results ******************")
print(f"Original text: {tes1}")
print(f"Your input: {testinput}")
print(f"Time taken: {round(time2 - time1, 2)} seconds")
print(f"Number of mistakes: {errors}")
print(f"Typing speed: {speed} characters per second")
