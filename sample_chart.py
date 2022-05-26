
import pandas as pd
import plotly.express as px


df  = pd.DataFrame({
    'x': ['A','B','C','D','E'],
    'y': [10, 25, 89, 76, 90],
    'z': [30,40,45,60,55]
})

def barChart(df,w, h,x,y) :

    fig_bar = px.bar(df, x=x, y=y,title="Bar Chart", width=w, height=h)
    fig_bar.update_layout(
    margin=dict(l=0,r=0,t=40,b=0),
    paper_bgcolor='RGB(167, 178, 196)',
    plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_bar
def lineChart(df,w,h,x,y) :
    fig_line = px.line(df, x=x, y=y,title='Line Chart', width=w, height=h)
    fig_line.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_line
def areaChart(df,w,h,x,y) :
    fig_area = px.area(df, x=x, y=y,title='Area Chart', width=w, height=h)
    fig_area.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_area

def boxChart(df,w,h,x,y):
    fig_box = px.box(df,x=x, y=y, title='Box Chart', width=w, height=h)
    fig_box.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        # paper_bgcolor="RGB(168,247,226)"
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_box

def funnelChart(df,w,h,x,y) :
    fig_funnel = px.funnel(df, x=x, y=y, title='Funnel Chart', width=w, height=h)
    fig_funnel.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_funnel

def scatterChart(df,w,h,x,y):
    fig_scatter = px.scatter(df, x=x, y=y, title='Scatter Chart', width=w, height=h)
    fig_scatter.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_scatter


def line3DChart(df,w,h,x,y,z):
    fig_3DLine = px.line_3d(df,  x=x, y=y,z=z, title='3D Line Chart', width=w, height=h)
    fig_3DLine.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_3DLine


def histogramChart(df,w,h,x,y):
    fig_histogram = px.histogram(df, x=x, y=y, title='Histogram Chart', width=w, height=h)
    fig_histogram.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_histogram

def scatter3DChart(df,w,h,x,y,z):
    fig_Scatter3D = px.scatter_3d(df,  x=x, y=y, z=z, title='3D Scatter Chart', width=w, height=h)
    fig_Scatter3D.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_Scatter3D

def heatmapChart(df,w,h,x,y,z):
    fig_Heat = px.density_heatmap(df, x=x,  y=y, z=z, title='Heat Chart', width=w, height=h,)
    fig_Heat.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_Heat

def pieChart(df,w,h,x):
    fig_Pie = px.pie(df,str(x), title='Pie Chart', width=w, height=h)
    fig_Pie.update_layout(
        margin=dict(l=0,r=0,t=40,b=0),
        paper_bgcolor='RGB(167, 178, 196)',
        plot_bgcolor='RGB(167, 178, 196)',
    )
    return fig_Pie



