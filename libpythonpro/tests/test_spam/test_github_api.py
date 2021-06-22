from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login':'wartrax13','id' : 84944254,
        'avatar_url': 'https://avatars.githubusercontent.com/u/84944254?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('wartrax13')
    assert 'https://avatars.githubusercontent.com/u/84944254?v=4' == url
