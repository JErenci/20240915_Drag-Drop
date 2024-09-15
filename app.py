from dash import Dash, dcc, html, Input, Output, State, callback, dash_table
import pandas as pd
import base64
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# df = pd.read_csv('https://git.io/Juf1t')
root_path = 'C:\\Users\\User\\Downloads\\'
# csv_path = root_path+'DE_customers.csv'
# df2 = pd.read_csv(csv_path, sep=';')

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # dash_table.DataTable(id='tbl',
    #                      # data=df.to_dict('records'),
    #                      # columns=[{"name": i, "id": i} for i in df.columns],
    #                      page_size=5,
    #                      ),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),

    # html.Div(id='out-tbl',
    #          # data=df_Out,
    #          ),
    # dash.dash_table.DataTable(id='output-tbl', data={})
    # html.Img(id='img_user',children='')
])

def parse_contents(contents, filename, date):

    print('filename:', filename)
    print()

    if ('csv' in filename):
        print(8)
        df_Out = pd.read_csv(root_path + filename)#, sep=';')
        im = dash_table.DataTable(df_Out.to_dict('records'), page_size=10)
    else:
        print('img')
        im = html.Img(src=contents)

    div = [
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        im,
        html.Hr(),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        }),
    ]
    return html.Div(div)

@callback(Output('output-image-upload', 'children'),
          # Output('tbl', 'data'),
          Input('upload-image', 'contents'),
          State('upload-image', 'filename'),
          State('upload-image', 'last_modified'),
          prevent_initial_callback=True)

def update_output(list_of_contents,list_of_names, list_of_dates):
    print(1)
    if list_of_contents is not None:
        print(2)

        # print('list_of_contents: ' + str(list_of_contents))
        # # path=root_path
        # # print('path: ' + str(path))
        # print('list_of_names: ' + str(list_of_names))
        # print('list_of_dates: ' + str(list_of_dates))

        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]

        # print('list_of_contents: '+str(list_of_contents))
        # print('list_of_names: '+str(list_of_names))
        # print('list_of_dates: '+str(list_of_dates))
        # print()
        # print()
        return children
    #
    #     filename=list_of_names[0]
    #     print(root_path+filename)
    #     df_Out = pd.read_csv(root_path+filename, sep=';')
    #     print(df_Out)
    #     ret_df = dash_table.DataTable(data=df_Out.to_dict('records'),
    #                                   page_size=10,)
    #     # dt = df.to_dict('records')#,[{"name": i, "id": i} for i in df.columns]
    #     # print(dt)
    #     print('children:'+str(type(children)))
    #     print('children:'+str(type(df_Out)))
    #     # print
    #     return [children, df_Out[2:].to_dict('records')] #+ dt
    # else:
    #     print(5)
    #     return [[],pd.DataFrame.empty.to_dict('records')]

if __name__ == '__main__':
    app.run(debug=True)
