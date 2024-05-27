import streamlit as st
import onnxruntime
import numpy as np
import cv2
from PIL import Image
from io import BytesIO
import zipfile

# Carregue o modelo ONNX
onnx_model_path = 'model/isnet-general-use.onnx'
session = onnxruntime.InferenceSession(onnx_model_path)

def preprocess_image(image):
    st.text("Redimensionando e pré-processando a imagem...")
    image = cv2.resize(image, (1024, 1024))
    image = image.astype(np.float32) / 255.0
    image = np.transpose(image, (2, 0, 1))
    image = np.expand_dims(image, axis=0)
    return image

def postprocess_mask(mask):
    st.text("Pós-processando a máscara... Quase lá!")
    mask = np.squeeze(mask)
    binary_mask = (mask > 0.5).astype(np.uint8)
    return binary_mask

def apply_blur(image, mask, sigmaX=20):
    st.text("Aplicando aquele desfoque charmoso...")
    blurred_image = cv2.GaussianBlur(image, (15, 15), sigmaX)
    adjusted_mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
    result_image = image * adjusted_mask[:, :, np.newaxis] + blurred_image * (1 - adjusted_mask[:, :, np.newaxis])
    return result_image

def main():
    st.title("Aplicativo de Desfoque de Imagens")
    st.write("Bem-vindo ao aplicativo!")

    col1, col2, col3 = st.columns(3)

    uploaded_files = st.file_uploader("Escolha uma ou mais imagens... Não seja tímido!", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    result_images = []
    
    if uploaded_files and len(uploaded_files) > 0:
        for idx, uploaded_file in enumerate(uploaded_files):
            st.text(f"Processando a imagem {uploaded_file.name}...")

            image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
            if image is None:
                st.error(f"Opa! A imagem {uploaded_file.name} não pôde ser carregada. Tente novamente com uma imagem válida.")
                continue

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            preprocessed_image = preprocess_image(image)

            output_name = session.get_outputs()[0].name
            result = session.run([output_name], {session.get_inputs()[0].name: preprocessed_image})

            segmentation_mask = postprocess_mask(result[0])
            sigmaX = st.slider(f"Escolha o nível de desfoque para a imagem {idx+1}", min_value=1, max_value=50, value=20)

            result_image = apply_blur(image, segmentation_mask, sigmaX)
            result_images.append(result_image)

            col = col1 if idx % 3 == 0 else col2 if idx % 3 == 1 else col3
            col.image(result_image, caption=f'Imagem Resultante - {uploaded_file.name}', use_column_width=True)
            download_button = col.download_button(label=f"Baixar Resultado - {uploaded_file.name}",
                                                  data=BytesIO(cv2.imencode('.jpg', cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR), [int(cv2.IMWRITE_JPEG_QUALITY), 100])[1].tobytes()),
                                                  file_name=f"resultado_{uploaded_file.name}",
                                                  mime="image/jpg")

        if st.button("Download de Todas as Imagens Resultantes"):
            st.text("Preparando todas as suas obras-primas em um pacote zip...")
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for idx, result_image in enumerate(result_images):
                    image_name = f"resultado_{idx + 1}.jpg"
                    zip_file.writestr(image_name, cv2.imencode('.jpg', cv2.cvtColor(result_image, cv2.COLOR_RGB2BGR), [int(cv2.IMWRITE_JPEG_QUALITY), 100])[1].tobytes())

            zip_buffer.seek(0)
            st.download_button(label="Baixar Todas as Imagens Resultantes", data=zip_buffer, file_name="resultados.zip", mime="application/zip")

if __name__ == "__main__":
    main()
