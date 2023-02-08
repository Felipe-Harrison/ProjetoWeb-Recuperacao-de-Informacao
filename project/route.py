from flask import Flask,request,render_template,jsonify
from documentController import searchDocuments,generateVocabulary,prepareDocuments

app = Flask(__name__,template_folder="./html/")
database = "./database"

# Ao iniciar gerar vocabulario
try:
    generateVocabulary(f"{database}/textos")
except:
    print("Erro ao gerar vocabulario da coleção")

# Ao iniciar calcular e analisar textos
databaseData = prepareDocuments(f"{database}/vocabulario.txt",f"{database}/textos")

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/getDocuments/<string:query>',methods=["GET"])
def getDocuments(query):
    if request.method == "GET":
        try:
            data = searchDocuments(databaseData,query=query)
            return jsonify({
                'query':query,
                'data':data,
                'status':200
            })
        except:
            return jsonify({
                'query':query,
                'data':"Erro Servidor",
                'status':500
            }) 

@app.route('/getDocument/<string:document>',methods=["GET"])
def getDocument(document):
    if request.method == "GET":
        try:
            for doc in databaseData["documents_data"]:
                if doc['file_name'] == document:
                    return jsonify({
                        'data': " ".join(doc['file_words']),
                        'status':200
                    })
        except:
            return jsonify({
                'data':"Erro Servidor",
                'status':500
            })

@app.route('/getDatabaseAnalyse/', methods=["GET"])
def returnDatabaseAnalyse():
    if request.method == "GET":
        try:
            return jsonify({
                'data':databaseData,
                'status':200
            })
        except:
            return jsonify({
                'data':"Erro Servidor",
                'status':500
            })

@app.route('/<string:ulrPath>')
def errorPage(ulrPath):
    return f'Pagina {ulrPath} não Existe'

app.run(debug=True)