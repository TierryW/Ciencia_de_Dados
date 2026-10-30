# Glossário:

## Scikit-learn:
Uma biblioteca de machine learning em Python que fornece ferramentas simples e eficientes para análise de dados e modelagem preditiva, incluindo a implementação de SVM através do SVC.

## SVC (Support Vector Classifier):
Uma implementação do algoritmo SVM na biblioteca Scikit-learn, usada para realizar tarefas de classificação em datasets, permitindo a escolha de diferentes kernels e parâmetros.

## Kernel:
Uma função utilizada no SVM para transformar dados em um espaço de maior dimensionalidade, permitindo que dados não linearmente separáveis sejam classificados. Exemplos incluem kernels lineares, polinomiais e RBF.

## Vetores de Suporte:
Os pontos de dados mais próximos ao hiperplano de separação em um modelo SVM. Eles são críticos para a definição do hiperplano e, portanto, para a classificação dos dados.

## Hiperplano:
Uma subespécie de espaço dimensional que divide um espaço de dados em duas partes distintas. No SVM, o hiperplano é usado para separar classes de dados, maximizando a margem entre elas.

## Função de Perda:
Uma função que quantifica o quão bem um modelo de machine learning está performando, medindo a diferença entre os valores previstos e os valores reais. No contexto do SVM, é usada para minimizar erros de classificação.

## Margem:
A distância entre o hiperplano de separação e os pontos de dados mais próximos de qualquer classe. O SVM busca maximizar essa margem para melhorar a precisão da classificação.

## Parâmetro C:
Um parâmetro de regularização no SVM que controla o trade-off entre maximizar a margem e minimizar o erro de classificação. Um valor maior de C dá mais importância à classificação correta de todos os pontos de treinamento.

## Regularização:
Uma técnica usada para prevenir o overfitting em modelos de machine learning, adicionando uma penalidade à função de perda. No SVM, o parâmetro C é usado para regularizar o modelo.

## RBF (Radial Basic Function):
Um tipo de kernel usado no SVM que transforma dados em um espaço de maior dimensionalidade, permitindo a separação de classes que não são linearmente separáveis no espaço original.
