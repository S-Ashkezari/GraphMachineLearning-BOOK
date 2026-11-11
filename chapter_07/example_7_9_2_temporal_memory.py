"""نمونه‌ی ساده‌ی حافظه‌ی زمانی با زوال؛ پیاده‌سازی کامل TGN نیست
Run: python chapter_07/example_7_9_2_temporal_memory.py

"""
import numpy as np
# Toy exponential memory, not a full TGN implementation.
events=[('v','u',1.),('v','u',2.),('v','w',3.)];memory={k:0. for k in ['u','v','w']};last={k:0. for k in memory}
for a,b,t in events:
    for node in [a,b]:memory[node]=np.exp(-(t-last[node]))*memory[node]+1;last[node]=t
    print('Time',t,'memory',memory.copy())
