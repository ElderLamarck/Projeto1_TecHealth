function consultaDados(endpoint, callback, dados) {
    var obj = null;
    if (dados != undefined) {
        obj = {
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify(dados)
        }
    }
    fetch(endpoint, obj).then(function(response) {
        var contentType = response.headers.get("content-type");
        if (contentType && contentType.indexOf("application/json") !== -1) {
        return response.json().then(function(json) {
            callback(json);
        });
        } else {
            console.log("Oops, we haven't got JSON!");
        }
    });
}
