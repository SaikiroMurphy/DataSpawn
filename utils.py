import random
import cv2
import os

cropPath = r"C:\Users\ASUS\Downloads\ANH QUET BAI THIv6\ANH QUET BAI THI\boxes"


def randV(amtV, amtH, rd, xNew, yNew, radius, y, w, h, count, path):
     for col in range(0, int(amtV)):
         draw = None

         for row in range(0, int(amtH)):
             mark = []

             rand = random.uniform(0.1, 1.0)

             if rand <= 0.3:
                 cropImg = cv2.imread(os.path.join(cropPath, str(random.randint(1, 2449)) + '.jpg'))
                 cropImg = cv2.resize(cropImg, (radius*2, radius*2), interpolation=cv2.INTER_CUBIC)

                 rd[int(yNew-radius):int(yNew+radius), int(xNew-radius):int(xNew+radius)] = cropImg
                 draw = cropImg

                 with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'r')) as read:
                     data = read.readlines()

                     for line in data:
                         mark = writeFile(line, xNew, yNew, rd, radius, mark)

                 with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'w')) as write:
                     for i in mark:
                         write.write(i)

                 break

             yNew += h

         if draw is None:
             write = drawEnd(h, xNew, yNew, rd, radius, count, path)

         xNew += w
         yNew = y

     return rd



def randH(amtV, amtH, rd, xNew, yNew, radius, x, w, h, count, path):
    for row in range(0, int(amtH)):
        draw = None
        for col in range(0, int(amtV)):
            mark = []

            rand = random.uniform(0.1, 1.0)

            if rand <= 0.35:
                cropImg = cv2.imread(os.path.join(cropPath, str(random.randint(1, 2449)) + '.jpg'))
                cropImg = cv2.resize(cropImg, (radius * 2, radius * 2), interpolation=cv2.INTER_CUBIC)

                rd[int(yNew - radius):int(yNew + radius), int(xNew - radius):int(xNew + radius)] = cropImg
                draw = cropImg

                with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'r')) as read:
                    data = read.readlines()

                    for line in data:
                        mark = writeFile(line, xNew, yNew, rd, radius, mark)

                with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'w')) as write:
                    for i in mark:
                        write.write(i)

                break

            xNew += w

        if draw is None:
            mark = []

            xNew = xNew - w
            cropImg = cv2.imread(os.path.join(cropPath, str(random.randint(1, 2449)) + '.jpg'))
            cropImg = cv2.resize(cropImg, (radius * 2, radius * 2), interpolation=cv2.INTER_CUBIC)

            rd[int(yNew - radius):int(yNew + radius), int(xNew - radius):int(xNew + radius)] = cropImg

            with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'r')) as read:
                data = read.readlines()

                for line in data:
                    mark = writeFile(line, xNew, yNew, rd, radius, mark)

            with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'w')) as write:
                for i in mark:
                    write.write(i)

        yNew += h
        xNew = x

    return rd



def randS(amtV, amtH, rd, xNew, yNew, radius, y, w, h, count, path):
    negative = False
    comma = False

    for col in range(0, int(amtV)):
        draw = None

        for row in range(0, int(amtH)):
            mark = []

            color = random.randint(-60, 60)

            if col == 0 and row == 1:
                yNew += h
                continue

            if (col == 1 or col == 2 or col == 3) and row == 0:
                yNew += h
                continue

            if col == 3 and row == 1:
                yNew += h
                continue

            rand = random.uniform(0.1, 1.0)

            if rand <= 0.3:
                if col == 1 and row == 1 and negative == True:
                    yNew += h
                    continue

                elif col == 2 and row == 1 and comma == True:
                    yNew += h
                    continue

                else:
                    cropImg = cv2.imread(os.path.join(cropPath, str(random.randint(1, 2449)) + '.jpg'))
                    cropImg = cv2.resize(cropImg, (radius * 2, radius * 2), interpolation=cv2.INTER_CUBIC)

                    rd[int(yNew - radius):int(yNew + radius), int(xNew - radius):int(xNew + radius)] = cropImg
                    draw = cropImg

                    with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'r')) as read:
                        data = read.readlines()
                        for line in data:
                            mark = writeFile(line, xNew, yNew, rd, radius, mark)

                    with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'w')) as write:
                        for i in mark:
                            write.write(i)

                    if col == 0 and row == 0:
                        negative = True

                    if col == 1 and row == 1:
                        comma = True

                    break

            yNew += h

        if draw is None:
            write = drawEnd(h, xNew, yNew, rd, radius, count, path)

        xNew += w
        yNew = y

    return rd



def writeFile(line, xNew, yNew, rd, radius, mark):
    split = line.split(" ")
    if float(split[1]) == float((xNew * (1. / rd.shape[1]))) and float(
            split[2]) == float((yNew * (1. / rd.shape[0]))):
        mark.append(f"3 {xNew * (1. / rd.shape[1])} {yNew * (1. / rd.shape[0])} "
                    f"{(radius + 2) * 2 * (1. / rd.shape[1])} {(radius + 2) * 2 * (1. / rd.shape[0])}\n")
    else:
        mark.append(line)

    return mark



def drawEnd(h, xNew, yNew, rd, radius, count, path):
    mark = []
    yNew = yNew - h

    cropImg = cv2.imread(os.path.join(cropPath, str(random.randint(1, 2449)) + '.jpg'))
    cropImg = cv2.resize(cropImg, (radius * 2, radius * 2), interpolation=cv2.INTER_CUBIC)

    rd[int(yNew - radius):int(yNew + radius), int(xNew - radius):int(xNew + radius)] = cropImg
    draw = cropImg

    with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'r')) as read:
        data = read.readlines()
        for line in data:
            mark = writeFile(line, xNew, yNew, rd, radius, mark)

    with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'w')) as write:
        for i in mark:
            write.write(i)

    return write
