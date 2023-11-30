def main():
    print("Bem-vindo à sua aventura na Segunda Guerra Mundial!\n")
    print("Ano: 1943. O mundo está mergulhado na Segunda Guerra Mundial. Você é um espião aliado infiltrado na cidade de Berlim, a capital do Terceiro Reich liderado por Adolf Hitler. As forças aliadas estão empenhadas em obter informações secretas cruciais que podem mudar o rumo da guerra a favor dos Aliados.\n")
    print("Sua missão: Como espião aliado, sua missão é dupla: coletar informações estratégicas importantes relacionadas às operações militares alemãs e identificar aliados dentro da cidade. No coração de Berlim, você está cercado por inimigos, incluindo soldados alemães e espiões nazistas. Sua sobrevivência e o sucesso de sua missão dependem de suas escolhas e habilidades de espionagem.\n")

    escolha_1 = input("Você está na rua de Berlim e vê um soldado alemão se aproximando. O que você faz? (1) Esconde-se em um beco escuro (2) Tenta passar despercebido na multidão: ")

    if escolha_1 == "1":
        print("Você se esconde no beco escuro e consegue evitar ser detectado pelo soldado alemão.\n")
        escolha_2 = input("Você encontra uma porta trancada no beco. (1) Tentar arrombar a porta (2) Continuar a andar pelo beco: ")

        if escolha_2 == "1":
            print("Você tenta arrombar a porta, mas o barulho chama a atenção de um guarda. Você é capturado e sua missão falha.\n")
        elif escolha_2 == "2":
            print("Você continua a andar pelo beco e encontra um esconderijo seguro para esperar até que o soldado alemão desapareça.\n")
            print("Sua missão continua.\n")
    elif escolha_1 == "2":
        print("Você tenta passar despercebido na multidão, mas o soldado alemão suspeita de você e pede seus documentos.\n")
        escolha_3 = input("Você tem documentos falsos, mas acredita que mostrá-los pode ser arriscado. O que você faz? (1) Mostrar os documentos (2) Tentar fugir: ")

        if escolha_3 == "1":
            print("Você mostra os documentos falsos e o soldado alemão os examina rapidamente antes de permitir que você continue.\n")
            print("Sua missão continua.\n")
        elif escolha_3 == "2":
            print("Você tenta fugir, mas o soldado alemão chama reforços e você é capturado. Sua missão falha.\n")
        else:
            print("Opção inválida. O soldado alemão fica impaciente e você é capturado. Sua missão falha.\n")
    else:
        print("Opção inválida. Sua hesitação chama a atenção do soldado alemão e você é capturado. Sua missão falha.\n")
    
    escolha_4 = input("Você agora está a salvo. O que você faz a seguir? (1) Seguir em direção ao quartel-general inimigo (2) Procurar por aliados: ")
    
    if escolha_4 == "1":
        print("Você decide se infiltrar no quartel-general inimigo. Encontra informações cruciais e consegue escapar com sucesso!\n")
        print("Parabéns, a missão foi um sucesso!\n")
        print("Você retorna com as informações valiosas que ajudam a mudar o rumo da guerra a favor dos Aliados.\n")
        print("A queda de Berlim marca o início do fim do conflito, e as informações que você trouxe contribuíram para o colapso do Terceiro Reich. A guerra chegou ao seu fim, e o mundo finalmente encontrou a paz.\n")
        print("Seu heroísmo e dedicação na missão fizeram a diferença, e sua contribuição foi fundamental para a vitória dos Aliados. O mundo agradece a você por seu serviço notável. Parabéns por completar com sucesso sua missão e ajudar a trazer o fim da guerra.\n")
        print("Obrigado por jogar e por sua participação na história!\n")
    elif escolha_4 == "2":
        print("Você procura por aliados e encontra outros espiões aliados. Juntos, vocês planejam como obter as informações necessárias.\n")
        escolha_5 = input("Como vocês planejam prosseguir? (1) Se disfarçar como oficiais alemães (2) Hackear os sistemas de comunicação inimigos: \n")

        if escolha_5 == "1":
            print("Vocês se disfarçam como oficiais alemães e conseguem acessar áreas restritas do quartel-general inimigo. Encontram as informações desejadas e escapam com sucesso!\n")
            print("Parabéns, a missão foi um sucesso!\n")
            print("Você e seus aliados retornam com as informações cruciais que auxiliam na vitória dos Aliados.\n")
            print("A queda de Berlim marca o início do fim do conflito, e as informações que você trouxe contribuíram para o colapso do Terceiro Reich. A guerra chegou ao seu fim, e o mundo finalmente encontrou a paz.\n")
            print("Seu heroísmo e dedicação na missão fizeram a diferença, e sua contribuição foi fundamental para a vitória dos Aliados. O mundo agradece a você por seu serviço notável. Parabéns por completar com sucesso sua missão e ajudar a trazer o fim da guerra.\n")
            print("Obrigado por jogar e por sua participação na história!\n")            
        elif escolha_5 == "2":
            print("Vocês decidem hackear os sistemas de comunicação inimigos, mas são pegos durante o processo. Sua missão falha.\n")
        else:
            print("Opção inválida. Seus aliados ficam indecisos e a missão é comprometida. Sua missão falha.\n")
    else:
        print("Opção inválida. Sua indecisão atrai a atenção das patrulhas inimigas e você é capturado. Sua missão falha.\n")

    print("O destino da sua missão está em suas mãos. Obrigado por jogar e por sua contribuição para a vitória dos Aliados!\n")

if __name__ == "__main__":
    main()