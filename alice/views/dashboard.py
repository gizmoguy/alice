from pyramid.view import view_config

@view_config(route_name='dashboard', renderer='../templates/mytemplate.pt')
def dashboard(request):
    return {'page': 'dashboard'}
