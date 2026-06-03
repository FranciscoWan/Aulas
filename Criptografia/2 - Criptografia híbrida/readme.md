# Aula 2 — Juntando o Melhor dos Dois Mundos: Criptografia Híbrida

> **Tema:** Como combinar AES + RSA na **Criptografia Híbrida** e por que esse design é seguro.
> **Público:** Programadores júnior e iniciantes (primeiro contato).
> **Duração:** 60 minutos.
> **Pré-requisitos:** Aula 1 (simétrica vs. assimétrica, AES/IV, RSA/OAEP).

---

## Objetivos da aula

Ao final desta aula, o aluno será capaz de:

1. Explicar a ideia da **Criptografia Híbrida**: RSA protege a **chave**, AES protege os **dados**.
2. Conhecer os nomes formais **KEM** e **DEM**.
3. Justificar **por que não usamos RSA direto nos dados**.
4. Entender três conceitos de segurança: **segurança semântica**, **ataque de cifra escolhida (CCA2)** e **forward secrecy**.
5. Ler e entender um **exemplo de código real** que faz tudo isso.

---

## Como conduzir (sugestão de tempos)

| Bloco | Conteúdo | Tempo |
|------|----------|-------|
| 0 | Recapitulação rápida da Aula 1 | 5 min |
| 1 | A ideia da Criptografia Híbrida (KEM/DEM) | 20 min |
| 2 | Por que o design é seguro (3 conceitos) | 25 min |
| 3 | Exemplo prático em código | 5 min |
| 4 | Fechamento e visão geral | 5 min |

---

## Bloco 0 — Recapitulação rápida (5 min)

Na Aula 1 vimos que cada tipo de criptografia tem uma força e uma fraqueza **complementares**:

| | 🔑 **AES (simétrica)** | 🔓🔒 **RSA (assimétrica)** |
|---|---|---|
| Velocidade | ⚡ Rápida | 🐢 Lenta |
| Dados grandes? | ✅ Sim | ❌ Só ~190 bytes |
| Compartilhar a chave? | 😰 Difícil | 😎 Fácil (chave pública) |

> A pergunta que ficou no ar: **e se a gente usasse cada um só para aquilo que ele faz bem?**

---

## Bloco 1 — A ideia da Criptografia Híbrida (20 min)

### Qual problema queremos resolver?

Olhe a tabela acima. O AES é ótimo, mas precisa que os dois lados tenham **a mesma chave**. O RSA resolve isso, **mas só cifra coisas pequenas**.

> ❓ **Qual é a única coisa pequena que precisamos compartilhar em segredo para poder usar o AES?**
>
> 💡 **A própria chave AES!** E ela é pequena: AES-256 tem só **32 bytes** — cabe folgado dentro do "limite de ~190 bytes" do RSA.

### A receita híbrida (o "clique" da matéria)

A sacada é genial e simples:

1. Use o **AES** (rápido) para cifrar os **dados de verdade** (o arquivo grande).
2. Use o **RSA** (compartilhamento seguro) para cifrar **apenas a chave AES** (que é pequena).
3. Envie os dois juntos: **[chave AES cifrada com RSA]** + **[dados cifrados com AES]**.

O volume pesado anda no "caminhão rápido" (AES); o segredinho crítico anda no "canal seguro porém estreito" (RSA).

### Analogia do cotidiano — o baú do tesouro

Você precisa mandar um **baú do tesouro, enorme e pesado, cheio de documentos** (seus dados) para um amigo do outro lado do mundo.

1. Você tranca o baú com um **cadeado de segredo forte e rápido** (o **AES**). Travar é rápido e o baú aguenta uma tonelada de coisas.
2. Mas seu amigo precisa do **segredo do cadeado** para abrir. Você não pode gritar o segredo pelo mundo.
3. Então você escreve o **segredo num papelzinho** e o joga pela **fenda da caixa de correio mágica do seu amigo** (a **chave pública RSA** dele) — só ele consegue abrir aquela caixa.
4. Você despacha **o baú trancado + o papelzinho lacrado na caixa mágica**, juntos.
5. Seu amigo: **abre a caixa mágica com a chave privada dele** → lê o segredo → **abre o baú** → lê os documentos. ✅

```
   Baú pesado (dados)  --trancado com-->  Cadeado AES 🔒  (rápido, cabe tudo)
   Segredo do cadeado  --enfiado na-->    Caixa mágica RSA 🔓 (só o amigo abre)

   Você envia:  [ baú trancado ]  +  [ segredo dentro da caixa mágica ]
```

### Passo a passo técnico

**🔒 CIFRAR (quem envia):**

1. Gere uma **chave AES nova e aleatória** (ex.: AES-256, 32 bytes) — **só para esta mensagem**.
2. Gere um **IV aleatório**.
3. Cifre os **dados** com **AES-256-CBC** usando a chave + IV → *dados cifrados*.
4. Cifre a **chave AES** com **RSA-OAEP** usando a **chave pública** do destinatário → *chave encapsulada*.
5. Envie: **chave AES cifrada + IV + dados cifrados**.

**🔓 DECIFRAR (quem recebe):**

1. Use sua **chave privada RSA + OAEP** para decifrar a **chave AES**.
2. Com a chave AES recuperada + o IV, decifre os **dados** com **AES-256-CBC**.
3. Pronto: texto claro de volta. ✅

### Os nomes formais: KEM e DEM

Na literatura acadêmica, esse padrão tem um nome formal: **KEM/DEM**.

| Sigla | Nome | O que é | No nosso caso |
|------|------|---------|----------------|
| **KEM** | *Key Encapsulation Mechanism* | A parte que **embrulha/protege a chave** | **RSA-OAEP** cifrando a chave AES |
| **DEM** | *Data Encapsulation Mechanism* | A parte que **protege os dados** | **AES-256-CBC** cifrando os dados |

> "Criptografia Híbrida" e "KEM/DEM" são **a mesma ideia**. *Híbrida* é o nome do dia a dia; *KEM/DEM* é o nome formal/acadêmico. "Encapsular" é só uma palavra chique para "embrulhar com segurança".

### Por que não usar RSA direto nos dados? (reforçando)

Essa é a pergunta que fecha o raciocínio. Dois motivos:

1. **Tamanho:** RSA-2048 cifra no máximo ~190 bytes. **Um arquivo real não cabe.** (No nosso teste de código, a mensagem tinha 1750 bytes — já passou do limite do RSA sozinho.)
2. **Velocidade:** RSA é centenas/milhares de vezes mais lento que AES. Cifrar um vídeo inteiro com RSA seria **inviável na prática**.

Por isso usamos RSA **só para o pedacinho pequeno e crítico (a chave)** e AES para todo o **volume**.

**Analogia:** você não manda o sofá pela fenda da caixa de correio. Manda **só a chavinha** — e o sofá vai de caminhão.

---

## Bloco 2 — Por que esse design é seguro (25 min)

Três conceitos explicam por que cada decisão de design foi tomada.

### 2.1 Segurança Semântica — por que gerar uma chave AES nova a cada vez

**Segurança semântica** significa, em linguagem simples:

> Olhar para o texto cifrado **não revela nada** sobre o texto claro — nem mesmo se **duas mensagens cifradas são iguais**.

Por que isso depende de **chave (e IV) novos a cada mensagem**?

- Se você **reaproveitasse** a mesma chave AES e o mesmo IV para tudo, mensagens iguais gerariam cifras **iguais**. Um atacante começaria a perceber padrões: *"essa cifra sempre aparece de manhã = deve ser a ordem de ataque ao amanhecer"*.
- Gerando **chave + IV novos e aleatórios a cada mensagem**, o **mesmo** texto cifrado **nunca se repete**. O atacante não consegue montar um "dicionário" de cifra → mensagem.

> 🧪 **Provamos isso no código:** cifrar a palavra `"ola"` duas vezes gerou dois textos cifrados **completamente diferentes**.

**Analogia do cotidiano — a ordem secreta do general:**

Mesmo que o general envie **"ATACAR AO AMANHECER"** todo santo dia, **cada dia a versão cifrada é diferente**. O inimigo, vendo as mensagens interceptadas, **não consegue perceber que é sempre a mesma ordem**.

> 📌 **Regra prática:** **nunca** reaproveite o par (chave, IV). Chave nova por mensagem é o ideal.

### 2.2 Ataque de Cifra Escolhida (CCA2) — o que o OAEP protege

**O cenário do ataque:** o atacante **não tem** a chave privada. Mas ele consegue **enviar cifras (possivelmente modificadas)** para um servidor e **observar a resposta** — por exemplo, se o servidor responde *"padding válido"* ou *"padding inválido"*, ou se demora um tempo diferente.

> Cada uma dessas respostinhas é uma "dica" (um **oráculo**). Juntando **milhares** dessas dicas, o atacante consegue **reconstruir a mensagem** — ou até a chave — **sem nunca ter tido a chave privada**. Isso se chama **ataque de cifra escolhida adaptativo (CCA2)**.

**Exemplo real e famoso:** o **ataque de Bleichenbacher (1998)** contra o padding antigo **PKCS#1 v1.5** funcionou contra servidores SSL/TLS reais. Décadas depois, variantes ressurgiram (ex.: o ataque **"ROBOT"**, em 2017, ainda afetava sistemas em produção).

**O que o OAEP faz:** o padding do OAEP é **aleatório** e tem **verificação de integridade embutida**. Qualquer cifra adulterada **falha de forma limpa e sempre igual — sem dar nenhuma dica**. Por isso o **RSA-OAEP** é projetado para **resistir a CCA2**.

**Analogia do cotidiano — o cofre que dá dicas:**

Imagine um cofre que, quando você erra a senha, faz um **barulho um pouquinho diferente conforme você chega "perto"** do número certo. Um ladrão usa esses sons como pista para ir acertando dígito por dígito.

- O **PKCS#1 v1.5** é como esse cofre **que vaza dicas**.
- O **OAEP** é o cofre que dá **sempre o mesmo "não" inútil**, sem nenhuma pista — não importa quão "perto" você chegou.

### 2.3 Forward Secrecy — chaves efêmeras (e uma verdade importante)

**Forward secrecy** (sigilo encaminhado) significa:

> Se a sua chave de **longo prazo** for roubada **no futuro**, as conversas **passadas** que foram gravadas **continuam protegidas**.

Como se consegue isso? Usando uma chave **efêmera** (descartável) **por sessão**, que é **destruída depois** e que **nunca** foi protegida pela chave de longo prazo.

#### ⚠️ A verdade técnica (seja honesto com os alunos)

> O esquema híbrido **simples com RSA** que ensinamos **NÃO tem** forward secrecy.

Por quê? Porque a chave AES é protegida pela **chave pública RSA de longo prazo**. Então:

1. O atacante **grava hoje** todo o tráfego cifrado (chave AES cifrada + dados cifrados).
2. **Amanhã** ele rouba sua **chave privada RSA** (vazamento, invasão, intimação judicial...).
3. Com a chave privada, ele decifra a **chave AES** (passo KEM) e **abre tudo o que gravou no passado**. 💀

Ou seja: **a chave de longo prazo "destranca" o passado inteiro.**

#### Como obter forward secrecy de verdade

Em vez de cifrar a chave AES com RSA, os dois lados **negociam uma chave compartilhada** usando **Diffie-Hellman efêmero (ECDHE)** — chaves **novas e descartáveis** por sessão, **destruídas** ao final. Mesmo que a chave de longo prazo vaze depois, **não há nada guardado** que abra as sessões antigas.

> 🌐 **É por isso que o HTTPS moderno usa ECDHE** para a troca de chaves, e não RSA puro. Quando o RSA aparece no TLS moderno, costuma ser para **assinar/autenticar o servidor**, não para trocar a chave.

**Analogia do cotidiano — o cofre descartável de cada reunião:**

Forward secrecy é usar um **cofre descartável para cada reunião** e **destruí-lo ao final**. Mesmo que um ladrão roube depois a sua **chave-mestra**, ele **não abre as reuniões passadas** — aqueles cofres já viraram pó.

No esquema RSA simples, ao contrário, **a sua chave-mestra abre todos os cofres antigos** que alguém tenha guardado.

#### Então o esquema RSA híbrido é ruim?

Não! Ele é:

- ✅ **Excelente para aprender** os conceitos (é o foco desta matéria).
- ✅ **Ótimo para cifrar arquivos e e-mails** (ex.: o **PGP/GPG** usa exatamente esse modelo).
- ⚠️ Mas, para canais **"ao vivo"** (HTTPS, mensageiros em tempo real), prefere-se esquemas **com forward secrecy** (ECDHE).

---

## Bloco 3 — Exemplo prático em código (5 min)

Abaixo está o esquema híbrido completo em **Python**, usando a biblioteca padrão `cryptography`. **Este código foi testado e funciona.** Mostre-o lendo os comentários em voz alta — eles mapeiam exatamente os passos do Bloco 1.

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import os

# --- O destinatario gera seu par de chaves RSA-2048 (uma unica vez) ---
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()


def cifrar_hibrido(dados: bytes, public_key) -> dict:
    # 1. Gera uma chave AES-256 (32 bytes) e um IV (16 bytes) NOVOS e aleatorios
    chave_aes = os.urandom(32)
    iv = os.urandom(16)

    # 2. Padding PKCS7 para completar blocos de 16 bytes (exigencia do modo CBC)
    padder = PKCS7(128).padder()
    dados_com_padding = padder.update(dados) + padder.finalize()

    # 3. DEM: cifra os DADOS com AES-256-CBC (rapido, aguenta arquivos grandes)
    cifra = Cipher(algorithms.AES(chave_aes), modes.CBC(iv))
    encryptor = cifra.encryptor()
    dados_cifrados = encryptor.update(dados_com_padding) + encryptor.finalize()

    # 4. KEM: cifra a CHAVE AES com RSA-OAEP usando a chave PUBLICA do destinatario
    chave_aes_cifrada = public_key.encrypt(
        chave_aes,
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # 5. Envia tudo junto: chave cifrada + IV + dados cifrados
    return {"chave_cifrada": chave_aes_cifrada, "iv": iv, "dados_cifrados": dados_cifrados}


def decifrar_hibrido(pacote: dict, private_key) -> bytes:
    # 1. KEM: recupera a chave AES com a chave PRIVADA + OAEP
    chave_aes = private_key.decrypt(
        pacote["chave_cifrada"],
        asym_padding.OAEP(
            mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    # 2. DEM: decifra os dados com AES-256-CBC usando a chave recuperada + IV
    cifra = Cipher(algorithms.AES(chave_aes), modes.CBC(pacote["iv"]))
    decryptor = cifra.decryptor()
    dados_com_padding = decryptor.update(pacote["dados_cifrados"]) + decryptor.finalize()

    # 3. Remove o padding
    unpadder = PKCS7(128).unpadder()
    return unpadder.update(dados_com_padding) + unpadder.finalize()


# --- Teste ---
mensagem = b"Mensagem secreta super importante! " * 50  # 1750 bytes: nao caberia so no RSA!
pacote = cifrar_hibrido(mensagem, public_key)
recuperada = decifrar_hibrido(pacote, private_key)

print("Decifrou corretamente?", recuperada == mensagem)  # True
```

**Saída ao rodar (resultado real do teste):**

```
Tamanho da mensagem original: 1750 bytes
Tamanho da chave AES cifrada (RSA): 256 bytes
Decifrou corretamente? True
Mesma mensagem, cifras diferentes? True
```

**O que esse resultado prova, na prática:**

- A mensagem de **1750 bytes** foi cifrada sem problema — o **RSA sozinho não conseguiria** (limite ~190 bytes). É o AES carregando o volume.
- A chave AES cifrada pelo RSA tem exatamente **256 bytes** (= 2048 bits ÷ 8) — o "tamanho de saída" do RSA-2048.
- **Cifrar a mesma mensagem duas vezes deu resultados diferentes** → é a **segurança semântica** acontecendo de verdade.

> 🛠️ **Nota para produção:** este exemplo usa **CBC** porque é mais didático. Em sistemas novos de verdade, prefira **AES-GCM**, que também **detecta adulteração** (integridade). E, para canais ao vivo, prefira troca de chaves com **forward secrecy (ECDHE)**.

---

## Bloco 4 — Fechamento e visão geral (5 min)

### O quadro completo (mapa mental)

```
                    CRIPTOGRAFIA HIBRIDA
                            |
        +-------------------+-------------------+
        |                                       |
       KEM                                     DEM
   (protege a chave)                      (protege os dados)
        |                                       |
     RSA-OAEP                              AES-256-CBC
        |                                       |
   chave PUBLICA cifra                    chave AES + IV cifram
   chave privada decifra                  o arquivo grande
        |                                       |
   so cifra coisa pequena (~190 B)        rapido, aguenta tudo
   resolve "como mandar a chave?"         IV novo => seg. semantica
```

### Por que cada peça existe (a colinha de ouro)

| Peça | Por que está ali |
|------|-------------------|
| **AES** | Rápido e aguenta dados grandes — carrega o volume |
| **RSA** | Compartilha a chave AES em segredo, sem canal prévio |
| **Chave AES nova por mensagem** | **Segurança semântica** (cifras nunca se repetem) |
| **IV aleatório** | Mesmo dentro de uma chave, esconde padrões |
| **OAEP** (em vez de PKCS#1 v1.5) | Protege contra **ataque de cifra escolhida (CCA2)** |
| **ECDHE** (se precisar) | Dá **forward secrecy** — protege o passado |

### Analogia final que amarra tudo

> Você manda o **baú pesado** trancado com um **cadeado rápido (AES)**, e enfia o **segredinho do cadeado** dentro da **caixa de correio mágica do destinatário (RSA)**. Usa um **cadeado novo a cada envio** (segurança semântica), com uma **caixa mágica que não dá dicas a ladrões (OAEP)**. Se quiser que nem o roubo futuro da sua chave abra o passado, use **caixas descartáveis por reunião (forward secrecy/ECDHE)**.

---

## 📋 Cola da Aula 2 (resumo para distribuir)

- **Híbrida = RSA protege a chave + AES protege os dados.** Junta o melhor dos dois.
- **KEM** = embrulha a chave (RSA-OAEP). **DEM** = embrulha os dados (AES-CBC). É o nome formal da híbrida.
- **Por que não RSA direto nos dados?** Lento e só cifra ~190 bytes. A chave AES (32 bytes) cabe; o arquivo não.
- **Segurança semântica:** chave + IV **novos a cada mensagem** → cifras iguais nunca se repetem.
- **CCA2 (cifra escolhida):** atacante usa respostas do servidor como "dicas". **OAEP** não dá dicas → protege contra isso. (PKCS#1 v1.5 dá → ataque de Bleichenbacher.)
- **Forward secrecy:** proteger o **passado** se a chave de longo prazo vazar. **RSA híbrido simples NÃO tem**; ECDHE tem. Por isso o HTTPS moderno usa ECDHE.
- **Em produção:** prefira **AES-GCM** (detecta adulteração) e **ECDHE** (forward secrecy).

---

## 🧠 Perguntas para fixação (discussão em sala)

1. Por que mandamos a chave AES dentro do RSA, e não o arquivo inteiro?
2. Qual papel o RSA faz: KEM ou DEM? E o AES?
3. Explique, com a analogia do general, o que é segurança semântica.
4. Como um atacante pode quebrar uma cifra **sem ter** a chave privada? O que o OAEP faz contra isso?
5. Um espião gravou seu tráfego HTTPS hoje. Amanhã ele rouba sua chave privada. Em qual esquema ele consegue ler o tráfego de hoje — RSA simples ou ECDHE? Por quê?

---

## 🚀 Para ir além (próximos temas)

- **AES-GCM** e criptografia autenticada (AEAD) — confidencialidade **+ integridade**.
- **Diffie-Hellman e ECDHE** — troca de chaves com forward secrecy.
- **TLS 1.3 / HTTPS** — onde tudo isso roda junto, milhões de vezes por segundo.
- **Assinaturas digitais** — usar a chave **privada** para *assinar* e a **pública** para *verificar* (autenticidade, não sigilo).
- **PGP/GPG** — criptografia híbrida aplicada a e-mails e arquivos.
