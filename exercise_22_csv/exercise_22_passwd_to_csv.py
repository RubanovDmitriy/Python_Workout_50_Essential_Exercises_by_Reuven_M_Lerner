import csv


def passwd_to_csv(pswd_filename, csv_filename):
    users = []
    with open(pswd_filename) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users.append({'username': user_info[0], 'user_id': int(user_info[2])})

    with open(csv_filename, mode='w') as csv_file:
        fieldnames = ['username', 'user_id']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')

        writer.writeheader()
        for element in users:
            writer.writerow(element)
