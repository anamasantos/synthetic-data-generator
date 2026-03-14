# 🤖 Synthetic Data Generator | GenVision

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-orange.svg)](https://ai.google.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto é um pipeline automatizado para a expansão de datasets de Visão Computacional. Utilizando a API do **Google Gemini 2.0 Flash**, o sistema gera variações sintéticas de imagens reais (alterando iluminação, clima, cenários e contexto) para mitigar a escassez de dados no treinamento de modelos de detecção de objetos, como o YOLO.

## 🚀 Funcionalidades

- **Expansão Multimodal:** Transforma imagens estáticas em múltiplos cenários através de prompts inteligentes.
- **Arquitetura Modular:** Separação clara entre consumo de API, processamento de dados e configurações.
- **Gestão via YAML:** Controle total sobre os tipos de aumentação de dados através de arquivos de configuração.
- **Segurança:** Implementação de variáveis de ambiente (.env) para proteção de chaves de API.

## 📁 Estrutura do Projeto

```text
├── Classes/
│   ├── ConsumerAPI/      # Wrapper do novo SDK 'google-genai'
│   └── ProcessData/      # Lógica de processamento e seleção de prompts
├── configs/              # Configurações do pipeline e prompts (YAML)
├── source-images/        # Dataset original (referência)
├── images_results/       # Imagens sintéticas geradas pela IA
├── agent.py              # Script principal de execução
└── .env                  # Chaves de API (ignorado no Git)


🚀 Desenvolvido por Ana Santos - Foco em MLOps e Visão Computacional.