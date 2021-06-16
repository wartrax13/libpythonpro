def buscar_avatar(usuario):
    """
    Busca o avatar de um usuario de GitHub
    :param usuario: str com o nome de usuario no GitHab
    :return: str com o link do avatar
    """
    url= f'https://api.github.com/users/{usuario}'
    resp = requestes.get(url)
    resp.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('wartrax13'))