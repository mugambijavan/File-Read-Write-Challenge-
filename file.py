def process_file(input_filename="input.txt", output_filename="output.txt"):
    """Reads an input file, adds line numbers, and writes to an output file."""
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line_number, line in enumerate(infile, 1):
                outfile.write(f"{line_number}: {line}")
        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file()