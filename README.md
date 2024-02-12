# PredictiveMaintenance IA

## Problema
Um conjunto de dados provenientes de uma máquina com motor elétrico, adquiridos por seis sensores diferentes.Cada sensor capturou dados simultaneamente em uma taxa de amostragem de 10 kHz, o que significa que cada sensor registrou informações a uma taxa de 10.000 amostras por segundo. Esses dados são armazenados em seis arquivos com extensão .npy, cada um representando as leituras de um sensor específico.

Além dos arquivos de dados do sensor, há um arquivo adicional chamado "Classes.npy", que contém informações sobre os diferentes estados de funcionamento da máquina. Esses estados podem incluir diferentes condições de operação, como funcionamento normal, bem como diferentes tipos de falhas. Os dados do arquivo "Classes.npy" representam as classes ou estados de funcionamento da máquina capturados pelos sensores. Cada entrada na lista corresponde a uma leitura de um momento específico no tempo, e a classe associada a essa leitura indica o estado de funcionamento da máquina naquele momento.

As classes identificadas são "Classe A", "Classe B", "Classe D" e "Classe E". É possível que cada uma dessas classes representa um estado diferente da máquina, como (p.e.):
- Classe A: Pode representar um estado de funcionamento normal da máquina, sem nenhuma anomalia ou falha detectada.
- Classe B: Pode indicar um estado de funcionamento anormal ou condições de operação específicas que não são consideradas ideais, mas que não constituem uma falha crítica.
- Classe D: Pode representar um estado de funcionamento com uma determinada falha detectada pelos sensores. O tipo específico de falha associado à Classe D dependeria do contexto do sistema e dos dados.
- Classe E: Pode indicar um estado de funcionamento com uma falha mais grave ou crítica, que requer intervenção imediata ou reparo.

# Análise
Com base na descrição fornecida, um cientista de dados poderia abordar esse problema usando técnicas de aprendizado de máquina supervisionado. O objetivo seria desenvolver um modelo capaz de prever o estado de funcionamento da máquina com base nas leituras dos sensores.

# Resolução
Etapas que um cientista de dados poderia seguir para resolver esse problema:
- Exploração e pré-processamento de dados
- Seleção de características
- Construção do modelo
- Avaliação do modelo
- Interpretação dos resultados

# Execução
- Crie uma pasta chamada 'datasets' dentro da pasta src/eda/conjunto/dataset
- Crie uma pasta chamada 'dataset' dentro da pasta src/aprendizagemMaquina/dataset
- Execute os scripts dentro da pasta src/eda/individual
- Execute o script dentro da pasta src/eda/conjunto
- Execute os scripts dentro da pasta src/aprendizagemMaquina/supervisionado



