# -*- coding:utf-8 -*- 

from tushare.stock import reference as rf

if __name__ == '__main__':
    df = rf.profit_data(top=60)
    print df[df.shares>=10]