goX = goY = 0
X, Y, W, H = map(int, input().split())

def compare(XY, WH):
    return XY if XY <= WH / 2 else WH - XY

print(min(compare(X, W), compare(Y, H)))