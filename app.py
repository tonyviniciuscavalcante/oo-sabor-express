from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Pāozinho', 2.00, 'O melhor pāo da cidade')
prato_paozinho.aplicar_desconto()

sobremesa_bolo = Sobremesa('Bolo de cenoura', 10.0, 'doce')
sobremesa_bolo.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_bolo)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()