# ProjetoWeb-Recuperacao-de-Informacao

Projeto para aplicar em website técnicas de Recuperação de informação, como TF-IDF, utlizadas por buscadores.

Projeto feito com JavaScript, Html5 e CSS3 para design. Foi utilizado Python para realizar lógica da Recuperação de Informação e uso do Flask, framework Python, para utilizar Python com tecnologias web.

# Objetivo:
Criar uma aplicação Web que atua como buscador de documentos, assim como Google e Bing. Utilizando técnicas de Recuperação de Informação, alem de praticar framework Flask.

# Tecnicas de Recuperação de Informação

## Ponderação TF-IDF(Term frequency – Inverse Document Frequency)
<p>É uma ponderação de termos na qual é associado para cada termo de um documento um peso que quantifica a importância deste termo na descrição do 
conteúdo do documento, o que permite dar pesos aos documentos de uma coleção com base na consulta feita pelo usuário. Este peso permite avaliar e ordenar quais documentos são relevantes para a consulta feita, entregando assim os documentos que mais vão ajudar o usuário.</p>
<p>Esta ponderação é obtida pelo produto da ponderação TF com a ponderação IDF, onde:</p>
<ul>
  <li>TF: peso é determinado pela alta frequencia do termo no documento, ou seja, documentos que possuem termos que repetem muitas vezes tem maior valor de TF;</li>
  <li>IDF: peso é determinado pela baixa frequencia de um termo na coleção(todos os documentos),em outras palavras, quanto menos um termo aparece em todos os documentos, maior será o valor de IDF. Esta abordagem é utilizada pois termos que aparecem em poucos documentos são mais específicos, facilitando a busca. </li></ul>
Nesse sentido, documentos com termos mais frequentes e mais raros dentro da coleção possuem um peso TF-IDF maior.

## Modelo Vetorial
Método utilizado para determinar um valor para cada documento armazenado no sistema com base numa consulta do usuário. Consiste em atribuir um valor de relevânica, para identificar o grau de correspondência entre cada documento e a consulta realizada pelo usuário, para assim fornecer os melhores resultados.
<p>Este modelo utiliza a ponderação TF-IDF.</p>

# Como utilizar na sua maquina:

1 - Realizar a clonagem do repositório:

https:
```shell
cd "diretorio de sua preferencia"
git clone https://github.com/Felipe-Harrison/ProjetoWeb-Recuperacao-Informacao
```
2 - Navegue com o cmd ate a pasta, onde o repositório esta salvo

```shell
cd ProjetoWeb-Recuperacao-de-Informacao
```
3 - Faça instalação das dependencias

```shell
pip install unidecode flask
```

4 - Navegue ate a pasta do projeto e realize o comando

```shell
cd .\project\  
python .\route.py 
```

5 - Um link será gerado, podendo ser acessado pelo seu navegador;

# Como alterar a coleção de documentos
<p>Para alterar os documentos disponíveis para consulta do usuário é necessário adicionar os documentos em formato .txt</p>
<p>Os arquivos .txt devem ser colocados dentro da pasta database/textos, assim como na imagem</p>
<img src="https://user-images.githubusercontent.com/76136248/217397726-b456a12d-8254-4315-9455-36412cbcc4eb.png">

# Páginas do Site:
As páginas do site foram criadas com um design inspirado no estilo vintage.

Tela de busca:
![image](https://user-images.githubusercontent.com/76136248/217398246-d8346ced-1d8e-47bb-a81b-9f493b5406e2.png)

Tela de busca:
![image](https://user-images.githubusercontent.com/76136248/217399210-fb184d0a-2cb5-445a-a941-629d2980b735.png)
