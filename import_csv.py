import csv

# with open('test.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['user_id', 'user_name', 'comments_qty'])
#     writer.writerow([5235, 'bogdan', 1352])
#     writer.writerow([5236, 'mike', 1350])
#     writer.writerow([5237, 'alice', 1361])

with open('test.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    print(reader)
    for line in reader:
        print(line)
