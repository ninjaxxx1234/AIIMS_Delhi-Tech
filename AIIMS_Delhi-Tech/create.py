def create_text_file(file_name, values):
    try:
        # Open the file in write mode ('w')
        with open(file_name, 'w') as file:
            # Write values to the file
            file.write(str(values) + '\n')
        #print(f"Values have been written to '{file_name}'.")
    except IOError:
        print(f"Error: Could not write to '{file_name}'.")

# Example usage:
