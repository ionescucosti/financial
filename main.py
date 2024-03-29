from calculation import calculate_statistics

# Function to read the input file and perform calculations
def process_input_file(file_path):
    try:
        with open(file_path, "r") as file_data:
            data = file_data.read()
            return calculate_statistics(data)
    except Exception as e:
        return e


if __name__ == '__main__':
    print(process_input_file("example_input.txt"))
