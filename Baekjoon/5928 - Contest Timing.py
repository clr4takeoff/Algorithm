#B4_5928_Contest Timing

d, h, m = map(int, input().split())
start_d, start_h, start_m = 11, 11, 11
end = (d - start_d) * 1440 + (h - start_h) * 60 + (m - start_m)
print(end if end >= 0 else -1)
