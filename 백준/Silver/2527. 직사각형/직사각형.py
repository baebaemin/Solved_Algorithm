for _ in range(4):
    Ax, Ay, Ap, Aq, Bx, By, Bp, Bq = map(int, input().split())
    if Ax > Bp or Ap < Bx or Ay > Bq or Aq < By:
        print('d')
    elif Ax == Bp or Ap == Bx: # 밑변/아랫변이 맞닿아있을 때
        print('b') if Ay != Bq and Aq != By else print('c')
    elif Ay == Bq or Aq == By: # 왼쪽/오른쪽 변이 맞닿아있을 때
        print('b') if Ap != Bx and Ax != Bp else print('c')
    else: print('a')