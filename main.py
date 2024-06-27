import os
import random
import cv2
import numpy as np
from tqdm import tqdm
import utils

path = "E:\OneDrive - bkacad.edu.vn\Documents\PhieuTN"

count = 1
for q in tqdm(range(0,1100)):
    for file in os.listdir(path):
        if file.endswith(".jpg") or file.endswith(".png"):

            rd = cv2.imread(os.path.join(path, file),cv2.IMREAD_COLOR)

            gamma = random.uniform(0.1, 2.0)
            invGamma = 1.0 / gamma
            table = np.array([((i / 255.0) ** invGamma)
                              * 255 for i in np.arange(0, 256)]).astype("uint8")

            rd = cv2.LUT(rd, table)

            prob = 0.005
            output = np.zeros(rd.shape, np.uint8)
            thres = 1 - prob

            for i in range(rd.shape[0]):
                for j in range(rd.shape[1]):

                    rdn = random.random()

                    if rdn < prob:
                        rd[i][j] = 100

                    elif rdn > thres:
                        rd[i][j] = 200

                    else:
                        rd[i][j] = rd[i][j]

            copy = rd.copy()

            with (open(os.path.join(path, file[:-4] + '.txt')) as conf):

                for line in conf:
                    # print(line)

                    split = line.split(' ')

                    directtion = int(split[0])
                    x = float(split[1])
                    y = float(split[2])
                    w = float(split[3])
                    h = float(split[4])
                    amtV = float(split[5])
                    amtH = float(split[6])
                    radius = int(split[7])

                    xNew = x
                    yNew = y

                    xCent = (x+w*amtV/2-w/2)*(1./rd.shape[1])
                    yCent = (y+h*amtH/2-h/2)*(1./rd.shape[0])
                    wCent = (w*amtV)*(1./rd.shape[1])
                    hCent = (h*amtH)*(1./rd.shape[0])

                    with (open(os.path.join(path, 'exam', "exam_" + str(count) + ".txt"), 'a')) as write:

                        if amtV == 6 and amtH == 10:
                            write.write(f"0 " + str(xCent) + " " + str(yCent)
                                        + " " + str(wCent) + " " + str(hCent) + "\n")

                        elif amtV == 3 and amtH == 10:
                            write.write(f"1 " + str(xCent) + " " + str(yCent)
                                        + " " + str(wCent) + " " + str(hCent) + "\n")

                        else:
                            write.write(f"2 " + str(xCent) + " " + str(yCent)
                                        + " " + str(wCent) + " " + str(hCent) + "\n")

                        for col in range(0, int(amtV)):
                            for row in range(0, int(amtH)):
                                if directtion == 2:
                                    if col == 0 and row == 1:
                                        yNew += h
                                        continue

                                    if (col == 1 or col == 2 or col == 3) and row == 0:
                                        yNew += h
                                        continue

                                    if col == 3 and row == 1:
                                        yNew += h
                                        continue

                                write.write(f"4 {xNew * (1. / rd.shape[1])} {yNew * (1. / rd.shape[0])} "
                                            f"{(radius + 1) * 2 * (1. / rd.shape[1])} {(radius + 1) * 2 * (1. / rd.shape[0])}\n")

                                yNew += h

                            xNew += w
                            yNew = y

                    xNew = x
                    yNew = y

                    # write.close()
                    # exit()

                    if directtion == 0:
                        rd = utils.randV(amtV,amtH,rd, xNew, yNew, radius, y, w, h, count, path)

                    elif directtion == 1:
                        rd = utils.randH(amtV,amtH,rd, xNew, yNew, radius, x, w, h, count, path)

                    else:
                        rd = utils.randS(amtV,amtH,rd, xNew, yNew, radius, y, w, h, count, path)

                trans = rd*0.9 + copy*0.1
                trans = trans.astype("uint8")

                # cv2.imshow(os.path.join(path, file), trans)
                # cv2.waitKey(0)
                cv2.imwrite(os.path.join(path, 'exam', "exam_" + str(count) + ".jpg"), trans)

                # print(count)
                count += 1

print("Images Genaration Complete!")