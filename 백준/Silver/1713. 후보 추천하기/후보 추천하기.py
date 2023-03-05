N = int(input())  # frame
P = int(input())  # 사람의 수
frame = [[0,0] for _ in range(N)]  # [[0,0], [0,0], [0,0]]
people = list(map(int, input().split()))

p = 0
while 1:
    if not people or p == N: break
    ppl = []                            # 있는 사람들 리스트
    for v in range(N):
        ppl.append(frame[v][0])
    person = people.pop(0)
    if person not in ppl:               # 액자에 해당 사람이 없다면
        frame[p] = [person, 1]      # 액자에 사람 채우기
        p += 1
    else: frame[ppl.index(person)][1] += 1

for p in range(len(people)):
    f_lst = []
    vote = []
    for v in range(N):
        f_lst.append(frame[v][0])
        vote.append(frame[v][1])
    if people[p] in f_lst:              # 사람이 이미 있다면
        frame[f_lst.index(people[p])][1] += 1  # 투표 추가
    if people[p] not in f_lst:
        frame.remove(frame[vote.index(min(vote))])
        frame.append([people[p], 1])

rlt = [frame[n][0] for n in range(N) if frame[n][0]]
print(*sorted(rlt))