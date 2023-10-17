import paq

# Initialize variables
c = 0  # You might want to define the 'c' variable appropriately
X1 = X2 = X3 = X4 = X5 = b = a = X6 = X7 = X8 = X9 = X10 = 0
Y = [0] * 35000  # Initialize a list to store Y values

# Define a function to count 255 and 0 bits
def count_bits(x):
    c = x.count
    return c(b'\xff') + c(b'\x00')

# Define a function to count X2 repetitions
def count_x2_repeats(x):
    return x.count(b'\xff\xff') + x.count(b'\x00')

# Prompt the user to choose between compression and extraction
user_option = input("Choose an option: (1) Compress (2) Extract: ")

if user_option not in ['1', '2']:
    print("Invalid option. Please choose (1) Compress or (2) Extract.")
else:
    num_iterations = 10  # Perform 10 iterations

    for _ in range(num_iterations):
        # Loop through Y1 to Y35000
        for Y_counter in range(1, 35001):
            # Loop based on the number of outer repetitions
            num_repetitions_outer = 1000 # Repeat the circle 1000 times
            num_repetitions_outer_times=0

            for _ in range(num_repetitions_outer):
                # Reset variables X1 to X10 at the beginning of each repetition
                X1 = X2 = X3 = X4 = X5 = X6 = X7 = X8 = X9 = X10 = 0
                
                

                # Ask the user for input and output file names
                num_repetitions_outer_times+=1
                #print(num_repetitions_outer1)
                if num_repetitions_outer_times==1:
                    input_file_name = input("Enter the name of the input file: ")
                    output_file_name = input("Enter the name of the output file: ")
                else:
                    input_file_name=output_file_name
                    output_file_name=output_file_name
                    

                try:
                    # Attempt to open the input file
                    with open(input_file_name, 'rb') as file:
                        data = file.read()

                    if user_option == '1':
                        # Perform compression
                        compressed_data = paq.compress(data)
                    elif user_option == '2':
                        # Perform extraction
                        compressed_data = paq.decompress(data)

                    # Write the result to the output file
                    with open(output_file_name, 'wb') as file:
                        file.write(compressed_data)

                    # Count 255 and 0 bits added
                    a = count_bits(compressed_data)
                    b += a

                    # Count repetitions of X2
                    X5 += count_x2_repeats(compressed_data)

                    # Update counters and flags
                    X3 += 1
                    X4 += 1

                    # Extend X6 to X10 as needed
                    X6 += a  # Count of 255 bits added
                    X7 += b  # Count of 0 bits added
                    X8 += X1  # Extend X8 as needed
                    X9 += X2  # Extend X9 as needed
                    X10 += X3  # Extend X10 as needed

                    # Check if the current Y variable (Y_counter) is 311
                    if Y[Y_counter - 1] == 311:
                        # Perform specific operations for Y equals 311
                        print(f"Y{Y_counter} reached 311!")

                except FileNotFoundError:
                    print(f"File {input_file_name} not found. Please make sure the file exists.") 