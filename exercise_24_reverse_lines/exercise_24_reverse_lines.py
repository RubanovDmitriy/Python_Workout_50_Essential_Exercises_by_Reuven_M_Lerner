def reverse_lines(input_file, output_file):
    with open(input_file) as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(f'{line.rstrip()[::-1]}\n')
