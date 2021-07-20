
def test_entry(client):
    """see if unlogged client gets redirected from any page to login page"""
    routes = ['/', '/login', '/logout', '/transactions', '/transactions/1', 'transactions/35']
    responses = [client.get(route, follow_redirects=True) for route in routes]

    assert all([response.status_code == 200 for response in responses])
    assert all([b'enter your username:' in response.data for response in responses])
    assert all([b'not logged in' in response.data for response in responses])


def test_404(client):
    """see if 404 returned for wrong route"""
    response = client.get('/blabla')
    assert response.status_code == 404


def test_login(client):
    """see if logging in is successful and redirects to Transactions summary"""

    response = client.post('/login', data={'login': 'sdkcadfjkhv'}, follow_redirects=True)

    assert response.status_code == 200
    assert b'login successful' in response.data
    assert b'logged in as sdkcadfjkhv' in response.data
    assert b'Transactions summary' in response.data


def test_logout(logged_client):
    """see if logged client gets properly logged out"""

    response = logged_client.get('/logout', follow_redirects=True)

    assert response.status_code == 200
    assert b'enter your username:' in response.data
    assert b'not logged in' in response.data


def test_summary_from_index(logged_client):
    """see if logged client lands on summary page"""

    response = logged_client.get('/', follow_redirects=True)
    assert b'Transactions summary' in response.data


def test_summary(logged_client):
    """see if logged client sees summary page"""

    response = logged_client.get('/transactions', follow_redirects=True)
    assert b'Transactions summary' in response.data


def test_details(logged_client):
    """see if details page is ok"""

    response = logged_client.get('/transactions/1', follow_redirects=True)
    assert b'Transaction 1 details' in response.data


def test_details_404(logged_client):
    """see if 404 is raised for non-existing transaction"""
    response = logged_client.get('/transactions/3', follow_redirects=True)
    assert response.status_code == 404


def test_notes_edit(logged_client):
    """see if notes can be posted from details view"""
    response = logged_client.post('/transactions/1', data={'note': 'hey i\'ve added this note'})
    assert response.status_code == 200
    assert b'hey i&#39;ve added this note' in response.data


def test_load(logged_client):
    """see if sample data can be loaded up"""
    response = logged_client.get('/load', follow_redirects=True)
    assert response.status_code == 200
    assert b'20 records of data added' in response.data
