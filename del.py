import os

path = [r"E:\OneDrive - bkacad.edu.vn\Documents\PhieuTN\exam\labels\train", r"E:\OneDrive - bkacad.edu.vn\Documents\PhieuTN\exam\labels\val"]
count = 1
for i in path:
    for file in os.listdir(i):
        with (open(os.path.join(i, file), 'r+')) as read:
            data = read.readlines()
            read.seek(0)
            for line in data:
                if line[0] != '4':
                    read.write(line)

            read.truncate()

        print(count)
        count += 1

    count = 1