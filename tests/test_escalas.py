"""
AAA - 3A

Arrenge - Act - Asserts!
Arrumar - Agir - Assegurar!
"""
from pytest import raises
from code.escalas import escala, ESCALAS, NOTAS

def test_deve_funcionar_com_notas_minusculas():
    # Arange
    tonica = "c"
    tonalidade = "maior"

    # Act - Chamo o que testar
    result = escala(tonica, tonalidade)

    # Assert
    assert result

def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'
    with raises(ValueError) as error:
        escala(tonica, tonalidade)
    
    assert mensagem_de_erro == error.value.args[0]

def test_deve_retotornar_um_erro_dizendo_que_a_escala_nao_existe():

    tonica = 'c'
    tonalidade = 'tonalidade'

    mensagem_de_erro = (
        'Essa escala não existe ou não foi implementada. '
        f'Tente uma dessas {list(ESCALAS.keys())}'
    )
    
    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]