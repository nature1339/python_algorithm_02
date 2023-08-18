# 1. 문자열을 입력 받는다
# 2. 앞뒤 공백을 제거한다
# 3. 공백 기준으로 split하여 리스트로 변환한다
# 4. 리스트 요소 개수 카운트
n = input()
n = n.strip()
l = n.split()
print(len(l))
