Trabalho-POO-tower-defence

Trabalho de POO dos alunos: José, Luiz, Mylena.  
Temos como objetivo fazer um joguinho tower defence em Python, implementando conceitos importantes de POO.

Link do diagrama UML:  
https://lucid.app/lucidchart/3097f040-d0ea-4233-99ef-f98bffa1019a/edit?invitationId=inv_dbd2feee-4e0e-472c-a10a-8e98c4e371e5&page=0_0#  
Será necessário criar uma conta no site para visualização. Por isso, também será anexado um PDF contendo o diagrama:  
[Tower Defence UML.pdf](https://github.com/user-attachments/files/15906885/Tower.Defence.UML.pdf)




FLuxogramas


#Classe Game:
![Game](https://github.com/ZeL-ucas/Trabalho-POO-tower-defence/assets/139146076/d870440d-e873-4fc5-b726-435d1d8213f2)

#Classe Tower:
![Tower](https://github.com/ZeL-ucas/Trabalho-POO-tower-defence/assets/139146076/620074ba-6154-4d70-a62f-2bbb268f1ac5)

#Classe Projectile:
![Projectile](https://github.com/ZeL-ucas/Trabalho-POO-tower-defence/assets/139146076/007122d4-0649-4831-977c-fed71783f940)

#Classe Enemy: 
![Enemy](https://github.com/ZeL-ucas/Trabalho-POO-tower-defence/assets/139146076/b9021676-52bd-4afb-8074-36888765d913)




## Tutorial como jogar:

1. Primeiro passo é instalar a biblioteca Pygame. Com ela instalada, basta rodar o arquivo `main.py` e o jogo abrirá.

2. Para jogar, deve-se selecionar a dificuldade e inserir o nome do usuário. Fazendo isso, o jogo abrirá e começará a lançar inimigos diversos em você. Ao serem mortos, os inimigos lhe darão ouro. Se chegarem ao final, removerão sua vida.

3. Para ganhar, basta derrotar todas as ondas de inimigos. Para perder, sua vida deve chegar a 0.

4. Para se defender dos inimigos, basta clicar em uma das torres no menu lateral e clicar onde posicioná-la. Cada torre tem uma propriedade única e age de forma diferente para atacar os inimigos. Você também pode melhorar torres já existentes clicando nelas e, logo após, clicando na setinha, aumentando seus atributos.

A lógica geral do jogo é então: Inimigos nascem e correm até o final, suas torres os atacarão e, ao morrer, eles lhe darão dinheiro para comprar mais torres. Caso muitos inimigos cheguem até o final, você terá um "game over".
