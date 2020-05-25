import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
 
colors = {
    'background': '#FF91AF',
    'text': '#000080'
}
 
app.layout = html.Div([
    dcc.Tabs(id="tabs-example", children=[
        dcc.Tab(label='Главная', value='tab-1'),
        dcc.Tab(label='Блог', value='tab-2'),
        dcc.Tab(label='Обо мне', value='tab-3'),
        dcc.Tab(label='Мои друзья', value='tab-4'),
        dcc.Tab(label='Мой университет', value='tab-5'),
        dcc.Tab(label='Что-то', value='tab-6'),
    ]),
    html.Div(id='tabs-example-content')
])
 
@app.callback(Output('tabs-example-content', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H1('Anna Mikhailova', style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.1.jpg'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.P('© Михайлова Анна. 2020', style = {'textAlign' : 'center'})
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H1('Новость дня', style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.2.png'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.H1('Воскресение', style = {'textAlign' : 'center'}),
            html.P(
                'Я встала сегодня в 9 утра! Мне кажется, что это очень рано! Я приготовила макароны и поела их! Уже почти полночь! Я не знаю на что потратила весь день!!!!'),
            html.P('© Михайлова Анна. 2020', style = {'textAlign' : 'center'})
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H1('Anna Mikhailova', style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.3.jpg'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.H1('Обо мне', style = {'textAlign' : 'center'}),
            html.P('Привет))))'),
            html.P(
                'Я учусь в ВШЭ! Это самый лучший ВУЗ в мире!!! В свободное время я ем и сплю. В целом, веду очень активный образ жизни!'),
            html.P('© Михайлова Анна. 2020', style = {'textAlign' : 'center'})
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.5.jpg'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.6.jpg'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.7.jpg'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.8.jpg'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.9.jpg'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
        ])
    elif tab == 'tab-5':
        return html.Div([
            html.H1('Сайт моего университета - Высшей Школы Экономики', style = {'textAlign' : 'center'}),
            html.P(html.A('Высшая Школа Экономики', href='https://www.hse.ru/'))
        ])
    else:
        return html.Div([
            html.H1('COVID-19: что мы знаем и чего не знаем', style = {'textAlign' : 'center'}),
            html.P(''),
            html.Div([html.Img(src=app.get_asset_url('Рис.10.png'), style = {'height': '500px', 'weight': '500px'})], style = {'textAlign' : 'center'}),
            html.P(''),
            html.P('Рисунок 1. Заражение SARS-CoV-2 клеток человека.', style = {'textAlign' : 'center'}),
            html.H4('Вирусолог Андрей Летаров:'),
            html.P('SARS-CoV-2 — это РНК-содержащий вирус, который в силу особенностей своего воспроизводства '
                   'достаточно часто подвергается мутациям. Уже сейчас наблюдается несколько десятков различных '
                   'генетических линий вируса, причем их филогения (родственные отношения) хорошо коррелирует с '
                   'местом выделения изолятов, то есть распространение вируса по планете происходит в масштабах '
                   'времени, сопоставимых с накоплением генетических изменений в его геноме. Однако не все мутации '
                   'имеют сколько-нибудь существенное значение. В определенной обстановке та или иная мутация может '
                   'иметь больший репродуктивный успех, и тогда этот вариант получит большее распространение в '
                   'определенной местности. И тогда мы сможем говорить о появлении нового штамма. Важно, '
                   'чтобы это были не просто отличия по последовательности, но и отличия, которые сопряжены с '
                   'изменением экологически важных свойств вируса, например, его контагиозности или тяжести '
                   'заболевания, которое он вызывает.'),
            html.H4('Памятка по профилактике коронавирусной инфекции:'),
            html.A('Скачать Файл', href='https://ria.ru/ips/op/COVID_19_Book.pdf')
        ])
 
 
if __name__ == '__main__':
    app.server.run(port=8000, host='127.0.0.1', debug=True)