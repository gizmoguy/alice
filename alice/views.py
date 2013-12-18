from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def home(request):
    return {'page': 'home'}

@view_config(route_name='login', renderer='templates/mytemplate.pt')
def login(request):
    return {'page': 'login'}

@view_config(route_name='logout', renderer='templates/mytemplate.pt')
def logout(request):
    return {'page': 'logout'}

@view_config(route_name='map', renderer='templates/mytemplate.pt')
def map(request):
    return {'page': 'map'}

@view_config(route_name='dashboard', renderer='templates/mytemplate.pt')
def dashboard(request):
    return {'page': 'dashboard'}
