"use strict";
// Introdução:
// Como introduzimos a propriedade type tanto em User quanto em Admin, agora ficou mais fácil distingui-los.
// Depois que a lógica de verificação do tipo de objeto foi extraída para funções separadas isUser e isAdmin, a função logPerson passou a apresentar novos erros de tipagem.
Object.defineProperty(exports, "__esModule", { value: true });
exports.isUser = isUser;
exports.isAdmin = isAdmin;
function isUser(pessoa) {
    if ('occupation' in pessoa) {
        return true;
    }
    return false;
}
function isAdmin(pessoa) {
    if ('role' in pessoa) {
        return true;
    }
    return false;
}
