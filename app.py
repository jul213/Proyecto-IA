import os
from transformers import pipeline


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def main():
    print("---Iniciando IA de julio🤖---")
    print("Cargando modelo de lenguaje (esto puede tardar un poco la primera vez)")

    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

    print("\n✅ IA LISTA. Por favor, introduce un texto largo para resumir:")
    texto_usuario = input("> ")

    if len(texto_usuario) < 30:
        print("❌ El texto es muy corto para resumirlo. Prueba con algo más largo.")
    else:
        # 3. La IA hace su magia
        print("\nAnalizando y procesando...")
        resumen = summarizer(texto_usuario, max_length=50, min_length=10, do_sample=False)
        
        print("\n✨ RESUMEN GENERADO:")
        print(resumen[0]['summary_text'])

if __name__ == "__main__":
    main()