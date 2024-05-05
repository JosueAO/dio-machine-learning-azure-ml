# Este repositório faz parte do Bootcamp Microsoft Azure AI Fundamentals da plataforma [DIO](https://dio.me). 
   
# dio-machine-learning-azure-ml
Nome do desafio de projeto: Trabalhando com Machine Learning na Prática no Azure ML

# Modelo de Previsão de Aluguel de Bicicletas com Azure Machine Learning

Este repositório contém todos os arquivos e instruções necessárias para criar e implantar um modelo de previsão de aluguel de bicicletas usando Azure Machine Learning. O objetivo é fornecer um guia passo a passo desde a criação do modelo até a configuração dos pontos de extremidade para sua utilização.

## Pré-requisitos

- Conta no Microsoft Azure.
- Conhecimento básico em Python e conceitos de machine learning.
- Ambiente de desenvolvimento configurado com acesso ao Azure Machine Learning Workspace.

## Estrutura do Repositório

- `train.py`: Script de treinamento do modelo.
- `score.py`: Script de pontuação para realizar previsões.
- `endpoint.json`: Arquivo JSON com configurações do ponto de extremidade.
- `README.md`: Este arquivo de documentação.

## Configuração do Ambiente

1. **Configuração do Workspace**:
   - Faça login no [Azure Portal](https://portal.azure.com).
   - Acesse o Azure Machine Learning Studio e configure um novo workspace.

2. **Criação do Ambiente**:
   - No portal do Azure Machine Learning, navegue até `Ambientes` e crie um novo ambiente virtual incluindo todas as bibliotecas necessárias (e.g., scikit-learn, pandas).

## Preparação dos Dados

- Carregue o dataset de aluguel de bicicletas, como o [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset).
- Utilize o Datastore do Azure para armazenar e gerenciar os dados.

## Treinamento do Modelo

1. **Crie e execute o experimento**:
   - Desenvolva um script em Python (`train.py`) para treinar o modelo.
   - Execute o script como um experimento no seu workspace do Azure ML.

## Configuração do Ponto de Extremidade

1. **Registre o Modelo**:
   - Após o treinamento, registre o modelo no Azure ML Studio para uso futuro.

2. **Crie o Ponto de Extremidade**:
   - Desenvolva o script de pontuação (`score.py`) que irá carregar o modelo e fazer previsões.
   - Configure o ponto de extremidade usando o Azure Kubernetes Service (AKS) ou Azure Container Instances (ACI).
   - Salve as configurações do ponto de extremidade em um arquivo JSON (`endpoint.json`).

## Implantação

- Implante o ponto de extremidade configurado para começar a receber dados de entrada e fornecer previsões de aluguel de bicicletas.

## Documentação Adicional

- Instruções detalhadas para cada etapa estão disponíveis no portal de documentação do Azure Machine Learning.

