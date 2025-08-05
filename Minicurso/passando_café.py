import time

def fazer_cafe():
    while True:
        chaleira = int(input("Você pegou a chaleira? \n0. NÃO \n1. SIM\nResposta: "))
        agua = int(input("\nVocê colocou a água na chaleira? \n0. NÃO \n1. SIM\nResposta: "))
        if agua and chaleira == 1:
            agua_quente = 1
            while True:
                print("\nA água está esquentando", end="", flush=True)
                for _ in range(5):
                        time.sleep(1)
                        print(".", end="", flush=True)
                termica = int(input("\n\nVocê pegou a térmica? \n0. NÃO \n1. SIM\nResposta: "))
                coador = int(input("\nVocê pegou o coador? \n0. NÃO \n1. SIM\nResposta: "))
                po_no_coador = int(input("\nVocê colocou o café dentro do coador?  \n0. NÃO \n1. SIM\nResposta: "))

                if termica and coador and po_no_coador == 1:
                    print("\nAgora é só despejar a água e fazer seu café.")
                    print("\nDespejando a água", end="", flush=True)

                    for _ in range(5):
                        time.sleep(1)
                        print(".", end="", flush=True) 

                    print("\nSeu café está pronto!!\nAgora é só aproveitar seu café e aprender mais sobre Python.")
                    print("\nPrograma encerrado!!")
                    break
                else:
                    print("\nA térmica, o coador ou o pó de café não foram pegos.\n")
            break
        else:
            agua_quente = 0
            print("\nA chaleira ou a água não foram pegas.\n\n")

fazer_cafe()