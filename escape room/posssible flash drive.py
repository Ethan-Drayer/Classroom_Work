import time

# The correct code (you can replace this with the real target code)
correct_code = "123456"  # The actual code to unlock


# Function to simulate brute force check
def brute_force_check():
    # Start from 000000 and increment until 999999
    for i in range(1000000):  # 000000 to 999999 (6-digit range)
        code = str(i).zfill(6)  # Ensure the code is always 6 digits long (e.g., 000001, 000002)
        print(f"Trying code: {code}")  # Optional: Print the attempted code for visibility
        time.sleep(0.1)  # Simulate delay, remove or adjust as needed

        if code == correct_code:
            print(f"Success! The correct code is {code}")
            with open("found_code.txt", "w") as f:  # Write the correct code to a file
                f.write(code)
            return True
    print("Brute force attempt failed. Code not found.")
    return False


# Run brute force check
if __name__ == "__main__":
    brute_force_check()
