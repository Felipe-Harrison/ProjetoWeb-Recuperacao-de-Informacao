import unidecode
import math

# file -> Caminho do arquivo
# vocabulary -> para unir vocabulario de varios documentos em um
def getWordsFile(file:any,vocabulary:list):

    vocabularyAux = vocabulary
    with open(file,"r", encoding='utf-8') as f:
        try:
            lines = f.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    word_formated = unidecode.unidecode(word.lower().replace(",","").replace('"',"").replace(".",""))
                    if not word_formated in vocabularyAux:
                        vocabulary.append(word_formated)
            return vocabularyAux
        finally:
            f.close()

def getAllWordsFile(file:any,vocabulary:list):
    vocabularyAux = vocabulary
    with open(file,"r", encoding='utf-8') as f:
        try:
            lines = f.readlines()
            for line in lines:
                words = line.split()
                for word in words:
                    word_formated = unidecode.unidecode(word.lower().replace(",","").replace('"',"").replace(".",""))
                    vocabulary.append(word_formated)   
            return vocabularyAux
        finally:
            f.close()

# retorna lista binaria, indicando se termo do vocabulario esta(1) ou não no documento(0)
def getBagofWordsBi(vocabulary: list, documentWords: list):

    bag = []

    for word in vocabulary:
        if word in documentWords:
            bag.append(1)
        else:
            bag.append(0)
    return bag

# Retorna lista indicando qual a frequencia de ocorrencia dos termos do vocabulario no documento
def getBagofWordsFrequency(vocabulary: list, documentWords: list):

    bag = []

    for word in vocabulary:
        bag.append(documentWords.count(word))
        
    return bag

# Calcular Term Frequency (TF)
def tf(frequency: int):
    if frequency == 0:
        return 0
    return 1 + math.log(frequency,2)

# Calcular Inverse Document Frequency (IDF)
def idf(numberDocuments: int, occurrence: int):
    if occurrence == 0:
        return 0
    return math.log((numberDocuments/occurrence),2)

# Calcular TFIDF
def tfidf(frequency: int, numberDocuments: int, occurrence: int):
    return tf(frequency) * idf(numberDocuments,occurrence)

# calcular tf de todos os documentos com base na bag of words
# Recebe lista de listas, cada lista corresponde a bag of words de cada documento
# retorna uma lista de listas, cada lista com os tf de cada termo de um documento
def getTfDocuments(bagofWords: list):
    docsTF = []
    for bag in bagofWords:
        TFdocument = []
        for wordFrequency in bag:
            TFdocument.append(tf(wordFrequency))
        docsTF.append(TFdocument)
    return docsTF
 
# calcular idf de cada termo do vocabulario com base nos documentos
# Recebe uma lista com o vocabulario;
# Recebe uma lista de listas, cada lista corresponde aos termos de um documento
# retorna uma lista com idf de cada termo
def getIdfDocuments(vocabulary: list, documents: list):
    
    vocabularyIDF = []
    colectionSize = len(documents)
    for word in vocabulary:
        appearinDocs = 0
        for doc in documents:
            if word in doc["file_words"]:
                appearinDocs+=1
        vocabularyIDF.append(idf(colectionSize,appearinDocs))
    return vocabularyIDF

# Realizar analise dos documentos e vocubulario, alem de obter TD-IDF de cada documento
def analiseDatabase(vocabulary: list, documents: list):
    # montar bag of words dos documentos
    docsBagofWords = []
    for doc in documents:
        wordsFrequency = getBagofWordsFrequency(vocabulary,doc["file_words"])
        docsBagofWords.append(wordsFrequency)
        doc['file_bow'] = wordsFrequency

    # calcular tf de cada documento
    docsTF = getTfDocuments(docsBagofWords)
    
    # calcular idf de cada termo
    vocabularyIDF = getIdfDocuments(vocabulary,documents)

    #calcular Tf-IDF
    docsTFIDF = []
    for docTf in docsTF:
        tfidfDoc = []
        for i in range(len(vocabulary)):
            tfidfDoc.append(docTf[i] * vocabularyIDF[i])
        docsTFIDF.append(tfidfDoc)
    
    # Preparar retorno
    for i in range(len(documents)):
        documents[i]['file_tf'] = docsTF[i]
        documents[i]['file_tfidf'] = docsTFIDF[i]
    
    return {
        'vocabulary_words': vocabulary,
        'vocabulary_idf': vocabularyIDF,
        'documents_data': documents,
    }
    
def getQueryTerms(query:str):
    formatQuery = query.lower().replace(" ",",").replace('"',"").replace(".","")
    queryTerms = formatQuery.split(",")
    return queryTerms

def getTfIdfQuery(queryTerms:list, vocabulary:list, documentsIdf:list ):
    # montar bag of words da consulta
    docsBagofWords = []
    docsBagofWords.append(getBagofWordsFrequency(vocabulary,queryTerms))
    
    # calcular tf de cada termo da consulta
    docsTF = getTfDocuments(docsBagofWords)

    #calcular Tf-IDF
    docsTFIDF = []
    for docTf in docsTF:
        tfidfDoc = []
        for i in range(len(vocabulary)):
            tfidfDoc.append(docTf[i] * documentsIdf[i])
        docsTFIDF.append(tfidfDoc)
    return docsTFIDF[0]

def productIntern(d:list,q:list):
    sum = 0
    for i in range(len(d)):
        sum += d[i] * q[i]
    return sum

def norma(vetor:list):
    sum = 0
    for item in vetor:
        sum += item**2
    return math.sqrt(sum)

def sim(document:list,query:list):
    divisor = norma(document) * norma(query)
    if(divisor <= 0):
        return 0
    return productIntern(document,query)/divisor
