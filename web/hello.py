def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers )

    body = environ['QUERY_STRING'].lstrip('/?').split('&')
    return body
