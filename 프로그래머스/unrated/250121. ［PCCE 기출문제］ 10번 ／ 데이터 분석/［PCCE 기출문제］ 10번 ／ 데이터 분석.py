def solution(data, ext, val_ext, sort_by):
    keyword = ["code", "date", "maximum", "remain"]
    idx = keyword.index(ext)
    sort_idx = keyword.index(sort_by)
    rlt = []
    for d in data:
        if d[idx] < val_ext:
            rlt.append(d)
    ans = sorted(rlt, key=lambda x: x[sort_idx])
    return ans