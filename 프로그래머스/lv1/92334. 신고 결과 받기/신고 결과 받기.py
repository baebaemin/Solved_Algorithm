def solution(id_list, report, k): 
    reporter_dict = {}
    reported_dict = {}
    answer = []
    
    for id in id_list:
        reporter_dict[id] = 0 # key: 신고자 / values: 신고대상
        reported_dict[id] = [] # key: 신고당한자 / values: 신고한사람
        
    for rep in report:
        reporter, reported = map(str, rep.split())
        reported_dict[reported].append(reporter)
    
    for key in reported_dict:
        reported_dict[key] = set(reported_dict[key]) 
        # key와 key를 신고한 유저의 id들
        if len(reported_dict[key]) >= k:
            for id in reported_dict[key]:
                reporter_dict[id] += 1
    
    for id in reporter_dict:
         answer.append(reporter_dict[id])
    return answer