#!/usr/bin/env python3
# pdf-to-csv.py

import sys
import os
import shutil
import subprocess
import PyPDF2
import csv
import camelot
from tqdm import tqdm # Importa a biblioteca para a barra de progresso

def verificar_ghostscript():
    """
    Verifica de forma robusta se o Ghostscript está instalado e funcional
    tentando executar o comando 'gs --version'.
    """
    try:
        # Tenta executar o comando do Ghostscript para obter a versão.
        # stdout e stderr são redirecionados para DEVNULL para não poluir a saída.
        subprocess.run(
            ["gs", "--version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True  # Levanta um erro se o comando falhar
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        # FileNotFoundError: O comando 'gs' não foi encontrado.
        # CalledProcessError: O comando foi encontrado mas retornou um erro.
        print("--- ERRO DE DEPENDÊNCIA ---")
        print("Ghostscript não está instalado ou não foi encontrado pelo Python.")
        print("Ele é uma dependência essencial para a biblioteca Camelot funcionar corretamente.")
        print("\nPara instalar no Lubuntu/Ubuntu/Debian, use o comando:")
        print("sudo apt update && sudo apt install ghostscript")
        print("\nO script será interrompido.")
        sys.exit(1)

def converter_pdf_para_csv(pdf_path, csv_path):
    """
    Converte tabelas de um arquivo PDF para um único arquivo CSV.

    Args:
        pdf_path (str): O caminho para o arquivo PDF de entrada.
        csv_path (str): O caminho para o arquivo CSV de saída.
    """
    try:
        with open(pdf_path, 'rb') as f:
            read = PyPDF2.PdfReader(f)
            pages = len(read.pages)
        print(f"Arquivo '{pdf_path}' encontrado com {pages} páginas.")

        with open(csv_path, 'w', newline='', encoding='utf-8') as f_out:
            writer = csv.writer(f_out, delimiter=',')
            header_written = False

            print("Iniciando extração de tabelas...")
            # Envolve o range com tqdm para criar a barra de progresso
            for i in tqdm(range(1, pages + 1), desc="Processando páginas"):
                try:
                    # Usando flavor='stream' que pode ser mais flexível
                    tables = camelot.read_pdf(pdf_path, pages=str(i), flavor='stream')

                    if tables.n > 0:
                        table_df = tables[0].df
                        
                        if not header_written:
                            heading = [str(s).replace("\n", " ") for s in table_df.values.tolist()[0]]
                            writer.writerow(heading)
                            header_written = True
                            data_rows = table_df.values.tolist()[1:]
                        else:
                            data_rows = table_df.values.tolist()

                        for line in data_rows:
                            writer.writerow(line)
                    
                except Exception as e:
                    # Imprime um aviso se uma página específica falhar, sem parar o loop
                    tqdm.write(f"Aviso: Não foi possível processar a página {i}. Erro: {type(e).__name__}")
        
        print(f"\nConversão concluída! Arquivo salvo em: '{csv_path}'")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{pdf_path}' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verificar_ghostscript()

    if len(sys.argv) < 2:
        print(f"Uso: ./{os.path.basename(__file__)} /caminho/para/arquivo.pdf")
        sys.exit(1)

    pdf_file_path = sys.argv[1]
    
    base_name = os.path.splitext(pdf_file_path)[0]
    # O nome do arquivo de saída será .csv
    csv_file_path = f"{base_name}.csv"
    
    converter_pdf_para_csv(pdf_file_path, csv_file_path)
