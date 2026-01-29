// Introdução:
// Como introduzimos a propriedade type tanto em User quanto em Admin, agora ficou mais fácil distingui-los.
// Depois que a lógica de verificação do tipo de objeto foi extraída para funções separadas isUser e isAdmin, a função logPerson passou a apresentar novos erros de tipagem.

// Exercício:
// Descubra como ajudar o TypeScript a entender os tipos nessa situação e aplique as correções necessárias.

import {Person} from './atividade2'
import {Admin} from './atividade3'

export function isUser(pessoa:Admin|Person): pessoa is Person{
    if ('occupation' in pessoa){
        return true
    }
    return false
}

export function isAdmin(pessoa:Admin|Person): pessoa is Admin{
    if ('role' in pessoa){
        return true
    }
    return false
}

