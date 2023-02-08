import os
import utils

# idf documents
#tf-idf documents
def prepareDocuments(vocabularyPath:any, documentPath:any):
    # ler vocabulario
    vocabulary = []
    vocabulary = utils.getWordsFile(vocabularyPath,vocabulary)

    # ler documentos do diretorio, pegar palavras
    documents = []
    for root, direc, files in os.walk(documentPath):
        for file in files:
            vocabularyDocuments = []
            if file.endswith(".txt"):
                vocabularyDocuments = utils.getAllWordsFile(f"{documentPath}/{file}",[])
                documents.append({
                    'file_words': vocabularyDocuments,
                    'file_name': file,
                })
    
    # Calcular tf-idf de cada termo nos documentos
    directoryAnalyse = utils.analiseDatabase(vocabulary,documents)
    return directoryAnalyse


# descobrir grau de similaridade de cada documento para a consulta
# identificar o documento e ordenar descrescente
def searchDocuments(databaseData, query ):

    # ler consulta e formatar
    queryTerms = utils.getQueryTerms(query)

    # calcular tf-idf da consulta
    tfIdfQuery = utils.getTfIdfQuery(queryTerms,databaseData["vocabulary_words"],databaseData["vocabulary_idf"])

    #calcular grau de similaridade de cada documento
    response = []
    for i in range(len(databaseData["documents_data"])):

        grauSimilaridade = utils.sim(databaseData["documents_data"][i]['file_tfidf'],tfIdfQuery)
        if grauSimilaridade > 0:
            response.append(
                {
                    'name':databaseData["documents_data"][i]['file_name'],
                    'sim': grauSimilaridade,
                    'words': " ".join(databaseData["documents_data"][i]['file_words'])[0:24]
                })
    responseSort = sorted(response, key=lambda d: d['sim'], reverse=True)
    return responseSort

def generateVocabulary(documentsPath:str):
    #Lendo diretorio e criando vocabulario
    vocabulary = []
    for root, direc, files in os.walk(documentsPath):
        for file in files:
            if file.endswith(".txt"):
                vocabulary = utils.getWordsFile(f"{documentsPath}/{file}",vocabulary)
    # guardar em txt
    with open(f"./database/vocabulario.txt","w") as f:
        try:
            for word in vocabulary:
                f.write(f"{word}\n")
        finally:
            f.close()

