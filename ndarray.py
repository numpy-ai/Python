import numpy as np

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]; print(x) # 2차원 배열 생성 후 출력
arr_x = np.array(x); print(arr_x) # Numpy의 ndarray로 변환 후 출력

arr_y = np.eye(3); print(arr_y) # 주 대각 성분이 1 나머지가 0인 단위 행렬 생성 후 출력

dot_xy = np.add(arr_x, arr_y); print(dot_xy) # 행렬 덧셈