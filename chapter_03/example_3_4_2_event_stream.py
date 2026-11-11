"""جریان پیام و دسترسی زمانی؛ داده‌ی مصنوعی آموزشی
Run: python chapter_03/example_3_4_2_event_stream.py

"""
events=[('A','B',1),('B','C',3),('A','C',4)]
arrival={'A':0}
for u,v,t in sorted(events,key=lambda e:e[2]):
    if arrival.get(u,float('inf'))<=t:arrival[v]=min(arrival.get(v,float('inf')),t)
print('Events:',events);print('Earliest arrival from A:',arrival)
assert arrival['C']==3
