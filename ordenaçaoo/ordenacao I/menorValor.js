const livros = require('./listaLivros');

function menorValor(arrPodutos, posicaoInicial){
    let maisBarato = posicaoInicial;    
    
    for(let atual = posicaoInicial; atual < arrPodutos.length; atual++){
        if (arrPodutos[atual].preco < arrPodutos[maisBarato].preco){
            maisBarato = atual;
        }
    }    
    return maisBarato;
}

module.exports = menorValor;