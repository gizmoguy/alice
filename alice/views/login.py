from pyramid.view import view_config

@view_config(route_name='login', renderer='../templates/mytemplate.pt')
def login(request):
    return {'page': 'login'}
