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
git clone https://github.com/yourusername/image-blur-app.git
cd image-blur-app
pip install -r requirements.txt
```
Rodar app
```bash
Copiar código
streamlit run app.py
```
Dependências
Python 3.8+
Streamlit
ONNX Runtime
NumPy
OpenCV
Pillow
Uso
Upload de Imagens
Seleção do Nível de Desfoque
Download das Imagens Processadas
Trabalho Futuro
Implantação em Serviço de Nuvem Robusto
Melhoria da Experiência do Usuário
## Referências: Silva, P. R. B. - "O objetivo da segmentação é evidenciar a região de interesse das imagens, removendo toda a informação desnecessária."
