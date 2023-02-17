from datetime import *

str_time = '20230112'
t = datetime.strptime(str_time, '%Y%m%d').date()
print(t)
offset=timedelta(days=2)
t0=(t+offset).strftime('%Y%m%d')
print(t0)