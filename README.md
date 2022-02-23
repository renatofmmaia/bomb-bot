# Bombcrypto Bot [Family JOW]
Bot desenvolvido em python, 100% do código é aberto, para aqueles que tenham conhecimento validarem que não existe nenhum código malicioso, o bot apenas trabalha com reconhecimento de imagens para poder gerenciar as interações na tela do bombcrypto, compatível com Windows e Linux.
O bot em constante atualização, e para que ele continue 100% free, não deixei de realizar sua contribuição, isso nos motiva a continuar!

# Doações
Faça seus testes, esta usando e ele te ajuda a otimizar seus ganhos? Mostre seu agradecimento em BUSD/BNB/BCOIN, assim nossa equipe se mantem empenhada em atualizar e trazer novas funcionalidades para a comunidade :relaxed:

Smart Chain Wallet(BUSD/BNB/BCOIN) 

***0xb3e7A42b647A0875682249294107Db182DDFC321***


# Funcionalidades
- Farm personalizado, defina a % que seus herois voltam a trabalhar, configurando por raridade e otimizando seu lucro :D
- Multi Acc, logue a metamask de todas as suas contas, de play no bot e faça coisas melhores na sua vida do que ficar colocando heroes to work. :beers:
- Integração com Telegram, receba uma print do seu baú a cada X minutos, o tempo é configuravel no arquivo config.yaml.
- Anti-Broken, mesmo que aconteça um erro não tratado em tela, o bot força atualização da pagina e refaz o login, reiniciando o processo de farm, no pain yes gain!
- Anti-bloco-Indestrutivel, o bot realiza atualização do navegador(CTRL+F5), reinicializando o farm, assim não te atrasando com os blocos que bugam, a função Refresh Login é configurada por tempo no arquivo config.yaml.
- Arquivo de configuração, para que você mesmo determine como o bot deve funcionar (./config.yaml).

# Automação com uso de bots no Bombcrypto é permitido?
O uso de automação com bots ou auto clickers é liberado, conforme post abaixo no discord oficial do bombcrypto, facilmente encontrado nos canais moderados de informações
![Liberação do bot pelo bombcrypto](https://github.com/renatofmmaia/bomb-bot/blob/master/assets/infos_and_tutorial/bot_autoclickers_allowed.png)

# Como utilizar
###  Requisitos:
- Instalação do Python, instale pelo [site oficial](https://www.python.org/downloads/) ou pela [windows store](https://www.microsoft.com/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab) durante a instalação do python, não se esqueça de marcar a opção add Python to Path.
- ![Path Python](https://github.com/renatofmmaia/bomb-bot/blob/master/assets/infos_and_tutorial/python_path.png)
- Realizar download da ultima versão do bot em releases do repositorio github, clicando em https://github.com/renatofmmaia/bomb-bot/releases
- Descompactar o bot na pasta em que desejar
- (Linux) Instalar o pacote xdtools (responsável por retornar as janelas de navegador no linux) através do comando: sudo apt-get install xdotool
- (Linux) Instalar pacote Scrot (responsável pela printscreen no linux) através do comando: sudo apt-get install scrot

###  Rodando o bot:
- Abra um terminal, se for windows (aperte a tecla do windows + r e digite "cmd").
- Navegue até a pasta onde o bot foi extraído, exemplo: cd "C:\bomb-bot".
- Instale as dependências do bot executando o comando, sem aspas: "pip install -r requirements.txt".
- **IMPORTANTE:** Seu navegador não pode estar com ZOOM, pois o bot usa reconhecimento de imagem e o tamanho e proporção dos objetos fazem diferença.
- Abra seu navegador acesse o link: https://app.bombcrypto.io/webgl/index.html este link é oficial do bomb e abre a interface sem vários blocos de informação, para que a tela fique limpa para o reconhecimento de imagens do bot.
- Faça o primeiro acesso na sua metamask, pois o bot realiza o login apenas se a mesma já estiver conectada.
- Execute o bot executando o cmando, sem aspas: "python main.py"
- Enjoy the moment :D

###  Configurando Telegram
- Em seu telegram, iniciei uma conversa com @BotFather
- Clique em Start, e quando abrir as opções, clique em "/newbot"
- Em seguida informe um nome e depois um username para o bot, lembrando que username tem que terminar com "_bot" no final, exemplo "meubomb_bot"
- Finalizando você vai ver uma mensagem contendo os dados do bot que vc criou, copie o Token e insira no arquivo de configuração, config.yaml
- O 2º parametro a ser configurado é o chat_id, para isso, siga os passos abaixo:
- Criei um grupo no telegram, e adicione o bot que você acabou de criar, informando o username para encontra-lo.
- Com o grupo criado, acesse o link a seguir, alterando o TOKEN na url, pelo o que você acabou de criar: https://api.telegram.org/botSEUTOKEN/getUpdates
- Vai ser exibido na tela um JSON, procure por "chat":"id", geralmente esse valor começa com o sinal de menos(-) e altere no arquivo config.yaml chat_id.
- Exemplo chat_id
- ![chatid](https://github.com/renatofmmaia/bomb-bot/blob/master/assets/infos_and_tutorial/chat_id.png)
- Config.yaml que você tem que configurar
- ![config trelegram](https://github.com/renatofmmaia/bomb-bot/blob/master/assets/infos_and_tutorial/token_chat_id.png)

### Possíveis soluções
- (linux) Muitos problemas se rolvem ao atualizar o OS, pois os pacotes da instalação são basicos para o sistema rodar, para atualizar seu linux execute o comando: ***sudo apt updade && sudo apt upgrade -y***
- (linux) Se apresentar o erro "No module named 'tkinter'", execute o comando para instalar a interface grafica do python: ***sudo apt install python3-tk***
- (linux) Caso seu linux não reconheca o comando pip ou pip3, será necessário instala-lo, através do comando: ***sudo apt install python3-pip***

# Contato/Sugestão/Bug
- Issues github: https://github.com/renatofmmaia/bomb-bot/issues/new

