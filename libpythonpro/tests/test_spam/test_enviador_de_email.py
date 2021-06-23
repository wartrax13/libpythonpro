import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'wartrax13@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'wartrax13@gmail.com',
        'Cursos Python Pro',
        'A primeira turma já está aberta. Testando...'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    [' ', 'pedro']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'wartrax13@gmail.com',
            'Cursos Python Pro',
            'A primeira turma já está aberta. Testando...'
        )
