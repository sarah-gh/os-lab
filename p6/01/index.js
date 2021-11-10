const fs = require('fs');
const util = require('util') //npm i util
const reader = require("readline-sync"); //npm install readline-sync
let words_bank = require('./words_bank.json');


async function translate1(input_text){
    let user_words=input_text.split(' ')
    let output_text=""
    for(user in user_words){ 
        let x = false
        for(word in words_bank){
            if(words_bank[word].en==user_words[user]){
                output_text += words_bank[word].fa+' '
                x = true
                break
            }
        }
        if(x==false){
            output_text += user_words[user]+' '
        }
    }
    console.log(output_text)
}

async function translate2(input_text){
    let user_words=input_text.split(' ')
    let output_text=""
    for(user in user_words){ 
        let x = false
        for(word in words_bank){
            if(words_bank[word].fa==user_words[user]){
                output_text += words_bank[word].en+' '
                x = true
                break
            }
        }
        if(x==false){
            output_text += user_words[user]+' '
        }
    }
    console.log("\ntranslate: ")
    console.log('** '+output_text+' **')
}

const operat = util.promisify(operation)

async function operation() {
    console.log(words_bank);
    let string = ''
    while(true) {
        let menu = require('readline-sync'),
        choise = ['Translate English to Persian', 'Translate Persian to English', 'Add new words to Data base'],
        index = menu.keyInSelect(choise, 'Which one?');
        if(index == 0){
            string = reader.question("please write your text: ");
            translate1(string)
        } else if (index == 1) {
            string = reader.question("please write your text: ");
            translate2(string)
        } else if (index == 2) {
            let t1 = reader.question("please write your english word: ");
            let t2 = reader.question("please write your translate word: ");
            const data = {
                en: t1,
                fa: t2
            }
            words_bank.push(data)
            fs.writeFileSync('words_bank.json',JSON.stringify(words_bank));
            console.log(t1, t2)
        } else {
            break
        }
    }
}

operat()
