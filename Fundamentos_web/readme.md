# Fundamentos de Redes e Protocolos Web

## Arquitetura Cliente-Servidor

### Cliente

Dispositivo do próprio usuário (Notebook, celular) ou software (navegador web) que inicia a comunicação.

**Responsabilidades:**
- Solicita serviços
- Exibe informações para usuários
- Lida com a interface

**Exemplo:** Seu navegador pedindo a página inicial de um site.

---

### Servidor

Um computador ou software que fornece serviços, dados, recursos.

**Responsabilidades:**
- Armazena dados
- Executa a lógica do aplicativo
- Processa requisições e envia respostas

**Exemplo:** Servidor da Netflix que envia o filme para sua televisão.

---

### Pedido / Resposta

O Cliente envia um pedido (request); o servidor envia uma resposta (response).

---

### Processamento

- **Cliente:** Mostra o resultado
- **Servidor:** Faz a parte mais pesada (banco de dados, cálculos)

---

### Client-side vs. Server-side

Refere-se a onde o código roda, sendo o lado do cliente no navegador e o lado do servidor no computador remoto (servidores, bancos de dados etc), o que é fundamental para o desenvolvimento web.

---

### Em resumo

**Clientes pedem e servidores servem**

---

## DNS (Sistema de Nomes de Domínio)

**O que é:** Um sistema distribuído que atua como um "dicionário" da internet, mapeando nomes de domínio para endereços IP.

**Função:** Quando você digita um site (ex: www.exemplo.com), o DNS converte esse nome no endereço IP correspondente do servidor, facilitando a navegação.

---

## IP (Endereço de Internet Protocol)

**O que é:** Um identificador numérico único atribuído a cada dispositivo (computador, celular, servidor), como se fosse o CEP do dispositivo, conectado a uma rede que usa o Protocolo de Internet para comunicação.

**Função:** Permite que os dispositivos se localizem e troquem dados na internet, como um endereço postal para pacotes de dados.

**Tipos:** Existem IPv4 (ex: 192.168.1.1) e IPv6 (versão mais recente, com mais endereços).

---

## Relação entre DNS e IP

**Independência e Interdependência:** O IP identifica os dispositivos, e o DNS traduz os nomes para esses IPs. Um não funciona sem o outro para a experiência moderna da internet.

**Analogia:** IP é como o número de telefone de uma pessoa; DNS é como a agenda que te ajuda a encontrar esse número usando o nome da pessoa.

---

## HTTP - HyperText Transfer Protocol

**HTTPS** - HyperText Transfer Protocol Secure (criptografa os dados trocados entre seu navegador e um site.)

---

## Verbos HTTP

- **GET** - Solicita os dados
- **POST** - Envia os dados
- **PUT** - Substitui os dados
- **DELETE** - Remove os dados
- **PATCH** - Modifica os dados parcialmente
- **HEAD** - Solicitar apenas cabeçalhos
- **OPTIONS** - Descreve opções de comunicação

---

## Status Code

- **1xx (Informativo):** Requisição recebida, processo continua
- **2xx (Sucesso):** Ação bem-sucedida
- **3xx (Redirecionamento):** Ações adicionais necessárias
- **4xx (Erro do cliente):** Erro na requisição
- **5xx (Erro do servidor):** Servidor falhou

---

## Headers

Metadados trocados entre cliente e servidor.

- **Request Headers** são enviados pelo cliente
- **Response Headers** são enviados pelo servidor

---

## Body

O body carrega os dados da requisição ou resposta, como dados a serem enviados em um POST/PUT ou o conteúdo solicitado em uma resposta.