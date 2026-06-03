# Aula 1 — Os Dois Mundos da Criptografia

> **Tema:** A base da Criptografia Híbrida — entender os dois tipos de criptografia que vamos combinar.
> **Público:** Programadores júnior e iniciantes (primeiro contato).
> **Duração:** 60 minutos.
> **Pré-requisitos:** Saber o que é um arquivo, um texto e o básico de "dados trafegando pela internet". Nenhum conhecimento prévio de matemática avançada é necessário.

---

## Objetivos da aula

Ao final desta aula, o aluno será capaz de:

1. Explicar com as próprias palavras o que é **cifrar** e **decifrar**.
2. Entender a diferença entre **criptografia simétrica** (chave única) e **criptografia assimétrica** (par de chaves).
3. Saber o que é **AES**, o que é um **bloco**, o que é o **IV** e por que ele precisa ser aleatório.
4. Saber o que é **RSA**, o que significa **RSA-2048** e por que usamos o padding **OAEP**.
5. Identificar o **"problema fatal"** de cada um dos dois tipos — o que prepara o terreno para a Aula 2.

---

## Como conduzir (sugestão de tempos)

| Bloco | Conteúdo | Tempo |
|------|----------|-------|
| 0 | Abertura: por que isso importa | 5 min |
| 1 | Criptografia Simétrica (AES, blocos, IV, modos) | 25 min |
| 2 | Criptografia Assimétrica (RSA, par de chaves, OAEP) | 25 min |
| 3 | Fechamento + gancho para a Aula 2 | 5 min |

> 💡 **Dica didática:** comece sempre pela analogia do cotidiano, depois mostre o termo técnico. Iniciantes aprendem muito melhor "do concreto para o abstrato".

---

## Bloco 0 — Abertura: por que isso importa? (5 min)

Toda vez que você manda uma mensagem no WhatsApp, entra no app do banco ou compra algo online, seus dados **viajam pela internet passando por dezenas de computadores** que você não controla (roteadores, provedores, servidores). Qualquer um deles, em tese, poderia ler o que passa por ali.

**Analogia do cotidiano — cartão-postal vs. carta lacrada:**

- Mandar dados **sem criptografia** é como mandar um **cartão-postal**: todo mundo que manuseia (carteiro, central dos Correios) consegue ler o que está escrito.
- Mandar dados **com criptografia** é como mandar uma **carta dentro de um envelope lacrado e escrita em um código secreto**: mesmo que alguém intercepte, não entende nada.

**Vocabulário que vamos usar a aula inteira:**

| Termo técnico | Em português simples | Exemplo |
|---|---|---|
| **Texto claro** (*plaintext*) | A mensagem original, legível | `Oi, minha senha é 1234` |
| **Texto cifrado** (*ciphertext*) | A mensagem embaralhada | `7f3a9c...` (lixo ilegível) |
| **Chave** (*key*) | O "segredo" que embaralha/desembaralha | um número gigante |
| **Cifrar** (*encrypt*) | Transformar claro → cifrado | "trancar" |
| **Decifrar** (*decrypt*) | Transformar cifrado → claro | "destrancar" |

> A criptografia que vamos estudar não é "inventar um código secreto na hora". São algoritmos **públicos, abertos e testados pelo mundo todo** há décadas. **O segredo não é o algoritmo — o segredo é a chave.**

---

## Bloco 1 — Criptografia Simétrica: a chave única (25 min)

### A ideia central

Na **criptografia simétrica**, **a mesma chave** tranca e destranca. Quem cifra e quem decifra precisam ter **uma cópia idêntica da mesma chave secreta**.

**Analogia do cotidiano — o diário com cadeado:**

Imagine um diário com um cadeado. Você tranca o diário com sua chave. Para sua melhor amiga ler o diário, ela precisa ter uma **cópia exata da mesma chave**. A mesma chave fecha e abre. Simples assim.

```
   Chave 🔑                           Chave 🔑 (a MESMA)
      |                                    |
      v                                    v
[Texto claro] --cifrar--> [Texto cifrado] --decifrar--> [Texto claro]
```

### Um exemplo bem simples para sentir o gosto (Cifra de César)

A forma mais antiga e simples de cifra: **deslocar cada letra algumas posições no alfabeto**. Se a "chave" é o número **3**, cada letra anda 3 casas para frente:

```
Texto claro:    O L A
Desloca +3:     R O D
```

Para ler, o destinatário só precisa saber a chave (3) e voltar 3 casas. A "chave única" aqui é o número **3** — tanto para cifrar quanto para decifrar.

> ⚠️ A Cifra de César é **fraquíssima** (só existem 25 chaves possíveis, dá pra testar todas em segundos!). Ela serve só para entender o conceito de "chave". Os algoritmos reais usam chaves astronomicamente maiores.

### O algoritmo real: AES

Na vida real usamos o **AES** (*Advanced Encryption Standard*). É o padrão de criptografia simétrica usado no mundo inteiro: WhatsApp, HTTPS dos sites, criptografia do seu HD/celular, Wi-Fi (WPA2)... está em todo lugar.

- **AES-256** = AES com uma chave de **256 bits**. Quanto mais bits, mais combinações possíveis e mais seguro. 256 bits significam um número de chaves possíveis tão absurdamente grande que nem todos os computadores do planeta juntos conseguiriam testar todas antes do Sol se apagar.

### Como o AES funciona por cima: "block cipher" (cifra de bloco)

O AES **não embaralha a mensagem inteira de uma vez**. Ele trabalha em **pedaços de tamanho fixo de 16 bytes** (128 bits), chamados de **blocos**.

**Analogia do cotidiano — o triturador de papel:**

Pense numa máquina que tritura **exatamente uma folha por vez**. Você alimenta seu documento folha a folha. O AES é parecido: ele "tritura/embaralha" os dados de 16 em 16 bytes.

```
[ bloco 1 ][ bloco 2 ][ bloco 3 ] ...   (cada bloco = 16 bytes)
```

### O problema dos blocos repetidos (e por que precisamos de "modos")

Se a gente simplesmente embaralhar **cada bloco de forma independente** com a mesma chave (esse modo ingênuo se chama **ECB**), aparece um problema grave:

> **Blocos de entrada iguais geram blocos de saída iguais.** Ou seja, padrões da mensagem original "vazam" para a mensagem cifrada.

**Exemplo clássico — o "pinguim do ECB":** se você cifrar a imagem de um pinguim usando o modo ECB, a imagem cifrada **ainda mostra o contorno do pinguim**, porque as regiões de cor repetida viram blocos repetidos. Embaralhou, mas não escondeu.

**Solução: modo CBC (*Cipher Block Chaining* — "blocos acorrentados").** No CBC, **cada bloco é misturado com o bloco cifrado anterior** antes de ser cifrado. Como cada bloco depende do anterior, blocos iguais **não** geram saídas iguais. Os padrões somem.

**Analogia do cotidiano — a corrente:** cada elo da corrente está preso ao elo anterior. Você não consegue mexer em um elo sem afetar a sequência. No CBC, cada bloco "se prende" ao resultado do bloco anterior.

### O IV (Vetor de Inicialização) — por que precisa ser aleatório

Tem um detalhe: o **primeiro** bloco não tem um "bloco anterior" para se misturar. O que fazer?

Usamos um **IV** (*Initialization Vector*, ou Vetor de Inicialização): um **valor aleatório** que funciona como o "bloco zero", o ponto de partida da corrente.

**Por que o IV precisa ser aleatório e diferente a cada vez?**

Se você cifrar **a mesma mensagem duas vezes**, com a **mesma chave**, mas com **IVs diferentes**, os resultados ficam **completamente diferentes**. Sem isso (ou com um IV fixo), cifrar a mesma mensagem duas vezes daria o **mesmo** texto cifrado — e um espião perceberia: *"eles mandaram a mesma coisa de novo"*.

**Analogia do cotidiano — o tempero aleatório da receita:**

O IV é como uma pitada de um ingrediente aleatório que você joga **no começo** da receita. Mesmos ingredientes (mensagem) + mesma chave, mas um tempero inicial diferente a cada vez → o prato sai com aparência diferente toda vez. Assim ninguém reconhece "ah, é o mesmo pedido de sempre".

> 📌 **Importante:** o IV **não precisa ser secreto** — ele é enviado junto com o texto cifrado (o destinatário precisa dele para decifrar). Mas ele **precisa ser aleatório e único** para cada mensagem.

### Os "modos de operação": CBC vs. CTR vs. GCM (visão geral)

Esses "modos" são as diferentes maneiras de encadear os blocos. Os três mais citados:

| Modo | Como funciona (resumo) | Protege contra adulteração? | Quando usar |
|------|------------------------|-----------------------------|-------------|
| **CBC** | Acorrenta os blocos; precisa de *padding* (completar o último bloco) | ❌ Não (só esconde o conteúdo) | Legado / aprendizado |
| **CTR** | Transforma a cifra de bloco em um "fluxo"; cifra um contador e mistura com os dados; não precisa de padding | ❌ Não | Quando se quer velocidade/paralelismo |
| **GCM** | É o CTR **+ um selo de autenticidade** | ✅ **Sim** | **Padrão recomendado hoje** |

**Resumo de uma linha:**
> **CBC** = mais antigo, só esconde o conteúdo. **GCM** = moderno, esconde o conteúdo **e avisa se alguém mexeu**. Nesta matéria, nosso exemplo usa **CBC** (porque é mais didático), mas, em sistemas novos de verdade, prefira **GCM**.

**Analogia do cotidiano:** o **CBC** é uma encomenda dentro de uma caixa fechada. O **GCM** é a mesma caixa **com uma fita lacre que rasga e denuncia se alguém abriu no caminho**.

### O problema fatal da criptografia simétrica: distribuição de chaves

Aqui está o calcanhar de Aquiles. Alice (no Brasil) quer mandar um arquivo cifrado para Beto (no Japão). Os dois precisam ter **a mesma chave AES**.

**Mas como a Alice entrega essa chave para o Beto pela internet sem que um espião (a Eva) intercepte?**

- Se a Alice mandar a chave por e-mail, a Eva lê a chave no caminho. 💀
- Para mandar a chave em segredo, a Alice precisaria... de **outra** chave secreta. E como ela manda **essa**? É um problema de "ovo e galinha".

**Analogia do cotidiano — a cópia da chave do armário:**

Você e um amigo precisam dos dois ter a mesma chave de um armário compartilhado. Mas a única forma de entregar a cópia da chave é **pelo correio** — e o carteiro pode tirar uma cópia no caminho. Como combinar a chave **sem já ter um canal secreto**?

> 🔑 **Esse é o "problema da distribuição de chaves".** É exatamente isso que a criptografia assimétrica vem resolver. Guarde esse problema na cabeça — ele é a ponte para o próximo bloco.

---

## Bloco 2 — Criptografia Assimétrica: o par de chaves (25 min)

### A grande ideia

Na **criptografia assimétrica** (também chamada de **criptografia de chave pública**, *public-key cryptography*), existem **duas chaves diferentes, mas ligadas matematicamente**:

- 🔓 **Chave pública** — você distribui para o mundo todo, sem medo.
- 🔒 **Chave privada** — você guarda só para você, em segredo absoluto.

**A mágica:** o que uma chave tranca, **só a outra destranca**. Se algo foi cifrado com a chave **pública**, **só a chave privada** correspondente consegue decifrar.

### Analogia do cotidiano nº 1 — a caixa de correio com fenda

Pense na sua **caixa de correio** com uma fenda:

- **Qualquer pessoa** pode depositar uma carta pela fenda → isso é **cifrar com a chave pública**.
- **Só você** tem a chave que abre a caixa para pegar as cartas → isso é **decifrar com a chave privada**.

A fenda é "pública" (qualquer um usa). A abertura da caixa é "privada" (só você).

### Analogia do cotidiano nº 2 — o cadeado aberto (a melhor analogia!)

Imagine que você tem vários **cadeados que abrem todos com a SUA única chave**. Você sai distribuindo esses **cadeados abertos** para todo mundo (isso é sua **chave pública**).

- Qualquer pessoa pode colocar uma mensagem numa caixa e **fechar o seu cadeado** (cifrar). É fácil fechar.
- Uma vez fechado, **só VOCÊ** consegue abrir, com a sua chave (decifrar).
- Detalhe genial: **nem mesmo quem fechou** o cadeado consegue reabrir! Quem trancou não consegue destrancar.

```
Mundo todo tem o cadeado aberto 🔓 (chave pública)
         |
         v
Alguém fecha a caixa  --->  só VOCÊ abre com a chave 🔑 (chave privada)
```

**O ponto que muda tudo:** para receber mensagens secretas, você **não precisa mais combinar nenhum segredo antes**. Você simplesmente **publica sua chave pública abertamente** (até num site!). A Eva pode ver a chave pública à vontade — isso **não** ajuda ela a decifrar, porque para isso precisaria da chave **privada**.

> ✅ **Isso resolve o problema da distribuição de chaves do Bloco 1!** Não preciso de um canal secreto prévio para receber segredos.

### O algoritmo real: RSA

O algoritmo assimétrico mais clássico é o **RSA** (das iniciais dos criadores: Rivest, Shamir e Adleman, 1977).

Ele se apoia em um fato matemático simples de entender:

> **Multiplicar dois números primos gigantes é fácil. Mas pegar o resultado e descobrir quais eram os dois primos (fatorar) é praticamente impossível** com os computadores de hoje.

É como misturar duas tintas: misturar é instantâneo, mas "desmisturar" para achar as cores originais é inviável.

### RSA-2048: o tamanho da chave

**RSA-2048** significa uma chave RSA de **2048 bits**. Esse número, escrito por extenso, tem cerca de **617 dígitos**.

- Tentar quebrar isso por força bruta (testar/fatorar) levaria **mais tempo que a idade do Universo** com a tecnologia atual.
- **Chave maior = mais segura, porém mais lenta.** 2048 bits é a linha de base comum hoje; para segurança extra usa-se 3072 ou 4096 bits.

**Analogia do cotidiano:** é um cadeado tão complexo que, mesmo testando bilhões de combinações por segundo, você não terminaria nem em trilhões de anos.

### Por que precisamos de "padding"? E por que OAEP e não PKCS#1 v1.5

Usar o RSA "puro" (só elevar o número da mensagem a uma potência) é **perigosamente inseguro**, por dois motivos principais:

1. É **determinístico**: a mesma mensagem sempre vira a mesma cifra → vaza informação.
2. Mensagens curtas ou previsíveis abrem brechas matemáticas.

A solução é o **padding**: antes de cifrar, embrulhamos a mensagem com **dados estruturados + dados aleatórios**. Existem dois esquemas famosos:

- **PKCS#1 v1.5** — o padding **antigo**. Funciona, mas tem uma vulnerabilidade célebre (o **ataque de Bleichenbacher**, 1998): um atacante que envia muitas cifras modificadas para um servidor e observa se o padding é "válido" ou "inválido" consegue, aos poucos, recuperar a mensagem. (Falaremos disso na Aula 2.)
- **OAEP** (*Optimal Asymmetric Encryption Padding*) — o padding **moderno e recomendado**. Ele mistura a mensagem com dados aleatórios usando funções de hash, de modo que: (a) a mesma mensagem cifra **diferente** a cada vez, e (b) qualquer adulteração faz a decifragem **falhar de forma limpa, sem dar pistas**.

**Regra de uma linha:**
> Em sistemas novos, use **RSA-OAEP**, nunca PKCS#1 v1.5.

**Analogia do cotidiano — o anelzinho na caixa com enchimento:**

Imagine mandar um **anel pequenininho** dentro de uma **caixa grande cheia de isopor (enchimento aleatório) e lacrada com fita anti-violação**. O isopor (padding aleatório) esconde o tamanho/formato real do conteúdo; a fita (verificação de integridade) denuncia se mexeram. O **OAEP** é essa caixa esperta. O **PKCS#1 v1.5** é uma caixa antiga cuja fita os atacantes aprenderam a descolar e recolar sem deixar rastro.

### O problema fatal da criptografia assimétrica: lenta e limitada no tamanho

O RSA é maravilhoso para o problema da chave, mas tem **duas limitações sérias**:

1. **É LENTO** — centenas a milhares de vezes mais lento que o AES para a mesma quantidade de dados.
2. **Só cifra dados MENORES que a chave.** Com RSA-2048 + OAEP, você cifra **no máximo ~190 bytes**. Você **literalmente não consegue** cifrar uma foto de 5 MB ou um vídeo de 1 GB diretamente com RSA.

**Analogia do cotidiano — a fenda minúscula e lenta:**

A fenda da caixa de correio mágica é **minúscula e o mecanismo é lento e caro**. Dá pra passar um bilhetinho pequeno por ali, mas você **não passa um sofá pela fenda** — e nem ia querer mandar mil cartas, uma a uma, por um sistema tão devagar.

---

## Bloco 3 — Fechamento e gancho para a Aula 2 (5 min)

### Recapitulando: os dois mundos lado a lado

| | 🔑 **Simétrica (AES)** | 🔓🔒 **Assimétrica (RSA)** |
|---|---|---|
| Quantas chaves? | **Uma** (igual para os dois lados) | **Duas** (pública + privada) |
| Velocidade | ⚡ **Muito rápida** | 🐢 **Lenta** |
| Tamanho dos dados | 📦 Arquivos enormes, sem problema | 🤏 Só dados minúsculos (~190 bytes) |
| Compartilhar a chave | 😰 **Difícil** (problema da distribuição) | 😎 **Fácil** (chave pública é pública) |
| Exemplos | AES-256-CBC, AES-GCM | RSA-OAEP, RSA-2048 |

### O gancho (deixe os alunos curiosos!)

Repare na simetria do problema:

- A **simétrica** é rápida e aguenta dados grandes, **mas não consegue compartilhar a chave com segurança**.
- A **assimétrica** compartilha chaves com segurança, **mas é lenta e só cifra dados minúsculos**.

> ❓ **E se a gente combinasse os dois?** Usar a assimétrica (RSA) só para o que ela faz bem (mandar uma coisinha pequena em segredo) e a simétrica (AES) para o que ela faz bem (cifrar o monte de dados)?
>
> É exatamente isso que veremos na **Aula 2: Criptografia Híbrida** — o esquema que de verdade protege seus sites HTTPS, seus arquivos cifrados e seus apps de mensagem.

---

## 📋 Cola da Aula 1 (resumo para distribuir)

- **Cifrar** = trancar (claro → cifrado). **Decifrar** = destrancar (cifrado → claro). **O segredo é a chave, não o algoritmo.**
- **Simétrica:** uma chave só, rápida, aguenta dados grandes. Ex.: **AES-256**. Problema: **como compartilhar a chave?**
- **AES** trabalha em **blocos de 16 bytes**. O modo **CBC** "acorrenta" os blocos. O **IV** é o ponto de partida aleatório — precisa ser **aleatório e único** (não precisa ser secreto).
- **Modos:** CBC (antigo, só esconde) → CTR (fluxo) → **GCM (moderno: esconde + detecta adulteração)**.
- **Assimétrica:** par **pública/privada**. Pública para cifrar, privada para decifrar. Resolve o compartilhamento de chave. Ex.: **RSA**.
- **RSA-2048** = chave de 2048 bits (~617 dígitos). Use **OAEP** como padding, **nunca PKCS#1 v1.5**.
- **Problema do RSA:** lento e só cifra ~190 bytes.

---

## 🧠 Perguntas para fixação (discussão em sala)

1. Por que a Cifra de César é insegura, mesmo sendo "criptografia"?
2. Se o IV não precisa ser secreto, por que ele ainda é importante?
3. Explique, na analogia do cadeado, por que quem fecha o cadeado não consegue reabri-lo.
4. Por que não dá para simplesmente cifrar um vídeo de 1 GB inteiro com RSA?
5. Em uma frase: qual problema a criptografia assimétrica resolve que a simétrica não consegue?

---

➡️ **Próxima aula:** juntamos AES + RSA na **Criptografia Híbrida (KEM/DEM)** e descobrimos por que esse design é seguro (segurança semântica, ataques de cifra escolhida e *forward secrecy*).
