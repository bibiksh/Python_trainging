def main():
  MAXN = 100010
  MAXL = 1000010
  ly = [0]*MAXL
  lx = [0]*MAXL
  px = []
  py = []

  N = int(input())

  for i in range(N):
    x, y = map(int, input().split())
    x = x + MAXL // 2
    y = y + MAXL // 2
    px.append(x)
    py.append(y)

  for i in range(N):
    j = (i + 1) % N
    if px[i] == px[j]:
      y1, y2 = py[i], py[j]
      if y1 < y2:
        ly[y1] += 1
        ly[y2] -= 1
      else:
        ly[y2] += 1
        ly[y1] -= 1
    else:
      x1, x2 = px[i], px[j]
      if x1 < x2:
        lx[x1] += 1
        lx[x2] -= 1
      else:
        lx[x2] += 1
        lx[x1] -= 1

  for i in range(MAXL):
    lx[i] = lx[i] + lx[i-1]
    ly[i] = ly[i] + ly[i-1]

  print(max(max(lx),max(ly)))

main()