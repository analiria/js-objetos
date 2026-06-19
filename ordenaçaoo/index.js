const livros = require('./ordenacao/listalivros.js');

let maisbarato = 0;

for(let atual = 0; atual < livros.length; atual++){
    if(livros[atual].preco < livros [maisbarato].preco){
        maisbarato= atual;
    }
}

console.log('o livro mais barato custa ${livros[maisbarato].preco}')