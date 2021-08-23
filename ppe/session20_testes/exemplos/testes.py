import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_nao_saudavel(self):
        """Testando o retorno com comida não saudável."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco."""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas.'
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito."""
        self.assertEqual(
            dormir(10),
            'Putz! Dormi Muito! Estou atrasado para o trabalho!.'
        )

    def test_eh_engracada(self):
        """Retorna que a pessoa é engraçada"""
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')

    def test_nao_eh_engracada(self):
        """Retorna que a pessoa não é engraçada"""
        self.assertFalse(eh_engracada('Sérgio Malandro'))


if __name__ == '__main__':
    unittest.main()
