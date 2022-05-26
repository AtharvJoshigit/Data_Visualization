import dash
import base64
import io
import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import style as stl
import sample_chart as sc
import dropDown as dd



class Help :
    def __init__(self):
        self.check = False
        self.buttonVal = 0
        self.file = None

    def setButtonValue(self,data):
        self.buttonVal = data
    def getButtonValue(self):
        return self.buttonVal

    def setFile(self,data):
        self.file = data
    def getFile(self):
        return self.file
    def isUploaded(self):
        return self.check
    def uploaded(self):
        self.check = True

help = Help()

app = Dash()



# app layout
app.layout = html.Div(children=[
    html.H1('Open Source Data Visualization',
            style=stl.h1_style),
    html.Div(id='result',style=stl.show_data_style),
    html.Div(id='fileInfo',style=stl.show_data_style),
    html.Div(id="show_data",style=stl.show_data_style),
    html.Div(
        id="data_print",
        children=[
            dcc.Upload(
                id= "file_uploaded",
                children=[
                    html.Div([
                        "Drag and Drop or ",
                        html.A('Select File')
                    ])
                ],
                style=stl.uploader_style,
                multiple=False
            )
        ]),
    html.Div(id='dropDown',style=stl.dropDownDivStyle),
    # html.Div(id='buttonSection',style=stl.btnStyle),
    html.Div(id='finalChart',style=stl.finalChartStyle),
    html.Div(id="chart_update",style=stl.chart_update_style),

    html.Div(children=[
        html.Button(
            id= 'btn_bar',
            # n_clicks='0',
            children=[
            dcc.Graph(
                figure=sc.barChart(sc.df,200,200,'x', 'y'),
                responsive=False,

        )],
            style=stl.sgraph_btn
        ),
        html.Button(
            id= 'btn_line',
            # n_clicks='0',
            n_clicks_timestamp='-1',
            children=[
            dcc.Graph(
                id='chart_btn',
                figure=sc.lineChart(sc.df,200,200,'x', 'y'),
        )],

            style=stl.sgraph_btn
        ),
        html.Button(
            id= 'btn_area',
            # n_clicks='0',
            children=[
            dcc.Graph(
                figure=sc.areaChart(sc.df,200,200,'x', 'y')
        )],
            style=stl.sgraph_btn
        ),
        html.Button(
            id= 'btn_box',
            # n_clicks='0',
            children=[
            dcc.Graph(
                figure=sc.boxChart(sc.df,200,200,'x', 'y')
        )],
            style=stl.sgraph_btn
        ),
        html.Button(
            id= 'btn_funnel',
            # n_clicks='0',
            children=[
            dcc.Graph(
                figure=sc.funnelChart(sc.df,200,200,'x', 'y')
        )],
            style=stl.sgraph_btn
        ),
        html.Button(
            id= 'btn_scatter',
            # n_clicks='0',
            children=[
            dcc.Graph(
                figure=sc.scatterChart(sc.df,200,200,'x', 'y')
        )],
            style=stl.sgraph_btn
        ),
    ],
    style=stl.sample_chart_style
    ),

    html.Div(children=[
        html.Button(
            id='line3D',
            # n_clicks='0',
            children=[
                dcc.Graph(
                    figure=sc.line3DChart(sc.df,200, 200,'x', 'y','z'),
                    responsive=False,

                )],
            style=stl.sgraph_btn
        ),
        html.Button(
            id='histogram',
            # n_clicks='0',
            children=[
                dcc.Graph(
                    figure=sc.histogramChart(sc.df,200, 200,'x', 'y'),
                )],

            style=stl.sgraph_btn
        ),
        html.Button(
            id= 'pie',
            # n_clicks='0',
            children=[
                dcc.Graph(
                    figure=sc.pieChart(sc.df,200, 200, 'y')
                )],
            style=stl.sgraph_btn
        ),
        html.Button(
            id='scatter3D',
            # n_clicks='0',
            children=[
                dcc.Graph(
                    figure=sc.scatter3DChart(sc.df, 200, 200,'x', 'y', 'z')
                )],
            style=stl.sgraph_btn
        ),
        html.Button(
            id='heatmap',
            # n_clicks='0',
            children=[
                dcc.Graph(
                    figure=sc.heatmapChart(sc.df, 200, 200, 'x', 'y', 'z')
                )],
            style=stl.sgraph_btn
        ),
    ],
        style=stl.sample_chart_style
    ),
    html.Div([
        html.Br(),
        html.Br(),
        html.Br(),
        "Tribe - H"
    ]),
],
style=stl.layout_style
)










@app.callback(Output('result','children'),
              Output('show_data','children'),
              Input('file_uploaded','contents'),
              Input('file_uploaded','filename'),
              prevent_initial_call=True)
def upload_data(contents, filename):
    if contents is not None :
        df = parse_data(contents, filename)
        if help.getFile() is None :
            return ['error in file format, please choose csv,txt or excel file format'], dash.no_update;
        row, col = df.shape
        children = [
            'File Name : ' + filename,
            html.Br(),
            'NUmber of Rows : ' + str(row),
            html.Br(),
            'Number of Columns : ' + str(col),
            html.Br(),
        ]



        return ['File is Uploaded'],children



def parse_data(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    df = None
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV or TXT file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        elif 'txt' or 'tsv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')), delimiter = r'\s+')

    except Exception as e:
        print(e)
    help.setFile(df)

    return df



@app.callback(Output('chart_update','children'),
              Output('dropDown','children'),
              Output('data_print','children'),
              # Output('buttonSection','children'),
              Input('btn_bar','n_clicks'),
              Input('btn_line','n_clicks'),
              Input('btn_area','n_clicks'),
              Input('btn_box','n_clicks'),
              Input('btn_funnel', 'n_clicks'),
              Input('btn_scatter','n_clicks'),
              Input('line3D','n_clicks'),
              Input('histogram','n_clicks'),
              Input('pie','n_clicks'),
              Input('scatter3D','n_clicks'),
              Input('heatmap','n_clicks'),
              prevent_initial_call=True)
def update_chart(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11) :
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if help.getFile() is None :
        return ['File is not Uploaded'], dash.no_update,dash.no_update

    # btn = [
    #     html.Button(['Generate'], id='button', style=stl.next_btn_style)
    # ]

    children1D = [
        html.P('X : ', style=stl.xyzStyle),
        dcc.Dropdown(options=dd.give_list(help.getFile()), id='dropdown1', style=stl.dropDownStyle),
        html.P('Y : ', style=stl.xyzStyle),
        dcc.Dropdown(options=[], id='dropdown2', style=stl.dropDownStyle),
        html.P('Z : ', style=stl.xyzStyle),
        dcc.Dropdown(options=[], id='dropdown3', style=stl.dropDownStyle),
    ]


    children2D = [
        html.P('x : ', style=stl.xyzStyle),
        dcc.Dropdown(options=dd.give_list(help.getFile()), id='dropdown1', style=stl.dropDownStyle),
        html.P('y : ', style=stl.xyzStyle),
        dcc.Dropdown(options=dd.give_list(help.getFile()), id='dropdown2', style=stl.dropDownStyle),
        html.P('Z : ', style=stl.xyzStyle),
        dcc.Dropdown(options=[], id = 'dropdown3', style = stl.dropDownStyle),

    ]
    children3D = [
        html.P('X : ', style=stl.xyzStyle),
        dcc.Dropdown(options=dd.give_list(help.getFile()), id='dropdown1', style=stl.dropDownStyle),
        html.P('Y : ', style=stl.xyzStyle),
        dcc.Dropdown(options=dd.give_list(help.getFile()), id='dropdown2', style=stl.dropDownStyle),
        html.P('Z : ', style=stl.xyzStyle),
        dcc.Dropdown(options=dd.give_list(help.getFile()), id='dropdown3', style=stl.dropDownStyle),
    ]



    if 'btn_bar' in button_id :
        help.setButtonValue(1)
        children1=[
            dcc.Graph(figure=sc.barChart(sc.df,400,400,'x','y')),
            ]
        return children1,children2D, [],
    elif 'btn_line' in button_id :
        help.setButtonValue(2)
        children1 = [
            dcc.Graph(figure=sc.lineChart(sc.df, 400, 400,'x','y')),
        ]
        return children1, children2D, [],
    elif 'btn_area' in button_id :
        help.setButtonValue(3)
        children1 = [
            dcc.Graph(figure=sc.areaChart(sc.df, 400, 400,'x','y')),
        ]
        return children1, children2D, [],
    elif 'btn_box' in button_id :
        help.setButtonValue(4)
        children1 = [
            dcc.Graph(figure=sc.boxChart(sc.df, 400, 400,'x','y')),

        ]
        return children1, children2D, [],
    elif 'btn_funnel' in button_id :
        help.setButtonValue(5)
        children1 = [
            dcc.Graph(figure=sc.funnelChart(sc.df, 400, 400,'x','y')),

        ]
        return children1, children2D, [],
    elif 'btn_scatter' in button_id :
        help.setButtonValue(6)
        children1 = [
            dcc.Graph(figure=sc.scatterChart(sc.df,400, 400,'x','y')),
        ]
        return children1, children2D, [],

    elif 'line3D' in button_id :
        help.setButtonValue(7)
        children1 = [
            dcc.Graph(figure=sc.line3DChart(sc.df,400, 400,'x','y','z')),
        ]
        return children1, children3D, [],

    elif 'histogram' in button_id :
        help.setButtonValue(8)
        children1 = [
            dcc.Graph(figure=sc.histogramChart(sc.df, 400, 400,'x','y')),
        ]
        return children1, children2D, []
    elif 'pie' in button_id :
        help.setButtonValue(9)
        children1 = [
            dcc.Graph(figure=sc.pieChart(sc.df, 400, 400,'y')),
        ]
        return children1, children3D,[],

    elif 'scatter3D' in button_id :
        help.setButtonValue(10)
        children1 = [
            dcc.Graph(figure=sc.scatter3DChart(sc.df, 400, 400,'x','y','z')),
        ]
        return children1, children3D,[],

    elif 'heatmap' in button_id :
        help.setButtonValue(11)
        children1 = [
            dcc.Graph(figure=sc.heatmapChart(sc.df,400, 400,'x','y','z')),
        ]
        return children1, children3D, [],



@app.callback(Output('finalChart','children'),
              # Input('button','n_clicks'),
              Input('dropdown1','value'),
              Input('dropdown2','value'),
              Input('dropdown3','value'),
              prevent_initial_call=True)
def update_graph(val1,val2,val3) :
    if help.getButtonValue() == 1 :
        if val1 is not None and val2 is not None :
            return dcc.Graph(figure=sc.barChart(help.getFile(),1000,800,val1,val2))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 2:
        if val1 is not None and val2 is not None :
            return dcc.Graph(figure=sc.lineChart(help.getFile(),1000,800,val1,val2))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 3:
        if val1 is not None and val2 is not None :
            return dcc.Graph(figure=sc.areaChart(help.getFile(),1000,800,val1,val2))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 4:
        if val1 is not None and val2 is not None :
            return dcc.Graph(figure=sc.barChart(help.getFile(),1000,800,val1,val2))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 5:
        if val1 is not None and val2 is not None :
            return dcc.Graph(figure=sc.funnelChart(help.getFile(),1000,800,val1,val2))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 6:
        if val1 is not None and val2 is not None :
            return dcc.Graph(figure=sc.scatterChart(help.getFile(),1000,800,val1,val2))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 7:
        if val1 is not None and val2 is not None and val3 is not None:
            return dcc.Graph(figure=sc.line3DChart(help.getFile(),1000,800,val1,val2,val3))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 8:
        if val1 is not None and val2 is not None :
            return dcc.Graph(figure=sc.histogramChart(help.getFile(),1000,800,val1,val2))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 9 :
        if val1 is not None :
            return dcc.Graph(figure=sc.pieChart(help.getFile(),1000,800,val1))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 10:
        if val1 is not None and val2 is not None and val3 is not None:
            return dcc.Graph(figure=sc.scatter3DChart(help.getFile(),1000,800, val1, val2, val3))
        else :
            dash.exceptions.PreventUpdate

    elif help.getButtonValue() == 11:
        if val1 is not None and val2 is not None and val3 is not None :
            return dcc.Graph(figure=sc.heatmapChart(help.getFile(),1000,800, val1, val2, val3))
        else :
            dash.exceptions.PreventUpdate









