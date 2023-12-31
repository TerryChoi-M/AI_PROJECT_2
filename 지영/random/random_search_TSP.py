# 무작위 탐색을 이용한 TSP 문제 해결
# --------------------------------
# 최단 거리: 42268.705345396564
# 실행 시간: 138.83111476898193 초
# --------------------------------

import csv 
import random
import math
import time

start_time = time.time()

# 파일에서 도시 위치 불러오기
with open('2023_AI_TSP.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    locations = [(float(row[0]), float(row[1])) for row in reader]

# 함수 정의: 두 도시 사이의 거리 계산
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 인덱스로부터 좌표값을 가져오는 함수 정의
def get_coordinates(path, locations):
    return [locations[i] for i in path]

# 인덱스로부터 도시 이름을 가져오는 함수 정의
def get_city_names(path):
    return [f"{i}" for i in path]

# 완전 무작위 탐색으로 TSP 문제 풀기
def random_search(cities):
    num_cities = len(cities)
    current_path = [0] + list(range(1, num_cities))  # 초기 경로: 0번 도시부터 시작
    best_path = current_path[:]  # 초기 최적 경로: 0번 도시부터 시작
    best_distance = sum(distance(cities[current_path[i]], cities[current_path[(i+1)%num_cities]]) for i in range(num_cities))

    for i in range(1000):  # 1000번 반복
        random.shuffle(current_path[1:])  # 경로 임의 섞기 (0번 도시는 고정)
        current_path = [0] + current_path[1:]  # 시작 노드는 0번 도시로 고정
        current_distance = sum(distance(cities[current_path[i]], cities[current_path[(i+1)%num_cities]]) for i in range(num_cities))
        if current_distance < best_distance:  # 현재 경로가 더 짧으면 최적 경로 갱신
            best_path = current_path[:]
            best_distance = current_distance
        else:
            # 현재 경로가 더 길면 무작위로 2개의 도시 위치를 바꿔서 경로 변경
            idx1, idx2 = random.sample(range(1, num_cities), 2)
            current_path[idx1], current_path[idx2] = current_path[idx2], current_path[idx1]

    best_city_names = get_city_names(best_path)
    return best_city_names, best_distance

# 결과 출력
best_city_names, best_distance = random_search(locations)
print('최적 경로:', best_city_names)
print('최단 거리:', best_distance)
