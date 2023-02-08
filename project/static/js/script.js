window.onload = () => {

    let searchInput = document.forms.searchBar;

    searchInput.addEventListener("submit", async (e) => {
        e.submitter.disabled = true;
        e.preventDefault();

        console.log("Buscando...");
        let load = loading();

        try {
            let returnField = document.querySelector(".searchResult");
            returnField.innerHTML = "";
            
            let response = await makeSearch(searchInput.query.value);
            if(response.status === 200) {
                console.log("Response",response);
                document.querySelector(".search-container").classList.add("searched");
                document.title = `Vetorial Search - exibindo documentos para  ${searchInput.query.value}`
                appendResult(response.data);
            }
            
        } catch (err) {
            console.log("error on search",err);

        } finally {
            load.stop();
            e.submitter.disabled = false

        }
        
    });

    document.querySelector("#icon-search").addEventListener("click", async (e) => {
        searchInput.lastElementChild.click();
    })

}

const loading = () => {
    this.icon = document.querySelector("#icon"),

    icon.className = "fa fa-spinner fa-spin";

    this.stop = () => {
        this.icon.className = "fa fa-search"
    }

    return this
}

async function makeSearch(search) {

    let opt = {
        method:"GET",
        headers: {"Content-Type": "application/json"}
    }

    let response = fetch(`/getDocuments/${search}`,opt)
        .then((response) => 
            response.json()
        ).then( data => {
            return data
        })
    return response
}

const appendResult = function (dados) {

    let content = document.querySelector(".searchResult");
    let template = document.querySelector("#templateResult");

    if(!dados.length) {
        content.innerHTML = "Não foi encontrado nenhum documento relevante para esta consulta";
        return;
    }

    for(item of dados){
        let Card = template.innerHTML
            .replace("{document-name}",item.name)
            .replace("{document-name}",item.name)
            .replace("{document-words}", item.words)
            .replace("{document-sim}", item.sim)
        content.insertAdjacentHTML("beforeend", Card);
    }
}

async function getDocumentText(e,documentName){

    if(e.lastElementChild.classList.contains("open")) {
        e.lastElementChild.innerHTML = `<p>${e.lastElementChild.innerText.slice(0,24)}</p>`;
        e.lastElementChild.classList.toggle("open");
        return;
    }

    try {
        let opt = {
            method:"GET",
            headers: {"Content-Type": "application/json"}
        }

        let response = await fetch(`/getDocument/${documentName}`,opt)
            .then((response) => 
                response.json()
            ).then( data => {
                return data
            })
        
        if(response.status == 200) {
            e.lastElementChild.innerHTML = `<p>${response.data}</p>`;
            e.lastElementChild.classList.toggle("open");
        }

    } catch (err) {
        console.log("Error in getDocumentText",err);
    }
    
    
}

async function getDataAnalyse() {
    let opt = {
        method:"GET",
        headers: {"Content-Type": "application/json"}
    }

    let response = fetch(`/getDatabaseAnalyse/`,opt)
        .then((response) => 
            response.json()
        ).then( data => {
            return data
        })
    return response
}
