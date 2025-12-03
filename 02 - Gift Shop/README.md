
We need to split the ranges up, e.g.

12-2050 -> 12-99, 100-999, 1000-2050

N=len(str(start))
M=len(str(end))
l=N

ranges = []
n0 = start
n1 = min(end, '9'*l)
while True:
    ranges.append((n0, n1))

    l += 1
    if l > M:
        break

    n0 = n1+1
    n1 = min(end, '9'*l)
    

============================
Given a range r0-r1:
- rr0 = int()