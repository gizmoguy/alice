from pyramid.view import view_config

@view_config(route_name='logout', renderer='../templates/mytemplate.pt')
def logout(request):
    return {'page': 'logout'}
