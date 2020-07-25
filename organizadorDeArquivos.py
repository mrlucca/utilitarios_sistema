import os

"""
AUTOR: @mrlucca
"""

# FORMATOS DE ARQUIVOS VALIDOS
AUDIOS =        ['.mp3', '.mid', '.wav']
VIDEOS =        ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv']
IMAGENS =       ['.tiff', '.jpeg', '.jpg', '.png', '.gif', '.svg']
DOCUMENTOS =    ['.txt', '.pdf', '.doc', '.docx', '.ppt', '.pps', '.html', '.xml', '.log']
TABELAS =       ['.xlsx', '.xlsm', '.csv', '.xls', '.xps']
COMPACS =       ['.zip', '.rar', '.tar', '.gz', '.tgz', '.deb']

def getExtension(name):
    """
        Pegando as extensões dos arquivos
        usando o rfind que procura da direita pra esquerda

    """
    index = name.rfind('.')

    #retorno do nome da extensão
    return name[index:]


def organizer(directory):
    AUDIO_DIR =     os.path.join(directory, "audios")
    IMAGENS_DIR =   os.path.join(directory, "imagens")
    DOCS_DIR =      os.path.join(directory, "documentos")
    VIDEOS_DIR =    os.path.join(directory, "videos")
    COMPAC_DIR =    os.path.join(directory, "compactados")
    TABLE_DIR =     os.path.join(directory, "tabelas")
    OUTROS_DIR =    os.path.join(directory, "outros")

    
    #VERIFICANDO SE EXISTE A PASTA NO DIRETORIO MODIFCADO
    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)

    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)

    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)

    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)

    if not os.path.isdir(COMPAC_DIR):
        os.mkdir(COMPAC_DIR)
    
    if not os.path.isdir(TABLE_DIR):
        os.mkdir(TABLE_DIR)

    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)



    arq_name = os.listdir(directory)
    pastaDeMundanca = ''

    for arquivo in arq_name:
        # ANTES DE PODER MODIFICAR TEM QUE VRIFICAR SE É UM ARQUIVO
        if os.path.isfile(os.path.join(directory, arquivo)):
            extensao = str.lower(getExtension(arquivo)) 
            if extensao in AUDIOS:
                pastaDeMundanca = AUDIO_DIR
            elif extensao in VIDEOS:
                pastaDeMundanca = VIDEOS_DIR
            elif extensao in IMAGENS:
                pastaDeMundanca = IMAGENS_DIR
            elif extensao in DOCUMENTOS:
                pastaDeMundanca = DOCS_DIR
            elif extensao in COMPACS:
                pastaDeMundanca = COMPAC_DIR
            elif extensao in TABELAS:
                pastaDeMundanca = TABLE_DIR
            else: 
                pastaDeMundanca = OUTROS_DIR

            # O RENAME É RESPONSAVEL POR MOVER O ARQUIVO E ATÉ RENOMEAR DINAMICAMENTE SE FOR NECESSÁRIO
            # NESSE CASO O NOME DO ARQUIVO VAI SER O NOME DELE MESMO.
            velho = os.path.join(directory, arquivo)
            novo = os.path.join(pastaDeMundanca, arquivo)
            os.rename(velho, novo)
            print('---'*30)
            print(f'Arquivo: {arquivo} foi movido para a pasta: {pastaDeMundanca} com sucesso!')



if __name__ == '__main__':
    print('-'*40)
    pasta = input('Digite o nome do arquivo você quer modificar: ')
    print('-'*40)

    organizer(pasta)