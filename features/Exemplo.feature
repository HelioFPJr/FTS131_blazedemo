Feature: Compra de passagem aerea
  Scenario: Viagem de Sao Paulo a New York
    Given que acesso o site da Blazedemo
    # Lista de parametros
    When pesquiso passagens de <origem> a <destino>
      | origem      | Destino    |
      | 'Sao Paulo' | 'New York' |
    And seleciono o primeiro voo
    And preencho os dados de pagamento como <cartao><titular><validade><cvv>
      | cartao         | titular   | validade | cvv |
      | '999999999999' | 'Juca Yu' | '11/2024 | 123 |