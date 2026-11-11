"""فعال‌بودن یال تماس از ۱۰:۰۵ تا ۱۰:۱۵؛ قرارداد بازه‌ی بسته
Run: python chapter_03/example_3_4_3_interval_edge.py

"""
start,end=10*60+5,10*60+15
for hour,minute in [(10,4),(10,5),(10,12),(10,15),(10,16)]:
    t=60*hour+minute
    print(f'{hour:02}:{minute:02}: active = {start<=t<=end}')
