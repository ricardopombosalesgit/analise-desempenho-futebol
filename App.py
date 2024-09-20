import streamlit as st
import subprocess
import os

# Função para executar um script Python específico
def executar_script(script_name):
    # Caminho da pasta onde os scripts estão armazenados (ajuste conforme necessário)
    scripts_dir = "scripts"  # Substitua com o nome da pasta correta ou deixe vazio se os arquivos estão no mesmo diretório
    script_path = os.path.join(scripts_dir, script_name)  # Junta o caminho da pasta com o nome do arquivo
    
    # Converte para o caminho absoluto para maior confiabilidade
    script_path = os.path.abspath(script_path)
    
    # Verifica se o arquivo existe antes de tentar executar
    if os.path.exists(script_path):
        try:
            # Executa o script especificado
            subprocess.run(["python", script_path], check=True)
            st.success(f"Executado: {script_name}")
        except subprocess.CalledProcessError as e:
            st.error(f"Erro ao executar {script_name}: {e}")
    else:
        st.error(f"Arquivo {script_name} não encontrado no caminho {script_path}")

# Função para listar arquivos no diretório especificado
def listar_arquivos(diretorio):
    st.write(f"Arquivos no diretório {diretorio}:")
    try:
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            st.write(arquivo)
    except FileNotFoundError:
        st.error(f"O diretório {diretorio} não foi encontrado.")

# Título do aplicativo
st.title('Execução de Scripts por Posição')

# Lista os arquivos na pasta 'scripts' para verificação
listar_arquivos("scripts")  # Substitua com o caminho correto se necessário

# Botões para cada posição
if st.button('Goleiros'):
    executar_script('Goleiros.py')

if st.button('Atacantes'):
    executar_script('Atacantes.py')

if st.button('Zagueiros'):
    executar_script('Zagueiros.py')

if st.button('Meias'):
    executar_script('Meias.py')

if st.button('Laterais'):
    executar_script('Laterais.py')

if st.button('Volantes'):
    executar_script('Volantes.py')

if st.button('Meia Atacantes'):
    executar_script('MeiaAtacantes.py')