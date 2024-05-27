# Aplicativo de Desfoque de Imagens com Streamlit

## Visão Geral
O projeto visa criar um aplicativo em Streamlit que reconhece objetos e pessoas em imagens, desfocando o fundo. Utiliza a biblioteca rembg e o modelo pré-treinado "isnet-general-use.onnx", seguido por desfoque Gaussiano com OpenCV.

## Funcionalidades
- Reconhecimento de Objetos e Pessoas
- Desfoque de Fundo
- Interface Web Amigável

## Como Funciona
1. **Upload de Imagens**
2. **Pré-processamento da Imagem**
3. **Remoção de Fundo**
4. **Aplicação de Desfoque**
5. **Download de Resultados**
   
## Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/isaiastec200/image-blur-app.git
cd image-blur-app
pip install -r requirements.txt
```
Rodar app
```bash
streamlit run app.py
```

## Dependências
1.  Python 3.8+
2. Streamlit
3. ONNX Runtime
4. NumPy
5. OpenCV
6. Pillow
   
## Uso

1. **Upload de Imagens**
2. **Seleção do Nível de Desfoque**
3. **Download das Imagens Processadas**

## Trabalho Futuro
- Implantação em Serviço de Nuvem
- Melhoria da Experiência do Usuário
## Referências:
Silva, P. R. B. - "O objetivo da segmentação é evidenciar a região de interesse das imagens, removendo toda a informação desnecessária."

## Demostração

https://github.com/isaiastec200/image-blur-app/assets/42812115/3565e3ca-1d8a-47b0-a43b-c9282f16d043

## Créditos

Isaías Rocha Santos

[LinkedIn](https://www.linkedin.com/in/isaias-rocha-7ab972196/)





