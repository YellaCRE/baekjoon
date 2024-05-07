# 29791번 에르다 노바와 오리진 스킬
import sys
input = sys.stdin.readline
IMMUNE = 90


def check_skill_cnt(skill_set, cool):
    skill_cnt = 0
    immune_time = 0
    cool_time = 0
    for timing in skill_set:
        if timing >= immune_time and timing >= cool_time:
            immune_time = timing + IMMUNE
            cool_time = timing + cool
            skill_cnt += 1

    return skill_cnt


N, M = map(int, input().split())
elda_skill_timing = set(map(int, input().split()))
origin_skill_timing = set(map(int, input().split()))

# 기록들이 바람에 날려 뒤죽박죽 섞이게 되었다
elda_sorted_set = sorted(elda_skill_timing)
origin_sorted_set = sorted(origin_skill_timing)

# 에르다 = 행동 불가, 오리진 = 절대 행동 불가
# 에르다 노바의 재사용 대기 시간은 100초, 오리진 스킬의 재사용 대기 시간은 360초다
# 맞으면 각각의 스킬에 대해 90초 동안 면역
# 몬스터가 행동 불가와 절대 행동 불가 상태가 된 횟수를 구하라
print(check_skill_cnt(elda_sorted_set, 100), check_skill_cnt(origin_sorted_set, 360))
