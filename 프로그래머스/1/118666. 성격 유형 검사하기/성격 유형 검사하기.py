def solution(survey, choices):
    surveyDict = {"R":0, "T":0, "F":0, "C":0, "M":0, "J":0, "A":0, "N":0}
    surveyList = ["R", "T", "C", "F", "J", "M", "A", "N"]
    rlt = ''
    for i in range(len(choices)):
        choice = choices[i] - 4
        if choice > 0:
            surveyDict[survey[i][0]] += choice
        elif choice < 0:
            surveyDict[survey[i][0]] += choice
    for i in range(0, 8, 2):
        if surveyDict[surveyList[i]] <= surveyDict[surveyList[i+1]]:
            rlt += surveyList[i]
        else:
            rlt += surveyList[i+1]
    
    return rlt