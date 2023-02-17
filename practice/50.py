import datetime


def get_date_of_year():
    y=input('年')
    m=input('月')
    d=input('日')
    t=datetime.date(int(y),int(m),int(d))
    m_t=datetime.date(int(y),1,1)
    print((t-m_t).days+1)
    print(t-m_t)
if __name__=='__main__':
    get_date_of_year()