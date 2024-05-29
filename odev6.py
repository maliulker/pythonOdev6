import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sabitler
MIN_VALUE: int = 0
MAX_VALUE: int = 2000  # değer aralığı
POINT_COUNT: int = 5000  # nokta sayısı
GRID_SIZE: int = 250  # daha ufak grid boyutu
GROUP_COUNT: int = MAX_VALUE // GRID_SIZE

if __name__ == "__main__":

    points = np.random.randint(MIN_VALUE, MAX_VALUE, size=(POINT_COUNT, 2))  # random nokta oluşturdum

    df = pd.DataFrame(points, columns=["X", "Y"])
    df.to_excel("points.xlsx", index=False)  # burda excele kaydettim datafram'lerimi, önce dataframe dönüştürdüm

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title("Random Points Distribution", fontsize=16)

    ax.set_xlabel("X Coordinate")
    ax.set_xticks(np.arange(MIN_VALUE, MAX_VALUE + 1, GRID_SIZE))
    ax.set_xlim([MIN_VALUE, MAX_VALUE])

    ax.set_ylabel("Y Coordinate")
    ax.set_yticks(np.arange(MIN_VALUE, MAX_VALUE + 1, GRID_SIZE))
    ax.set_ylim([MIN_VALUE, MAX_VALUE])

    ax.grid(True)

    groups = [[[] for _ in range(GROUP_COUNT)] for _ in range(GROUP_COUNT)]
    for point in points:
        x, y = point
        x //= GRID_SIZE
        y //= GRID_SIZE
        groups[x][y].append(point)

    colors = np.random.rand(GROUP_COUNT, GROUP_COUNT, 3)  # gruplar için random değerler
    for x in range(GROUP_COUNT):
        for y in range(GROUP_COUNT):
            for point in groups[x][y]:
                ax.scatter(point[0], point[1], color=colors[x][y], s=10, alpha=0.75)

    plt.show()
