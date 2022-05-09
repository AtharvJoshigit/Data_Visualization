import pandas as pd
from dash import html,dcc
from dash.dependencies import Output, Input
import layout as ly
import style as stl


need1Data = [9]
need2Data = [1,2,3,4,5,6,8]
need3Data = [7,10,11]


def give_list(df) :
    l=[]
    for i in df.columns :
       l.append(i)
    return l







