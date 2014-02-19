from pyramid.view import view_config

@view_config(route_name='map', renderer='../templates/mytemplate.pt')
def map(request):
    return {'page': 'map'}
