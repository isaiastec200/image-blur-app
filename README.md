# image-blur-app
Aplicativo de Desfoque de Imagens com Streamlit
Visão Geral
Este projeto tem como objetivo criar um aplicativo em Streamlit que reconhece objetos e pessoas em uma imagem e desfoca o fundo. A ideia é fornecer um serviço web onde os usuários possam facilmente desfocar o fundo de suas fotos. O aplicativo utiliza a biblioteca rembg e um modelo pré-treinado "isnet-general-use.onnx" para a remoção do fundo, seguido pela aplicação de um desfoque Gaussiano com OpenCV.

Funcionalidades
Reconhecimento de Objetos e Pessoas: Utiliza um modelo ONNX pré-treinado para a detecção precisa de objetos e pessoas.
Desfoque de Fundo: Aplica um desfoque Gaussiano ao fundo enquanto mantém o assunto principal em foco.
Interface Web: Streamlit fornece uma interface web fácil de usar para os usuários fazerem upload de imagens e baixarem os resultados processados.
Como Funciona
Upload de Imagens: Os usuários podem fazer upload de uma ou mais imagens.
Pré-processamento da Imagem: As imagens são redimensionadas e pré-processadas para a entrada do modelo.
Remoção de Fundo: A biblioteca rembg e o modelo "isnet-general-use.onnx" são usados para criar uma máscara de segmentação.
Aplicar Desfoque: Um desfoque Gaussiano é aplicado ao fundo usando a máscara de segmentação.
Baixar Resultados: Os usuários podem baixar as imagens processadas individualmente ou como um arquivo zip.
Instalação
Clone o repositório:
bash
Copiar código
git clone https://github.com/yourusername/image-blur-app.git
cd image-blur-app
Instale as dependências necessárias:
bash
Copiar código
pip install -r requirements.txt
Execute o aplicativo Streamlit:
bash
Copiar código
streamlit run app.py
Dependências
Python 3.8+
Streamlit
ONNX Runtime
NumPy
OpenCV
Pillow
Uso
Upload de Imagens: Selecione uma ou mais imagens para fazer upload.
Selecionar Nível de Desfoque: Ajuste o slider para escolher o nível de desfoque Gaussiano.
Baixar Imagens Processadas: Clique no botão de download para salvar as imagens processadas.
Trabalho Futuro
Implantar em um Serviço de Nuvem Robusto: Implantar o aplicativo em um serviço de nuvem mais poderoso para lidar com as demandas computacionais.
Melhorar a Experiência do Usuário: Melhorar a interface do usuário e adicionar mais opções de personalização.
Referências
Silva, P. R. B. - "O objetivo da segmentação é evidenciar a região de interesse das imagens, removendo toda a informação desnecessária."
