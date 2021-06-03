def avg_run_time():
    resulted_run_time = []

    while True:
        one_run = input('Enter 10 km run time: ')
        if not one_run:
            break

        try:
            resulted_run_time.append(float(one_run))
        except ValueError as e:
            print(f'Hey! {e}\'s not a valid number!')

    average_run_time = sum(resulted_run_time) / len(resulted_run_time)

    return print(f'Average of {average_run_time}, over {len(resulted_run_time)} runs')
