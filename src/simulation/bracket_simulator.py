"""
Simulação de torneio (Monte Carlo) a partir de ratings de força de time.

INTENCIONALMENTE NÃO IMPLEMENTADO AINDA — ver src/rating/elo.py para o
motivo. A simulação depende de já ter um modelo de rating funcionando
e validado, e de decisões metodológicas (ex: como modelar melhor-de-N
dentro do bracket, não só jogo único) que fazem mais sentido definir
depois da leitura teórica.

Uso pretendido (após implementação):
    bracket = load_bracket_2027()
    result = simulate_tournament(bracket, rating_model, n_simulations=10_000)
    result.champion_probabilities()  # -> {"T1": 0.18, "Gen.G": 0.15, ...}
"""


def simulate_tournament(bracket, rating_model, n_simulations: int = 10_000):
    raise NotImplementedError(
        "Implementar após validar o modelo de rating e definir a "
        "metodologia de simulação (ver docs/reading-list.md)."
    )
