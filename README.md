# Sistema de Visão com Raspberry Pi e YOLO V5 para Identificação de Açaí

Este repositório contém um sistema de visão computacional que utiliza uma webcam conectada a um Raspberry Pi para identificar em tempo real se um objeto é um açaí, utilizando o modelo YOLO V5. O projeto é uma aplicação prática de aprendizado de máquina e visão computacional, demonstrando como é possível utilizar tecnologia acessível para tarefas de identificação de objetos.

## Visão Geral

O sistema foi desenvolvido para ser uma solução de baixo custo que permite a detecção de açaí em ambientes variados, utilizando hardware simples como um Raspberry Pi e uma webcam. O modelo YOLO V5 (You Only Look Once) foi escolhido por sua eficácia em detecção de objetos em tempo real, proporcionando uma combinação ideal de velocidade e precisão.

A ideia principal é permitir que usuários interajam com o sistema e obtenham feedback visual instantâneo sobre a presença de açaí, o que pode ser útil em diversas aplicações, desde controle de qualidade em processos industriais até experiências interativas em feiras e eventos.

### Como Funciona o Projeto

1. **Captura de Imagem:**
   O sistema utiliza a webcam conectada ao Raspberry Pi para capturar imagens em tempo real. As imagens são processadas em sequência, permitindo a análise contínua do que está sendo visualizado.

2. **Processamento com YOLO V5:**
   As imagens capturadas são enviadas para o modelo YOLO V5. Este modelo foi previamente treinado para identificar diferentes objetos, incluindo o açaí. Quando uma imagem é recebida, o modelo a analisa, procurando por padrões que correspondam ao que ele foi treinado para reconhecer.

3. **Detecção e Classificação:**
   Se o modelo identificar um objeto que corresponde ao açaí, ele marca a localização do objeto na imagem e exibe um rótulo correspondente. O sistema pode indicar a probabilidade de acerto, permitindo que o usuário tenha uma noção da confiabilidade da detecção.

4. **Exibição do Resultado:**
   Após a detecção, os resultados são exibidos em uma janela de visualização. O usuário pode ver em tempo real o que o sistema está analisando, com as detecções visíveis sobrepostas à imagem original. Isso cria uma experiência interativa e informativa.

5. **Feedback e Melhoria:**
   O sistema pode ser melhorado ao longo do tempo, com a coleta de dados e feedback sobre as detecções. Os desenvolvedores podem ajustar o modelo ou melhorar a interface com base nas experiências dos usuários.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para discutir melhorias e novas funcionalidades.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
