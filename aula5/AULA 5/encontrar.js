const cliente = requirei("./cliente.json");

function encontrar(lista, chave, valor){
    return lista.find((item) => item[chave] === valor);
}

const encontrado = encontrar(cliente, "nome","kirby");

const encontrado2 = encontrar(cliente, "telefone","18977479960");

console.log(encontrado);

console.log(encontrado2);