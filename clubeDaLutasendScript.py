async function enviarScript(...scriptTexts) {
    const lines = scriptTexts.flatMap(text => text.split(/[\n\t]+/).map(line => line.trim()).filter(line => line));
    let main = document.querySelector("#main"),
        textarea = main?.querySelector(`div[contenteditable="true"]`);
    
    if (!textarea) throw new Error("Não há uma conversa aberta");

    for (const line of lines) {
        console.log("Enviando:", line);

        textarea.focus();
        setTimeout(() => {
            document.execCommand("insertText", false, line);
            textarea.dispatchEvent(new KeyboardEvent("keydown", { key: "Enter", bubbles: true }));
            textarea.dispatchEvent(new KeyboardEvent("keypress", { key: "Enter", bubbles: true }));
            textarea.dispatchEvent(new KeyboardEvent("keyup", { key: "Enter", bubbles: true }));
        }, 100);

        await new Promise(resolve => setTimeout(resolve, 300));

        let botaoEnviar = document.querySelector('[aria-label="Enviar"]');

        if (botaoEnviar) {
            botaoEnviar.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true }));
        } else {
            console.warn("Botão de enviar não encontrado");
        }
        if (lines.indexOf(line) !== lines.length - 1) {
            await new Promise(resolve => setTimeout(resolve, 500));
        }
    }

    return lines.length;
}

enviarScript(`
Clube da Luta

v2- Digitalizado por TailsApnea

Chuck Palahniuk Gostaria de agradecer às seguintes pessoas pelo amor e apoio, apesar das coisas terríveis

que acontecem:

Ina Gebert, Geoff Pleat, Mike Keefe, Michael Bern Smith, Suzie Vitello, Tom Spanbauer, Gerald Howard, Edward Hibbert, Gordon Growden, Dennis Stovall, Linni Stovall, Ken Foster, Monica Drake e Fred Palahniuk.

1

Primeiro Tyler me arruma um emprego de garçom, depois enfia um revólver na minha boca e diz que o primeiro passo para a vida eterna é morrer. Por muito tempo Tyler e eu fomos grandes amigos. As pessoas estão sempre me perguntando se conheço Tyler Durden.

Com o cano da arma quase encostado no fundo da minha garganta, ele afirma:

— Ninguém quer morrer de verdade.

Sinto na língua os buracos silenciadores que furamos no cano do revólver. Grande parte do ruído da detonação é produzido pela expansão dos gases, tem aquele silvo supersônico que a bala faz quando disparada. Para fazer um silenciador, basta furar buracos no cano da arma, vários deles. Isso permite que o gás escape e a bala saia abaixo da velocidade do som. Se furar errado, o revólver explode na sua mão. — Não é realmente uma morte. A gente vira lenda. Não vai envelhecer — continua ele.

Empurro com a língua o cano da arma para a bochecha e digo, Tyler, você está falando de vampiros.

Estamos no alto de um prédio que em dez minutos deixará de existir. Pegue vapor de ácido nítrico com 98% de concentração e adicione o ácido a três vezes a mesma quantidade de ácido sulfúrico. Faça isso num banho de gelo. Depois, com um conta-gotas, pingue glicerina lentamente. E você obterá nitroglicerina. Sei disso porque Tyler sabe disso. A nitro misturada a pó de serra também dá um bom explosivo plástico. É só misturar a nitro com algodão e adicionar sal amargo como sulfato. Também funciona. Outros preferem misturar parafina. Para mim, parafina nunca funcionou.

Tyler e eu estamos no alto do Parker-Morris Building com a arma enfiada na minha boca e ouvindo os vidros se estilhaçando. Estamos na beira do telhado. É um dia nublado, mesmo na altura em que estamos. É o prédio mais alto do mundo, aqui em cima é sempre frio. E muito silencioso; você se sente como um desses macacos do espaço que só fazem aquilo que são treinados para fazer. Puxe a alavanca. Aperte o botão.

Você não entende nada e, depois, simplesmente morre. Acima do centésimo nonagésimo primeiro andar, na beira do telhado, a rua matiza-se de um tapete rústico, com as pessoas paradas, olhando para cima. O vidro que se quebrou foi de uma janela logo abaixo de nós. Outra vidraça

explode na parede lateral do prédio, de onde sai um fichário grande como uma

geladeira preta, logo abaixo um arquivo cora seis gavetas despenca pelo paredão e cai em lentas cambalhotas, e cai, cada vez menor, e cai, desaparecendo entre a massa de pessoas.

Num desses 191 andares sob os nossos pés, os macacos espaciais do Comitê de Maldades do Projeto de Ações Violentas estão feito loucos, tentando destruir cada resto de história.

Sabe aquele velho ditado que diz que a gente destrói quem mais ama? Bom, o inverso também é verdadeiro.

Com a arma enfiada na sua boca e o cano entre os dentes, só dá para falar as vogais.

Estamos nos nossos dez minutos finais.

Outra janela estoura no prédio, o vidro espirra para todo lado como uma revoada de pombos, e uma escrivaninha, empurrada pelo Comitê de Maldades, vem surgindo na parede lateral, balança, escorrega e vira um objeto mágico voador que se perde na multidão.

Em nove minutos o Parker-Morris Building não existirá mais. Pegue uma boa quantidade de gelatina explosiva e amarre nas colunas estruturais de qualquer coisa; dá para derrubar qualquer prédio do mundo. É só escorar bem com sacos de areia na base para que a explosão se dê contra a coluna e não se espalhe pela garagem.

Não se ensina nos livros como fazer isso. Há três maneiras de fazer napalm: primeiro, misturando partes iguais de gasolina e suco de laranja concentrado e congelado. Segundo, misturando partes iguais de gasolina e coca diet. Terceiro, dissolvendo alimento granulado para gatos em gasolina, até formar uma pasta. Quer saber como se faz o gás que afeta o sistema nervoso? Ah, e aqueles carros bombas fantásticos!

Nove minutos.

O Parker-Morris Building voará pelos ares, todos os 191 andares, e tombará lentamente como uma árvore na floresta. É possível derrubar qualquer coisa. É estranho pensar que o lugar em que você está será apenas um ponto no céu. Tyler e eu na beira do telhado, o revólver na minha boca, fico pensando se esse revólver está limpo. Ninguém mais se lembra das histórias de assassinato e suicídio de Tyler enquanto vemos outro arquivo despencar pela parede lateral do prédio, as gavetas se abrirem, uma pilha de papéis ser apanhada por uma corrente ascendente e se espalhar com o vento. Oito minutos. Depois a fumaça, a fumaça saindo das vidraças quebradas. A equipe de demolição chegará à carga principal em, talvez, oito minutos. A carga principal explodirá a carga da base, as colunas estruturais vão desmoronar e as fotos do Parker-Morris Building entrarão para os livros de história. Uma seqüência de cinco fotos. Na primeira, o prédio ainda em pé. Na segunda, num ângulo de oitenta graus. Depois, 75 graus. Na quarta foto o prédio está num ângulo de 45 graus, a estrutura começa a ceder e a torre a se curvar levemente. Na última foto, a torre, todos os 191 andares, despencam ruidosamente sobre o museu nacional, que é o verdadeiro alvo de Tyler.

— O mundo é nosso, o nosso mundo, e toda essa velharia vai morrer — diz

Tyler.

Se eu soubesse aonde tudo iria dar, ficaria mais feliz se morresse e fosse logo para o céu.

Sete minutos.

No alto do Parker-Morris Building com a arma de Tyler dentro da minha boca. Enquanto mesas, arquivos e computadores despencam como meteoros sobre a multidão ao redor do prédio, enquanto saem espirais de fumaça pelos vidros quebrados e a três quarteirões daqui a equipe de demolição olha o relógio, eu sei de tudo: a arma, a anarquia, a explosão, tudo isso tem que ver com Marla Singer.

Seis minutos.

Existe uma espécie de triângulo entre nós. Eu quero Tyler. Tyler quer Marla. Marla quer a mim.

Eu não quero Marla, e Tyler não me quer ver por perto, nunca mais. Isso não tem nada que ver com amor, como na proteção. Tem que ver com proprie- dade, como no domínio.

Sem Marla, Tyler não teria nada.

Cinco minutos.

Talvez a gente se torne uma lenda, talvez não. Eu acho que não, mas espere. Onde estaria Jesus se ninguém tivesse escrito os evangelhos? Quatro minutos.

Empurro o cano do revólver para a bochecha e digo, se você quer ser uma lenda, Tyler, deixe comigo. Estou aqui desde o começo. Eu me lembro de tudo.

Três minutos.

2

Os grandes braços de Bob se fecham em torno de mim, e eu fico espremido no escuro, entre suas novas tetas suadas, penduradas e enormes, tão grandes quanto imaginamos que Deus seja. Circulando pelo porão da igreja repleto de homens, nós nos encontrávamos todas as noites: este é Art, este é Paul, este é Bob; seus ombros largos me lembravam o horizonte. A cabeleira loira de Bob, resultado de cremes para cabelos que se autodenominam mousse de esculpir, é loira e espessa, a risca muito reta.

Os braços dele estão em volta de mim, a mão espalmada prensando minha cabeça de encontro às novas tetas que despontaram em seu peito nu. — Tá tudo bem. Pode chorar — diz Bob.

Dos joelhos até a testa sinto as reações químicas da queima de comida e oxigénio dentro de Bob.

— Eles pegaram no começo — continua Bob. — Talvez seja apenas um seminoma. Se for, as chances de sobreviver são quase 100%. Os ombros de Bob erguem-se numa longa inspiração e então vão caindo, caindo, caindo, em convulsivos soluços.

Há dois anos venho aqui semanalmente, e toda vez Bob me abraça e eu

choro.

— Chore — Bob inspira e soluça, soluça, soluça. — Pode chorar. Sua grande cara molhada apóia-se no topo da minha cabeça e eu me entrego. É sempre assim quando choro. Chorar é só o que dá para fazer nesta escuridão asfixiante, dentro de outra pessoa, quando você percebe que tudo o que já fez não passa de lixo.

Tudo de que você mais se orgulhava foi jogado fora. Eu me entrego.

Foi o mais perto do sono que pude chegar em quase uma semana. Foi assim que conheci Marla Singer.

Bob chora porque seis meses atrás seus testículos foram removidos. Depois a terapia de suporte hormonal. Bob tem tetas porque suas taxas de testosterona são muito altas. Quando o nível de testosterona sobe demais, o corpo produz estrogênio para tentar compensar.

Foi então que eu chorei porque, nesse momento, sua vida não é nada, e não só nada, mas um sono profundo.

Excesso de estrogênio e você ganha tetas de vaca. É fácil chorar quando a gente sente que as pessoas que amamos vão nos rejeitar ou morrer. Em pouco tempo o índice de sobrevivência de todo mundo cairá a zero.

Bob me ama porque pensa que meus testículos também foram removidos. Em volta de nós no porão da Trinity Episcopal com seus sofás xadrezes de loja de segunda mão há talvez vinte homens e apenas uma mulher, todos aos pares, a maioria chorando. Alguns pares se curvam, encostam as cabeças, orelha contra orelha, como dois lutadores atracados. O homem que está com a única mulher tem os cotovelos apoiados nos ombros dela, um em cada lado da cabeça, segura a cabeça entre as mãos, esconde o rosto no pescoço dela e chora. A mulher entorta a cara para o lado e pega um cigarro. Eu espio por baixo do sovaco do Big Bob. — A vida toda — lamenta Bob. — Por que isso, eu não sei. A única mulher presente nos Remanescentes Unidos, o grupo de apoio ao câncer testicular; essa mulher fuma um cigarro sob o peso de um estranho e seus olhos acabam encontrando os meus.

Fingida.

Fingida.

Fingida.

Cabelos curtos, pretos, desgrenhados, olhos redondos como num desenho animado japonês, cor de leite aguado, amarelada, um vestido estampado com rosas escuras, essa mulher também estava no meu grupo de apoio à tuberculose da sexta-feira à noite. Estava na minha mesa-redonda de melanoma de quarta à noite. Na segunda, estava no meu grupo de discussão sobre leucemia, os Firmes na Fé. Atrás da cabeça dela, pouco abaixo do centro, tem um pino entortado enfiado no couro cabeludo branco.

Quando a gente procura esses grupos de apoio, todos têm nomes mais ou menos otimistas. O meu grupo de quinta-feira à noite de parasitas do sangue chama-se Livres e Soltos.

O grupo que frequentei de parasitas do cérebro chamava-se Para Cima e

Para o Alto.

Tarde de domingo com os Remanescentes Unidos no porão da Trinity Episcopal, e essa mulher está outra vez aqui. O pior é que não consigo chorar com ela me olhando. Era a parte de que eu mais gostava, ficar abraçado e chorar com Big Bob, perder toda a esperança. A gente trabalha tanto, o tempo todo. Este é o único lugar em que consigo relaxar e me entregar. São as minhas férias.

Entrei no meu primeiro grupo de apoio há dois anos, depois de consultar o médico sobre a minha insónia, outra vez. Eu não dormia havia três semanas. Três semanas sem dormir, e tudo se transforma numa experiência extracorpórea. O médico disse: — A insónia é apenas um sintoma de algo muito maior. Descubra o que está errado de fato. Ouça o seu corpo.

Eu só queria dormir. Queria aquelas capsulazinhas azuis de Amytal Sodium, de 200 miligramas. Queria as tubinhos vermelhos e azuis de Tuinal, os batonzinhos de Seconal.

O médico me mandou mascar raiz de valeriana e fazer mais exercícios. Eu acabaria dormindo uma hora ou outra.

Do jeito que minha cara caiu, amassada, murcha como fruta velha, você diria que eu já estava morto.

O médico disse, se eu quisesse saber o que era sofrimento, que desse uma espiada no Primeira Comunhão de terça-feira à noite. Visse os parasitas de cérebro. Visse as doenças degenerativas dos ossos. As disfunções cerebrais orgânicas. Visse os doentes de câncer indo embora. Então eu fui.

Entrei no primeiro grupo e foram feitas as apresentações: esta é Alice, esta é Brenda, este é Dover. Todos sorrindo com uma arma invisível encostada na cabeça.

Nunca dei meu nome verdadeiro nos grupos de apoio. Uma pequena e esquelética mulher chamada Chloe, com o fundilho da calça pendendo murcho e vazio, diz que a pior coisa em relação aos seus parasitas de cérebro é que ninguém quer fazer sexo com ela. Aqui está ela, tão perto da morte que o seguro de vida já havia pago setenta e cinco mil pratas, e Chloe só queria se deitar com alguém pela última vez. Nada de preliminares, só sexo.

O que você vai dizer? O que é que se pode dizer? A morte começou com Chloe sentindo-se meio cansada, agora Chloe estava desgostosa demais para pensar em tratamento. Filmes pornográficos, ela tinha filmes pornográficos em seu apartamento. Durante a Revolução Francesa, Chloe me contou, as prisioneiras, duquesas, baronesas, marquesas, o que for, elas davam para qualquer um que ficasse por cima. Chloe respirava em meu pescoço. Ficar por cima. Montar, sabe. Passar o tempo fodendo.

La petite morte, como dizem os franceses.

Chloe tinha filmes pornográficos, se eu estivesse interessado. Ecstasy.

Lubrificantes.

Em outras épocas, eu teria tido uma ereção. Nossa Chloe, entretanto, é um esqueleto imerso em cera amarela.

Sendo Chloe quem é, eu não sou nada. Menos que nada. Mesmo assim ela me cutuca o ombro quando nos sentamos em círculo na esteira. Fechamos os olhos. É a vez de Chloe nos conduzir numa meditação dirigida, levando-nos pelo jardim da serenidade. Chloe nos faz subir a montanha até o palácio das sete portas. Dentro do palácio há sete portas, a verde, a amarela, a laranja, e Chloe nos faz abrir cada uma, a azul, a vermelha, a branca, e ver o que há dentro. De olhos fechados, imaginamos nossa dor como uma bola de luz curativa flutuando sobre nossos pés, subindo pelos joelhos, nos quadris, no peito. Nossos chakras estão se abrindo. O chakra do coração. O chakra da cabeça. Chloe nos leva para dentro de cavernas para conhecermos nosso animal de poder. O meu era um pinguim.

O chão da caverna coberto de gelo e o pinguim ordena escorregue. Sem nenhum esforço, deslizamos por túneis e galerias. Chegou a hora de se abraçar. Abram os olhos. Era um contato físico terapêutico, Chloe avisa. Devemos escolher um parceiro. Chloe se atira nos meus ombros e chora. Tem umas roupas de baixo especiais, e chora. Chloe tem óleos e algemas, e chora, enquanto olho o ponteiro maior do relógio dar onze voltas.

Não chorei no meu primeiro grupo de apoio, dois anos atrás. Não chorei nem no segundo, nem no meu terceiro grupo de apoio. Não chorei no parasita do sangue, no câncer de bexiga ou na demência cerebral orgânica. Isso é que acontece com a insónia. Tudo fica muito distante, a cópia da cópia da cópia. A insónia distância tudo, você não pode tocar em nada e nada toca em você.

E também havia o Bob. A primeira vez que fui ao câncer testicular, Bob, a bruacona, o grande pão de queijo, veio para cima de mim nos Remanescentes Unidos e desandou a chorar. A bruaca sai do outro lado da sala na hora de abraçar, os braços soltos, ombros caídos. O queixo da bruaca encostado no peito, os olhos apertados, banhados de lágrimas. Arrasta os pés, joelhos juntos em passos quase invisíveis, Bob desliza pelo soalho para jogar-se sobre mim. Bob estatelou-se em cima de mim.

Seus grandes braços me envolveram.

Big Bob, segundo ele próprio, vivia dopado. Era uma salada diária de Dianabol e esteróide Wistrol, uma bomba. Uma academia, Big Bob teve uma academia. Casou três vezes. Fazia apresentação de produtos, eu já não o teria visto na televisão? O programa para expandir os peitorais era praticamente invenção sua.

Pessoas estranhas com esse tipo de franqueza me deixam totalmente desarmado, se é que você me entende.

Bob não entendia. Talvez por só ter descido um de seus huevos, ele sabia que era um fator de risco. Bob me falou da terapia hormonal pós-operatória. Esses fisioculturistas se injetam rios de testosterona e acabam

desenvolvendo o que eles próprios chamam de tetas de puta.

Precisei perguntar a Bob o que queria dizer huevos. Huevos, explicou ele. Gônadas. Saco. Gemas. Bolas. No México, o lugar

onde você pode comprar os seus esteróides, eles chamam de "ovos". Divórcio, divórcio, divórcio, Bob repetiu e mostrou-me uma foto dele na carteira, grande e nu em primeiro plano, posando em algum lugar. É um jeito besta de ganhar a vida, continua ele, mas quando você está lá no palco, bombado e depilado, totalmente nu com a gordura corporal em torno de 2% e os diuréticos que o deixam frio e rígido como concreto, você fica cego com as luzes, surdo com o ruído de fundo do sistema de som, até o juiz dar a ordem: — Estenda os quadríceps direito, flexione e segure. — Estenda o braço esquerdo, flexione o bíceps e segure. Não há nada melhor nesta vida.

Mas é o caminho direto para o câncer, completou ele. Perdera tudo o que tinha. Inclusive dois filhos que não retornavam as ligações. Para tirar as tetas de puta é só fazer um corte sob os peitorais e drenar todo o líquido.

É só disso que me lembro, porque então Bob passou os braços em torno de mim, cobriu-me com seu tronco e abaixou a cabeça. Eu me entreguei ao repouso, ao escuro, silencioso e completo repouso, e quando finalmente me afastei daquele peito macio, na camisa de Bob havia uma máscara úmida de tanto que chorei.

Isso foi há dois anos, a minha primeira noite nos Remanescentes Unidos. E desde então, em quase todos os encontros, Big Bob me faz chorar. Nunca mais voltei ao médico, parei de mascar raiz de valeriana. Era a liberdade. Liberdade é perder toda a esperança. Se eu não dissesse nada, as pessoas do grupo pensariam o pior. Elas choravam muito. Eu chorava muito. Você olha para uma estrela e desaparece dentro dela. Ao voltar para casa depois do grupo, sentia-me mais vivo que nunca. Não tinha câncer nem parasita de sangue; era um pequeno centro de calor em torno do qual a vida se concentrava.

E eu dormia. Só um bebê dormiria tão bem. Eu morria e renascia a cada noite.

Ressuscitava.

Até esta noite; foram dois anos de sucesso até esta noite, porque não consigo chorar com essa mulher olhando para mim. E por não poder ir mais fundo, não posso ser salvo. Sinto na boca um gosto de papel picado, está toda mordida por dentro. Não durmo há quatro dias. Com essa mulher olhando para mim, sinto-me um mentiroso. Ela é falsa. É mentirosa. Na hora das apresentações, nesta noite, nós nos identificamos. Sou Bob, sou Paul, sou Terry, sou David.

Nunca dou meu verdadeiro nome.

— É câncer? — pergunta ela. E diz:

— Oi, sou Marla Singer.

Ninguém jamais disse a Marla que tipo de câncer. Logo depois já estávamos todos ocupados, embalando a nossa criança interior.

O homem ainda chora em seu ombro e Marla traga o cigarro outra vez.

Eu a observo por entre as tetas trêmulas de Bob. Para Marla, eu sou falso. Desde a segunda noite em que a vi não consigo dormir. E ainda assim, era eu o grande fingido, talvez toda aquela gente fingisse suas lesões, suas tosses e seus tumores, até Big Bob, a bruacona. O grande pão de queijo.

Você tinha de ver o cabelo dele esculpido. Marla fuma e olha para os lados.

Nesse momento, a mentira de Marla reflete a minha mentira e eu só vejo mentiras. Em meio a tanta verdade. Todos se abraçando e se arriscando a revelar seus maiores medos, a morte se aproximando e o cano de uma arma encostado na garganta. Bom, Marla fuma e olha para mim, eu estou afundado num tapete que soluça, e a morte está bem ali, tão sem importância quanto flores de plásticos no vídeo.

— Bob, você está me esmagando — tento avisar, mas desisto. — Bob — procuro falar baixo, mas acabo gritando. — Bob, preciso ir ao banheiro. Há um espelho pendurado sobre a pia do banheiro. Se nada de extraordinário acontecer, verei Marla Singer no Para Cima e Para o Alto, o grupo de disfunção parasítica do cérebro. Marla estará lá. Certamente Marla estará lá e eu me sentarei perto dela. E depois das apresentações e da meditação dirigida, das sete portas do palácio, da bola de luz curativa, depois que abrirmos nossos chakras e chegar a hora de abraçar, eu agarro aquela putinha. Ela com os braços rígidos ao longo do corpo, meus lábios colados em sua orelha, eu direi: Marla, sua grande fingida, dê o fora daqui. Esta é a única coisa boa da minha vida e você está tentando destruir. Sua grande turista.

Da próxima vez que nos encontrarmos, direi: Marla, não consigo dormir com você aqui. Eu preciso disto. Dê o fora. 3

Você acorda no Air Harbor International. Em decolagens e aterrissagens, ou se o avião tomba muito para o lado, eu rezo para que ele caia. Esse momento cura a minha insônia com a narcolepsia, quando podemos morrer impotentes como um maço de cigarros no meio da fuselagem.

Foi assim que conheci Tyler Durden.

Você acorda no O'Hare.

Você acorda no LaGuardia.

Você acorda no Logan.

Tyler trabalha meio período como projecionista de filmes. Sendo como é, Tyler só pode fazer serviços noturnos. Se um projecionista adoecia, o sindicato chamava Tyler.

Algumas pessoas são noturnas. Outras são diurnas. Eu só posso trabalhar de dia.

Você acorda em Dulles.

O seguro de vida paga o triplo se você morrer numa viagem de negócios. Rezei para pegarmos um vácuo. Rezei para um pelicano ser sugado pelas tur- binas, raios perdidos e gelo nas asas. Na decolagem, quando o avião levanta na pista e os flaps se abrem, com nossas poltronas na posição horizontal, nossas bandejas recolhidas e a bagagem de mão no compartimento superior, quando no fim da pista o avião decola e os cigarros estão apagados, eu rezo por uma colisão. Você acorda em Love Field.

Na sala de projeção, Tyler fazia a troca de projetores se o cinema fosse muito velho. Nas trocas, você tem dois projetores na cabina e só um deles está rodando.

Sei disso porque Tyler sabe disso.

O segundo projetor está carregado com o próximo rolo de filme. Em geral os filmes têm seis ou sete rolos que são rodados numa determinada ordem. Nos cinemas mais novos, os rolos são emendados num só, com cinco pés. Assim você não precisa controlar dois projetores, fazer as trocas, ligar e desligar, rolo um, ligar, rolo dois no segundo projetor, ligar, rolo três no primeiro projetor. Ligar.

Você acorda em SeaTac.

Olho as figuras no cartão da companhia aérea. Uma mulher flutua no mar, cabelos castanhos soltos ao vento, o assento abraçado contra o peito. Seus olhos estão arregalados, mas ela nem ri nem franze a testa. No outro quadro, pessoas calmas como vacas hindus esticam os braços nas poltronas para alcançar as máscaras de oxigênio que caem do teto.

Deve ser uma emergência.

Oh!

Perdemos pressão na cabine.

Oh!

Você acorda e está em Willow Run.

Cinema velho, cinema novo, despachar o filme Para outro cinema, Tyler volta a separar o filme nos seis ou sete rolos originais. Os rolos são colocados em duas maletas de aço hexagonais. As maletas têm alça na parte de cima. Você ergue uma e desloca o ombro. É muito pesada. Tyler é garçom de banquete num hotel no centro da cidade, e é projecionista do sindicato dos operadores de projetor. Não sei por quanto tempo Tyler trabalhou nas noites em que não consegui dormir. Nos cinemas antigos que passam filmes com dois projetores, o projecionista tem de saber fazer a troca no momento exato para que a platéia não perceba quando um rolo acabou e o outro começou a rodar. Você tem de olhar para os pontos brancos no alto da tela, do lado direito. É o aviso. Olhe bem para o filme e verá duas manchas no final de cada rolo. Queimado de cigarro, o pessoal do ramo costuma dizer. O primeiro ponto branco, esse é o aviso dos dois minutos. Você liga o segundo projetor para que ele vá ganhando velocidade. O segundo ponto branco é o aviso dos cinco segundos. Emoção. Você fica no meio dos dois projetores, a cabina ferve sob as lâmpadas de xenônio, que

podem até cegar. O primeiro ponto aparece. O som do filme vem de um grande

alto-falante atrás da tela. A cabina do projecionista é à prova de som porque lá dentro é uma barulheira, a roda dentada abocanhando o filme que passa pela lente a cerca de dois metros por segundo, 32 quadros por metro, sessenta quadros engolidos por segundo, como tiros de metralhadora. Os dois projetores ligados, você no meio segurando a alavanca do obturador de cada um. Os projetores mais velhos têm alarme no eixo do rolo alimentador. Mesmo depois que o filme vai para a televisão, os pontos continuam lá. Continuam até nos filmes de aviões.

Se a maior parte do filme está no rolo receptor, ele gira mais devagar e o rolo alimentador tem de rodar mais depressa. Quando o rolo alimentador está chegando ao fim, gira tão rápido que o alarme começa a soar para avisar que é hora de fazer a troca.

É muito quente sob as lâmpadas dos projetores e o alarme tocando. Fique bem no meio dos dois projetores com uma alavanca em cada mão e olhe para o canto da tela. Surge a segunda mancha. Conte até cinco. Feche bem um obturador. Ao mesmo tempo, abra bem o outro. Troca feita. O filme continua. Ninguém da platéia percebe o que aconteceu. Como o alarme fica no rolo alimentador, o projecionista pode tirar um cochilo. O projecionista faz muita coisa que não deve fazer. Não são todos os projetores que têm alarme. Em casa, às vezes você acorda assustado porque pensa que dormiu na cabine e perdeu a hora da troca. A platéia quer acabar com você. A platéia, a magia do filme destruída, o gerente ligando para o sindicato. Você acorda em Krissy Field. O que mais me encanta nas viagens é que em todos os lugares a que vou, tudo é pequenino. Vou para o hotel, sabãozinho, xampuzinho, tabletinho individual de manteiga, toalhinha úmida e escova de dentes de uso único. Embrulhados na poltrona da classe turística. Você é um gigante. O problema é que seus ombros são muito largos. De repente, as pernas de Alice no País das Maravilhas crescem tanto que tocam os pés da pessoa da frente. O jantar chega, um kit faça-você- mesmo em miniatura da Galinha Cordon Bleu, um tipo de quebra-cabeça para mantê-lo ocupado.

O piloto acende o sinal de apertar o cinto e vai pedir às pessoas que retornem aos seus lugares.

Você acorda em Meigs Field.

Às vezes, Tyler acorda na cabine escura apavorado porque perdeu uma troca ou porque o filme quebrou ou escorregou um pouquinho no projetor e os dentes da roda mascaram uma linha na trilha sonora. Depois que o filme passou pelo dente, a luz da lâmpada incide sobre a trilha sonora e, em vez da fala, você é atingido pelo som de uma hélice de helicóptero, vup vup vup, toda vez que um pouco de luz escapa pelo furo.

Eis mais uma que um projecionista não deve fazer: Tyler faz slides das melhores cenas dos filmes. Ninguém se esquece daquele primeiro nu frontal da atriz Angie Dickinson.

Quando uma cópia do filme saiu dos cinemas da Costa Oeste e foi para a Costa Leste, a cena do nu tinha desaparecido. Um projecionista pegou um qua- dro. Outro projecionista pegou outro. Todo mundo queria um slide da Angie

Dickinson nua. O pornô chegou aos cinemas, e os projecionistas, alguns che-

garam a formar coleções que se tornaram épicas. Você acorda em Boeing Field.

Você acorda em LAX.

Temos um vôo quase vazio esta noite, por isso fique à vontade para erguer os braços das poltronas e se esticar. Você se estica, vira de um lado, vira do outro, dobra os joelhos, dobra a cintura, dobra os cotovelos, ao longo de três ou quatro poltronas. Atrasei meu relógio duas horas ou adiantei três, Pacífico, Montanha, hora no Centro ou no Leste; perdi uma hora, ganhei uma hora. Essa é a sua vida, ela vai terminando a cada minuto. Você acorda em Cleveland Hopkins.

Você acorda em SeaTac, outra vez.

Você é projecionista, está cansado, nervoso, mas principalmente irritado, então encontra um quadro de pornografia que deixou perdido na cabine e emenda o close de um pênis vermelho ou de uma vagina molhada em outro filme. Este é uma dessas aventuras com animais; um cachorro e um gato são deixados para trás pela família que viajou e querem voltar para casa. No terceiro rolo, o cão e o gato, que têm vozes humanas e conversam entre si, estão procurando comida na lata de lixo e, de repente, o flash da ereção. Tyler faz isso.

Cada quadro fica na tela por sessenta-avos de segundo. Um segundo dividido em sessenta partes iguais. É quanto dura a ereção. Contempla grandiosa a platéia comedora de pipoca, insinua-se vermelha e assustadora, e ninguém a vê. Você acorda em Logan, outra vez.

É horrível viajar assim. Vou a reuniões às quais meu patrão não quer comparecer. Tomo notas. E as devolverei a você. Aonde quer que eu vá, aplicarei a fórmula. Manterei o segredo intacto. É pura aritmética.

O enunciado de um problema.

Se o novo carro fabricado pela minha companhia sai de Chicago em direção ao oeste a noventa quilômetros por hora, e o diferencial traseiro trava, o carro bate e pega fogo com todo mundo dentro, minha empresa deve iniciar um recall? Pegue o número total de veículos na área (A) e multiplique pelo índice provável de defeitos (B), depois multiplique o resultado pelo custo médio de um acordo extrajudicial (C).

A vezes B vezes C é igual a X. Isso é o que vai nos custar se não iniciarmos

já o recall.

Se X for maior do que custará para recolher o carro, faremos o recall e. ninguém vai se machucar.

Se X for menor do que custará para recolher o carro, então não faremos o recall.

Em toda parte há uma carcaça de carro queimada esperando por mim. Sei onde estão todos os esqueletos. Esse é o meu trabalho como segurança. Quartos de hotel, comidas de restaurante. Por onde passo, vou fazendo rápidas amizades com quem está ao meu lado, em Logan, Krissy e Willow Run. O que faço é coordenar uma campanha de recall, digo ao amigo sentado ao

lado, mas estou me esforçando para chegar a lavador de pratos.

Você acorda no O'Hara, outra vez.

Tyler emendou o pênis em quase tudo. Geralmente closes, ou uma vagina Grand Canyon com eco, contemplando do alto de quatro andares, contorcendo-se sob a pressão sangüínea enquanto Cinderela dança com seu Príncipe Encantado e as pessoas assistem. Ninguém reclamou. As pessoas comeram e beberam, mas a noite não foi mais a mesma. Não sei por quê, começaram a sentir-se mal, a chorar. Só um beija-flor teria flagrado Tyler trabalhando. Você acorda no JFK.

Eu me dissolvo e me dilato no momento da aterrissagem quando a roda encosta na pista mas o avião pende para o lado e não sabe se corrige a inclinação ou se tomba. Agora nada mais importa. Você olha para uma estrela e desaparece dentro dela. Nem sua bagagem. Não importa nada. Nem o seu mau hálito. As janelas estão escuras lá fora e os motores turbinados roncam lá atrás. A cabine pende num ângulo errado sob o ronco das turbinas e nunca mais você terá de preencher o formulário de reembolso. É obrigatório declarar itens acima de 25 dólares. Nunca mais você vai ter de cortar o cabelo. Outro tranco, e a segunda roda encosta no asfalto. O staccato de cem fivelas de cinto se abrindo e o amigo ao lado de quem você quase morreu diz: — Espero que você pegue a sua conexão.

Eu também.

E isso é quanto dura esse seu momento. E a vida continua. Não sei como, por acaso, Tyler e eu nos conhecemos. Era hora de tirar umas férias.

Você acorda em LAX.

Outra vez.

Conheci Tyler numa praia de nudismo. O verão estava quase no fim, e eu dormia. Tyler estava nu, suado, areia grudada no corpo, cabelo molhado caindo no rosto.

Tyler já andava por ali muito antes de nos conhecermos. Ele tirava troncos de madeira da água e os trazia para a praia. Na areia molhada, havia plantado meio círculo de troncos próximos uns dos outros, na altura dos seus olhos. Havia quatro troncos e, quando acordei, vi Tyler puxando o quinto para a praia. Tyler cavou um buraco sob uma das extremidades do tronco, levantou a outra, o tronco escorregou para dentro do buraco e lá ficou, levemente inclinado.

Você acorda na praia.

Tyler desenhou uma linha reta na areia, alguns metros à frente. Depois voltou para pôr o tronco em pé e socou areia ao redor da base. Só eu estava vendo isso.

Tyler gritou de longe:

— Sabe que horas são? Eu sempre uso relógio. — Sabe que horas são? Onde? — perguntei. — Aqui mesmo. Agora — disse ele.

Eram quatro horas e seis minutos da tarde. Em seguida, Tyler sentou-se com as pernas cruzadas na sombra dos troncos

plantados. Ficou lá um tempo, levantou, tomou banho, vestiu camiseta e calça

moletom e se pôs a caminho. Eu tinha de perguntar. Precisava saber o que Tyler ficara fazendo enquanto eu dormia. Se eu pudesse acordar em outro lugar, numa outra época, seria outra pessoa?

Perguntei a Tyler se ele era artista.

Tyler ergueu os ombros e mostrou que os troncos eram mais largos na base. Mostrou o traço que havia feito na areia e disse que usou essa linha para nivelar a sombra projetada pelos troncos.

Às vezes, você acorda e precisa perguntar onde está. O que Tyler fez foi a sombra da mão de um gigante. Naquele momento os dedos eram longos como os de Nosferatu e o polegar muito curto, mas ele disse que às quatro e meia em ponto as mãos ficariam perfeitas. A mão do gigante ficou perfeita por um minuto, e por um minuto perfeito Tyler sentou-se na palma da perfeição que ele próprio criara.

Você acorda e não está em parte alguma.

É só um momento, disse Tyler, você dá um duro danado, mas um momento de perfeição vale qualquer esforço. Um momento é o máximo que se pode esperar da perfeição.

Você acorda e basta.

Seu nome era Tyler Durden, era projetista de filmes do sindicato, era garçom de banquete num hotel no centro da cidade, e me deu seu telefone. Foi assim que nos conhecemos.

4

Os parasitas de cérebro mais comuns estão presentes esta noite. O Para Cima e Para o Alto tem sempre muita gente. Este é Peter. Este é Aldo. Esta é Marcy.

Oi.

As apresentações: Hei, todo mundo, esta é Marla Singer, é a primeira vez que está conosco.

Oi, Marla.

No Para Cima e Para o Alto começamos com Pôr o Papo em Dia. O grupo não se autodenomina Parasitas do Cérebro Parasitado. Ninguém jamais pronun- cia a palavra "parasita". Todos estão sempre melhorando. Ah, o novo medicamento. Todo mundo sempre acabou de sair de ura ponto crítico. Mesmo assim, vê-se por todo lado os olhos apertados de cinco dias com dor de cabeça. Uma mulher enxuga lágrimas involuntárias. Todos usam crachá com o nome, e pessoas que se encontram todas as terças-feiras, há um ano, aproximam-se de você com a mão estendida, olhando para o seu crachá. Já nos conhecemos?

Ninguém diz "parasita". Diz "agente". Ninguém diz "cura'. Diz "tratamento". No Pôr a Conversa em Dia, alguém conta que o agente espalhou-se pela

coluna vertebral e que, de repente, o fez perder o controle da mão esquerda. O

agente, diz a pessoa, corroeu o tecido que reveste o cérebro que escapou dentro do crânio e está provocando ataques.

Na última vez que estive aqui, a tal Chloe deu a boa notícia do dia. Chloe apoiou-se nos braços da cadeira para se levantar e dizer que perdera o medo da morte.

Esta noite, após as apresentações e o Pôr a Conversa em Dia, uma moça que não conheço, com um crachá escrito Glenda, diz que é irmã de Chloe e que às duas horas da madrugada da última terça Chloe finalmente morreu. Ah, quanta ternura! Por dois anos Chloe chorou em meus braços na hora do abraço, e agora está morta, morta no túmulo, morta na urna, no mausoléu, no columbário. Ah, isso é a prova de que um dia você pensava, andava por aí, e agora virou fertilizante ou banquete para os vermes. É o espantoso milagre da morte, que seria uma ternura se não fosse... ela. Marla.

Ah, Marla olha outra vez para mim, o escolhido dentre todos os parasitas de cérebro.

Mentirosa.

Falsa.

Marla é farsante. É falsa. Todos ali estremecem, entram em convulsão e caem no chão molhando a virilha da calça jeans, tudo uma grande encenação. Esta noite a meditação conduzida não me leva a lugar algum. Atrás de cada uma das sete portas do palácio, a porta verde, a porta laranja, está Marla. Porta azul, e lá está ela. Mentirosa. Na meditação conduzida pela caverna de meu animal de poder, é Marla o meu animal. Marla, fumando um cigarro, olhando para os lados. Mentirosa. Cabelos negros e lábios franceses carnudos. Lábios de sofá italiano de couro preto. Você não me escapa. Chloe era um artigo autêntico.

Chloe era o que seria o esqueleto da Joni Mitchell circulando e sorrindo pela festa, sendo supergentil com todo mundo. Imagine o popular esqueleto de Chloe do tamanho de um inseto saltitando por abóbadas e galerias de seu mundo interior, às duas da manhã. A pulsação é uma sirene anunciando: prepare-se para morrer em dez, nove, oito segundos. A morte começará em sete, seis... À noite, Chloe percorre o labirinto de suas veias destruídas e tubos destroçados espirrando linfa quente. Os nervos rasgam a pele como arames entortados. Os abscessos irrompem como pérolas brancas. A voz anuncia: preparar para esvaziar os intestinos em dez, nove, oito, sete. Preparar para esvaziar a alma em dez, nove, oito. Chloe está chapinhando no líquido de seus rins debilitados. A morte começará em cinco minutos.

Cinco, quatro.

Quatro.

Em toda volta, borrifos de vida parasitária mancham o coração. Quatro, três.

Três, dois.

Chloe escala o tecido necrosado da garganta.

A morte vai começar em três, dois.

O luar banha o céu da boca.

Preparar para o último suspiro, já.

Abandonar.

Já.

A alma sai do corpo.

Já.

A morte começa.

Já.

Ah, que lindo é lembrar do corpo inerte de Chloe ainda quente em meus braços, e ela morta em algum lugar.

Mas não, Marla está me observando.

Na meditação dirigida, abro os braços para receber minha criança interior, e a criança é Marla fumando seu cigarro. Não há bola de luz curativa. Mentirosa. Não há chakra. Imagine os chakras como uma flor se abrindo e no centro deles uma explosão de luzes em câmara lenta.

Mentirosa.

Meus chakras não se abrem.

Quando a meditação termina, todos se espreguiçam, viram a cabeça para os lados e ajudam o outro a se levantar. Preparar para o contato físico terapêutico. Na hora do abraço, dou três passos e estou diante de Marla, que olha para mim enquanto olho para os outros, esperando pela ordem. Abrace quem estiver perto de você.

Meus braços se fecham em torno de Marla. Esta noite, escolha alguém muito especial. Marla põe as mãos manchadas de nicotina na cintura. Diga a essa pessoa o que você está sentindo. Marla não tem câncer testicular. Marla não tem tuberculose. Ela não está morrendo. Está certo que, filosoficamente falando, estamos todos morrendo, Marla não está morrendo como Chloe morreu. Outra ordem, entregue-se.

E então, Marla, como vai querer suas maçãs? Entregue-se completamente. Então, Marla, dê o fora. Dê o fora. Dê o fora. Vamos, chore se estiver precisando. Marla me olha nos olhos. Os dela são castanhos. Ela tem orelhas furadas, mas não usa brincos. Os lábios rachados estão soltando pele morta. Vamos, chore! — Você também não está morrendo — diz Marla. A nossa volta, os pares estão se abraçando.

— Se você me denunciar, eu denuncio você — ameaça ela. Então vamos dividir a próxima semana, digo. Marla fica com doenças de ossos, parasitas de cérebro e tuberculose. Eu fico com câncer de testículo, parasitas do sangue e demência cerebral orgânica. Marla pergunta:

— Que tal câncer de bexiga?

A garota fez bem o trabalho de casa.

Vamos dividir câncer de bexiga. Ela fica com os primeiros e terceiros

domingos do mês.

Não, ela recusa. Não, ela quer tudo. Cânceres e parasitas. Marla estreita os olhos. Nunca imaginou que pudesse sentir-se tão bem. Estava mais viva que nunca. A pele melhorava. Nunca vira uma pessoa morta. A vida não fazia sentido porque não havia nada com que compará-la. Ah, mas agora havia a morte, a perda, a tristeza. Lágrimas, horror e remorso. Agora que sabe para onde vamos todos, Marla vive cada momento da sua vida. Não, ela não sairia de grupo algum.

— Não vou voltar àquela vida — ela diz. — Trabalhei numa funerária para me sentir bem, só por estar respirando. E se eu não conseguir trabalhar em outra? Volte para a sua funerária, então.

— Os funerais não são nada perto disto — continua ela. — São cerimônias abstratas. Só aqui tem-se a verdadeira sensação da morte. Os pares à nossa volta enxugam as lágrimas, fungam, dão tapinhas nas costas e relaxam.

Não podemos vir os dois aqui, eu lhe disse. — Então não venha. Eu preciso disto.

— Então vá a enterros.

Os pares se separaram e estão se dando as mãos para a oração final. Eu solto Marla.

— Há quanto tempo você vem aqui? A oração final. Há dois anos.

Um homem pega minha mão. Outro pega a mão de Marla. As orações começam e, geralmente, me fazem perder o fôlego. Ah, nos abençoe. Ah, abençoe a nossa raiva e nosso medo. — Dois anos? — ela se vira para perguntar. Ah, nos abençoe e nos proteja. Quem notou a minha presença nesses dois anos morreu ou sarou e nunca mais voltou.

Ajude-nos e ajude-nos.

— Está bem, está bem, pode ficar no câncer de testículo — concede Marla. Big Bob, o grande pão de queijo chora em cima de mim. Obrigado. Conduza-nos em nosso destino. Nos dê a paz. — Não conte para ninguém.

Foi assim que conheci Marla.

5

O cara da segurança me explicou tudo.

Os carregadores de bagagem às vezes não percebem o tique-taque na maleta. O cara da segurança chamava os carregadores de Throwers. As bombas modernas não fazem barulho. Mas se a maleta vibra, os carregadores de bagagem, os Throwers, precisam chamar a polícia. Fui morar com Tyler porque a maioria das companhias aéreas adota essa política com bagagens vibratórias.

Voltando de Dulles, eu tinha tudo naquela mala. Quando você viaja muito,

aprende a levar sempre as mesmas coisas. Seis camisas brancas. Duas calças

pretas. O mínimo necessário para sobreviver. Despertador de viagem.

Barbeador sem fio.

Escova de dentes.

Seis cuecas.

Seis pares de meias pretas.

É que a minha maleta estava vibrando quando foi embarcada em Dulles, disse-me o cara da segurança, por isso a polícia tirou-a do avião. Eu tinha tudo naquela maleta. Os apetrechos das minhas lentes de contato. Uma gravata vermelha com lisas azuis. Uma gravata azul com listras vermelhas. Listras verticais, não diagonais. E uma vermelha lisa. Eu deixava uma lista dessas coisas atrás da porta do quarto, na minha casa. Minha casa ficava no décimo quinto andar de um condomínio, uma espécie de arquivo de viúvas e jovens profissionais. O folheto de vendas prometia piso, teto e paredes com quarenta centímetros de concreto entre mim e um aparelho de som ou uma televisão ligada no vizinho. Quarenta centímetros de concreto e ar- condicionado, você não pode abrir as janelas porque, apesar do soalho com tábuas de madeira e dos interruptores com dimmer, todos os andares recendiam a última comida que você cozinhou ou a sua última visita ao banheiro. É, e tinha balcão de madeira maciça e iluminação com lâmpada dicróica. Mesmo assim, quarenta centímetros de concreto são importantes quando a sua vizinha deixa acabar a bateria do aparelho de ouvido e assiste aos seus programas de auditório no volume máximo. Ou quando uma explosão vulcânica provocada pela queima de gás e os escombros do que um dia já foram o seu conjunto de sala e os seus objetos pessoais voam pelas paredes envidraçadas e despencam em chamas, para fazer do seu apartamento, só o seu, um buraco queimado na parede do prédio.

Essas coisas acontecem.

Tudo, inclusive os seus pratos verdes de vidro soprado com bolhinhas, imperfeições e grãozinhos de areia, a prova de que foram feitos por indígenas primitivos, simples, honestos e trabalhadores, bem, todos eles se estilhaçaram com a explosão.

Imagine as suas cortinas em tiras flamejantes soltas ao vento. Quinze andares sobre a cidade e tudo queimando, despedaçando-se e estilhaçando sobre os carros.

Quanto a mim, enquanto vou para oeste, dormindo a 0.83 mach ou a 700 quilómetros por hora em velocidade aerodinâmica, o FBI procura uma bomba na minha maleta numa estrada deserta de Dulles. Na maioria das vezes, diz o cara da segurança, a vibração é provocada por um barbeador elétrico. Desta vez foi o meu barbeador elétrico. Da outra foi um vibrador. O cara da segurança me disso isso. Foi quando cheguei ao meu destino sem a minha maleta e tomei um táxi para ver meus lençóis de flanela em farrapos no meio da rua.

Imagine, disse o cara da segurança, dizer a um passageiro que sua bagagem ficou presa na Costa Leste por causa de um vibrador. Às vezes é até um homem.

A política da companhia aérea é não sugerir propriedade no caso de vibradores.

Mas usar o artigo indefinido.

Um vibrador.

Jamais o seu vibrador.

Nunca, jamais diga que o vibrador ligou sozinho, acidentalmente. Um vibrador ligou sozinho e criou uma situação de emergência que exigiu a retirada da sua bagagem.

Chovia quando acordei para a minha conexão em Stapleton. Chovia quando acordei no meu destino final. Um último aviso nos pede para olhar ao redor das nossas poltronas para ver se não esquecemos nenhum objeto pessoal. Em seguida ouço o meu nome. Por favor, queira procurar um representante da companhia aérea no portão. Atraso meu relógio três horas e mesmo assim já passa da meia-noite. Lá estava o representante da companhia aérea no portão, e lá estava o cara da segurança para dizer, ah, a sua bagagem ficou presa em Dulles por causa do barbeador elétrico. O cara da segurança chamou os carregadores de bagagem de Throwers. Depois de Rampers. Para piorar as coisas, o cara me disse que, no fim das contas, não era um vibrador. Depois, talvez por eu ser homem e ele também, e já ser uma hora da manhã, ou talvez só para me fazer rir, o cara disse que eles se referiam às comissárias de bordo como Garçonete Espacial. Ou Colchão de Ar. O cara parecia estar usando um uniforme de piloto, camisa branca com pequenas dragonas e gravata azul. Minha bagagem estava sendo examinada, disse ele, e chegaria no dia seguinte.

O segurança pediu meu nome, endereço e telefone, depois perguntou se eu sabia qual era a diferença entre uma camisinha e a cabine de comando. — Na camisinha só dá para pôr um pau — disse ele. Tomei o táxi para casa com os últimos dez dólares que me restavam. A polícia local também andara fazendo muitas perguntas. Meu barbeador elétrico, que não era uma bomba, ficou três fusos horários para trás.

Mas algo que seria uma bomba, uma grande bomba, havia destruído minhas lindas mesinhas Njurunda no formato de um yin verde-limão e um yang cor-de- laranja que se encaixavam perfeitamente. Bom, elas estavam em cacos agora. Meus sofás Haparanda cor-de-laranja, desenho de Erika Pekkari, não passavam de lixo agora.

Não sou o único escravo do instinto doméstico. Conheço pessoas que já se sentaram na privada com uma revista de sacanagem e hoje se sentam com um catálogo da IKEA.

Todo mundo tem uma poltrona Johanneshov com o mesmo padrão Strinne de listras verdes. A minha caiu quinze andares, em chamas, dentro de uma fonte. Todo mundo tem luminárias Rislampa/Har de arame e papel reciclado não- desbotável. As minhas são com bolinhas coloridas. Tudo isso sentado na privada.

Um conjunto de facas Alle. Puro aço inoxidável. Lavável em lava-louça. O relógio de parede Vild de aço galvanizado, ah, eu precisava de um. As estantes modulares Klipsk, ah!

É, e as caixas de chapéu Hemlig. Essas sim!

Tudo isso queimado e despedaçado na calçada do edifício. O jogo de cama Mommala. Desenhado por Tomas Harila e encontrado nas seguintes cores:

Orquídea.

Fúcsia.

Cobalto.

Ébano.

Carvão.

Casca de ovo ou urze.

Levei uma vida para comprar tudo isso.

A tampo laqueado lavável das minhas mesinhas de apoio Kalix. As mesinhas de café Steg.

Você compra móveis. E pensa, este é o último sofá que vou comprar na vida. Compra o sofá, e por um par de anos fica satisfeito porque, aconteça o que acontecer, ao menos tem o seu sofá. Depois precisa de um bom aparelho de jantar. Depois de uma cama perfeita. De cortinas. E de tapetes. Então cai prisioneiro de seu adorável ninho, e as coisas que antes lhe pertenciam passam a possuir você.

Até eu chegar em casa do aeroporto.

O porteiro surge das sombras e diz: houve um acidente. A polícia, eles estiveram aqui e fizeram uma porção de perguntas. A polícia acha que talvez tenha sido gás. Talvez a chama do piloto do forno tenha se apagado ou um queimador ficou ligado, o gás vazou e tomou todo o apartamento. Um apartamento de 60 metros quadrados, pé-direito alto, o gás deve ter vazado por dias e dias para ocupar todos os espaços. Então o motor da geladeira ligou.

E detonou.

As paredes envidraçadas com molduras de alumínio explodiram e os sofás e os abajures e os pratos e os jogos de lençóis em chamas, os anuários da faculdade e os diplomas e o telefone. Tudo lançado do décimo quinto andar, como uma ex- plosão solar.

Ah, minha geladeira não. Eu tinha uma coleção de mostardas especiais, algumas granuladas, outras em pasta como nos pubs ingleses. Tinha catorze sabores de molho para salada sem óleo e sete espécies de alcaparras. Eu sei, eu sei, uma casa repleta de condimentos e nenhuma comida de verdade.

O porteiro assoou o nariz e aquilo que saiu no lenço foi como um arremesso perfeito, bem na luva do apanhador.

Você pode subir até o décimo quinto, disse o porteiro, mas ninguém vai entrar no apartamento. A polícia andou fazendo perguntas, se eu tinha alguma ex- namorada que pudesse ter feito aquilo, algum inimigo ou alguém que conhecesse explosivos.

— Não vale a pena subir — disse o porteiro. — Só sobraram as paredes. A polícia não encontrou indícios de incêndio criminoso. Ninguém sentiu cheiro de gás. O porteiro ergueu a sobrancelha. Esse cara vivia flertando com as

diaristas e babás que trabalhavam nos apartamentos grandes dos andares

superiores e esperava na poltrona do saguão que elas saíssem do trabalho. Três anos eu morei lá e esse porteiro passou as noites lendo a revista Ellery Queen enquanto eu me via atrapalhado com pacotes e sacolas para abrir a porta e tentar entrar.

O porteiro ergue a sobrancelha e diz que algumas pessoas viajam e deixam uma vela acesa, uma vela bem grande queimando sobre uma poça de gasolina. Gente com problemas financeiros faz esse tipo de coisa. Gente que quer sair do buraco.

Pedi para usar o telefone da portaria.

— Os jovens querem impressionar o mundo comprando um monte de coisas — continuou o porteiro.

Eu liguei para Tyler.

O telefone tocava na casa alugada de Tyler na Paper Street. Ah, Tyler, por favor me tire dessa.

O telefone tocava.

O porteiro aproximou-se de mim e disse:

— Os jovens não sabem o que querem da vida. Ah, Tyler, por favor me salve.

O telefone tocava.

— Os jovens pensam que são donos do mundo. Livre-me dos móveis suecos.

Livre-me da arte inteligente.

O telefone tocava e Tyler atendeu.

— Quem não sabe o que quer acaba tendo o que não quer — continuou o porteiro.

Que eu nunca me sinta completo.

Que eu nunca me sinta satisfeito.

Que eu nunca seja perfeito.

Livre-me, Tyler, de ser completo e perfeito. Tyler e eu nos encontraríamos no bar.

O porteiro pediu um número no qual a polícia pudesse me encontrar. Ainda chovia. Meu Audi estava no estacionamento, mas o tocheiro halógeno Dakapo tinha voado como uma lança sobre o pára-brisa. Tyler e eu, nós nos encontramos e bebemos não sei quantas cervejas, e Tyler disse que sim, que eu podia morar com ele, mas só se lhe fizesse um favor. No dia seguinte, a minha maleta chegaria com o mínimo necessário, seis camisas e seis cuecas.

Ali, bebendo naquele bar onde ninguém nos ouvia ou se importava conosco, perguntei a Tyler o que ele queria que eu fizesse. Tyler disse:

— Quero que você me bata com toda a força. 6

Duas telas na apresentação da Microsoft, sinto o gosto de sangue na boca e

vou começar a engolir. Meu patrão não conhece o material, mas não me permitiu fazer a apresentação com um olho preto e metade do rosto inchado por causa dos pontos dentro da bochecha. Os pontos se soltaram, posso senti-los com a língua nas paredes internas da boca. Imagine linha de pesca embaraçada na praia. Eu imagino uns pontos costurados num cachorro e continuo engolindo. Meu patrão está fazendo a apresentação a partir do meu roteiro, eu estou operando o projetor, por isso estou no canto da sala, no escuro. Meus lábios estão melados de sangue, e quando acender a luz vou me dirigir aos consultores Ellen, Walter e Linda da Microsoft para agradecer-lhes a presença, com a boca suja de sangue e sangue espalhado pelos vãos dos dentes. Dá para engolir uns dois copos de sangue sem passar mal. Amanhã tem clube da luta e eu não vou perder. Antes da apresentação, Walter da Microsoft sorri com seu maxilar de escavadeira mecânica, uma ferramenta de marketing bronzeada como uma batata assada. Walter com seu anel de sinete segura a minha mão na sua mão suave e macia e diz:

— Nem quero saber o que aconteceu com o outro cara. A primeira regra do clube da luta é não falar do clube da luta. Digo ao Walter que caí.

Eu mesmo fiz isso comigo.

Antes da apresentação, quando me sento com meu chefe para mostrar em que parte do roteiro cada slide deve entrar e quando devo passar o segmento de vídeo, meu chefe diz:

— Onde é que você se enfia todo fim de semana? Digo apenas que não quero morrer sem algumas cicatrizes. Não estou mais a fim de um corpo bonito. Sabe aqueles carros superconservados que parecem ter saído direto da vitrine do revendedor em 1955, acho um desperdício. A segunda regra do clube da luta é não falar do clube da luta. Talvez na hora do almoço um garçom venha atender a sua mesa com dois olhos pretos como um panda gigante, conquistados no clube da luta do último sábado, quando você viu a cabeça dele espremida entre o piso de concreto e o joelho de um cara parrudo de quase 100 quilos, que socava sem dó o nariz do garçom com baques secos que podiam ser ouvidos apesar da gritaria, até o sangue se espalhar e o garçom tomar fôlego e dizer pare. Você não diz nada porque o clube da luta só existe naquelas horas em que começa e termina o clube da luta.

Você viu o garoto que trabalha na copiadora, faz um mês que você viu esse garoto que nunca se lembra de anotar um pedido ou separar as cópias, mas esse menino foi bom por dez minutos, quando você o viu desviar-se dos chutes de um representante de contas com o dobro do tamanho dele, e voar para cima do sujeito e socar a cara dele até ele dizer pára. Essa é a terceira regra do clube da luta, se a pessoa diz pára, ou se não consegue mais parar em pé, mesmo que esteja fingindo, a luta termina. Se você visse esse garoto, não imaginaria que tivesse feito uma grande luta.

São só dois por luta. Uma luta por vez. Os dois lutam sem camisa e sem

sapatos. A luta continua até onde eles aguentam. Essas são outras regras do clube de luta.

No clube da luta ninguém é o mesmo da vida real. Você pode dizer ao garoto da copiadora que ele fez uma boa luta, mas não vai estar falando com a mesma pessoa.

No clube da luta não sou a mesma pessoa que meu patrão conhece. Depois de uma noite no clube da luta, o mundo real não é mais o mesmo. Nada vai deixá-lo puto. Sua palavra é lei, e mesmo que alguém vá contra a lei ou provoque você, nem isso o deixa puto.

Na vida real, sou coordenador de campanhas de recall de camisa e gravata, sentado no escuro com sangue na boca, trocando transparências e slides enquanto meu patrão diz à Microsoft porque escolheu especialmente aquele tom de azul- centáurea para o ícone.

O primeiro clube da luta éramos apenas Tyler e eu, batendo um no outro. Antes, se eu chegasse em casa nervoso, vendo que a vida não estava de acordo com meus planos, bastava limpar o apartamento ou lustrar o carro. Um dia eu morreria sem nenhuma cicatriz e deixaria um apartamento e um carro muito bons. Muito bons mesmo, até juntar poeira ou mudar de dono. Nada é estático. Até a Mona Lisa está se desintegrando. Desde que o clube da luta começou, tenho metade dos dentes moles na boca. O auto-aperfeiçoameno talvez não seja a solução. Tyler não conheceu o pai dele.

A solução talvez seja a autodestruição.

Tyler e eu continuamos indo juntos ao clube da luta. O clube da luta acontece nas madrugadas de sábado para domingo, no porão de um bar, quando as portas se fecham; a cada semana tem mais gente. Tyler fica embaixo da única lâmpada no meio do porão escuro e vê a luz refletida em centenas de olhos. A primeira coisa que Tyler grita é: — A primeira regra do clube da luta é não falar do clube da luta. — A segunda regra do clube da luta é não falar do clube da luta. Eu vivi com meu pai uns seis anos, mas não me lembro de nada. A cada seis anos meu pai formava uma nova família em outra cidade. Não se tratava tanto de formar uma família como de abrir outra franquia. O que se vê no clube da luta é uma geração de homens criados por mulheres.

Tyler fica sob a única lâmpada em plena madrugada, no porão repleto de homens, e passa as outras regras: dois homens por luta, uma luta por vez, sem camisa e sem sapatos, a luta só termina quando os dois quiserem. — E a sétima regra é: se esta é a sua primeira noite no clube da luta, você tem de lutar.

O clube da luta não é futebol pela televisão. Você não está assistindo a um bando de homens que nem conhece batendo um no outro ao vivo via satélite com delay dois minutos, comerciais de cerveja a cada dez minutos e uma pausa para a

vinheta da estação. Depois de conhecer o clube da luta, assistir a futebol pela televisão é como ver filme de sacanagem quando você poderia estar dando uma

boa trepada.

O clube da luta acaba sendo um bom motivo para você frequentar academia, manter cabelo e unhas bem aparados. Nas academias está cheio de gente tentando ser homem, como se ser homem é ser o que determinam os escultores e diretores de arte.

Como Tyler diz, um soufflé também é bombado. Meu pai nunca fez faculdade, por isso achei importante fazer uma. Quando terminei a faculdade, liguei para ele e perguntei e agora? Ele não soube dizer.

Quando fiz 25 anos e arrumei um emprego, liguei de novo e perguntei e agora? Ele me disse case-se.

Sou um cara de trinta anos, e me pergunto se realmente preciso de outra mulher.

Não se pode dizer o que acontece no clube da luta. Há gente que precisa lutar toda semana. Nesta semana, Tyler avisa que só lutarão os primeiros cinquenta que chegarem e mais ninguém.

Na semana passada, escolhi um cara e nos inscrevemos para lutar. Esse cara deve ter tido uma semana dura, porque prendeu meus dois braços atrás da minha cabeça num full nelson e socou minha cara no concreto até meus dentes abrirem um corte dentro da boca, o olho inchar e eu começar a sangrar, e quando eu disse pára olhei para o chão e vi a metade ensanguentada do meu rosto marcada no concreto.

Tyler chegou perto de mim, e nós dois olhamos o grande O da minha boca ensanguentada e meu olho quase fechado vendo a gente aqui do chão. Tyler diz: — Legal.

Aperto a mão do sujeito cumprimentando-o pela boa luta. O cara diz:

— Quer mais na semana que vem?

Tento sorrir apesar do meu estado e digo: olhe só para mim. Que tal no mês que vem?

Você não se sente tão vivo em nenhum outro lugar como no clube da luta. Quando estão só você e o outro cara embaixo da lâmpada e toda aquela gente assistindo. Clube da luta não tem nada que ver com ganhar ou perder lutas. Clube da luta não tem nada que ver com palavras. Quando um cara chega ao clube da luta, a bunda dele é uma massa de pão branco. Vê o mesmo cara seis meses de- pois, e ele parece esculpido em madeira. Esse cara se sente seguro para fazer qualquer coisa. No clube da luta você ouve barulhos e grunhidos como em qualquer academia, mas ninguém está preocupado em ficar bonito. Há gritos histéricos e línguas estranhas como nas igrejas, mas quando você acorda no domingo à tarde se sente salvo.

Depois da minha última luta, o cara que lutou comigo limpou o chão enquanto eu ligava para o seguro para aprovar minha entrada no pronto-socorro. No hospital, Tyler disse que eu tinha caído. As vezes, Tyler fala por mim.

Eu mesmo teria dito isso.

Do lado de fora, o sol vinha surgindo.

Você não fala do clube da luta porque, além daquelas cinco horas, entre

duas da madrugada de sábado e sete da manhã de domingo, o clube da luta não existe.

Quando Tyler e eu criamos o clube da luta, nós nunca tínhamos nos envolvido em lutas. Quem nunca lutou fica se perguntando. E se eu me ma- chucar, e se machucar outra pessoa. Fui o primeiro cara com quem Tyler sentiu- se à vontade para pedir, estávamos bêbados num bar, ninguém prestava atenção em nós, e Tyler pediu:

— Me faz um favor. Bata em mim com toda a sua força. Eu não queria, mas Tyler me explicou tudo, que não queria morrer sem cicatrizes, que estava cansado de ver só profissionais lutando e queria se conhecer mais.

Saber mais sobre autodestruição.

Na hora, minha vida me parecia perfeita demais e talvez devêssemos romper com tudo para tornar as coisas melhores. Olhei em volta e disse, está bem. Está bem, disse, mas lá fora, no estacionamento.

Então nós saímos, e perguntei a Tyler se ele queria na cara ou no estômago. Tyler pediu:

— Me pegue de surpresa.

Eu disse: feche os olhos.

Tyler disse:

— Não.

Como na primeira noite de todos no clube da luta, respirei fundo e agitei o punho na frente do queixo de Tyler, como nos filmes de cowboy que todo mundo vê, mas o soco pegou de lado, no pescoço. Merda, disse eu, não valeu. De novo.

Tyler disse:

— Valeu sim —, e me acertou um direto, pow, como uma luva de boxe de desenho animado, bem no meio do peito e eu caí de costas em cima do carro. Nós ficamos ali, Tyler esfregando o pescoço e o peito, mas nós dois sabíamos que havíamos chegado a um lugar em que nunca estivemos e como o gato e o rato dos desenhos, ainda estávamos vivos e queríamos saber até onde poderíamos levar essa história e ainda continuar vivos. Tyler disse: — Legal.

Eu pedi: me bata outra vez.

Tyler disse:

— Não, bata você em mim.

Então eu bati, dei um soco bem embaixo da orelha, e Tyler me empurrou e acertou o salto dos sapatos no meu peito. Não posso dizer o que aconteceu em seguida nem depois, mas o bar fechou e as pessoas estavam gritando em volta de nós no estacionamento.

Em vez de Tyler, finalmente senti que podia arrebentar com tudo que não funcionava na minha vida, da lavanderia que entrega minhas camisas com os botões quebrados, ao banco avisando que estou centenas de dólares no vermelho. Do meu trabalho, onde meu chefe usa meu computador e desfaz todos os meus

comandos do DOS, a Marla Singer, que roubou de mim os grupos de apoio.

Nada ficou resolvido quando a luta terminou, mas tudo bem. Essa primeira luta foi numa noite de domingo, Tyler não tinha feito a barba no fim de semana e os nós dos meus dedos arranharam na barba por fazer. Deitados de costas no chão do estacionamento, olhando uma estrela além das luzes da rua, Perguntei a Tyler com quem ele estava brigando. Tyler disse que era com o pai dele.

Acho que ninguém precisa de pai para se sentir completo. Não há nada pessoal entre as pessoas que lutam no clube da luta. Você luta por lutar. Não podemos falar no clube da luta, mas nós conversamos, e nas semanas seguintes o pessoal se encontrava naquele estacionamento depois que o bar fechava, mas começou a esfriar e outro bar ofereceu o porão em que estamos agora. Quando o clube da luta se reúne, Tyler explica as regras que ele e eu estabelecemos.

— A maioria de vocês está aqui porque alguém quebrou as regras — berra Tyler dentro do cone de luz, num porão cheio de homens. — Alguém contou a vocês do clube da luta.

Tyler continua.

— Bom, tratem de não falar mais ou terão de procurar outro clube da luta porque na semana que vem você vai pôr seu nome na lista quando chegar aqui, e só vão entrar os primeiros cinquenta nomes da lista. Quem entrar tem de marcar a luta logo se quiser lutar. Se não quiser lutar, há gente que quer, então é melhor ficar em casa. Se esta é a sua primeira noite no clube da luta você tem de lutar. A maioria do pessoal vai ao clube da luta porque morre de medo de lutar por alguma coisa. Algumas lutas depois, o medo já é bem menor. Você faz boas amizades no clube da luta. Hoje, vou a reuniões e conferências e encontro pessoas, administradores, executivos e advogados com o nariz quebrado escapando como berinjela por baixo do curativo, alguns pontos embaixo do olho, o maxilar amarrado. São aqueles rapazes quietos que ficam escutando até a hora de tomar a decisão. A gente se cumprimenta só com um movimento de cabeça. Depois meu patrão vem me perguntar de onde conheço tanta gente. Segundo ele, há cada vez menos cavalheiros e cada vez mais bandidos em nosso ramo.

A apresentação prossegue.

Os olhos de Walter da Microsoft encontram os meus. Ele tem dentes perfeitos, pele bem-cuidada e o tipo de trabalho que você pensa em escrever para a revista da faculdade para saber onde conseguir. Vê-se que ele é muito novo para ter lutado nas guerras e, se os pais dele não forem divorciados, o pai vivia fora de casa, e ele está me vendo com a metade do rosto barbeada e a outra metade arrebentada escondida no escuro. A boca melada de sangue. Talvez Walter esteja pensando no jantar beneficente contra o sofrimento dos animais de corte ou na camada de ozônio ou na necessidade premente da Terra de interromper os testes com animais, ou talvez não.

7

Acordo de manhã e vejo aquela coisa molenga, uma camisinha usada flutuando na privada.

Foi assim que Tyler conheceu Marla.

Levantei para dar uma mijada e encontrei isso na privada imunda. E me pergunto: o que pensará um esperma?

É isso?

É isso a cavidade vaginal?

O que está havendo?

Durante toda a noite, sonhei que estava trepando com Marla Singer. Marla Singer fumando um cigarro. Marla Singer revirando os olhos. Acordo sozinho na cama e vejo a porta do quarto do Tyler fechada. A porta do quarto do Tyler nunca fecha. Choveu a noite toda. O telhado de madeira está cheio de bolhas, as telhas estão vergadas, onduladas, a água passa por elas, acumula-se no reboco e escorre pelo buraco da luz.

Quando chove, desligamos os fusíveis. Não temos coragem de acender as luzes. A casa que Tyler aluga tem três andares e um porão. Nós usamos velas. Tem despensa, varandas com telas, janelas com vidros manchados, patamares entre os lances de escada. Tem bay windows com bancos na sala de estar. E rodapés embolorados.

Chove dentro da casa e a madeira dilata e enruga, e os pregos nas madeiras dos pisos, rodapés e ombreiras de janelas estão dilatados e enferrujados. Por toda parte há pregos enferrujados para pisar ou raspar o cotovelo, só há um banheiro para sete quartos, agora com uma camisinha usada. A casa está à espera de alguma coisa, mudança de zoneamento ou homologação de testamento, para ser derrubada. Perguntei a Tyler há quanto tempo está nela, e ele me diz que há seis semanas. Nos primórdios havia um morador que durante toda a vida colecionou National Geographic e Reader's Digest. São imensas pilhas instáveis que ficam ainda mais altas quando chove.

Tyler diz que o último morador usava as páginas das revistas para embrulhar cocaína. A porta da frente não tranca porque foi chutada, talvez por um policial. As nove camadas de papel de parede da sala de jantar estão empapadas, são flores por cima de listras por cima de flores por cima de pássaros por cima de juta.

Nossos únicos vizinhos são uma oficina fechada, e do outro lado da rua um depósito ocupa todo o quarteirão. Na casa há um closet com rolos de toalhas de linho adamascado que não precisam ser passadas a ferro. E outro closet de cedro refrigerado para guardar peles. O azulejo do banheiro é decorado com flores miúdas, mais bonito que muita louça de casamento, e há uma camisinha usada na privada.

Estou morando com Tyler há um mês, mais ou menos. Tyler desce para o café da manhã com marcas de chupadas no pescoço e no peito, e eu estou folheando uma Reader's Digest. A casa é perfeita para vender drogas. Não temos vizinhos. Não há mais nada na Paper Street além de um depósito e um moedor de

polpa. O moedor de papel solta um cheiro de peido e as aparas de madeira em

volta do moedor formam pirâmides alaranjadas que cheiram a gaiola de hamster. É uma casa perfeita para vender drogas porque durante o dia zilhões de ca- minhões passam pela Paper Street, mas à noite Tyler e eu estamos sozinhos num raio de oitocentos metros em todas as direções. Encontrei as Readers Digest no porão, e agora há uma pilha de Reader's Digest em cada cómodo.

A Vida nestes Estados Unidos.

Rir é o Melhor Remédio.

As pilhas de revistas são praticamente os únicos móveis. Nas revistas mais antigas, há uma série de artigos em que os órgãos do corpo humano se expressam na primeira pessoa: sou o Útero de Jane. Sou a Próstata de Joe.

Sem brincadeira, Tyler apareceu na cozinha com chupões e sem camisa, falando blá, blá, blá, blá, blá, que conheceu Marla Singer na noite anterior e que eles transaram.

Ouvindo isso, sou a Vesícula Biliar de Joe. A culpa foi minha. Às vezes você faz as coisas e acaba se ferrando. Outras, são as coisas que não faz que acabam ferrando você.

Ontem à noite liguei para Marla. Nós bolamos um esquema: se eu quero ir a um grupo de apoio, ligo antes para Marla para saber se ela está a fim de ir. Ontem à noite foi o Melanoma, e eu estava meio para baixo. Marla mora no Regent Hotel, que não passa de uma pilha de tijolos vagabundos, onde os colchões ficam dentro de capas de plástico porque muita gente vai morrer lá. Se você não se senta direito na cama não só você, mas lençóis e cobertores vão todos para o chão. Liguei para Marla no Regent Hotel para saber se ela ia ao Melanoma. Marla respondeu em câmara lenta. Não era suicídio para valer, disse Marla, provavelmente mais para chamar a atenção, mas ela havia tomado muitos Xanax. Imagine eu chegar ao Regent Hotel e encontrar Marla andando em círculos naquele quarto vagabundo e dizendo: vou morrer. Morrer. Vou morrer. Morrer. Morrer.

Isso levaria horas.

Então ela ficaria em casa nesta noite?

Estava bolando uma morte espetacular, contou. Eu deveria chegar logo se quisesse assistir.

Obrigado, mas tenho outros planos.

Tudo bem, continuou Marla, poderia morrer perfeitamente vendo televisão. Só queria encontrar alguma coisa decente para assistir. Eu fui ao Melanoma. Voltei cedo para casa. E dormi. E agora, dia seguinte, hora do café, Tyler aparece coberto de chupões e diz que Marla é uma cadela escrota, mas que gosta muito dela. Depois do Melanoma de ontem à noite, voltei para casa, fui para o quarto e dormi. Sonhei que estava trepando, trepando e trepando com Marla Singer. E agora, ouço o que Tyler diz e finjo que estou lendo uma Readers Digest. Piadas de Caserna.

Sou o Dueto Biliar Enfurecido de Joe.

As coisas que Marla disse ontem à noite, Tyler continua. Nunca uma mulher havia falado com ele daquele jeito. Sou os Dentes Rangendo de Joe. Sou as Narinas Dilatadas de Joe. Tyler e Marla treparam umas dez vezes, contou ele, e Marla disse que queria engravidar. Queria fazer um aborto de Tyler.

Sou os Punhos Trancados de Joe. Como Tyler não ia adorar uma coisa dessa. Ontem à noite, Tyler estava sozinho, emendando órgãos sexuais em Branca de Neve.

Como posso competir pela atenção dele? Sou o Sentimento de Rejeição Enfurecido de Joe. O pior é que a culpa é toda minha. Quando fui dormir ontem à noite, Tyler contou que veio para casa depois do turno de garçom e Marla ligou outra vez do Regent Hotel. Marla contou do túnel e da luz que a conduzia pelo túnel. A morte era uma experiência tão tranqüila, Marla queria descrevê-la enquanto saía do corpo e flutuava no ar. Marla não sabia se o espírito podia falar ao telefone, mas queria que ao menos eu ouvisse seu último suspiro.

Não, isso não, Tyler pede ao telefone, sem saber o que fazer. Eles não se conhecem, mas Tyler não gosta que Marla esteja à beira da morte.

Não, isso não.

Mesmo não sendo da sua conta, Tyler liga para a polícia e sai correndo para o Regent Hotel.

Agora, de acordo com um antigo costume chinês que todos aprendem na televisão, Tyler é responsável por Marla para sempre, porque salvou a vida dela. Tyler me conta que Marla mora no quarto 8G, no último andar do Regent Hotel, oito lances de escada, no final de um corredor barulhento, com risada enlatada da televisão saindo pelos vãos das portas. A cada dois ou três segundos, o grito de atriz ou de um ator morrendo sob uma rajada de balas. Tyler chega ao final do corredor, e antes que possa bater, um braço muito fino e muito branco se estica como um estilingue pelo vão da porta do 8G, agarra seu pulso e o puxa para dentro.

Eu enfio a cabeça na Reader's Digest. Dentro do quarto de Marla, Tyler ouve freadas e sirenes na frente do Regent Hotel. Sobre a cômoda há um vibrador feito com o mesmo plástico cor-de-rosa das bonecas Barbie, e por um instante Tyler imagina milhões de bonecas e Barbies e vibradores passando pela linha de montagem em Taiwan. Marla vê Tyler olhando o seu vibrador, revira os olhos e diz: — Não tenha medo. Ele não vai te comer.

Marla empurra Tyler de volta para o corredor e diz que sente muito, que ele não deveria ter ligado para a polícia e que a polícia já devia estar lá embaixo. No corredor, Marla tranca a porta do 8G e leva Tyler para a escada. Na escada, Tyler e Marla se afastam para dar passagem aos policiais e paramédicos que trazem o oxigênio e perguntam onde fica o 8G. Marla mostra a porta no final do corredor. Marla grita para os policiais que a moça que mora no 8G era um amor de

menina, mas que virou um monstro. A garota é um lixo humano infectado, não

diz coisa com coisa e que, para não se meter em coisa errada, não se mete em nada.

— A garota do 8G não confia nem em si mesma — grita Marla; — ela tem medo de ficar velha e ter cada vez menos opções. Marla grita:

— Boa sorte.

A polícia pára diante da porta trancada do 8G, e Marla e Tyler descem as escadas correndo. Um policial grita à porta: — Viemos ajudá-la, Miss Singer! Você tem razões para viver! Deixe-nos entrar, Marla, e vamos ajudá-la a livrar-se dos problemas! Marla e Tyler saem pela rua. Tyler enfia Marla num táxi e vê no oitavo andar as sombras passando pela janela do quarto. Na avenida, tantas luzes e tantos carros, seis pistas de tráfego correndo para um mesmo ponto de convergência. Marla pede a Tyler que cuide dela nesta noite. Se dormir, ela vai morrer.

Há muita gente querendo que ela morra, Marla diz a Tyler. São pessoas que já morreram, mas à noite telefonam para ela. Marla entra num bar e ouve o barman chamar seu nome, mas quando vai atender, não há ninguém na linha.

Tyler e Marla passaram a noite acordados no quarto ao lado do meu. Quando Tyler acordou, Marla já havia sumido, tinha voltado para o Regent Hotel.

Eu disse a Tyler que Marla Singer não precisa de ninguém que a ame, mas de um assistente social.

Tyler diz:

— Não chame isso de amor.

Para encurtar a história, Marla agora quer destruir outra parte da minha vida. Desde a faculdade que eu faço amigos. Eles se casam. Eu os perco. Ótimo.

Bem-feito, digo.

Tyler pergunta se eu tenho algum problema. Sou o Nó nas Tripas de Joe.

Não, está tudo bem.

Aponte uma arma para a minha cabeça e pinte as paredes com os meus miolos.

Está tudo certo, digo. Fique frio.

8

Meu patrão me manda para casa por causa do sangue ressecado na minha calça, e eu fico feliz da vida.

Os cortes abertos no meu rosto não fecham nunca. Vou trabalhar, e as órbitas dos meus olhos são duas massas entumecidas com dois risquinhos que me sobraram para enxergar. Até hoje fico puto da vida porque estou centrado como Mestre Zen e ninguém percebe. Mesmo assim continuo mandando FAX. Escrevo

pequenos HAICAIS e mando por FAX para todo mundo. Quando cruzo com as

pessoas no trabalho, fico totalmente ZEN diante de tanta CARA feia. As operárias são livres

Os zangões também voam

Mas a rainha é escrava

Você abre mão dos seus bens materiais e do seu carro e vai morar numa casa alugada na área mais Poluída da cidade e à noite ainda ouve Marla e Tyler no quarto, chamando um ao outro de bosta de gente. Toma isto, bosta de gente.

E isto, sua bosta.

Mais devagar, seu bosta. Assim, baby.

Por outro lado, isso faz de mim um pequeno centro de calma no mundo. Enquanto eu, com meus olhos inchados e as manchas ressecadas de sangue na calça, vou dizendo Oi para todo mundo no trabalho. Oi! Olhe para mim. Oi! Sou tão ZEN. Isto é SANGUE. Não é NADA. Oi! Tudo é nada, e é muito legal ser ILUMINADO. Como eu.

Suspiro.

Olho. Pela janela. Um pássaro.

O patrão perguntou se o sangue era meu.

O pássaro flutua no vento. Crio um pequeno haicai na cabeça. Sem ninho

O pássaro faz do mundo sua casa

Da vida sua profissão.

Conto nos dedos: cinco, sete, cinco.

Este sangue é meu?

É, respondo. Em parte.

Resposta errada.

Como se fosse grande coisa. Tenho duas calças pretas. Seis camisas brancas. Seis cuecas. O mínimo necessário. Vou ao clube da luta. Essas coisas acontecem.

— Vá para casa trocar de roupa — ordena o padrão. Começo a desconfiar de que Tyler e Marla são a mesma pessoa. Não fossem as trepadas todas as noites no quarto de Marla. Trepar.

Trepar.

Trepar.

Tyler e Marla nunca estão no mesmo lugar. Nunca os vejo juntos. Mas ninguém nunca me viu com Zsa Zsa Gabor nem por isso somos a mesma pessoa. Tyler simplesmente some quando Marla está por perto. Então, para lavar a calça, Tyler tem de me ensinar a fazer sabão. Tyler está lá em cima, e a cozinha cheira a cravo e a pêlo queimado. Marla está sentada,

queimando a parte interna do braço com a brasa do cigarro de cravo e chamando

a si mesma de bosta humana.

— Sou corrupta, doente e pustulenta — Marla fala para a brasa do cigarro. E esmaga o cigarro na pele fina do braço. — Queime, bruxa, queime. Tyler está lá no meu quarto olhando os dentes no espelho, e diz que me arrumou um emprego de garçom.

— No Pressman Hotel, se puder trabalhar à noite. Esse emprego vai deixar seus colegas com ódio.

É, digo, tanto faz.

— Vão querer que você use gravata borboleta. Vai precisar de uma camisa branca e uma calça preta.

Sabão, Tyler. Digo que preciso do sabão. Temos de fazer um pouco de sabão. Preciso lavar minha calça.

Seguro os pés de Tyler enquanto ele faz duzentos abdominais. — Para fazer o sabão, primeiro tem de derreter a banha. Tyler é cheio das informações úteis.

Se não estão trepando, Marla e Tyler nunca ficam no mesmo lugar. Quando Tyler está por perto, Marla finge que não o vê. Sei como é isso. É como meus pais faziam. Então meu pai foi embora para abrir outras franquias. Meu pai sempre dizia:

— Ou você casa antes de o sexo esfriar ou não casa nunca mais. Minha mãe sempre dizia:

— Não compre nada que tenha zíper de náilon. Meus pais nunca disseram nada que merecesse ser gravado. Tyler faz cento e noventa e oito abdominais. Cento e noventa e nove. Duzentos.

Tyler está vestindo roupão de flanela ensebado e calça de moletom. — Tire a Marla de casa. Mande-a comprar uma lata de soda cáustica. Soda em flocos. Cristal não. Mas se livre dela. Sinto-me outra vez com seis anos de idade, o garoto de recados dos meus pais. Odiava isso quando tinha seis anos. E odeio agora. Tyler começa a fazer alongamento de perna, e eu desço para falar com Marla: soda cáustica em flocos, dou a ela uma nota de dez dólares e um passe de ônibus. Marla continua sentada na cozinha, e eu tiro o cigarro de cravo da mão dela. É fácil e tranqüilo. Pego o pano de prato e enxugo as queimaduras no braço de Marla, as cascas de ferida se soltaram e começou a sangrar. Depois enfio os pés dela nos sapatos de salto, um por vez. Marla assiste à minha rotina de Príncipe Encantado com os sapatos e diz: — Eu entrei. Achei que não havia ninguém em casa. A sua porta da frente não tem fechadura.

Não digo nada.

— Sabe, a camisinha é o sapatinho de cristal da nossa geração. Você calça quando conhece uma pessoa. Dança a noite toda e depois joga fora. A camisinha, não a pessoa.

Não converso com Marla, ela pode se meter nos grupos de apoio ou entre mim e o Tyler, mas não vai conseguir ser minha amiga.





—Esperei você a manhã inteira.

As flores nascem e morrem

O vento traz borboletas ou neve

A pedra nem percebe

Marla se levanta, está usando um vestido azul sem mangas. Marla levanta a saia e vira a barra para que eu veja os pontos do lado de dentro. Ela está sem calcinha. E pisca.

— Queria mostrar meu vestido novo — diz. — É um vestido de dama de honra e todo feito à mão. Gostou? Comprei em loja de segunda mão por um dólar. Alguém costurou todos esses pontos e fez o vestido mais feio que já vi. Dá pra acreditar?

A saia é mais comprida de um lado que do outro e a cintura do vestido fica na altura dos quadris.

Antes de sair para as compras, Marla ergue a saia com a ponta dos dedos e começa a dançar ao redor de mim e da mesa da cozinha, a bunda girando por baixo da saia. Marla diz que ama essas coisas que as pessoas adoram intensamente, mas logo se livram delas. A árvore de Natal, por exemplo, que é o centro das atenções, mas depois do Natal você vê essas árvores secas ainda com as guirlandas jogadas nas calçadas. Vê as árvores e lembra do assassinato de animais em estradas ou das vítimas de crime sexual com a calcinha do avesso, barradas com fita isolante.

Quero que ela saia logo.

— O melhor lugar para se ir é no Controle de Animais — continua ela. — É lá que ficam os animais, cachorrinhos e gatinhos que as pessoas amam e depois abandonam, até animais velhos eles saltam e latem para chamar a sua atenção porque depois de três dias eles dão uma superinjeção de fenobarbital de sódio e vão parar no forno para animais.

— Um grande sono, como em O vale dos cães.** E mesmo que alguém os ame e salve a vida deles, mesmo assim são castrados.— Marla olha para mim como se fosse eu quem estivesse trepando com ela e pergunta:

— Não vou conseguir nada com você, vou? Marla sai pela porta da cozinha cantarolando a música horrível de O vale das bolinhas. Fico olhando ela se afastar. Eu me viro e dou de cara com Tyler. Ele pergunta: — Conseguiu se livrar dela?

Nem um ruído, nem um cheiro, Tyler simplesmente aparece. — Primeiro — Tyler se afasta da porta e vai direto para o freezer. — Primeiro, vamos derreter um pouco de banha. Quanto ao meu patrão, diz Tyler, se eu estivesse muito bravo com ele, podia ir até o correio, preencher um cartão de mudança de endereço e mandar toda a correspondência dele para Rugby, na Dakota do Norte. Tyler começa a tirar do freezer os sacos de sanduíche com um troço branco congelado e joga tudo na pia. Sobrou para mim, pôr a panela grande no fogo com * Trocadilho com o título do filme Valley of Dolls, que foi traduzido no Brasil por O Vale das Bonecas.

água quase até a boca. Se a água for pouca a banha escurece quando a gordura

começa a separar.

— Como essa banha tem muito sal, quanto mais água melhor — diz Tyler. Ponha a banha na água e espere levantar fervura. Tyler espreme a massa branca dos sacos de sanduíche na água, depois enfia os sacos vazios no fundo do lixo.

Tyler diz:

— Basta usar a imaginação. Lembre-se de todas aquelas besteiras sobre pioneirismo que ensinaram a você nos escoteiros. Lembre-se das aulas de quí- mica no colégio.

É difícil imaginar Tyler escoteiro.

Uma coisa eu poderia fazer, me diz Tyler, ir uma noite à casa do meu patrão e soltar a mangueira da torneira do jardim. Depois, ligar a mangueira numa bomba manual e injetar uma carga de tinta industrial no encanamento. Vermelha, azul ou verde, e esperar o dia seguinte para ver meu patrão. Ou então, podia ficar atrás de uma moita e bombear ar nos canos da casa até atingir o máximo de pressão, umas 110 libras. Quando alguém desse a descarga na privada, a caixa d'água explodiria. Com 150 libras, se alguém abrisse o chuveiro, a pressão da água soltaria a tampa do chuveiro, arrancaria os fios e blam, o chuveiro viraria uma arma mortal.

Tyler diz isso para que eu me sinta melhor. A verdade é que eu gosto do meu patrão. Além disso, agora estou iluminado. Sabe, só comportamentos de Buda. O Sutra do Diamante, Gravadora Penhasco Azul. Hari Rama, sabe, Krishna, Krishna. Iluminado, sabe.

— Se você grudar penas na sua bunda não vai virar galinha — comenta Tyler.

À medida que a banha derrete, o sebo começa a subir à superfície da água fervendo.

Ah, digo, então estou grudando penas na minha bunda. Como se Tyler, com suas queimaduras de cigarro subindo pelos braços, fosse uma alma muito evoluída. Senhor e Senhora Bosta Humana. Abaixo humildemente a cabeça e me transformo numa vaca hindu a caminho do matadouro como no cartão de procedimentos de emergência da companhia aérea. Abaixe o fogo.

Não pare de mexer.

O sebo sobe, até a superfície da água ficar coberta por uma película perolada com as cores do arco-íris. Use uma colher grande para tirar o sebo e reserve.

E então, como vai a Marla?

Tyler responde:

— Pelo menos ela está tentando ir fundo. Não pare de mexer. Continue mexendo até a gordura parar de subir. É gordura que tiramos da água. Gordura limpa e boa.

Tyler diz que ainda nem cheguei perto do fundo. E se não levar alguns tombos pelo caminho, não serei salvo. Aconteceu isso com Jesus na tal de crucificação. Não basta abrir mão de dinheiro, bens materiais e conhecimentos.

Não é um mero retiro de fim de semana. Eu devia esquecer a autoperfeição e

perseguir a desgraça. Não podia mais ficar brincando de salvação. Isto não é um seminário.

— Se você não tiver coragem de bater no fundo, não vai conseguir — diz Tyler.

Só se pode ressuscitar depois do desastre. — Só depois de perder tudo você vai fazer o que quiser — continua Tyler. O que estou sentindo é iluminação prematura. — Não pare de mexer— determina Tyler.

Quando a banha estiver bem derretida e a gordura parar de subir, jogue fora essa água. Lave a panela e encha com água limpa. Eu pergunto: estou ao menos próximo do fundo? — Onde você está agora, não consegue nem imaginar onde é o fundo. Repita todo o processo com o sebo reservado. Ferva o sebo em água. Vá retirando a nata. — Essa banha que estamos usando tem muito sal. Se tiver muito sal, o sabão não solidifica — diz Tyler. Ferva e retire a nata. Ferva e retire a nata.

Marla volta.

No instante em que Marla abre a porta de tela, Tyler some, sai da cozinha, desaparece.

Ou Tyler subiu a escada ou desceu para o porão. Poof.

Marla entra pela porta da cozinha com a lata de soda cáustica em flocos. — Na loja tem papel higiênico 100% reciclado — diz Marla. — Reciclar papel higiênico deve ser o pior serviço do mundo. Pego a lata de soda e ponho na mesa. Não digo nada. Posso passar a noite aqui? — pergunta ela. Não respondo. Conto mentalmente: cinco, sete, cinco sílabas. O tigre sorri

A serpente diz que te ama

Mentiras fazem mal

Marla pergunta:

— O que está cozinhando?

Sou o Ponto de Fervura do Joe.

Digo, saia, saia, saia daqui, tá? Já não basta ter se apossado de um bom pedaço da minha vida?

Marla segura a manga da minha camisa e me puxa para dar um beijo no meu rosto.

— Por favor, ligue para mim. Por favor. Precisamos conversar. E eu digo tá ,tá, tá, tá, tá.

Assim que Marla sai pela porta, Tyler aparece na cozinha. Rápido como um truque de mágica. Meus pais fizeram essa mágica durante cinco anos.

Fervo e tiro a nata enquanto Tyler abre espaço na geladeira. O vapor sobe pela cozinha e pinga água do teto. Não se vê a lâmpada de 40 watts no fundo da

geladeira, atrás das garrafas de ketchup, dos potes de conservas e de maionese,

mas vejo o perfil de Tyler iluminado por ela. Ferva e tire a nata. Ferva e tire a nata. Ponha essa gordura desnatada em caixas de leite com a tampa cortada.

Tyler arrasta uma cadeira para a porta da geladeira e se senta para ver o sebo esfriar. Na cozinha aquecida, a nuvem de vapor resfriado sai da geladeira e abraça os pés de Tyler.

Encho as caixas de leite com sebo, e Tyler vai guardando na geladeira. Ajoelho-me ao lado de Tyler, ele abre minhas mãos e vira as palmas para cima. A linha da vida. A linha do amor. Os montes de Vênus e de Marte. Somos envolvidos pelo vapor frio, os rostos fracamente iluminados. — Preciso que me faça um favor — pede Tyler. É sobre Marla, não é?

— Jamais fale de mim para ela. Nunca fale de mim pelas costas. Promete? Prometo.

— Se você pronunciar meu nome para ela, nunca mais vai me ver. Prometo.

— Promete?

Prometo.

E Tyler insiste:

— Não esqueça que você prometeu três vezes. Uma camada grossa e branca começa a se formar na superfície das caixas de leite, dentro da geladeira. Olhe, eu mostro, está começando a separar.

— Não se preocupe. Essa camada branca é glicerina. Você pode misturar a glicerina outra vez para fazer o sabão. Ou pode jogar fora. Tyler molha os lábios com saliva e põe minha mão sobre sua coxa, a palma virada para baixo, no roupão de banho aflanelado. — Você pode misturar glicerina com ácido nítrico e fazer nitroglicerina — diz ele.

Respiro pela boca e repito, nitroglicerina. Ele molha novamente os lábios e beija as costas da minha mão. — Pode misturar nitroglicerina com nitrato de sódio e pó de serra e fazer dinamite — continua Tyler.

O beijo molhado brilha nas costas da minha mão. Dinamite, repito, e me sento sobre os calcanhares.

Tyler levanta a tampa da lata de soda.

Pode explodir uma ponte.

— Pode misturar nitroglicerina com mais ácido-nitrico e parafina e fazer gelatina explosiva — continua ele.

— Pode explodir um prédio — decreta Tyler. Tyler inclina a lata de soda sobre o beijo molhado, nas costas da minha mão.

— Isto é queimadura química, mas dói muito mais do que queimadura de fogo. É pior que cem cigarros.

O beijo molhado brilha nas costas da minha mão — Você vai ganhar uma cicatriz.

Tendo bastante sabão, é possível explodir o mundo. Agora se lembre do que

prometeu.

E Tyler despeja a soda.

9

A saliva de Tyler teve duas conseqüências. O beijo molhado colou os flocos de soda nas costas da minha mão e ficou queimando. Esse foi o primeiro efeito. O segundo é que a soda só queima se for misturada com água. Ou saliva. — É queimadura química — diz Tyler — e dói muito mais do que qualquer queimadura que você conheça.

Você pode usar soda para desentupir cano de esgoto. Fecho os olhos.

Uma pasta de soda e água pode furar uma panela de alumínio. Misturada com água, a soda esquenta a mais de duzentos graus, à medida que vai esquentando queima as costas da minha mão, e Tyler põe a mão sobre a minha e nossas mãos se abrem sobre a minha perna, na calça suja de sangue, e Tyler diz para eu prestar atenção porque é o momento mais importante da minha vida.

— Porque se até agora foi uma história, daqui para a frente será outra história.

Este é o momento mais importante da nossa vida. A soda cáustica grudada perfeitamente sobre o beijo de Tyler é uma fogueira, um ferro em brasa um reator atômico derretendo minha mão no final de uma estrada muito, muito longa que vejo estender-se na minha frente. Tyler pede que eu volte e fique com ele. Minha mão vai desaparecendo, minúscula no horizonte, no final da estrada.

Imagine o fogo queimando, só que, agora, além do horizonte. No crepúsculo.

— Volte para a dor — ordena Tyler.

Isso me lembra a meditação dirigida dos grupos de apoio. Não pense na palavra "dor".

A meditação dirigida funciona para o câncer, mas não para isto. — Olhe para a sua mão — diz Tyler.

Não olhe para a sua mão.

E não pense nas palavras "queimar", "carne", "pele", "carbonizar". Não ouça os próprios gritos.

Meditação dirigida.

Você está na Irlanda. Feche os olhos.

Você está na Irlanda no verão, depois da faculdade, e está bebendo num pub próximo ao castelo onde ônibus diários carregados de turistas ingleses e

americanos chegam para beijar a pedra Blarney. — Não limpe. Sabão e o sacrifício humano andam de mãos dadas — diz Tyler.

Você sai do pub com outros homens e caminha em silêncio por entre os

carros molhados pela chuva que acabou de cair. É noite. E chega ao castelo da pedra Blarney.

Os pisos do castelo estão podres, e você sobe as escadas de pedra, a escuridão vai ficando mais e mais profunda por todo lado, a cada degrau. Todos sobem em silêncio, é a tradição deste pequeno ato de rebeldia. — Ouça, abra os olhos — diz Tyler. Na história antiga — continua ele — os sacrifícios humanos eram feitos em colinas à beira dos rios. Eram milhares de pessoas. Ouça o que estou dizendo. Nesses sacrifícios os corpos eram queimados numa pira.

— Pode chorar — diz Tyler. — Pode ir até a pia e deixar a água correr na sua mão, mas antes precisa saber que você é um estúpido e que vai morrer. Olhe para mim.

Você está na Irlanda.

— Pode chorar — diz Tyler — mas cada lágrima que cair nos flocos de soda vai deixar a marca de uma queimadura de cigarro. Meditação dirigida. Você está na Irlanda no verão, depois da faculdade, e talvez tenha sido quando desejou a anarquia pela primeira vez. Muito antes de conhecer Tyler Durden, antes de mijar no seu primeiro crême anglaise, aprendeu pequenos atos de rebeldia.

Na Irlanda.

Você está na plataforma, no alto da escadaria do castelo. — Podemos pôr vinagre para neutralizar a queimadura, mas você vai ter de pedir — diz Tyler.

Depois que dezenas de pessoas são sacrificadas e queimadas, continua Tyler, uma gosma branca desce pela encosta e cai no rio. Primeiro você terá de chegar ao fundo.

Você está na plataforma do castelo irlandês rodeado pela escuridão abissal, e na sua frente, não muito longe, há um muro de pedra. — Chove na pira ardente ano após ano, as pessoas são queimadas ano após ano, e a água penetra no carvão que se transforma em soda cáustica, e a soda se mistura com a banha derretida dos sacrifícios e uma gosma branca de sabão se desprende do pé do altar e desce pela encosta em direção ao rio. E os irlandeses que estão em volta de você e de seu pequeno ato de rebeldia no meio da escuridão aproximam-se da beira da plataforma, param sobre a escuridão abissal e começam a mijar.

E dizem, vá em frente, solte seu fantástico mijo americano farto e amarelo e cheio de vitaminas. Farto, caro e inútil. — Este é o momento mais importante da sua vida — diz Tyler — e você nem está aqui para ver.

Você está na Irlanda.

Ah, e está mijando. Ah, sim. Tem cheiro de amônia e das doses diárias de vitamina B.

Onde o sabão cai no rio, diz Tyler, depois de milhares de anos de chuva e gente morta, os antigos descobrem que as roupas lavadas nesse lugar ficam mais limpas.

Estou mijando na pedra Blarney.

— Porra! — grita Tyler.

Estou mijando na calça preta manchada de sangue ressecado que quase fez meu chefe vomitar. Você está numa casa alugada da Paper Street. — Isso não é nada — diz Tyler.

— É só um sinal — diz Tyler. Tyler é cheio das informações úteis. As culturas que não conhecem o sabão, continua ele, usam a própria urina e a urina de seus cachorros para lavar as roupas e o cabelo, por causa do ácido úrico e da amônia.

Sinto cheiro de vinagre, e o fogo que queima a minha mão, no fim da longa estrada, é apagado.

Sinto cheiro de soda cáustica penetrando nas cavidades nasais e um cheiro de vômito hospitalar de mijo e vinagre.

— Fizeram bem em matar toda aquela gente — continua Tyler. As costas da sua mão estão vermelhas e inchadas como dois lábios perfeitos do beijo de Tyler. Em volta do beijo, as queimaduras provocadas pelas lágrimas de alguém que chorou.

— Abra os olhos — diz Tyler, com o rosto banhado em lágrimas. — Meus parabéns. Você está a um passo do fundo. Vai ver — continua ele — que o primeiro sabão foi feito de heróis. Pense nos animais usados em testes de produtos. Pense nos macacos lançados ao espaço.

— Se eles não morressem, se não sofressem, sem o sacrifício deles não seríamos nada — conclui Tyler.

10

Aperto o botão do elevador entre os andares para que Tyler solte o cinto. Quando o elevador pára, as tigelas de sopa empilhadas no carrinho param de chacoalhar, e a fumaça dos cogumelos sobe pelas paredes do elevador quando Tyler ergue a tampa da sopeira.

Tyler começa a tirar e diz:

— Não olhe ou não vou conseguir.

A sopa é um caldo grosso de tomate com coentro e mariscos. Entre um e outro, ninguém vai sentir o cheiro de nada que se puser dentro. Eu digo anda logo, e vejo por cima do ombro Tyler com seu último meio centímetro pendurado sobre a sopa. Me faz lembrar um elefante com camisa de garçom e gravata borboleta chupando a sopa pela tromba. Tyler diz:

— Já disse, não olhe.

Na minha frente, a porta do elevador tem uma janelinha de vidro do tamanho do meu rosto e por ela espio o corredor de serviço do salão de banquete. Com o elevador parado entre os andares, meu ponto de vista é o de uma barata no linóleo verde, e daqui de onde está a barata, o corredor verde se estende até onde a vista alcança, passa por portas entreabertas onde os titãs e suas gigantescas mu-

lheres bebem barris de champanhe e gritam entre si usando imensos diamantes.

Na semana passada, eu disse a Tyler que, quando os Advogados do Empire State estiveram aqui para a festa de Natal, tinha ficado de pau duro e gozara sobre a mousse de laranja.

Na semana passada, Tyler disse que parou o elevador e peidou no carrinho todo de Boccone DoJce, para o chá da Liga de Juniores. Ele sabe que suspiro absorve o fedor.

Do ponto de vista da barata, ouvimos o harpista cativo tocando para os titãs que erguem em seus garfos nacos de cordeiro assado, cada um do tamanho de um porco, cada boca um impressionante Stonehenge de marfim. Eu digo, vai logo.

Ele diz:

— Não consigo.

Se a sopa esfriar, eles a mandarão de volta. Os gigantes mandam os pratos voltar para a cozinha por nada. Só querem ver você correr para lá e para cá pelo dinheiro deles. Num jantar como esse, um banquete, todos sabem que a gorjeta já está incluída na conta, então tratam você como pó. Nunca levamos nada de volta para a cozinha. Basta mudar um pouquinho de lugar as Pommes Parisienne e os Asperges Hollandaise no prato, servir outra pessoa, e fica tudo bem.

Digo Cataratas do Niagara. Rio Nilo. Na escola, a gente pensa que se puser a mão de uma pessoa dormindo numa tigela de água quente, ela molha a cama Tyler diz:

— Pronto.

Atrás de mim, Tyler diz:

— Agora sim. Ah, estou fazendo. Pronto. Pelas portas entreabertas dos salões ouço as saias pretas e vermelhas roçar o chão, fartas como a cortina de veludo dourado do velho Broadway Theatre. De vez em quando vejo Cadillacs de couro preto com cordões de amarrar em vez de limpadores de pára-brisa. Sobre eles movimenta-se uma cidade inteira de torres de escritórios com faixas vermelhas de smoking.

Foi pouco, digo.

Tyler e eu somos guerrilheiros terroristas da indústria de serviços. Sabotadores de jantares. O hotel oferece jantares comemorativos e fornece também a comida, o vinho, a louça, os cristais e os garçons. Eles cobram os serviços, tudo numa conta só. E como os convidados sabem que não vão lhe dar gorjeta, você não passa de uma barata para eles. Uma vez, Tyler serviu um jantar. Foi quando ele se tornou um garçom renegado. Nesse primeiro jantar, Tyler servia peixe numa nuvem de vidro que parecia flutuar sobre a cidade do alto de uma montanha, apoiada em pernas de aço. Entre o primeiro e o segundo prato, que seria o peixe, Tyler limpava os pratos de massa, quando a anfitriã entrou na cozinha acenando um pedaço de papel como se fosse uma bandeira, a mão tremendo muito. Com os dentes cerrados, Madame pergunta se os garçons viram algum convidado entrar no corredor dos quartos. Especialmente uma convidada. Ou o anfitrião. Na cozinha estão Tyler, Albert, Len e Jerry, limpando e empilhando os

pratos e a auxiliar de cozinha, Leslie, regando com manteiga de alho rações de

alcachofra recheados de camarão e escargô. — Não podemos ir a essa parte da casa — respondeu Tyler. Nós entramos pela garagem. Só vemos a garagem, a cozinha e a sala de jantar.

O anfitrião entra na cozinha atrás da mulher e tira o pedaço de papel da sua mão trémula.

— Já está tudo bem — diz ele.

— Como vou enfrentar aquela gente, se não souber quem fez isto? — pergunta Madame.

O anfitrião põe a mão aberta nas costas do vestido de festa branco que combina com a casa e Madame se endireita, ergue os ombros, e a cozinha volta a ficar em silêncio.

— Eles são nossos hóspedes — diz ele. —Esta festa é muito importante. Acho engraçado porque me lembra um ventríloquo manipulando seu boneco. Madame olha para o marido, e com um empurrãozinho o anfitrião leva a mulher de volta para a sala de jantar. O bilhete cai no chão e o vaivém das portas de mola joga o papel nos pés de Tyler.

Albert pergunta:

— O que diz aí?

Len sai para servir o peixe.

Leslie põe a bandeja de corações de alcachofra no forno e pergunta: — O que é que diz?

Tyler olha para Leslie, e sem erguer o papel do chão, diz: Urinei num de seus elegantes perfumes.

Albert sorri:

— Você mijou nos perfumes dela?

Não, diz Tyler. Mas deixou o bilhete no meio dos frascos. Há no mínimo uns cem frascos sobre o balcão do banheiro dela. Leslie sorri:

— Não fez mesmo?

— Não, mas ela não sabe disso — diz Tyler. O resto da noite, nesse jantar da nuvem de vidro no céu, Tyler tirou o prato de alcachofra fria, depois o de vitela fria com Pommes Duchesse, depois o de Chouíleur à Ia Polonaise fria da frente da anfitriã, e encheu a taça de vinho dela

uma dezena de vezes. Madame não tirava os olhos de suas convidadas, até que, entre uma taça de sorbet e o gateau de abricô, o lugar de Madame na cabeceira da mesa de repente ficou vazio.

Eles lavavam os pratos depois que os convidados saíram e guardavam os refrigerantes e a louça na van do hotel, quando o anfitrião entrou na cozinha e pediu se Albert podia por favor ajudá-lo a erguer uma coisa. Leslie diz: acho que Tyler foi longe demais. Rápido e em voz alta, Tyler diz que se matam baleias para fazer um perfume que vale mais que ouro. Muita gente nunca viu uma baleia. Leslie mora com dois filhos num apartamento na beira da auto-estrada e Madame tem mais dinheiro do que ela consegue ganhar em um ano dentro daquelas garrafinhas no

balcão do banheiro.

Albert volta para a cozinha e disca 9-1-1 no telefone. Albert tampa o bocal com a mão e diz: Tyler, você não devia ter deixado aquele bilhete. Tyler diz:

— Então conte para o gerente de banquetes. Ele que me mande embora. Não estou casado com esta bosta de trabalho. Todos abaixam os olhos.

— Ser despedido é a melhor coisa que nos pode acontecer — diz Tyler. — Assim a gente consegue sair do lugar e fazer alguma coisa na vida. Albert diz ao telefone que precisamos de uma ambulância e dá o endereço. Enquanto espera na linha, Albert diz que, naquele momento, a anfitriã está num estado lamentável. Albert encontrou-a caída ao lado da privada. O anfitrião não conseguia erguê-la porque Madame dizia que ele havia mijado nos seus frascos de perfume e que estava querendo enlouquecê-la tendo um caso com uma das convidadas e que ela estava cansada, cansada daquelas pessoas que se diziam amigas.

O anfitrião não conseguia erguê-la porque Madame estava caída entre a parede e a privada com seu vestido branco sobre os vidros de perfume quebrados. Madame ameaçou cortar o pescoço se ele tentasse encostar nela. Tyler diz:

— Legal.

E Albert está fedendo. Leslie diz:

— Albert, meu bem, você está fedendo.

É impossível sair daquele banheiro sem feder, diz Albert. Tem caco de vidro espalhado por todo o chão, até dentro da privada. Parece gelo, diz Albert, lembra das festas do hotel que a gente enchia os penicos com gelo picado? O banheiro fede, o chão está coberto de gelo moído que não derrete, e quando Albert consegue pôr Madame em pé, com o vestido branco todo manchado de amarelo, Madame atira um frasco quebrado no anfitrião, escorrega no perfume e nos cacos de vidro e apoia as mãos no chão quando cai. Ela fica gritando e sangrando, encolhida contra a privada. — Ai, como arde, diz. Ai, Walter, está ardendo. Está ardendo — diz Madame. O perfume, as baleias mortas nos cortes das mãos, faz arder. O anfitrião tenta pôr Madame em pé, mas Madame ergue as mãos como se estivesse rezando, o sangue escorre pelas palmas, desce pelos pulsos, atravessa a pulseira de diamantes, chega aos cotovelos e começa a pingar. E o anfitrião diz:

— Você vai ficar bem, Nina.

— Minhas mãos, Walter — Madame chora.

— Vão ficar boas. Madame pergunta:

— Quem faria isto comigo? Quem poderia me odiar tanto? O anfitrião pede a Albert:

— Pode chamar uma ambulância?

Essa foi a primeira missão de Tyler como terrorista da indústria de serviços. Garçom guerrilheiro. Tyler já faz isso há muito tempo, mas diz que é muito mais divertido fazer junto com alguém.

Quando Albert termina de contar a história, Tyler diz:

— Legal.

Voltando ao hotel, estamos no elevador parado entre dois andares, conto a Tyler que escarrei em cima da galantina de truta da convenção dos dermatologistas; três pessoas me disseram que estava muito salgada e uma achou deliciosa.

Ele dá uma sacudida em cima da terrina de sopa e diz que não tem mais. Fica mais fácil em sopa fria, vichyssoise, ou quando os chefs fazem gazpacho. É impossível em sopa de cebola com aquela crosta de queijo derretido em ramekins. Se eu comesse neste lugar, pediria isso.

Já estávamos ficando sem ideias, Tyler e eu. Fazer essas coisas com comida acaba ficando aborrecido, á faz parte da rotina do serviço. Então ouço um médico ou um advogado, não importa, dizendo que o vírus da hepatite sobrevive até em aço inoxidável por seis meses. Pode imaginar por quanto tempo não sobreviverá esse vírus em Charlotte Russa com Creme ao Rum? Ou num Empadão de Salmão?

Perguntei ao médico onde a gente poderia conseguir uns vírus de hepatite, e ele ri, porque está bêbado.

Vai tudo para o lixo hospitalar, diz.

E ri.

Tudo.

Ouço "lixo hospitalar" e sinto que cheguei ao fundo. Seguro a alavanca do elevador e pergunto a Tyler se ele está pronto. A ferida nas costas da minha mão está inchada e vermelha e lustrosa como um par de lábios na forma exata do beijo de Tyler. — Só um segundo — diz Tyler.

A sopa de tomate ainda deve estar quente porque aquele troço encolhido que Tyler enfia dentro da calça está cor-de-rosa como um camarão gigante. 11

Na América do Sul, Terra do Encantamento, estamos caminhando pelas águas límpidas de um rio e os peixinhos entram pela uretra de Tyler. Um peixe com farpas na espinha entra em Tyler, arruma a casa e começa a botar seus ovos. Pensando bem, nossa noite de sábado poderia ter sido bem pior. — Poderia ter sido pior — diz Tyler —, o que fizemos com a mãe de Marla.

Eu digo: cale a boca.

Tyler diz: o governo francês nos mandaria para um complexo subterrâneo nos subúrbios de Paris, onde nem cirurgiões, mas técnicos semi-habilitados, raspariam nossos cílios para o teste de toxidade de um bronzeador em aerosol. — Essas coisas acontecem — diz Tyler. — Leia jornal. O pior é que eu sabia o que Tyler estava fazendo com a mãe de Marla, mas pela primeira vez, desde que nos conhecemos, Tyler tinha dinheiro para gastar. Ele estava ganhando mesmo. Ligaram de Nordstrom pedindo duzentas barras do

sabonete facial de açúcar mascavo de Tyler, antes do Natal. A 20 paus a barra,

preço declarado de varejo, já tínhamos dinheiro para sair sábado à noite. Dinheiro para consertar o vazamento na tubulação de gás. Para ir dançar. Sem ter de me preocupar com dinheiro, talvez eu pudesse largar o emprego. Tyler se deu o nome de Fábrica de Sabão Paper Street. Andam dizendo que é o melhor sabão que existe.

— Seria muito pior — diz Tyler — se você tivesse comido a mãe de Marla por acidente.

Com a boca cheia de Galinha Kung Pao, digo: quer calar essa droga de boca?

Numa noite de sábado estamos os dois dentro de um Impala 1968 apoiado sobre dois pneus, na primeira fila de um estacionamento de carros usados. Tyler e eu estamos conversando e bebendo cerveja, e o banco do Impala é maior que o sofá de muita gente. Os carros ocupam um grande terreno na avenida, o pessoal do ramo chama esses estacionamentos de PotLots, porque qualquer carro custa uns duzentos dólares e durante o dia os proprietários ciganos ficam num escritório de madeira compensada, fumando cigarros compridos e finos. Foram todos o primeiro carro da garotada da highschool. Gremlins e Pavers, Mavericks e Hornets, Pintos, caminhonetes International Harvester, Camaros, Dusters e Impalas rebaixados. Carros que foram adorados e depois abandonados. Animais encurralados. Vestidos de noiva em lojas de Segunda mão. São carros com pára-lamas amassados, amassados de cinza, vermelho ou preto e com remendos na lataria que ninguém lembrou de lixar. Interiores de madeira plastificada, couro plastificado e cromo plastificado. À noite, os ciganos nem se lembram de trancar as portas.

Os faróis dos carros na avenida passam por trás do preço pintado no pára- brisa em Cinemascope do Impala. Veja os U.S.A. O preço é 98 dólares. Daqui de dentro, parece 89 cents. Zero, zero, ponto decimal, oito, nove. A América pede que você ligue.

A maioria desses carros custa por volta de cem dólares, e todos eles têm uma etiqueta de "Como está" pendurada no vidro do motorista. Nós escolhemos o Impala porque, se tivermos de passar a noite de sábado dentro de um carro, este tem bancos maiores. Estamos comendo comida chinesa porque não podemos ir para casa. Ou dormimos aqui ou passamos a noite acordados num salão de dança 24 horas. Nós não vamos a salões de dança, Tyler acha a música muito alta, principalmente os baixos, que acabam fodendo com o seu biorritmo. Na última vez que saímos, Tyler disse que a música alta deixou-o com prisão de ventre. Além disso, as pessoas falam muito alto, e depois de uns goles a mais todo mundo se acha o centro das atenções, sem nenhuma condição de se relacionar com quem quer que seja.

Você é o cadáver de um misterioso crime inglês. Viemos dormir no carro esta noite porque Marla chegou em casa dizendo que ia chamar a polícia e mandar me prender porque cozinhei a mãe dela; Marla corria em volta da casa aos berros, me chamando de demônio e canibal, depois saiu chutando as pilhas de Reader's Digest e National Geographic e então eu a

deixei sozinha. Foi o que aconteceu.

Depois de seu acidental suicídio intencional com Xanax, no Regent Hotel, não acho que Marla chamaria a polícia, mas Tyler preferiu passar a noite fora de casa. No caso de.

No caso de Marla pôr fogo na casa.

No caso de Marla conseguir um revólver.

No caso de Marla ainda estar em casa.

No caso de.

Tento manter-me centrado:

Olhando a cara da lua-cheia

As estrelas nunca se zangam

Blá, blá, blá, ponto final.

Aqui, com os carros passando pela avenida e uma cerveja na mão, dentro de um Impala com volante de baquelite duro e frio, talvez uns 90 centímetros de diâmetro, e assento de vinil rachado pinicando minha bunda por cima do jeans, Tyler diz:

— Só mais uma vez. Me diga exatamente o que aconteceu. Passei a semana sem saber o que Tyler estava fazendo. Um dia, entramos juntos em uma loja da Western Union, e eu o vi mandar um telegrama para a mãe de Marla:

RUGAS HORRENDAS (ponto) AJUDE-ME POR FAVOR! (fim) Tyler entregou ao atendente o cartão de biblioteca de Marla, assinou o recibo com o nome dela, e gritou, sim, Marla também é nome de homem, e o atendente que fosse cuidar da vida.

Quando saímos da Western Union, Tyler disse se eu o amasse, teria de confiar nele. Eu não precisava saber de nada, disse-me ele, e me levou ao Garbonzo's para comer homus.

Nem tive tanto medo do telegrama quanto de sair com Tyler para comer. Nunca, jamais Tyler pagou nada com dinheiro. Suas roupas, Tyler ia às academias e aos hotéis e as pegava nos achados e perdidos. Melhor que Marla, que ia às Laundromats roubar calça jeans das secadoras para vendê-las a doze dólares nesses lugares que compram jeans usados. Tyler não comia em restaurantes, e Marla não estava enrugada. Sem nenhuma razão aparente, Tyler mandou à mãe de Marla uma caixa de chocolates.

Outra forma de a noite de sábado ser pior, Tyler me diz dentro do Impala, teria sido a aranha marrom solitária. Quando ela morde, não injeta só veneno, mas uma enzima ou um ácido digestivo que dissolve o tecido ao redor da picada e literalmente derrete seu braço, sua perna ou seu rosto. Tyler estava fora na noite em que tudo começou. Marla apareceu em casa. Sem bater, ela enfia a cabeça pela porta e chama: — Tem gente?

Estou na cozinha lendo Reader's Digest. Fico sem saber o que fazer.

Marla grita:

— Tyler, Posso entrar? Você está em casa? Eu grito de volta: Tyler não está em casa. Marla grita outra vez:

— Não seja mesquinho.

Nesse momento vou para a porta. Marla está no vestíbulo segurando um pacote de encomenda noturna da Federal Express, e diz: — Preciso pôr uma coisa no seu freezer. Vou atrás dela na cozinha dizendo não.

Não.

Não.

Não.

Ela não vai começar a trazer seu lixo para esta casa. — Mas, Pumpkin — diz Marla —, eu não tenho freezer no hotel, e você disse que eu podia.

Não, eu não disse. A última coisa que quero é Marla se enfiando aqui dentro, uma porcaria por vez.

Marla abre o pacote da Federal Express sobre a mesa da cozinha, tira um saquinho plástico de amendoins com um troço branco dentro e sacode na minha cara. —Isto não é porcaria — diz. — É da minha mãe que você está falando, por isso vá se danar.

O que Marla tira daquele pacote é um daqueles saquinhos de sanduíche com um troço branco que Tyler converteu em sebo para sabão. — Seria muito pior — diz Tyler — se você comesse sem querer o que havia naqueles sacos de sanduíche. Se acordasse no meio da noite, espremesse a meleca branca em sopa de cebola em pó Califórnia e fizesse uma pasta para comer com batatas chips. Ou brócolis.

A última coisa que eu queria na vida, quando Marla e eu estávamos na cozinha, é que ela abrisse o freezer.

Eu perguntei: o que vai fazer com essa coisa branca? — Lábios parisienses — diz Marla. — Quando você envelhece, os lábios encolhem. Estou juntando para fazer uma aplicação de colágeno nos lábios. Já tem uma boa quantidade no seu freezer.

Eu pergunto: de que tamanho quer os lábios? Marla disse que só temia a operação.

Eu disse a Tyler no Impala que aquele troço no Pacote da Federal Express era o mesmo que usamos para fazer sabão. Desde que o silicone ficou perigoso, o colágeno tornou-se o mais indicado para suavizar as rugas ou para estufar lábios finos ou queixos pequenos. Do jeito que Marla explicou, esse colágeno barato é gordura de vaca processada e esterilizada, mas é um tipo de colágeno que não dura muito no corpo. Onde quer que você o aplique, nos lábios, por exemplo, o corpo rejeita e começa a expulsá-lo. Em seis meses, seus lábios estão finos outra vez.

O melhor colágeno, continuou Marla, é a sua própria gordura, aspirada das coxas, processada, limpa e injetada outra vez nos lábios. Ou onde você quiser.

Esse colágeno dura.

Aquelas coisas na geladeira de casa eram a poupança de colágeno de Marla. Toda vez que a mãe dela engordava, fazia lipoaspiração e guardava a gordura no saquinho. Marla diz que o processo se chama "recolher". Se a mãe de Marla não precisasse do colágeno, mandava por encomenda para Marla. Marla não tem gordura alguma, e a mãe dela acha que usar o colágeno da família é melhor do que usar gordura de vaca barata.

Os faróis dos carros na avenida atravessam o anúncio de venda no vidro do carro e imprimem "Como está" no rosto de Tyler, que diz: — As aranhas botam ovos e as larvas cavam um túnel sob a sua pele. É isso que vai acontecer com a sua vida.

Nessa hora, o meu Frango Xadrez com molho cremoso tem o mesmo gosto da gordura aspirada das coxas da mãe de Marla. Foi nesse momento, ali naquela cozinha com Marla, que eu vi o que Tyler andava fazendo.

RUGAS HORRENDAS.

E entendi por que ele mandou os chocolates para a mãe dela. POR FAVOR, AJUDE.

Eu digo: Marla, você não vai olhar nesse freezer. Marla diz:

— Não vou por quê?

— Não comemos carne vermelha — me diz Tyler dentro do carro; e ele não pode usar gordura de galinha porque o sabão não endurece e não forma barras. — Isso vai nos deixar ricos — continua Tyler. — Pagamos o aluguel com aquele colágeno.

Eu digo: você devia ter contado a Marla. Ela pensa que fui eu. Tyler diz:

— A saponificação é a reação química necessária para fazer um bom sabão. Gordura de galinha não funciona nem gordura com muito sal. — Ouça — continua Tyler —, temos um pedido grande para entregar. E vamos mandar mais chocolates e provavelmente um bolo de frutas para a mãe da Marla.

Eu não sei mais se isso vai dar certo.

Para encurtar a história, Marla olhou dentro do freezer. Tudo bem, primeiro houve um pequeno susto. Eu tentei impedi-la, o saquinho que ela tinha na mão caiu e se estatelou sobre o linóleo, e nós dois começamos a escorregar naquela meleca branca, procurando fincar em pé. Estou atrás de Marla agarrado aos seus quadris, os cabelos dela na minha cara, seus braços caídos ao longo do corpo, e eu continuo dizendo que não fui eu. Não fui eu. Eu não fiz isso.

— Minha mãe! Você espalhou ela pela cozinha toda! Nós precisamos fazer sabão, digo, agarrado às costas dela. Precisamos lavar a minha calça, pagar o aluguel, consertar o vazamento de gás. Não fui eu Foi Tyler.

Marla grita:

— Do que é que você está falando? — e se livra da saia que está usando.

Tento levantar no chão engordurado, abraçado à saia de algodão com estampa indiana, e Marla só de calcinha, salto Annabella e blusa camponesa abre a porta do freezer e não vê mais sua poupança de gordura. Só duas pilhas velhas de lanterna, e nada mais. — Onde foi parar?

Vou me arrastando para trás, as mãos escorregando, os pés escorregando no linóleo, minha bunda abrindo uma trilha no chão imundo, vou me afastando de Marla e da geladeira. Ergo a saia para não ver a cara dela quando contar. A verdade.

Nós fizemos sabão com ela. Dela. Da mãe de Marla. — Sabão?

Sabão. Você cozinha a gordura. Mistura com soda cáustica. E o sabão está pronto.

Quando Marla grita, jogo a saia na cara dela e saio correndo. Escorrego. E corro.

Marla vem correndo atrás de mim pela casa, patinando pelos cantos, apoiando-se nos parapeitos das janelas para ganhar impulso. Escorregando. Deixando as mãos engorduradas e sujas nas flores do papel de parede. Caindo e escorregando, levantando e correndo. Marla gritava:

— Você cozinhou a minha mãe!

Tyler cozinhara a mãe dela.

Marla aos gritos, quase me agarrando pelas costas. Tyler cozinhara a mãe dela.

— Você cozinhou a minha mãe!

A porta da frente estava aberta.

Saí por ela com Marla gritando atrás de mim. Meus pés não escorregaram na calçada, então continuei correndo. Até encontrar Tyler ou Tyler me encontrar, e contar a ele o que acontecera.

Com uma lata de cerveja cada um, Tyler e eu nos esticamos nos bancos do carro, eu no da frente. Marla deve estar em casa até agora, atirando revistas nas paredes e me xingando de monstro capitalista de duas caras, canalha bunda-mole. Os quilômetros de noite entre mim e Marla geram insetos, melanomas e vírus devoradores de carne. Aqui onde estou não é tão mau. — Quando o homem é atingido por um relâmpago — diz Tyler —, a cabeça é consumida pelas chamas, o zíper derrete e não se abre nunca mais. Eu pergunto: esta noite nós chegamos ao fundo? Tyler, deitado de costas no banco, pergunta:

— Se Marilyn Monroe estivesse viva agora, o que ela estaria fazendo? Eu digo: boa noite.

A manchete se desprega do teto rasgado, e Tyler diz:

— Se agarrando à tampa do próprio caixão.

12

Meu chefe chega perto da minha mesa com um sorrizinho nos lábios apertados e esticados, a virilha na altura do meu cotovelo. Ergo os olhos da carta de apresentação que estou escrevendo para uma campanha de recall. Essas cartas sempre começam do mesmo jeito:

"Esta notícia lhe está sendo enviada de acordo com as especificações do Ato Nacional de Segurança dos Veículos Motorizados. Concluímos que há um defeito..."

Esta semana, apliquei a fórmula de risco e, pela primeira vez, A vezes B vezes C foi maior que o custo de um recall. Esta semana foi o prendedor de plástico que segura a borracha dos seus limpadores de pára-brisa. Um defeito insignificante. Apenas duzentos veículos afetados. Quase nada pelo custo da mão-de-obra. Na semana passada foi mais grave. Na semana passada foi o couro do estofamento tratado com uma substância reconhecidamente teratogênica, o Nirret sintético ou qualquer coisa igualmente ilegal que ainda é usada em curtumes do terceiro mundo. É tão forte que é capaz de provocar defeitos congênitos no feto da mulher grávida que entrar em contato com ele. Na semana passada, ninguém ligou para o Departamento de Entregas. Ninguém iniciou um recall. O couro novo multiplicado pelo custo de mão-de-obra multiplicado pelos custos administrativos é maior que o nosso lucro no primeiro trimestre. Mesmo que alguém descubra o nosso erro, podemos indenizar muitas famílias enlutadas e não chegar nem perto do que custaria para reformar os 650 estofamentos de couro.

Mas esta semana estamos fazendo uma campanha de recall. E esta semana a insônia voltou. A insônia, e agora parece que o mundo inteiro resolveu descarregar em cima de mim.

Se meu chefe está de gravata cinza, hoje deve ser terça-feira. Ele se aproxima da minha mesa com uma folha de papel e pergunta se não perdi alguma coisa. Deixaram este papel na máquina copiadora, diz ele, e começa a ler:

— A primeira regra do clube da luta é não falar do clube da luta. Seus olhos correm pelo papel, e ele dá uma risadinha. — A segunda regra do clube da luta é não falar do clube da luta. Ouço Tyler falando pela boca do meu chefe, o Senhor Chefe em plena meia-idade com foto da família sobre a mesa, sonhos de aposentadoria precoce e invernos passados em trailer no deserto do Arizona. Meu chefe, com suas camisas superengomadas e horário fixo no cabeleireiro todas as terças após o almoço, olha para mim e diz:

— Espero que isto não seja seu.

Sou o Sangue Fervendo de Ódio de Joe.

Tyler pediu que eu escrevesse à máquina as regras do clube da luta e fizesse dez cópias para ele nem nove nem onze. Dez, disse Tyler. Por outro lado estou com insônia e há três noites não sei o que é dormir. O papel que está com ele

deve ser o original. Fiz dez cópias e esqueci o original. A lâmpada da copiadora

estourava na minha cara. A insônia distancia tudo, a cópia da cópia da cópia. Você não consegue tocar em nada e nada toca em você. Meu chefe continua lendo:

— A terceira regra do clube da luta é apenas dois homens por luta. Nós dois nem piscamos. Meu chefe continua lendo: — Uma luta por vez.

Não durmo há três dias, mas poderia estar dormindo agora. Meu chefe balança o papel na minha cara. O que é isso, pergunta ele. Que brincadeira é essa que andou fazendo no horário de trabalho? Sou pago pela minha atenção exclusiva, e não para perder tempo com joguinhos de guerra. Não sou pago para abusar das máquinas copiadoras.

O que é isto? Ele sacode o papel embaixo do meu nariz. O que estou pensando, pergunta ele, o que fazer com um funcionário que desperdiça o tempo da empresa em seu mundinho fantástico? Se eu estivesse no lugar dele, o que faria?

O que eu faria?

O buraco no meu rosto, o inchaço azul-esverdeado ao redor dos olhos e a cicatriz vermelha do beijo de Tyler nas costas da minha mão, cópia da cópia da cópia.

Especulação.

Para que Tyler quer dez cópias das regras do clube da luta? Vaca hindu.

O que eu faria, digo, é ter muito cuidado com quem eu falo sobre esse papel.

Digo que pode ter sido escrito por um perigoso assassino psicótico, um esquizofrênico capaz de a qualquer momento perder a cabeça durante o expe- diente e entrar de sala em sala com uma carabina semi-automática Armalite AR-180.

Meu patrão só me olha.

Esse cara, continuo, passou a noite limando uma cruz na ponta de cada bala. Ele aparece um dia no trabalho e descarrega sua carga no chefe rabugento, improdutivo, chorão, babaca e bunda-mole, e a bala explode e se espalha dentro dele, estourando as vísceras fedorentas ao longo da espinha. Imagine o seu chakra do umbigo explodindo em câmara lenta e trazendo tudo o que há no intestino grosso.

Meu chefe afasta a folha de papel da minha cara. Vá em frente, digo, leia um pouco mais.

Que coisa fascinante! Só pode ter saído de uma mente doentia. Dou um sorriso.

As ranhuras que contornam o corte no meu rosto têm o mesmo preto- azulado das gengivas de um cachorro. A pele esticada nos olhos inchados parece envernizada.

Meu chefe continua olhando para mim.

Deixe ver no que posso ajudar, digo.

E leio, a quarta regra do clube da luta é uma por vez.

Meu chefe olha para as regras e olha para mim.

Eu digo: a quinta regra é lutar sem sapatos e camisa. Meu chefe olha para as regras e olha para mim Talvez, digo, esse maldito demente esteja usando uma carabina Eagle Apache, porque a Apache tem pente de trinta balas e pesa só quatro quilos. A Armalite só aceita pente com cinco balas. Com trinta tiros, o nosso herói pode entrar no corredor de lambris de mogno e acabar com os vice-presidentes e ainda sobrar cartuchos para cada diretor.

É Tyler falando pela minha boca. Eu era uma pessoa tão gentil. Olho para o meu chefe. Meu chefe tem os olhos mais azuis que já vi. As carabinas semi-automáticas J e R 68 também têm pentes com trinta balas e pesam somente três quilos.

Meu chefe continua olhando para mim.

Tenho medo, digo. Deve ser alguém que ele conhece há muitos anos. Talvez o cara saiba tudo a seu respeito, onde mora, onde sua mulher trabalha, onde seus filhos estudam.

Isto está me cansando e, de repente, estou ficando muito, muito aborrecido. Para que Tyler precisa de dez cópias das regras do clube da luta? Eu não preciso dizer que sei dos estofamentos de couro que provocam defeitos congênitos. Que sei dos alinhamentos de freio que passaram pelo controle de qualidade, mas vão apresentar defeito após três mil quilômetros. Sei que o reostado do ar-condicionado pode esquentar a ponto de incendiar os mapas que você deixa no porta-luvas. Sei que muita gente já se queimou por causa da lâmpada do injetor de combustível. Já vi pernas amputadas na altura dos joelhos porque o turbocompressor explodiu e as palhetas atravessaram o fogo e entraram no compartimento do passageiro. Saí a campo e vi os carros queimados e os relatórios em que a cláusula CAUSA DO DEFEITO foi preenchida como “desconhecida”.

Não, digo, esse papel não é meu. Seguro o papel com dois dedos e puxo. O fio do papel deve ter cortado o dedo do meu chefe, porque ele levou a mão à boca e ficou chupando o dedo com os olhos arregalados. Amasso a folha de papel e jogo na lata de lixo, ao lado da minha mesa. E digo: é melhor não me trazer todo lixo que encontrar por aí. Domingo à noite, vou aos Remanescentes Unidos e o porão da Trinity Episcopal está quase vazio. Apenas Big Bob e eu, arrastando-me com quase to- dos os músculos machucados por dentro e por fora, mas com o coração disparado e um tornado de pensamentos na cabeça. Isso é a insônia. À noite os pensamentos ficam soltos no ar.

Durante a noite você fica pensando: estou dormindo? Será que dormi? Os braços de Big Bob sob as mangas da camiseta têm músculos tão rígidos que chegam a brilhar. Big Bob sorri, está feliz por me ver. Pensou que eu tivesse morrido.

E, digo, eu também.

— Bem — diz Big Bob —, tenho boas notícias. Onde está todo mundo?

— Essa é a boa notícia — continua Big Bob. — O grupo terminou. Só vim

aqui para avisar quem aparecesse.

Jogo-me de olhos fechados no sofá xadrez de segunda mão. — A boa notícia é que há um novo grupo, primeira regra desse novo grupo é que não se deve falar sobre ele.

Ah.

Big Bob continua:

— E a segunda regra é que não se deve falar sobre ele. Merda! Abro os olhos.

Porra!

— O grupo se chama clube da luta — diz Big Bob — e se reúne quinta- feira à noite numa oficina fechada do outro lado da cidade. Nas noites de terça há outro clube da luta que se reúne num galpão ali perto. Eu não conheço nenhum deles.

— A primeira regra do clube da luta — diz Big Bob — é não falar do clube da luta.

Nas noites de quarta, quinta e sexta, Tyler é projecionista de filmes. Vi os recibos de pagamento na semana passada.

— A segunda regra do clube da luta é não falar do clube da luta — repete Big Bob.

No sábado ã noite Tyler e eu vamos juntos ao clube da luta. — Apenas dois homens por luta.

No domingo de manhã chegamos em casa arrebentados e dormimos a tarde toda.

— Apenas uma luta por vez.

Terça-feira à noite, Tyler fica em casa fazendo sabão, embalando em papel de seda e despachando as encomendas. A Fábrica de Sabão Paper Street. — As lutas — diz Big Bob — continuam até onde der. São as regras inventadas pelo cara que inventou o clube da luta. —Você o conhece? — pergunta Big Bob. __ Nunca o vi pessoalmente continua ele —, mas sei que o nome dele é Tyler Durden. A Fábrica de Sabão Paper Street.

Se eu o conheço.

Não sei.

Pode ser.

13

Chego ao Regent Hotel e encontro Marla no saguão, de roupão de banho. Marla ligou para mim no trabalho e pediu que eu não passasse pela academia, pela biblioteca, pela lavanderia ou por qualquer outro lugar quando saísse do trabalho, mas fosse direto me encontrar com ela. Marla ligou porque está com raiva de mim. Ela não diz uma palavra sobre a sua poupança de colágeno. Marla quer que eu lhe faça um favor. Ela estava na cama no começo da

tarde. Marla sobrevive das refeições que os entregadores da Meals on Wheels

entregam aos hóspedes que já morreram; recebe os pratos e diz que eles estão dormindo. Para encurtar a história, nessa tarde Marla estava deitada, esperando a entrega da Meals on Wheels entre meio-dia e duas horas. Marla não tem seguro- saúde há vários anos, por isso parou de procurar, mas esta manhã olhou e pareceu sentir um caroço embaixo do braço, os nódulos próximos eram ao mesmo tempo duros e moles, ela não quer contar a ninguém para não assustar as pessoas que a amam, e se não for nada não tem dinheiro para o médico, mas precisava conversar com alguém e queria que outra pessoa olhasse. A cor dos olhos de Marla é a mesma de um animal assado numa fornalha e mergulhado em água fria. Chama-se a isso de vulcanizar, galvanizar ou temperar. Marla diz que esquece a historia do colágeno se eu prometer ajudá-la. Imagino que ela não tenha chamado Tyler para não assustá-lo. Eu sou neutro; devo isso a ela.

Nós subimos ao quarto, e Marla me diz que na selva não se vêem animais velhos porque, assim que começam a envelhecer, eles morrem. Se ficam doentes ou lentos, vem outro mais forte e os mata. Os animais não envelhecem. Marla deita na cama, solta a tira do roupão e diz que a nossa cultura considera a morte uma coisa errada. Os animais velhos deviam ser uma exceção não natural.

Fanática.

Marla sua frio enquanto vou contando que tive uma verruga quando estava na faculdade. No pênis, continuo, no pau. Fui à faculdade de medicina para removê-la. A verruga. Mais tarde, contei isso ao meu pai. Foi muitos anos depois, e meu pai deu risada e me chamou de trouxa, porque ter uma verruga nes- se lugar é um presente da natureza. As mulheres adoram, foi um presente que recebi de Deus.

Ajoelhado ao lado da cama de Marla com as mãos ainda frias, sentindo a pele fria de Marla um pouco por vez, Marla diz que essas verrugas que são um presente de Deus provocam câncer cervical nas mulheres. Então, sentado sobre o papel que reveste a maca da sala de exames na escola de medicina, um aluno de medicina espirra nitrogênio líquido no meu pau e oito colegas observam. É aí que você vai parar quando não tem seguro-saúde. Só que eles não chamam de pau, chamam de pênis mesmo assim espirram nitrogênio líquido, que poderia ser soda cáustica de tanto que dói. Marla ri até notar que meus dedos pararam. Como se eu tivesse encontrado algo.

Marla pára de respirar, o peito parece um tambor, é o coração socando de dentro para fora a pele esticada do tambor. Mas não, parei porque estou falando, e parei porque, por um instante, não estávamos mais no quarto de Marla. Estávamos na faculdade de medicina anos atrás, sentados sobre um papel grudento com meu pau em chamas por causa do nitrogênio líquido, quando um dos estudantes viu meus pés descalços e saiu correndo da sala. O estudante voltou com mais três médicos formados, e os médicos empurraram o homem que estava usando nitrogênio líquido.

Um médico formado segurou meu pé direito e mostrou aos outros médicos

formados. Os três viraram o pé de um lado e de outro, espetaram, tiraram fotos

Polaroid, como se o resto de mim, seminu e com o presente divino semicongelado, não existisse. Apenas o pé e o grupo de estudantes de medicina se acotovelando na frente dele.

— Há quanto tempo — perguntou o médico — tem essa mancha vermelha no pé?

O médico se referia à minha marca de nascença. O meu pé direito tem uma marca de nascença que meu pai achava parecida com uma Austrália vermelha ao lado de uma pequena Nova Zelândia. Foi isso que eu disse a eles e fiz todo mundo rir. Meu pau estava descongelando. Saíram todos, menos o aluno que tinha o nitrogênio, eu achei que ia sair também mas ele ficou tão desapontado que nem me olhou nos olhos quando pegou a cabeça do meu pau esticou na direção dele. Da latinha saiu um jato sobre o que sobrara da verruga. A sensação, feche os olhos e imagine seu pau a centenas de quilômetros de distância, e ainda por cima doendo.

Marla olhou minha mão com a cicatriz do beijo de Tyler. Eu disse ao estudante de medicina, vocês não devem ver muita marca de nascença por aqui.

Não é isso. O aluno diz que todo mundo achou que a marca de nascença fosse câncer. É um novo tipo de câncer que está atingindo homens jovens. De repente aparece uma pinta vermelha no pé ou no tornozelo. As pintas não desaparecem, mas se espalham por todo o corpo e acabam matando você. O estudante disse: os médicos e os outros ficaram tão excitados porque acharam que você tinha esse novo câncer. Pouca gente tem, por enquanto, mas já está se espalhando.

Isso foi há dez anos.

O câncer é assim, digo a Marla. Haverá outros erros, talvez o mais importante é não esquecer o resto de você quando uma parte vai mal. Marla diz: talvez.

O estudante terminou com o nitrogênio e me disse que a verruga cairia dentro de alguns dias. Colada num papel próximo à minha bunda pelada estava a foto Polaroid do pé que ninguém quis. Eu disse: Posso ficar com a foto? Ainda tenho essa foto no meu quarto, presa na dura do espelho. Todas as manhãs, quando me penteio para ir trabalhar, lembro que por dez minutos eu quase tive um câncer, o pior de todos.

Conto a Marla que no Dia de Ação de Graças fez um ano que meu avô e eu não fomos escorregar no gelo, embora a camada de gelo estivesse grossa. Minha avó usava esses esparadrapos redondos na testa e nos braços, quando as pintas que ela teve a vida inteira não estavam bem. Ou tinham bordas franjadas ou de marrons tinham passado a azuis e pretas. Quando minha avó foi a última vez para o hospital, a maleta que meu avô carregava estava tão pesada que ele se queixou de estar pendendo para um lado. Minha avó franco-canadense era tão recatada que nunca usou maio em público e abria a torneira da pia para abafar qualquer ruído que fizesse no banheiro. Saindo do Hospital Nossa Senhora de Lourdes depois de uma mastectomia parcial, ela diz:

— É você que está pendendo para um lado?

Para o meu avô, isso resume toda a história, minha avó, o câncer, o casamento deles, a sua vida. Ele ri toda vez que conta isso. Marla não está rindo. Quero fazê-la rir, animá-la. Para que ela me perdoe pelo colágeno, digo que não encontrei nada. Se ela sentiu alguma coisa de manhã, deve ter se enganado. Foi só uma marca de nascença. Marla tem a marca do beijo de Tyler nas costas da mão. Quero que Marla ria, por isso nada lhe conto sobre a última vez que abracei Chloe, Chloe sem cabelo, um esqueleto mergulhado em cera amarela com um lenço de seda amarrado no crânio pelado. Abracei Chloe pela última vez antes que ela desaparecesse para sempre. Eu disse que ela parecia um pirata, e a fiz rir. Eu, quando vou à praia, sempre me sento sobre o pé direito. Austrália ou Nova Zelândia, enterro o pé na areia. Não quero que as pessoas vejam meu pé e pensem que estou morrendo. O câncer que não tenho está por toda parte. Não digo isso a Marla.

Há uma série de coisas que não queremos saber sobre as pessoas que amamos.

Para animá-la, para fazê-la rir, contei de uma mulher que escreveu para o Querido Abby dizendo que se casara com um agente funerário muito bonito e bem-sucedido, mas na noite de núpcias foi obrigada a entrar numa banheira com água fria até a pele gelar, depois deitou-se na cama completamente imóvel para que ele tivesse um intercurso sexual com um corpo inerte e gelado. O mais engraçado é que essa mulher fez isso na lua-de-mel e continuou fazendo pelos dez anos que durou o casamento, e escrevia para o Querido Abby perguntando o que significava isso.

14

Eu adorava os grupos de apoio porque, se as pessoas achassem que você ia morrer, davam-lhe toda a atenção.

Se fossem vê-lo pela última vez, elas realmente o viam. Tudo mais, os débitos no talão de cheques, as músicas no rádio, o cabelo despenteado, tudo era jogado pela janela.

Você merecia toda a atenção delas.

As pessoas ouviam e esperavam sua vez de falar. E quando falavam, não contavam histórias. Se você conversasse com alguém, ambos construíam alguma coisa e tornavam-se pessoas diferentes do que eram antes.

Marla começou a ir aos grupos de apoio quando encontrou o primeiro caroço.

Na manhã que encontramos o segundo, Marla entrou pulando na cozinha, com as duas pernas dentro de uma só perna da meia-calça e disse: — Veja, sou uma sereia.

Marla disse:

— Não é a mesma coisa que dois caras sentado de costas na privada,





fingindo que é motocicleta. Isto é um acidente de verdade.

Pouco antes de Marla e eu nos conhecermos nos Remanescentes Unidos o primeiro caroço já existia, e agora havia outro. O que você precisa saber é que Marla ainda está viva. Sua filosofia de vida, ela me disse, é que ela pode morrer a qualquer momento. A tragédia da sua vida é que não morre.

Quando Marla encontrou o primeiro caroço, foi a uma clínica onde mães encurvadas como espantalhos ocupavam as poltronas de plástico em três lados da sala de espera com crianças fracas emboladas no colo ou deitadas aos seus pés. Crianças abatidas de olhos encovados, como bananas ou laranjas que apodrecem e caem, e as mães coçando sobre a camada de caspa das constantes infecções no couro cabeludo. Do jeito como os dentes pareciam imensos naqueles rostos magros, você via que são cacos de ossos que rasgam a pele para triturar as coisas. É aí que você vai parar quando não tem seguro-saúde. Antes que alguém se desse conta, muitos gays quiseram ter filhos, e hoje eles estão doentes, as mães estão morrendo e os pais já morreram, e sentados ali no meio daquele cheiro de vómito hospitalar, enquanto uma enfermeira pergunta a cada mãe há quanto tempo ela está doente e quanto já perdeu de peso, se o filho dela tem um pai ou um responsável vivo, Marla decide que não. Marla nem quer saber se vai morrer ou não. Ela dobrou a esquina da clínica em direção à City Laundry e roubou todos os jeans das secadoras, depois seguiu andando até o comerciante que pagou 15 paus por calça. Depois comprou para si uma meia-calça de ótima qualidade, dessas que não desfiam.

— Mas até as que não desfiam podem furar — diz Marla. Nada é eterno. Tudo está desmoronando.

Marla começou a frequentar os grupos de apoio porque seria mais fácil estar perto de outra bosta humana. Todo mundo tem alguma coisa errada. E por algum tempo os sinais vitais do coração dela foram quase uma linha reta. Marla começou a vender planos de funeral pré-pago para uma agência funerária, onde às vezes uns homens gordos, mas geralmente mulheres gordas, saíam do showroom da funerária com uma urna crematória do tamanho de um porta-ovo, e Marla, ali sentada à mesa da recepção com o cabelo preso, a meia- calça furada e o caroço no seio, dizia:

— Senhora, não tente enganar a si mesma. Não vamos conseguir enfiar nem a sua cabeça incinerada numa coisa desse tamanho. Volte e escolha uma urna do tamanho de uma bola de boliche.

O coração de Marla estava parecido com o meu rosto. A merda e o lixo do mundo. A bosta humana pós-consumo que ninguém jamais se dará ao trabalho de reciclar.

Entre os grupos de apoio e a clínica, Marla contou, ela conheceu muita gente que já tinha morrido. Eram pessoas que haviam passado para o outro lado e que à noite a chamavam pelo telefone. Marla entrava num bar e ouvia o barman chamando o nome dela, e quando ia atender, o telefone estava mudo. Nessa época, ela achou que havia chegado ao fundo do poço. — Quando se tem 24 anos — diz ela—, ninguem imagina que possa cair tão

fundo, mas acaba aprendendo.

A primeira vez que Marla encheu uma urna crematória, não usou máscara, e mais tarde, quando assoou o nariz, saiu uma secreção preta das cinzas do Senhor Fulano de Tal.

Na casa da Paper Street, se o telefone tocava só uma vez e você atendia e não havia ninguém do outro lado, já sabia que alguma coisa queria falar com Marla. Isso acontecia mais vezes do que se possa imaginar. Na casa da Paper Street, um detetive da polícia começou a ligar por causa da explosão no meu apartamento, e Tyler, encostado em mim, cochichava ao meu ouvido enquanto eu segurava o fone na outra orelha, e o detetive perguntava se eu conhecia alguém que soubesse fazer dinamite. Tyler cochichava:

— O desastre faz parte da minha evolução natural rumo à tragédia e à dissolução.

Eu disse ao detetive que foi a geladeira que mandou meu apartamento para os ares. E Tyler cochichava:

— Estou rompendo meus vínculos com a força física e os bens materiais, porque só destruindo a mim mesmo vou descobrir a força superior do meu espírito.

A dinamite, disse o detetive, continha impurezas, um resíduo de oxalato de amônia e percloreto de potássio, o que indicava ser uma bomba caseira, e a fechadura da porta estava quebrada.

Eu digo a ele que naquela noite eu estava em Washington, D.C. O detetive revelou ao telefone que alguém tinha espirrado Freon na lingueta da fechadura e arrebentou o tambor com um formão. É assim que os ladrões andam roubando as bicicletas.

— O libertador que destruir a minha propriedade de estará salvando o meu espírito — diz Tyler. — O mestre que tirar os bens materiais do meu caminho me libertará.

O detetive disse que a mesma pessoa que pôs a dinamite pode ter ligado o gás e apagado a chama do piloto no forno dias antes da explosão, o gás foi apenas o gatilho. Levou alguns dias para se espalhar pelo apartamento e alcançar o compressor ao pé da geladeira, quando o motor do compressor detonou a explosão.

Tyler cochichou:

— Diz a ele que foi sim, que foi você quem fez isso. Foi você quem mandou tudo para os ares. É isso o que ele quer ouvir. Eu disse ao detetive: não, não deixei o gás aberto e viajei. Eu amava a minha vida. Eu amava aquele apartamento. Amava cada peça de móvel. Eles eram a minha vida. Tudo, os abajures, as poltronas, os tapetes, tudo era eu. A louça nos armários era eu. As plantas eram eu. A televisão era eu. Fui eu quem voou pelos ares. Será que ele não entendia? O detetive me disse para não sair da cidade.

15

Sua Excelência, o senhor presidente da sede local do sindicato nacional dos projecionistas e operadores de cinema independentes, sentou-se. Por baixo, por trás e por dentro de tudo o que esse homem dava por certo, uma coisa terrível vinha acontecendo.

Nada é estático.

Tudo está desmoronando.

Sei disso porque Tyler sabe disso.

Há três anos Tyler vinha fazendo montagens e desmontagens de filmes para uma cadeia de cinemas. O filme chegava nas caixas de metal, em seis ou sete rolos. O trabalho de Tyler era emendar os rolos num único rolo de um metro e meio para os projetores auto-ajustáveis que enrolam o filme sozinho. Depois de três anos trabalhando em sete cinemas, com pelo menos três telas cada um e um novo filme a cada semana, Tyler já havia emendado e separado centenas de cópias.

Uma pena, mas com os projetores auto-ajustáveis que enrolavam o filme sozinhos, o sindicato não precisava mais de Tyler. O senhor presidente chamou Tyler para uma conversinha.

O serviço era um tédio e o salário uma merda por isso o presidente da união dos sindicatos dos operadores independentes de projeção unidos e dos funcionários de cinemas unidos disse a Tyler Durden que estava fazendo um favor por lhe dar esse diplomático pé na bunda. Não veja isso como uma rejeição. Veja como corte de pessoal. Do alto de sua autoridade, o senhor presidente em pessoa diz: — Apreciamos sua contribuição ao nosso sucesso. Ah, não há problema, diz Tyler e sorri. Desde que o sindicato continuasse enviando seu cheque, ele ficaria de boca fechada. Tyler disse:

— Veja isso como uma aposentadoria precoce, uma pensão. Centenas de cópias passaram pelas mãos de Tyler. Filmes que já tinham voltado para o distribuidor. Filmes que já tinham sido re-relançados. Comédias. Dramas. Musicais. Romances. Aventuras. Emendados com pelo menos um fotograma de pornografia. Sodomia. Felação. Cunilíngua. Submissão. Tyler nada tinha a perder. Tyler era a palmatória do mundo, o lixo da hu- manidade.

Foi isso que Tyler e eu ensaiamos para dizer também ao gerente do Pressman Hotel.

Em seu outro emprego, no Pressman Hotel, Tyler disse que não era ninguém. Ninguém se importava se ele estivesse vivo ou morto, assim como ele também não se importava com os outros. Foi isso que Tyler mandou que eu dissesse na sala do gerente do hotel com guardas de segurança do outro lado da porta.

Tyler e eu ficamos acordados até tarde pensando como seria depois que tudo terminasse.

Depois que ele esteve no sindicato dos projecionistas, Tyler obrigou-me a

enfrentar o gerente do Pressman Hotel.

Tyler e eu estávamos cada dia mais parecidos um com o outro, como irmãos gêmeos. Nós dois tínhamos um soco no queixo, nossa pele desmemoriada já não lembrava mais como se recuperar.

Meus ferimentos vinham do clube da luta, e o rosto de Tyler foi desfigurado pelo presidente do sindicato dos projecionistas. Depois que Tyler saiu se arrastando da sala do presidente, fui ver o gerente do Pressman Hotel. Estou ali sentado, na sala do gerente do Pressman Hotel. Sou o Olhar Vingativo de Joe.

A primeira coisa que o gerente do hotel disse foi que eu tinha três minutos. Nos primeiros trinta segundos, contei que tinha mijado na sopa, peidado no creme brúlées, escarrado nas endívias ao vapor, e agora queria que o hotel me

mandasse um cheque semanal equivalente à média do meu salário mais gorjetas. Em troca, eu sumiria de vista, não procuraria os jornais nem a saúde pública com uma confissão confusa e chorosa.

As manchetes:

Garçom Perturbado Admite Contaminar Pratos. E claro, disse, que ia parar na cadeia. Eles iam me pendurar de ponta- cabeça, me chutar o saco, me arrastar pela rua, arrancar minha pele e me queimar com soda cáustica, mas o Pressman Hotel seria lembrado para sempre como o hotel em que os ricaços da cidade comeram mijo. Eram as palavras de Tyler que saíam pela minha boca. E eu era uma pessoa tão gentil.

Na sala do sindicato dos projecionistas, Tyler deu risada quando levou um soco do presidente. Um único soco derrubou Tyler da cadeira, e ele caiu contra a parede, rindo.

— Continue, você não pode me matar — ria Tyler. — Seu babacão. Pode me arrancar as tripas mas não pode me matar. Você tem muito que perder.

Eu não tenho nada.

Você tem tudo.

Vamos, agora um direto no estômago. Outro soco na cara. Arranque meus dentes, mas continue mandando aqueles cheques. Arrebente as minhas costelas, mas se falhar uma só semana, vou a público e você e o seu sindicatozinho vão ter de se explicar nos tribunais para todos os donos de cinema, os distribuidores de filmes e as mamães cujos filhinhos assistiram a um Bambi pornô. — Sou um lixo — disse Tyler. — Sou um lixo, um merda, um doido, para você e para toda esta porra de mundo — disse Tyler ao presidente do sindicato. —Você nem quer saber onde moro, o que sinto, como alimento meus filhos ou como vou pagar o médico se ficar doente, e, sim, sou frouxo, chato e estúpido, mas ainda estou sob sua responsabilidade. Sentado no escritório do Pressman Hotel, meus lábios do clube da luta ainda estavam rachados em uns dez segmentos. O corte no rosto voltado para o gerente do Pressman Hotel era totalmente convincente.

Eu disse basicamente a mesma coisa que Tyler.

Quando o presidente do sindicato derrubou Tyler no chão, quando o senhor presidente viu que ele não ia reagir, sua excelência com seu corpanzil Cadillac muito maior e mais forte do que o necessário, sua excelência recuou o bico do sapato e chutou as costelas de Tyler, e Tyler riu. Sua excelência meteu o bico do sapato nos rins de Tyler encolhido, e Tyler continuou rindo. — Pode bater — disse Tyler. — Confie em mim. Você vai se sentir muito melhor. Vai se sentir ótimo.

Na sala do Pressman Hotel, perguntei ao gerente se podia usar o telefone e disquei o número de um jornal. Com o gerente olhando para mim, eu disse: — Alô, cometi um crime terrível contra a humanidade como protesto político. Meu protesto é contra a exploração dos trabalhadores da indústria de serviços.

Se eu fosse preso, não seria apenas um peão desequilibrado que mijou na sopa. Isso ganharia uma escala heróica.

Robin Hood, o Herói dos Garçons.

Seria muito mais que um mero hotel e um mero garçom. O gerente do Pressman Hotel tirou o fone da minha mão, gentilmente. O gerente disse que não me queria mais trabalhando lá, não desse jeito. Paro diante da mesa do gerente e pergunto: o quê? Você não gostou da idéia?

Sem vacilar, sempre olhando para o gerente, faço meu punho girar com a força centrífuga do meu braço e arranco sangue fresco das cascas do meu próprio nariz.

Não sei por que me lembro da noite em que Tyler e eu tivemos nossa primeira luta. Quero que você me bata o mais forte que puder. Esse soco não foi tão forte. Dou outro soco em mim mesmo. Este parece melhor, faz bastante sangue, eu me jogo contra a parede fazendo muito barulho e derrubando um quadro que está pendurado. O vidro quebrado e a moldura e o desenho de flores e o sangue, tudo vai para o chão junto comigo. Sou tão desajeitado. O sangue se espalha pelo tapete, eu estico o braço e seguro a quina da mesa do gerente com as mãos sujas de sangue e digo, por favor, me ajude, mas começo a rir. Me ajude, por favor.

Por favor, não bata em mim.

Caio de novo no chão e saio arrastando sangue pelo tapete. A primeira coisa que vou dizer é "por favor". Mas fico de boca fechada. O monstro se arrasta sobre os adoráveis buquês e guirlandas do tapete oriental. O sangue escorre pelo meu nariz, escorrega para dentro da minha boca e desce pela garganta, quente. O monstro se arrasta pelo tapete, fiapos e poeira grudam nas patas ensangüentadas. E as patas se aproximam do gerente do Pressman Hotel prontas para agarrar o tornozelo de riscas finas e dizer:

Por favor.

Diga.

O por favor sai numa bolha de sangue.

Diga.

Por favor.

A bolha explode sangue por todo lado.

E é assim que Tyler fica livre para reunir o clube da luta todas as noites da semana. Depois disso foram sete clubes da luta, depois quinze clubes da luta, depois 23 clubes da luta, e Tyler queria mais. O dinheiro nunca mais parou de entrar.

Por favor, pedi ao gerente do Presman Hotel, me dê o dinheiro. E dou outra risadinha.

Por favor.

E, por favor, não me bata mais.

Você tem tanto, eu não tenho nada. E começo a fazer meu sangue subir pelas pernas de riscas finas do gerente do Pressman Hotel, que está inclinado para trás, as mãos apoiadas no peitoril da janela às suas costas, os lábios finos encolhidos contra os dentes.

O monstro engancha sua pata sangrenta na cintura do gerente e consegue se erguer para agarrar a camisa imaculadamente branca, onde as mãos ensangüentadas se fecham em torno dos punhos do gerente. Por favor. Dou um sorriso largo que rasga ainda mais meus lábios. Estamos lutando quando o gerente grita e tenta afastar as mãos de mim, do meu sangue, do meu nariz quebrado, o sangue viscoso grudando em nós dois, e quando estamos no melhor momento, entram os guardas da segurança. 16

Deu nos jornais de hoje que alguém invadiu os escritórios entre o décimo e o décimo quinto andar da Hein Tower, escalou as janelas pelo lado de fora, pintou a parede do lado sul com uma máscara que ocupa os cinco andares e pôs fogo nas janelas que ficam no meio dos olhos, que queimaram imensos, vivos e inevitáveis sobre a cidade, ao amanhecer. Na foto de primeira página, a máscara é uma moranga raivosa, um demônio japonês, o dragão da avareza pairando no céu, e a fumaça são as sobrancelhas da bruxa ou os chifres do demônio. E as pessoas gritando com a cabeça jogada para trás.

O que era aquilo?

Quem faria uma coisa dessas? Depois que o fogo apagou, a cara continuou lá, mas estava ainda pior. Os olhos vazios pareciam observar as pessoas na rua e ao mesmo tempo não tinham vida.

Os jornais não param de falar nisso.

É claro que você lê uma coisa dessas e logo se pergunta se faz parte do Projeto de Ações Violentas.

O jornal diz que a polícia não tem pistas. Gangues jovens ou alienígenas do espaço, fosse quem fosse poderia ter morrido arrastando-se pela saliência do paredão ou pendurando-se nos parapeitos das janelas munidos com sprays de tinta preta.

Seria o Comitê de Maldades ou o de Incêndio Criminoso? A máscara

gigantesca deve ter sido a lição de casa da semana passada. Tyler deve saber, mas a primeira regra do Projeto de Ações Violentas é não fazer perguntas sobre o projeto de Ações Violentas. Esta semana, no Comitê de Ataque do Projeto de Ações Violentas, Tyler diz que vai ensinar como se usa uma arma. O que a arma faz é concentrar a explosão numa única direção.

Na última reunião do Comitê de Ataque, Tyler levou um revólver e as páginas amarelas da lista telefônica. O pessoal se reuniu no porão do clube da luta no sábado à noite. Cada comitê se reúne numa noite diferente. O de Incêndio Criminoso se reúne segunda-feira. O de Ataque, terça-feira. O de Maldades, na quarta-feira. E o de Informações Falsas reúne-se às quintas. O Caos Organizado. A Burocracia da Anarquia. Sabe como é. Grupos de apoio. Um tipo de.

É terça-feira à noite, e o Comitê de Ataque propôs os eventos para a próxima semana, Tyler leu as propostas e passou as tarefas ao comitê. A esta hora, na próxima semana, cada membro do Comitê de Ataque terá uma luta em que não sairá como herói. E não será no clube da luta. Isso é mais difícil do que parece. Um cara na rua vai fazer qualquer coisa para não entrar numa briga.

A idéia é pegar qualquer um que nunca tenha se envolvido em luta e recrutá-lo. Deixá-lo conhecer a vitória uma vez na vida. Fazê-lo explodir. Dar permissão para que ele estoure os seus miolos. Você consegue. Se vencer, vai estragar tudo. — O que vocês têm de fazer, pessoal, é mostrar a esses caras que eles ainda têm algum poder — disse Tyler ao comitê. Foi um discurso emocionado. Depois Tyler abriu os papeizinhos dobrados que estavam na caixa de papelão. É assim que cada comitê propõe os eventos da semana seguinte, escrevendo o evento no bloquinho do comitê. Arranca a folha, dobra e põe na caixa. Tyler lê cada proposta e joga fora as idéias que não são boas.

Para cada idéia descartada, Tyler põe um papel em branco na caixa. Então, todos os membros do comitê tiram um papelzinho da caixa. Tyler me explicou que se alguém tirar o papel em branco, tem só a sua tarefa para fazer na semana.

Se você tira uma proposta, talvez tenha de ir ao festival de cerveja importada no fim de semana e provocar um cara no mictório. Vai obter um favor especial se conseguir apanhar por isso. Ou tenha de ir a um desfile de modas no átrio de um shopping center e atirar gelatina de morango do mezanino. Se você for preso, cai fora do Comitê de Ataque. Se der risada, cai fora do comitê.

Ninguém sabe quem fez a proposta, e ninguém, senão Tyler, sabe quais são as propostas, qual delas foi aceita e qual foi para o lixo. No meio da semana, você lê no jornal que um homem não identificado, no centro da cidade, arrancou o motorista da direção de um Jaguar conversível e jogou o carro numa fonte. E fica se perguntando. Teria sido uma proposta do comitê?

Na terça-feira seguinte, você vai olhar as pessoas na reunião do Comitê de

Ataque, sob a única lâmpada do porão escuro do clube da luta, e vai se perguntar quem teria jogado o Jaguar dentro da fonte. Quem teria subido no telhado do museu de arte e atirado paint balls na escultura do saguão de recepção?

Quem teria pintado a máscara de fogo na Hein Tower? Na noite da tarefa na Hein Tower, fico imaginando uma turma de escriturários, guarda-livros ou mensageiros dos escritórios de advocacia e conta- bilidade entrando sorrateiramente nas salas em que trabalham durante o dia. Talvez estivessem meio bêbados, embora isso vá contra as regras do Projeto de Ações Violentas, e usassem chaves-mestras ou sprays de Freon para estourar o tambor das fechaduras e se pendurar, escalar a fachada de tijolos do edifício, saltar, confiar no outro para segurar as cordas, balançar, arriscar a vida nos escritórios onde, diariamente, sentem a vida se acabar a cada minuto. Na manhã seguinte, esses mesmos escriturários e mensageiros estarão no meio da multidão de cabelo penteado e gravata, bêbados de sono mas sóbrios, ouvindo as pessoas especular sobre quem teria feito isso, e a polícia gritando para todos que por favor se afastem, enquanto a água escorre no centro enfumaçado dos olhos imensos.

Tyler me disse em segredo que nunca há mais de quatro propostas boas em cada reunião, então as chances de você tirar uma proposta real, e não meramente um papel em branco, são mais ou menos quatro entre dez. Há 25 caras no Comitê de Ataque incluindo Tyler. Todo mundo tem como tarefa perder uma luta em público; e cada membro vai tirar uma proposta. Esta semana, Tyler disse a eles:

— Saiam e comprem uma arma.

Tyler entregou a um dos caras as páginas amarelas da lista telefônica e pediu que ele escolhesse um anúncio. Depois passasse a lista para outro. Duas pessoas não podiam comprar nem usar a arma no mesmo lugar. — Isto — disse Tyler, tirando um revólver do bolso do casaco —, isto é uma arma; em duas semanas cada um deve ter uma deste tamanho, mais ou me- nos, para trazer à reunião.

— Melhor pagá-la em dinheiro — disse Tyler. — No nosso próximo encontro, todo mundo vai trocar de arma e dar queixa de roubo daquela que comprou.

Ninguém perguntou nada. Não fazer perguntas é a primeira regra do Projeto de Ações Violentas.

Tyler fez a arma circular de mão em mão. Era muito pesada pelo tamanho, como se algo gigantesco como uma montanha ou o sol tivesse desmoronado ou derretido para fazê-la. Os rapazes do comitê a seguravam com dois dedos. Todos queriam perguntar se estava carregada, mas a segunda regra do Projeto de Ações Violentas é não fazer perguntas.

Talvez estivesse, talvez não. Talvez devêssemos pensar sempre no pior. — As armas — disse Tyler — são simples e perfeitas. Basta puxar o gatilho.

A terceira regra do Projeto de Ações Violentas e nada de desculpas.

— O gatilho — disse Tyler — solta o cão, que detona a espoleta.

A quarta regra é nada de mentiras.

— A explosão detona um projétil de metal pela extremidade aberta da cápsula e o cano da arma dirige a pólvora e impulsiona o projétil — disse Tyler. Quando Tyler inventou o Projeto de Ações Violentas, ele disse que o objetivo do projeto nada tinha que ver com outras pessoas. Tyler não se importava se alguém saísse ferido ou não. O objetivo era que cada homem do projeto aprendesse que tinha o poder de controlar a história. Nós, cada um de nós, podíamos assumir o controle do mundo. Foi no clube da luta que Tyler inventou o Projeto de Ações Violentas. Uma noite, no clube da luta, pus um novato a nocaute. Era sábado, um garoto com cara de anjo veio pela primeira vez ao clube da luta, e eu o desafiei para lutar. Essa é a regra. Se é a sua primeira noite no clube da luta, você tem de lutar. Eu sabia disso, e o desafiei porque a insônia havia voltado e eu estava a fim de destruir qualquer coisa que fosse bela. Como boa parte do meu rosto nunca teve tempo de se recuperar, eu nada tinha que perder no departamento aparência. No trabalho, meu chefe perguntou o que eu andava fazendo com aquele buraco no rosto que nunca fechava. Quando bebo café, eu disse a ele, tampo o buraco com dois dedos para não vazar. Há um golpe de luta que deixa o outro com ar suficiente para ficar consciente, e nessa noite no clube da luta eu bati no nosso calouro e soquei a linda carinha de anjo, primeiro com os nós dos dedos, depois com o punho fechado, até ficar com os dedos feridos de tanto socar os dentes. Então o garoto desmoronou em meus braços.

Tyler me disse depois que nunca me vira destruir uma coisa daquele jeito. Naquela noite, Tyler , percebeu que precisava dar um tempo no clube da luta ou fechá-lo.

Tyler disse, tomando café da manhã no dia seguinte: — Você parecia um doido, Psycho-Boy. Onde você foi parar? Eu disse que estava me sentindo uma merda e que não conseguia relaxar. Eu não tinha tomado nenhum tipo de bola. Talvez já estivesse viciado. É possível criar tolerância à luta, por isso eu talvez precisasse de algo mais forte. Foi nessa manhã que Tyler inventou o Projeto de Ações Violentas. Tyler perguntou com que eu estava lutando. Sabe as coisas que Tyler diz sobre ser um merda, um escravo da história? Pois era assim que eu me sentia. Queria destruir tudo de belo que nunca tive. Pôr fogo na floresta Amazônica. Injetar CFCs direto na camada de ozônio. Abrir válvulas de descarga dos superpetroleiros e destampar poços de petróleo em alto- mar. Queria matar os peixes que não pudesse comer e contaminar as praias francesas que não conheci.

Queria que o mundo todo chegasse ao fundo. Batendo naquele garoto, o que eu queria, na verdade, era meter uma bala no meio da testa de todos os pandas ameaçados que não trepavam para salvar a espécie e de cada baleia ou golfinho que desistisse de lutar e encalhasse na praia. Não veja isso como extinção. Veja como diminuição da espécie. Por milhares de anos, os seres humanos fodem e sujam e cagam em cima

deste planeta, e agora a história quer que eu limpe tudo. Preciso lavar e amassar

as latas de sopa. E dar conta de cada gota de óleo dos motores. E ainda tenho de pagar a conta pelo lixo nuclear, pelos depósitos de gasolina queimados e pela lama tóxica despejada por uma geração anterior à minha.

Apoiei a cabeça do anjinho como se fosse um bebê ou uma bola de futebol na dobra do meu braço e bati nela com os nós dos dedos, bati até sentir os dentes se quebrando. Depois, usei o cotovelo, e ele foi escorregando dos meus braços até cair aos meus pés.

Eu queria sentir cheiro de fumaça.

Pássaros e cervos são meros luxos e todo peixe deveria voar. Eu queria pôr fogo no Louvre. E limpar a bunda com a Mona Lisa. Este é o meu mundo, agora.

Este é o meu mundo, o meu mundo, e os antigos estão mortos. Foi naquele café da manhã que Tyler inventou o Projeto de Ações Violentas.

Ele queria que o mundo ficasse livre da história. Nós tomávamos nosso café na casa da Paper Street, e Tyler disse: imagine você plantando rabanetes e semeando batatas no décimo quinto gramado de um campo de golfe abandonado.

Você, caçando alce nas florestas úmidas do cânion formado pelas ruínas do Rockfeller Center, colhendo marisco perto do esqueleto do Space Needle, numa inclinação de 45 graus. Pintaremos os arranha-céus com imensas carrancas totêmicas, e todas as noites o que sobrou da humanidade será recolhido nos zoológicos vazios e trancado em jaulas para se proteger dos ursos, dos grandes felinos e dos lobos que nos rondam do lado de fora das grades durante a noite. — Reciclagem e limites de velocidade são uma bobagem — diz Tyler. — É como alguém parar de fumar no leito de morte. É o Projeto de Ações Violentas que vai salvar o mundo. A era glacial da cultura. A era do obscurantismo prematuramente induzido. O Projeto de Ações Violentas forçará a humanidade a entrar em estado de dormência ou de enfraquecimento o tempo que for preciso para a Terra se recuperar. — Você justifica a anarquia — diz Tyler. — Você a compreende. O que o clube da luta faz pelos escriturários e bilheteiros, o Projeto de Ações Violentas fará pela civilização, para que façamos algo de bom pelo mundo.

— Imagine — diz Tyler — os alces passando pelas janelas das lojas de departamento e seus cabideiros fedorentos com lindos vestidos e smokings pendurados. Você vai usar roupas de couro que vão durar a vida toda e escalar as trepadeiras grossas como um pulso enroladas na Sears Tower. Como João e o pé de feijão, você vai atravessar a copa das árvores e o ar será tão limpo que verá pessoinhas batendo milho e estendendo tiras de carne de veado para secar nos acostamentos vazios de uma auto-estrada com oito pistas e milhares de quilômetros de extensão.

Esse é o objetivo do Projeto de Ações Violentas, diz Tyler, a destruição mais completa e direta da civilização.

O que virá depois do Projeto de Ações Violentas, só Tyler sabe dizer.

A segunda regra é não fazer perguntas.

— Nada de balas — disse Tyler ao Comitê de Ataque. — E quando não se preocuparem com isso, aí, sim, terão de matar alguém. Incêndio criminoso. Ataque. Ação Violenta e Informação Errada. Nenhuma pergunta. Nenhuma pergunta. Não se aceitam desculpas nem mentiras.

A quinta regra do Projeto de Ações Violentas e confiar em Tyler. 17

Meu chefe aparece na minha mesa com outra folha de papel e a encosta no meu cotovelo. Nunca mais usei gravata. Meu chefe está de gravata azul, então deve ser quinta-feira. A porta da sala do meu chefe fica sempre fechada agora, e não trocamos mais que duas palavras desde que ele encontrou as regras do clube da luta na copiadora e talvez depois de eu ter insinuado que ia arrancar as tripas dele com um tiro de espingarda. É claro que era só brincadeira. Ou então eu devesse ligar para o pessoal do Departamento de Entregas. Há uma braçadeira na montagem do banco da frente que nunca passou pelo teste de colisão antes de entrar em produção.

Se você souber para onde olhar, verá corpos enterrados por toda parte. Bom dia, digo.

Ele responde: bom dia.

Sobre o meu cotovelo há um outro documento ultra-secreto que Tyler pediu-me para digitar e copiar. Na semana passada, Tyler media com passos as dimensões do porão da casa da Paper Street. Tem 65 passos de fundo por 40 de largura. Tyler pensava em voz alta e me perguntou: — Quanto é seis vezes sete?

Quarenta e dois.

— E 42 vezes três?

Cento e vinte e seis.

Tyler me deu uma lista manuscrita e mandou que eu a digitasse e fizesse 72 cópias. Para que tantas?

— Porque é o número de caras que vai poder dormir no porão, se usarmos beliches de três camas — disse Tyler.

Eu perguntei: e para que isso?

Tyler disse:

— Eles só vão trazer o que estiver nesta lista e deve caber tudo embaixo do colchão.

A lista que meu chefe encontrou na copiadora, a copiadora ainda regulada para 72 cópias, a lista em que se lia:

'Trazer os itens exigidos não é garantia de admissão ao treinamento, mas os candidatos só serão aceitos se vierem equipados com os itens abaixo e quinhen- tos dólares em dinheiro para a sua cremação."

Custa pelo menos trezentos dólares para cremar o corpo de um indigente,

me disse Tyler, e o preço vai subir. Se você não tiver dinheiro quando morrer, seu corpo vai parar nas aulas de autópsia. Esse dinheiro deve ser levado no sapato do discípulo, e se o discípulo morrer, sua morte não será um peso para o Projeto de Ações Violentas. Além disso, o candidato deve trazer o que segue: Duas camisas pretas.

Duas calças pretas.

Um par de sapatos pretos reforçados.

Dois pares de meias pretas e duas cuecas pretas lisas. Um casaco preto pesado.

Isso inclui as roupas que o candidato está vestindo. Uma toalha branca.

Um saco de dormir.

Uma tigela de plástico branco.

Na minha mesa, com meu chefe ainda ali de pé, peguei a lista original e disse obrigado. Meu chefe vai para a sala dele, e eu começo a jogar paciência no meu computador.

Depois do trabalho, entrego as cópias a Tyler, e os dias se passam. Chego em casa.

Vou trabalhar.

Chego em casa e encontro um cara na varanda. O cara está ali parado com a segunda camisa e calça pretas dentro de um saco de papel, e deixou os últimos três itens, a toalha branca, o saco de dormir e a tigela de plástico sobre a grade da varanda. Da janela do primeiro andar, Tyler e eu o vemos, e Tyler me diz para mandá-lo embora.

— Ele é muito novo.

O cara no terraço é a carinha de anjo que eu quase destruí, quando Tyler inventou o Projeto de Ações Violentas. Apesar das manchas pretas ao redor dos olhos e do cabelo à escovinha, seu belo semblante não tem rugas nem cicatrizes. Ponha um vestido nele, faça-o sorrir e será uma mulher. O senhor anjo está parado diante da porta, olhos fixos à frente, braços caídos, sapatos pretos, camisa e meias pretas.

Livre-se dele, é jovem demais — me diz Tyler. Eu pergunto o que é ser muito jovem.

Não importa — diz Tyler. — Se o candidato for jovem, diremos que é muito jovem. Se for gordo, que é muito gordo. Se for velho, que é muito velho. Se for magro, que é muito magro. Se for branco, é muito branco. Se for preto, que é muito preto.

É assim que os candidatos são testados nos templos budistas há milhares e milhares de anos, diz Tyler. Você o manda embora, e se a vontade dele for tão forte que o faça esperar na porta sem comer sem dormir e sem convite por três dias, então ele pode entrar e começar o treinamento. Digo ao senhor anjo que ele é muito jovem, mas na hora do almoço ele continua ali. Depois do almoço, saio e expulso o senhor anjo com uma vassoura e

chuto o saco de papel no meio da rua. Lá de cima, Tyler me vê sacudir a vassoura

na orelha do garoto, chutar as coisas dele na valeta, e ele continua ali. Vá embora, grito. Não está ouvindo? Você é muito jovem. Não vai conseguir nunca, continuo gritando. Volte daqui a alguns anos e se inscreva de novo. Anda. Caia fora do meu terraço.

No dia seguinte, o cara ainda está lá. Tyler sai e diz: — Sinto muito. Tyler diz que sente muito por ter dito ao garoto sobre o treinamento, mas ele é muito jovem ainda, por favor, vá embora. O tira bonzinho e o tira durão.

Eu volto a gritar com o pobre garoto. Seis horas depois, Tyler sai outra vez e diz que sente muito, mas não, o garoto tem de ir. Tyler diz que vai chamar a polícia se ele não for embora.

E o garoto não vai.

As roupas dele continuam na valeta. O vento já levou embora o saco rasgado.

E o garoto não vai.

No terceiro dia, há outro na porta. O senhor anjo continua lá, e Tyler desce e diz ao senhor anjo:

— Entre. Tire as suas coisas da rua e entre. Para o cara que chegou depois, Tyler pede desculpas e diz que houve um engano. O novo cara é muito velho para treinar e, por favor, deve ir embora. Vou trabalhar todos os dias. Volto para casa e todos os dias encontro um ou dois caras esperando no terraço. Esses caras nem me olham. Fecho a porta e os deixo no terraço. Isso acontece já faz tempo, às vezes os candidatos desistem e vão embora, mas na maioria das vezes não arredam pé por três dias, e as 72 camas de campanha que Tyler e eu compramos e armamos no porão já estão ocupadas.

Um dia, Tyler me deu quinhentos dólares em dinheiro e disse para não tirá- los do sapato. Eram para a minha cremação. Isso é também um hábito dos antigos mosteiros budistas.

Agora, volto para casa do trabalho e encontro muitos estranhos que Tyler aceitou. Todos estão trabalhando. O primeiro andar da casa transformou-se em cozinha e fábrica de sabão. O banheiro nunca está vazio. Os grupos desaparecem por alguns dias e voltam trazendo uma banha aguada e fina em sacos vermelhos de borracha.

Uma noite, Tyler desce a escada, me encontra no quarto e diz: — Não os perturbe. Eles sabem o que fazer. Faz parte do Projeto de Ações Violentas. Ninguém conhece o plano todo, mas cada um é treinado para realizar ao menos uma tarefa com perfeição.

A regra no Projeto de Ações Violentas é confiar em Tyler. Tyler sai.

As turmas do Projeto de Ações Violentas derretem banha diariamente. Não estou dormindo. À noite ouço aquela gente misturando soda cáustica, cortando e cozinhando barras de sabão, embalando cada uma e fechando com a etiqueta da Fábrica de Sabão Paper Street. Todos menos eu parecem saber o que fazer, e Tyler nunca está em casa.

Abraço as paredes, como um rato encurralado numa engrenagem de homens

silenciosos com energia de macacos treinados, cozinhando, trabalhando e dormindo por turnos. Puxe a alavanca. Aperte o botão. Uma turma de macacos espaciais faz a comida enquanto outras turmas de macacos espaciais comem em tigelas de plástico branco.

Uma manhã estou saindo para trabalhar e encontro Big Bob no terraço de sapato preto, camisa e calça pretas. Pergunto: você esteve com Tyler? Tyler mandou você para cá?

— A primeira regra do Projeto de Ações Violentas — diz Big Bob, batendo os calcanhares e erguendo os ombros — é não fazer perguntas sobre o Projeto de Ações Violentas.

Que diabo de honraria insana Tyler teria atribuído a ele, me pergunto. Há uns caras cuja função é só cozinhar arroz o dia todo, lavar as tigelas e limpar privada. O dia inteiro. Tyler teria prometido a iluminação a Big Bob se passasse dezesseis horas por dia embalando barras de sabão? Big Bob não diz nada.

Vou trabalhar. Volto para casa e Big Bob ainda está no terraço. Não durmo a noite toda e, na manhã seguinte, Big Bob está lá fora, vigiando o jardim. Antes de sair, pergunto a Big Bob quem o deixou entrar. Quem passou essa tarefa a ele. Teria visto Tyler? Tyler esteve em casa ontem à noite? Big Bob diz:

— A primeira regra do Projeto de Ações Violentas é não falar... Eu o interrompo. Digo tá, tá, tá, tá, tá. Enquanto estou trabalhando, equipes de macacos espaciais reviram a grama molhada em volta da casa e misturam sal grosso na terra com esterco de gado recolhido em currais para baixar a acidez e sacos de cabelo cortado recolhido em barbearias para espantar toupeiras e camundongos e aumentar a proteína no solo. A qualquer hora da noite, os macacos espaciais chegam dos matadouros com sacos de farinha de sangue para aumentar o ferro e farinha de osso para aumentar o fósforo da terra.

As turmas de macacos espaciais plantam manjericão, tomilho e alface, broto de hamamélis, eucalipto, silindra e menta, formando um padrão caleidoscópico. Uma rosácea perfeita em todos os tons de verde. E outras turmas saem à noite para matar lesmas e caracóis à luz de vela. Uma turma de macacos espaciais colhe só as folhas perfeitas e as bagas de junípero para fazer tintura natural. Confrei porque é um desinfetante natural. Folhas de violeta porque curam dor de cabeça e aspérula porque dá ao sabão um aroma de grama cortada. Na cozinha há garrafas de vodca para fazer o sabão translúcido de gerânio rosa, sabão de açúcar mascavo e sabão de patchouli, e eu roubo uma garrafa e compro cigarros com o dinheiro da minha cremação. Marla aparece. Nós falamos de plantas. Marla e eu andamos pelos caminhos de cascalho por entre o caleidoscópio verde do jardim, bebendo e fumando. Falamos sobre os seios dela. Falamos de tudo menos de Tyler Durden.

Um dia deu no jornal que um bando de homens de preto invadiu um bairro fino e uma distribuidora de carros de luxo batendo tacos de beisebol nos pára- choques dianteiros para que os air bags explodissem e os alarmes disparassem.

Na fábrica de Sabão Paper Street, outras turmas colhiam pétalas de rosas,

de anêmonas ou lavanda e punham as flores dentro de caixas com um bolo do mais puro sebo para absorver o perfume e fazer sabão com aroma de flores. Marla me fala de plantas.

A rosa, diz, é um adstringente natural.

Algumas plantas têm nomes obituários: Íris Arruda, Margarida e Verbena. Outras, como a barba-de-bode e o beiço-de-negra, o cálamo e o nardo-da-índia, têm nomes das fadas de Shakespeare. Língua de veado com cheiro adocicado da baunilha. A hamamélis, outro adstringente natural. Caule de lírio, a selvagem íris espanhola. Todas as noites, Marla e eu caminhamos pelo jardim até eu ter certeza de que Tyler não voltará para casa. Atrás de nós há sempre um macaco espacial para recolher a folhinha de erva-cidreira ou de arruda ou de menta que Marla esmagou no meu nariz. Eu jogo fora a bituca de cigarro. O macaco espacial passa o ancinho atrás de nós para apagar nossas pegadas. Uma noite, num parque da cidade, um grupo de homens despejou gasolina em volta de cada árvore e entre uma árvore e outra, e criou um perfeito incêndio florestal em miniatura. Deu no jornal que as janelas das casas do outro lado da rua derreteram e os pneus dos carros estacionados explodiram. A casa de Tyler na Paper Street está viva, molhada do suor e respira ofegante com tanta gente. E tanta gente se mexendo lá dentro que a casa parece se mover.

Outra noite que Tyler não voltou para casa, alguém andou usando uma furadeira em caixas eletrônicos e telefones públicos e uma pistola de graxa para encher os furos das máquinas de banco dos telefones públicos com graxa de eixo de roda ou pudim de baunilha.

Tyler nunca estava em casa, mas um mês depois alguns macacos espaciais tinham o beijo de Tyler gravado nas costas da mão. Em seguida, esses macacos espaciais também desapareceram e outros vieram para substituí-los. E todos os dias, turmas de homens iam e vinham em carros diferentes. Nunca se via o mesmo carro duas vezes. Uma noite, ouvi Marla no terraço dizendo a um macaco espacial:

— Vim aqui para ver Tyler. Tyler Durden. Ele mora aqui. Sou amiga dele. O macaco espacial diz:

— Desculpe, mas você é muito... — ele pára — é muito jovem para treinar aqui.

Marla diz:

— Vá se foder.

— Além disso — continua o macaco espacial — você não trouxe os itens exigidos: duas camisas pretas, duas calças pretas... Marla grita:

— Tyler!

— Um par de sapatos pretos.

— Tyler!

— Dois pares de meias pretas e duas cuecas pretas lisas. — Tyler!

Ouço a porta da frente bater. Marla não espera os três dias.

Quase todo dia chego em casa depois do trabalho e faço um sanduíche com manteiga de amendoim. Chego em casa, e encontro um macaco espacial lendo para os macacos espaciais sentados pelo chão. — Você não é um floco de neve, bonito e único. É a matéria orgânica em decomposição como todo mundo e todos fazemos parte da mesma composteira. O macaco espacial continua:

— A nossa cultura nos tornou todos iguais. Ninguém é mais branco, mais preto ou mais rico. Todos queremos a mesma coisa. Individualmente, não somos nada.

O leitor pára quando entro para fazer o sanduíche, e os macacos espaciais permanecem em silêncio como se eu estivesse sozinho. Eu digo: não se incomodem comigo. Eu já li isso. Fiquem à vontade. Os macacos espaciais esperam eu fazer o meu sanduíche, pegar outra garrafa de vodca e subir a escada. Atrás de mim, ouço: — Você não é um floco de neve, bonito e exclusivo. Sou o Coração Partido de Joe porque Tyler me abandonou. Porque meu pai me abandonou. Ah, eu poderia continuar infinitamente.

Algumas noites depois do trabalho vou a um clube da luta em algum porão, alguma garagem ou algum bar e pergunto se alguém viu Tyler Durden. A cada novo clube da luta que entro, há alguém que eu nunca vi sob a única lâmpada, rodeado por homens e lendo as palavras de Tyler. A primeira regra do clube da luta é não falar sobre o clube da luta. Quando as lutas começam, puxo o líder do clube de lado e pergunto se viu Tyler. Eu moro com Tyler, digo, e já faz um tempo que não o vejo. O cara arregala os olhos e pergunta se eu realmente conheço Tyler Durden. Isso acontece em quase todos os novos clubes da luta. Sim, digo, sou o melhor amigo de Tyler. Então, de repente, todo mundo quer apertar minha mão. Esses novos caras olham o buraco em meu rosto e os hematomas escuros com as bordas amarelas e esverdeadas e me chamam de senhor. Não senhor. Nem tanto, senhor. Eles não conhecem ninguém que já tenha visto Tyler Durden. Amigos de amigos conheceram Tyler Durden e fundaram esta sede do clube da luta, senhor.

Depois me ignoram.

Ninguém que eles conheçam já viu Tyler Durden. Senhor.

É verdade, me perguntam? Que Tyler Durden está formando um exército? Pode ser. É verdade que Tyler Durden só dorme uma hora por noite? Dizem que Tyler está inaugurando clubes da luta por todo o país. O que vai acontecer depois, eles querem saber.

As reuniões do Projeto de Ações Violentas mudaram para porões maiores porque cada comitê — o de Ataque, de Maldades e de Informações Falsas — aumenta à medida que mais gente se forma no clube da luta. Cada comitê tem um líder e nem os líderes sabem onde Tyler está. Tyler fala com eles semanalmente por telefone.

Todo mundo do Projeto de Ações Violentas quer saber o que vai acontecer

depois.

Para onde estamos indo?

O que estamos procurando?

Na Paper Street, Marla e eu passeamos descalços pelo jardim à noite, nossos passos roçam no perfume da artemísia, do limão verbena, do gerânio rosa. Camisas e calças pretas passam por nós com velas, erguendo as folhas das plantas para matar uma lesma ou um caracol. Marla pergunta o que está acontecendo aqui.

Tufos de cabelo brotam em torrões de terra. Cabelo e bosta. Farinha de osso e farinha de sangue. As plantas estão crescendo mais rápido do que os macacos espaciais estão dando conta.

Marla pergunta:

— O que você vai fazer?

O que dizer?

Na terra há um pontinho dourado brilhando e eu me ajoelho para ver o que é. Não sei o que vai acontecer, digo a Marla. Pelo rabo do olho vejo macacos espaciais rondando, cada um com a sua vela. O pontinho dourado na terra é um dente com obturação de ouro. Perto dele há dois molares com amálgama prateada. É um maxilar. Eu digo, não, não sei dizer o que vai acontecer. E empurro o primeiro, o segundo e o terceiro molares para dentro da terra e o cabelo e a bosta e o osso e o sangue, para que Marla não os veja.

18

É sexta-feira à noite, e acabei dormindo na minha mesa de trabalho. Acordo com a cabeça deitada sobre os braços cruzados, quando o telefone toca e não há mais ninguém por perto. O telefone toca em meu sonho, e não sei se a realidade entrou em meu sonho ou se o sonho respingou na realidade. Atendo o telefone, Indenizações e Débitos. Esse é o meu departamento. Indenizações e Débitos. O sol se põe no horizonte e gordas nuvens cinzentas, grandes como o Wyoming e o Japão estão se formando lá fora. Não é propriamente uma janela que eu tenho no trabalho. As paredes externas são todas de vidro, do teto ao chão. Tudo em meu trabalho é de vidro, do teto ao chão. Tudo é persiana vertical. Tudo é carpete cinza de pêlo baixo pontilhado com pequeninas lajes tumulares onde os PCs se ligam à rede. Tudo é um labirinto de cubículos de madeira compensada.

Há um aspirador de pó zumbindo em algum lugar. Meu chefe está em férias. Ele mandou um e-mail e desapareceu. Devo me preparar para uma inspeção formal em duas semanas. Reserve uma sala de conferência. Organize minhas coisas. Atualize meu sumário. Esse tipo de coisa. Eles estão montando um processo contra mim. Sou a Total Ausência de Surpresa de Joe. Tenho me comportado terrivelmente mal.

Atendo o telefone, é Tyler dizendo:

— Saia, há uns caras esperando por você no estacionamento. Pergunto, quem são eles?

Sinto cheiro de gasolina nas mãos.

Tyler continua:

— Vá para a rua. Eles estão de carro. É um Cadillac. Ainda estou meio dormindo.

Não tenho certeza se Tyler faz parte do sonho. Ou se sou um sonho de Tyler.

Minha mão cheira a gasolina. Não há mais ninguém por perto, eu me levanto e vou para o estacionamento.

Um cara do clube da luta que trabalha com carros está parado no meio-fio em um Corniche preto que não deve ser dele, fico olhando para o carro, todo preto e dourado, um imenso maço de cigarros que vai me levar a algum lugar. O mecânico sai do carro e diz para eu não me preocupar, as placas foram trocadas no estacionamento do aeroporto.

Nosso mecânico do clube da luta diz que pode fazer qualquer coisa funcionar. Dois fios saem da coluna da direção. Encoste um fio no outro, com- plete o circuito da partida e saia para um passeio perigoso. Ou isso ou você pode copiar o código da chave no revendedor. Três macacos espaciais estão no banco de trás, de camisa e calça pretas. Nada vejo, nada ouço, nada falo.

Pergunto: onde está Tyler?

O mecânico do clube da luta está bancando o chauffeur de Cadillac conversível para mim. Ele é alto, ossos salientes, ombros que lembram a barra transversal de um poste telefônico.

Pergunto: vamos encontrar com Tyler?

No banco da frente há um bolo de aniversário com velinhas esperando para serem acesas. Eu entro. O carro sai andando. Uma semana depois do clube da luta, você ainda dirige no limite de velocidade sem nenhum problema. Talvez esteja passando o inferno com os ferimentos internos há uns dois dias, mas nunca esteve tão calmo. Os carros passam por você. Grudam no seu pára-choque. Os motoristas erguem um dedo para você. Gente completamente estranha que o odeia. Não é nada pessoal. Depois do clube da luta, você fica tão relaxado que tanto faz. Nem lembra de ligar o rádio. Talvez sinta uma pontada nas costelas ao inspirar por causa de uma fratura da grossura de um fio de cabelo. Os carros atrás piscam os faróis. O sol se põe, laranja e dourado.

O mecânico continua dirigindo. Há um bolo de aniversário entre nós dois, no banco da frente.

Dá até medo ver esses caras como o nosso mecânico no clube da luta. São uns caras magros, que nunca desistem. Lutam até ficarem moídos. Brancos tatuados como esqueletos mergulhados em cera amarela, negros como carne seca, esses caras sempre lutam juntos, como os Narcóticos Anônimos. Jamais dizem pára. São energia pura, recuperam-se rápido de qualquer coisa. É como se a única coisa que lhes resta é morrer, e eles querem morrer lutando.

Esses caras têm de lutar entre si.

Ninguém se inscreve para lutar com eles, e eles não podem escolher ninguém para lutar senão outro magrelo, só ossos e ímpeto, porque ninguém quer lutar com eles.

Os que assistem nem gritam quando caras como o nosso mecânico se enfrentam.

Só se ouvem os lutadores expelindo o ar por entre os dentes, as mãos tentando se segurar em alguma coisa, o impacto dos punhos socando as costelas, um gancho direto. Você vê saltar os tendões e os músculos e as veias sob a pele desses caras. A pele brilhante, suada, encordoada e molhada sob a única lâmpada. Dez, quinze minutos voam. Eles exalam um cheiro, eles suam e exalam um cheiro que faz lembrar galinha frita.

Vinte minutos do clube da luta passam voando. Até que um deles caia. Depois da luta, os dois caras ficam juntos pelo resto da noite, como que drogados, exaustos, sorrindo.

Desde o clube da luta, este mecânico vive rondando a casa da Paper Street. Quer que eu ouça a música que ele compôs. Quer que eu veja a gaiola que ele construiu. O cara me mostrou a foto de uma garota e perguntou se eu a achava bonita para casar.

Sentado no banco da frente do Corniche, o cara pergunta: — Viu o bolo que fiz para você? Fui eu quem fiz. Não é meu aniversário. — Tá escapando um pouco de óleo pelos anéis — diz o mecânico —, mas troquei o óleo e o filtro de ar. Chequei válvulas e distribuidor. Como parece que vai chover esta noite, troquei também a borracha dos limpadores de pára-brisa. Pergunto o que Tyler está planejando.

O mecânico abre o cinzeiro e tira o acendedor de cigarro. Ele pergunta: — Isso é um teste? Você está testando a gente? Onde Tyler está? — A primeira regra do clube da luta é não falar do clube da luta — diz o mecânico. — E a última regra do Projeto de Ações Violentas é não fazer per- guntas.

Então o que é possível dizer? Ele diz:

— O que você tem de entender é que seu pai foi o modelo que Deus usou para fazer você.

Atrás de nós, meu emprego e minha sala vão ficando menores, menores, menores, e desaparecem. Sinto cheiro de gasolina nas mãos. O mecânico diz: — Se você é macho, é cristão e mora nos Estados Unidos, seu pai é o seu modelo de Deus. Se você não conhece seu pai, se ele sumiu ou morreu ou se nunca estava em casa, você acredita em Deus? Esse é o dogma de Tyler Durden. Rabiscado num pedaço de papel enquanto eu dormia e entregue a mim para que eu digitasse e tirasse cópias no trabalho. Já li tudo isso. Até meu chefe deve ter lido. — E o que você acaba fazendo — diz o mecânico é passar a vida procurando pelo pai e por Deus.

— Pense na possibilidade de Deus não gostar de você. É possível que Deus odeie a gente. Não é a pior coisa que pode acontecer — continua ele. Para Tyler, é melhor chamar a atenção de Deus por ser mau do que não ter

nenhuma atenção por ser bom. Talvez o ódio de Deus seja melhor que a sua

indiferença.

Se você pudesse ser o pior inimigo de Deus ou não ser nada, o que escolheria?

Somos os filhos do meio de Deus, segundo Tyler Durden, e não temos um lugar na história nem merecemos atenção especial. Se não conseguirmos chamar a atenção de Deus, não teremos a menor chance de condenação ou de redenção. O que é pior, o inferno ou nada? Só se formos pegos e punidos poderemos ser salvos. — Pôr fogo no Louvre — diz o mecânico — e limpar a bunda com a Mona Lisa. Pelo menos assim Deus vai saber qual é o nome da gente.

Quanto mais você cair, mais alto vai voar. Quanto mais longe for, mais Deus vai querer você de volta.

— Se o filho pródigo nunca tivesse saído de casa — diz o mecânico —, o novilho do banquete ainda estaria vivo.

Não basta contar os grãos de areia na praia ou as estrelas no céu. O mecânico entra com o Corniche preto numa estrada secundária sem acostamento e uma fila de caminhões logo se forma atrás de nós, todos no limite de velocidade permitido. O Corniche é preenchido pelas luzes dos faróis atrás de nós, e aqui estamos nós, conversando, refletidos no vidro do pára-brisa. Guiando no limite de velocidade. Como a lei determina. Lei é lei, diria Tyler. Dirigir em alta velocidade que é igual a atear fogo que é igual a plantar uma bomba que é igual a atirar em alguém. Um crime é um crime é um crime.

— Na semana passada, a gente podia ter enchido mais quatro clubes da luta — diz o mecânico.

Talvez Big Bob queira cuidar do próximo se a gente encontrar um bar. Então na semana que vem ele passará as regras para Big Bob e dará um clube da luta para ele.

De agora em diante, quando um líder inaugura um clube da luta, todo mundo esperando em volta da lâmpada, o líder anda em volta do círculo de pessoas, no escuro.

Eu pergunto: quem fez as novas regras? Foi Tyler? O mecânico sorri e diz:

— Você sabe quem faz as regras.

A nova regra é que ninguém mais fica no centro do clube da luta, diz ele. Ninguém é o centro do clube da luta senão os dois homens que estão lutando. Ouve-se a voz do líder gritando, andando por fora do círculo de pessoas, no escuro. Os homens que estão assistindo vão ficar de frente para os outros homens do outro lado do círculo.

É assim que vai ser em todos os clubes da luta. Encontrar um bar ou uma garagem para abrigar o novo clube da luta não é difícil; o primeiro bar, aquele onde o clube da luta original se reúne, consegue pagar o aluguel só com dinheiro arrecadado num único sábado de clube da luta. Pelo que disse o mecânico, a nova regra do clube da luta é que o clube da luta será sempre gratuito. Nunca vai custar nada para entrar. O mecânico põe a

cabeça para fora da janela e grita para o tráfego e o vento noturno que passa pela

lateral do carro.

— Nós queremos você, não o seu dinheiro. O mecânico grita pela janela:

— Se você estiver no clube da luta, tanto faz o dinheiro que tenha no banco. Você não é o que faz para viver. Você não é a sua família e não é quem pensa que é.

O mecânico grita para o alto:

— Você não é o seu nome.

Um macaco espacial sentado no banco de trás emenda: — Você não é os seus problemas.

O mecânico grita:

— Você não é os seus problemas.

Outro macaco espacial diz:

— Você não é a idade que tem.

Neste ponto, o mecânico dá uma guinada na direção e sai para o acostamento e a luz dos faróis entra pelo pára-brisa com a frieza de uma punhalada. Um carro e depois outro passam buzinando, e o mecânico desvia dos dois a tempo.

Os faróis nos atingem, cada vez mais fortes, as buzinas tocam, e o mecânico estica o pescoço para o clarão, o barulho e os gritos: — Você não é suas esperanças.

Ninguém ouve nada.

Desta vez, um carro desvia bem na nossa frente e estamos salvos. Outro carro se aproxima, faróis piscando, alto, baixo, alto, baixo, buzina berrando, e o mecânico grita:

— Vocês não se salvarão.

O mecânico não desvia, mas o outro carro sim. Outro carro, e o mecânico grita:

— Vamos todos morrer um dia.

Desta vez, o carro desvia, mas o mecânico vai para cima dele. O carro consegue sair de lado e pára mais à frente, outra vez. Nessa hora, você acha que vai morrer. Porque nesse momento nada importa. Olha para as estrelas e desaparece. Nem sua bagagem. Nada importa. Nem a sua dificuldade de respirar. Está escuro la fora e as buzinas tocam ao redor. Os faróis piscam na sua cara e você nunca mais terá de ir trabalhar. Nunca mais terá de cortar o cabelo.

— Rápido — diz o mecânico.

O carro desvia de novo, e o mecânico desvia junto. — O que você gostaria de fazer antes de morrer? — pergunta o mecânico. Um carro se aproxima buzinando, mas o mecânico, com toda a calma, vira- se para mim e diz:

— Dez segundos para o impacto.

— Nove.

— Em oito.

— Sete.

— Em seis.

Meu emprego. Gostaria de abandonar meu emprego, digo. A buzina continua tocando quando o carro passa e o mecânico vai em frente.

Outras luzes se aproximam, e o mecânico vira-se para os três macacos no banco de trás.

— Ei, macacos espaciais — diz —, viram só como é? Ou confessa ou morre.

Um carro nos ultrapassa pela direita com um adesivo no pára-choque em que se lê: "Dirijo Melhor Quando Bebo". Deu nos jornais que milhares de adesivos como esse apareceram nos carros de um dia para o outro. "Motoristas Bêbados contra as Mães." "Recicle os Animais."

Lendo o jornal, logo vi que o Comitê de Informações Falsas era responsável por aquilo. Ou então o Comitê de Maldades. Sentado ao meu lado, o nosso limpo e sóbrio mecânico do clube da luta me diz, é, o adesivo do Bêbado faz parte do Projeto de Ações Violentas. Os três macacos espaciais estão quietos no banco de trás. O Comitê de Maldades está imprimindo cartões de companhias aéreas que mostram os passageiros brigando por uma máscara de oxigênio enquanto o jato despenca em direção às rochas a milhares de quilômetros por hora. Os Comitês de Maldades e Informações Falsas estão disputando quem vai desenvolver primeiro um vírus de computador que fará os caixas automáticos de banco vomitar um turbilhão de notas de dez e vinte dólares. O acendedor de cigarro salta no cinzeiro, e o mecânico me diz para acender as velas do bolo de aniversário.

Acendo as velas, e o bolo bruxuleia envolvido num pequeno halo de fogo. — O que você gostaria de fazer antes de morrer? — pergunta o mecânico e desvia o carro de um caminhão que se aproxima na nossa frente. O caminhão aperta a buzina de ar, primeiro um toque longo, depois outro, e os faróis do caminhão, como o sol nascendo no horizonte, brilham cada vez mais fortes e iluminam o sorriso do mecânico.

— Façam logo o seu pedido — diz ele pelo espelho retrovisor para os três macacos no banco de trás. — Estamos a cinco segundos da morte. — Um — diz ele.

— Dois.

O caminhão está bem na nossa frente, rugindo. — Três.

— Montar a cavalo — diz uma voz no banco de trás. — Construir uma casa — diz a outra voz.

— Fazer uma tatuagem.

O mecânico diz:

— Creiam em mim e morrerão para sempre. Tarde demais, o caminhão sai de lado, o mecânico gira a direção, mas a traseira do nosso Corniche rabo-de- peixe bate na ponta do pára-choque dianteiro do caminhão. Na hora eu não sabia disso, mas sabia das luzes, as luzes do caminhão

piscando na escuridão, e sou jogado primeiro contra a porta do passageiro, depois

em cima do bolo de aniversário e do mecânico, que está atrás do volante. O mecânico segura firme o volante e o bolo de aniversário está apagado. Um segundo depois está tudo escuro no interior de couro preto do carro e nossos gritos têm o mesmo tom grave, o mesmo gemido baixo da buzina de ar do caminhão, e não temos nenhum controle, nenhuma escolha, nenhuma direção, não temos escapatória e estamos mortos.

Meu desejo neste momento é morrer. Não sou nada neste mundo comparado a Tyler.

Perdi as esperanças.

Sou um estúpido, só o que faço é querer as coisas e precisar delas. Minha vidinha. Meu trabalhinho de merda. Minha mobília sueca. Eu nunca, nunca disse isso a ninguém, mas antes de conhecer Tyler, estava querendo com- prar um cachorro e pôr o nome de "Entourage". É até onde a vida consegue chegar.

Mate-me.

Seguro na direção e ponho o carro outra vez na estrada. Agora.

Preparar para evacuar a alma.

Agora.

O mecânico gira o volante em direção à valeta, e eu me volto para a droga de morte.

Já. O incrível milagre da morte: num instante você está andando e conversando, no outro não passa de um objeto. Não sou nada, sou menos que isso.

Frio.

Invisível.

Sinto cheiro de couro. Meu cinto de segurança enrola-se como camisa-de- força em torno de mim, e quando tento me sentar, bato a cabeça no volante. Dói mais do que deveria. Minha cabeça está no colo do mecânico, eu ergo os olhos, vejo o rosto do mecânico bem em cima de mim, sorrindo, dirigindo, e vejo as estrelas passando pela janela do motorista. Minhas mãos e meu rosto estão melados com alguma coisa. Sangue?

Cobertura de bolo.

O mecânico olha para baixo:

— Feliz aniversário.

Sinto cheiro de fumaça e me lembro do bolo de aniversário. — Você quase quebrou o volante com a sua cabeça — diz ele. Não foi nada, foi só o frescor da noite, o cheiro de fumaça, as estrelas e o mecânico sorrindo e dirigindo, minha cabeça no colo dele; de repente não sinto nenhuma vontade de me sentar.

Onde está o bolo?

O mecânico diz:

— No chão.

São só o frescor da noite e um cheiro de fumaça mais forte.

Eu já fiz o meu pedido?

Bem em cima de mim, contornado pelas estrelas, um rosto sorridente. — Essas velas de aniversário são daquelas que não se apagam — diz ele. À luz das estrelas, meus olhos se ajustam e vejo fumaça saindo de pequenas chamas, no tapete do carro.

19

O mecânico do clube da luta está parado na bomba de gasolina, com um ar gozador atrás do volante, e ainda temos uma coisa importante para fazer esta noite.

Uma coisa que tenho de aprender antes que a civilização chegue ao fim é olhar para as estrelas e saber para onde estou indo. Está tudo quieto, é como dirigir um Cadillac no espaço sideral. Devemos estar longe da estrada. Os três sujeitos no banco de trás ou estão mortos ou dormindo. — Tivemos uma experiência de quase morte — diz o mecânico. Ele tira a mão do volante e toca o vergão em minha testa, provocado pela pancada que dei no volante. Minha testa inchou e meus olhos estão fechados, e ele passa o dedo frio pela extensão do ferimento. O Corniche dá um solavanco e a dor parece encobrir meus olhos como a sombra da aba de um boné. As molas retorcidas e o pára-choque traseiro gemem e rangem no silêncio da noite. O mecânico diz que o pára-choque traseiro do Corniche está pendurado por ligamentos e foi quase arrancado quando enganchou na ponta do pára-choque dianteiro do caminhão.

Eu pergunto: esta noite fez parte da nossa tarefa no Projeto de Ações Violentas?

— Em parte — diz ele. — Eu tinha de fazer quatro sacrifícios humanos, e tenho de pegar um carregamento de banha. Banha?

— Para o sabão.

O que Tyler está planejando? O mecânico começa a falar, mas é puro Tyler Durden.

— Vejo os homens mais fortes e mais inteligentes que jamais existiram — diz ele, o rosto delineado pelas estrelas na janela do motorista —, homens que estão bombeando gasolina nas salas de espera. A inclinação da testa, as sobrancelhas, a linha do nariz, os cílios, a curva dos olhos, o contorno plástico da boca, o jeito de falar, tudo é delineado pelas estrelas.

— Se pudéssemos colocar esses homens num campo de treinamento e terminar de educá-los.

— O que a arma faz é direcionar a explosão. — Você tem uma classe de mulheres e homens jovens e fortes que estão dispostos a dar a vida por alguma coisa. A publicidade persegue essa gente com carros e roupas desnecessários. As gerações vêm trabalhando em empregos que odeiam, comprando o que não têm a menor necessidade.

— Nossa geração não viveu uma grande guerra ou uma grande depressão,

mas nós sim, nós vivemos uma grande guerra espiritual. Uma grande revolução contra a cultura. A grande depressão é a nossa vida. Nossa depressão é espiritual. — Temos de mostrar a esses homens e a essas mulheres o que é a liberdade escravizando-os, mostrar o que é a coragem amedrontando-os. — Napoleão gabava-se de que seus homens eram capazes de sacrificar a própria vida por um pedaço de fita.

— Imagine se decretássemos greve e todos se recusassem a trabalhar até que toda a riqueza do mundo fosse redistribuída. — Imagine caçar um alce nas florestas úmidas do cânion em torno das ruínas do Rockefeller Center.

— Aquilo que você disse sobre o seu trabalho era sério? — pergunta o mecânico.

É, era sério.

— É por isso que você não está na rua esta noite — diz ele. Somos um batalhão de caça e estamos caçando banha. Estamos indo para o depósito de lixo hospitalar. Estamos indo para o incinerador do lixo hospitalar, e lá, entre lençóis cirúrgicos descartáveis e curativos, tumores com dez anos de idade e tubos intravenosos e agulhas descartáveis, coisas assustadoras, assustadoras mesmo, entre amostras de sangue e pedaços amputados, vamos encontrar mais dinheiro do que poderíamos carregar em uma noite, mesmo que estivéssemos num caminhão basculante.

Tem dinheiro de sobra para lotar este Corniche até o eixo de suspensão. — Banha — diz o mecânico —, banha lipoaspirada, sugada das coxas mais ricas da América. As coxas mais ricas e gordas do mundo. Nossa meta são os grandes sacos vermelhos de banha lipoaspirada que vamos levar para Paper Street e derreter e misturar com soda cáustica e alecrim e revender a essas mesmas pessoas que pagaram para aspirá-la. A vinte paus a barra, são os únicos que podem pagar.

— A banha mais rica e cremosa do mundo, a gordura da terra — diz ele. — Isso faz desta noite uma coisa Robin Hoodiana. Pequenos focos de cera respingam no tapete. — Enquanto estivermos lá, vamos ter de procurar também uns vírus de hepatite — diz ele.

20

As lágrimas começam a aparecer agora, e um fiapo de banha se enrola no cano do revólver, faz a volta na alça do gatilho e espalha gordura no meu dedo indicador. Raymond Hessel fechou os olhos quando pressionei o cano da arma em sua testa para que ele sentisse a arma, eu estava do lado dele, era a vida dele e ele podia morrer a qualquer momento.

Não era um revólver barato, e eu me perguntei se o sal não ia estragá-lo. Tudo foi tão rápido, pensei. Fiz tudo o que o mecânico mandou fazer. Por

isso tive de comprar um revólver. Essa foi a minha lição de casa.

Cada um tinha de trazer para Tyler doze carteiras de habilitação. Isso era a prova de que cada um fizera doze sacrifícios humanos. Nesta noite, estaciono o carro e fico por ali esperando que Raymond Hessel termine seu turno da noite na Korner Mart, e lá pela meia-noite ele está espe- rando o ônibus noturno quando eu surjo e digo, alô. Raymond Hessel não diz nada. Deve ter pensado que eu queria o dinheiro dele, quase nada, os catorze dólares que ele tinha na carteira. Oh, Raymond Hessel, com todos os seus 23 anos de idade, quando você começou a chorar, as lágrimas rolando pelo cano da minha arma encostada na sua fronte, não, isso não tem nada que ver com dinheiro. Nem tudo tem que ver com dinheiro. Você nem me cumprimentou.

Você não é essa sua patética carteirinha. Eu disse: bonita noite, fria mas limpa.

Você nem me disse oi.

Eu disse: não corra ou vou atirar nas suas costas. Eu apontava a arma e usava uma luva cirúrgica, porque se a arma viesse a se tornar a prova A, não haveria nada nela senão as lágrimas secas de Raymond Hessel, caucasiano, 23 anos, sem marcas de identificação.

Então eu chamei a atenção dele. Tinha olhos tão grandes que mesmo sob a luz da rua via-se que eram verdes.

Você foi se inclinando para trás com a arma encostada em seu rosto, como se o cano estivesse ou muito quente ou muito frio. Até eu dizer pare, então você deixou a arma encostar, mas mesmo assim conseguiu desviar a cabeça do cano. Você me deu a sua carteira como eu pedi. Seu nome era Raymond K. Hessel na carteira de habilitação. Morava na 1320 SE Benning, apartamento A. Devia ser um apartamento no porão. Ge- ralmente eles recebem letras em vez de números. Raymond K. K. K. K. K. K. Hessel, eu estou falando com você. Você tentou desviar a cabeça da arma e disse sim. Você disse que morava no subsolo.

Tinha também algumas fotos na carteira. Era a sua mãe. Não era fácil ter de abrir os olhos e ver a foto da mamãe e do papai sorrindo e ao mesmo tempo ver a arma, então você fechou os olhos e começou a chorar. Você ia morrer, o fantástico milagre da morte. Num momento é uma pessoa, no momento seguinte é um objeto, e mamãe e papai vão ter de chamar um velho médico qualquer e olhar sua ficha dentária porque não vai sobrar muita coisa do seu rosto, e mamãe e papai esperavam tanta coisa de você, não, a vida não era justa, e agora acontecia isso.

Catorze dólares.

Esta, pergunto, esta é a sua mãe?

É. Você chorava, soluçava e chorava. Você engoliu. É. Você tinha um cartão da biblioteca. Tinha um cartão da locadora de vídeo. Um cartão do seguro social. Catorze dólares em dinheiro. Eu quis pegar os passes de ônibus, mas o mecânico disse para tirar só a carteira de habilitação. Uma carteira vencida da comunidade de estudantes universitários.

Você estudava alguma coisa.

Neste momento, você ameaçou uma crise de choro, então eu pressionei mais o revólver no seu rosto, e você começou a se afastar até eu dizer pare ou morre agora mesmo. Então, o que você estudou? Onde?

Na faculdade, eu disse. Você tem carteira de estudante. Ah, você não sabia, soluça, engole, funga, qualquer coisa, biologia. Ouça bem, você vai morrer, Raymond K. K. K. Hessel, agora. Pode ser em um segundo ou em uma hora, você decide. Então minta para mim. Fale a primeira coisa que passar pela sua cabeça. Realize alguma coisa. Não estou ligando a mínima. Sou eu que estou com a arma. Finalmente você me ouviu e saiu da pequena tragédia que imaginava na sua cabeça.

Preencha os espaços. O que Raymond Hessel quer ser quando crescer? Ir para casa, você disse que só queria ir para casa, por favor. Besteira, eu disse. E então, como gostaria de viver? Se pudesse fazer qualquer coisa.

Realizar alguma coisa.

Você não sabia.

Então você já está morto, disse. Agora vire a cabeça. A morte vai começar em dez, em nove, em oito. Veterinário, você disse. Você queria ser veterinário. Isso envolve os animais. Você tem de ir para a escola para isso. Envolve muita escola, você disse.

Você poderia estar na escola rachando de estudar, Raymond Hessel, ou estar morto. Você escolheu. Enfiei sua carteira no bolso de trás da sua calça. Então você resolveu ser médico de animais. Tiro a boca da arma de um lado do rosto e pressiono o outro. É isso o que você sempre quis ser, dr. Raymond K. K. K. K. Hessel, um veterinário?

É.

Sem brincadeira?

Não. Não, você corrigiu, sim, sem brincadeira. Sim. Okay, eu disse, e pressionei a ponta úmida do cano na ponta do seu queixo, depois na ponta do seu nariz, e em todo lugar que encostei a boca do cano deixei um anel molhado das suas lágrimas.

Então, eu disse, volte para a escola. Se você acordar amanhã cedo, dê um jeito de voltar para a escola.

Encostei a boca do cano molhada em cada lado do rosto, depois no seu queixo, e então na sua testa e deixei a marca do cano nela. Você poderia estar morto agora, eu disse.

Vou pegar só a sua carteira de habilitação. Sei quem você é. Sei onde mora. Vou ficar com a sua carteira e vou checar as informações a seu respeito, senhor Raymond K. Hessel. Daqui a três meses, depois daqui a seis meses, depois daqui a um ano, e se você não voltou para a escola para ser um veterinário, será um homem morto. Você não disse nada.

Se manda daqui e vai cuidar dessa sua vidinha, mas não esqueça que estou

de olho em você, Raymond Hessel, e prefiro matar você a vê-lo trabalhando num emprego de merda só para ter dinheiro para comprar queijo e assistir a televisão. Agora, vou embora e não se vire.

Isso é o que Tyler quer que eu faça.

Essas são as palavras de Tyler saindo pela minha boca. Sou a boca de Tyler.

Sou as mãos de Tyler.

Todo mundo no Projeto de Ações Violentas é parte de Tyler Durden, e vice-versa.

Raymond K. K. Hessel, você vai jantar melhor que qualquer outra refeição que já tenha feito e amanhã terá o dia mais bonito de toda a sua vida. 21

Você acorda no Sky Harbor International. Atrasa o relógio duas horas.

O ônibus me leva para o centro de Phoenix, e em todo bar que entro encontro caras com pontos ao redor do olho, onde uma pancada violenta compri- miu a carne do rosto. Tem gente com o nariz torto, os caras vêem o buraco na minha cara e imediatamente somos uma família. Tyler não aparece em casa já faz tempo. Continuo fazendo meu servicinho. Vou de aeroporto em aeroporto ver os carros que mataram as pessoas. A magia da viagem. Vidinhas. Sabõezinhos. Poltroninhas de linhas aéreas. Em todo lugar que passo pergunto por Tyler. Caso o encontre, as carteiras de habilitação dos meus doze sacrifícios humanos estão no bolso.

Em todo bar que entro, em toda droga de bar, vejo caras arrebentados. Em todos os bares, eles me abraçam e querem me pagar uma cerveja. Como se eu já soubesse quais são os bares do clube da luta. Pergunto: vocês viram um sujeito chamado Tyler Durden? É besteira perguntar se eles conhecem o clube da luta. A primeira regra é não falar do clube da luta. Mas teriam visto Tyler Durden?

Eles dizem: nunca ouvimos falar, senhor. Mas talvez o encontre em Chicago, senhor. Deve ser pelo buraco no meu rosto que me tratam por senhor. E dão uma piscada.

Você acorda no O'Hare e toma o ônibus para Chicago. Adianta o relógio uma hora.

Se a gente pudesse acordar num lugar diferente. Se pudesse acordar como uma pessoa diferente. Por que não se pode acordar como uma pessoa diferente? Em todo bar que você entra, os caras arrebentados querem lhe pagar uma cerveja.

Não, senhor, ninguém conhece Tyler Durden.

E dão uma piscada.

Nunca ouviram esse nome, senhor.

Pergunto do clube da luta. Tem clube da luta por aqui, esta noite? Não, senhor.

A segunda regra do clube da luta é não falar do clube da luta. Os caras machucados balançam a cabeça.

Nunca ouviram falar. Senhor. Mas o senhor vai encontrar esse clube da luta em Seattle.

Você acorda no Meigs Field e liga para Marla, pergunta o que está acontecendo em Paper Street. Marla diz que agora os macacos espaciais estão raspando a cabeça. Os cortadores elétricos chegam a ficar quentes e a casa cheira a cabelo queimado. Os macacos espaciais usam soda cáustica para apagar as impressões digitais.

Você acorda em SeaTac.

Atrasa o relógio duas horas.

O ônibus leva você para o centro de Seattle, e no primeiro bar em que você entra, o barman está usando um colar cervical que empurra tanto a cabeça para trás que ele tem de olhar por cima do nariz de berinjela para sorrir. O bar está vazio, e o barman diz: — Que bom que tenha voltado, senhor.

Eu nunca estive naquele bar, nunca na minha vida. Pergunto se ele já ouviu o nome Tyler Durden. O barman sorri com o queixo apoiado sobre o colar cervical e pergunta: — Isto é um teste?

É, digo, é um teste. Conhece Tyler Durden? — O senhor esteve aqui a semana passada, sr. Durden — diz ele. — Não se lembra?

Tyler esteve lá.

— O senhor veio aqui.

Eu nunca estive aqui antes.

— Como quiser, senhor — diz o barman—, mas na noite de quinta-feira o senhor veio e perguntou quando a polícia ia fechar as nossas portas. Na quinta-feira passada, tive insônia e passei a noite acordado, sem saber se estava acordado ou dormindo. Eu acordei tarde no dia seguinte, com os ossos moídos, como se não tivesse fechado os olhos por um só minuto. — Sim, senhor — diz o barman. — Na quinta-feira o senhor estava exatamente aí onde está agora e me perguntou da batida policial, e quis saber quantos caras teríamos de recusar no clube da luta de quarta-feira. O barman torce os ombros e o colar cervical para olhar o bar vazio e diz: — Não há ninguém aqui para ouvir, sr. Durden. Nós tivemos de dispensar vinte e sete ontem à noite. Isto fica sempre vazio quando tem clube da luta. Em todos os bares onde entrei esta semana, todos me trataram por senhor. Em todos os bares em que entro, os caras machucados do clube da luta começam a ficar parecidos entre si. Como um estranho pode saber quem eu sou? — O senhor tem a marca de nascença, sr. Durden — diz o barman. No seu

pé. Tem a forma de uma Austrália vermelha ao lado da Nova Zelândia.

Só Marla sabe disso. Marla e meu pai. Nem Tyler sabe disso. Quando vou à praia, sento em cima do pé.

O câncer que não tenho está por toda parte, agora. — Todo mundo no Projeto de Ações Violentas sabe, sr. Durden. O barman ergue a mão, vira as costas para mim, o beijo está marcado nas costas da mão. Meu beijo?

O beijo de Tyler.

— Todos sabem da marca de nascença — diz o barman. — É o que diz a lenda. O senhor já está virando lenda, cara. Ligo para Marla do quarto de motel em Seattle para perguntar se nós já tínhamos feito aquilo. Você sabe. No interurbano, Marla pergunta: — O quê? Dormir juntos.

— O quê!

Alguma vez eu já fiz sexo com ela?

— Que é isso!

Fiz?

— Fez o quê?

Já fizemos sexo alguma vez?

— Você é uma bosta mesmo.

Fizemos?

— Vou matar você!

Isso é sim ou não?

— Eu sabia que isso ia acontecer — diz Marla — Você é maluco. Você me ama. Me ignora. Salva minha vida, depois cozinha minha mãe para fazer sabão. Eu me belisco com força.

Pergunto a Marla como nos conhecemos.

— Naquela história de câncer de testículo — diz Marla. — Depois você salvou minha vida.

Eu salvei a vida dela?

— Você salvou a minha vida.

Tyler salvou a vida dela.

— Você salvou a minha vida.

Enfio o dedo no buraco do rosto e giro de um lado e de outro. Isso deve bastar para que a dor me faça acordar.

Marla diz:

— Você salvou minha vida. O Regent Hotel. Acidentalmente tentei me suicidar. Lembra?

Oh.

— Naquela noite — diz Marla — eu disse que queria fazer um aborto seu. Estamos perdendo pressão na cabine.

Pergunto a Marla como é meu nome.

Vamos todos morrer.

Marla diz:

— Tyler Durden. Seu nome é Tyler Bundão Durden. Mora na 5123 NE Paper Street que atualmente é ocupada por seus discípulos que raspam a cabeça e

queimam a pele com soda cáustica.

Preciso dormir um pouco.

— É bom você aparecer por aqui — grita Marla ao telefone —, antes que essas bichas resolvam fazer sabão comigo. Preciso encontrar Tyler.

A marca na sua mão, pergunto a Marla, onde foi que conseguiu? — Foi você — diz Marla. — Você beijou minha mão. Preciso encontrar Tyler.

Preciso dormir um pouco.

Preciso dormir.

Preciso ir dormir.

Dou boa-noite a Marla, e a voz de Marla vai desaparecendo, desaparecendo, desaparecendo, quando estico o braço para desligar o telefone. 22

Os pensamentos ficam girando a noite toda. Estou dormindo? Será que já dormi? Assim é a insônia. Tento relaxar a cada vez que expiro, mas seu coração está acelerado e os pensamentos em turbilhão na cabeça.

Nada funciona. Nem meditação dirigida.

Você está na Irlanda.

Nem contar carneirinhos.

Você conta os dias, as horas, os minutos desde a última vez em que se lembra de ter dormido. Seu médico dá risada. Ninguém morre por falta de sono. Sua cara parece uma fruta murcha e você acha que vai morrer. Depois das três da manhã numa cama de motel em Seattle, é muito tarde para encontrar um grupo de apoio ao câncer. Tarde demais para encontrar as capsulazinhas azuis de Amytal Sodium ou bastõezinhos de Seconal, toda a coleção do Vale das Bolas. Depois das três da manhã, você não pode ir a um clube da luta.

Preciso encontrar Tyler.

Preciso dormir um pouco.

Então você está acordado e Tyler parado ao lado da cama. Você acorda.

Mal conseguiu pegar no sono e Tyler está ali, dizendo: — Acorde. Acorde, resolvemos o problema com a polícia aqui de Seattle. Acorde.

O comissário de polícia quis estourar o que ele chamou de atividade de gangue e clubes de boxe depois do horário normal. — Mas não há com que nos preocupar — diz Tyler. — O senhor comissário de polícia não é problema — diz Tyler. — Já está nas nossas mãos. Pergunto se Tyler está me seguindo.

— Engraçado — diz Tyler—, eu ia perguntar a mesma coisa. Você falou de mim para outras pessoas, seu bosta. Quebrou a sua promessa.

Tyler quer saber se eu ia entender.

— Toda vez que você pega no sono — diz Tyler— , eu me mando e cometo uma barbaridade, uma loucura, uma coisa completamente fora do normal. Tyler se ajoelha ao lado da cama e sussurra: — Terça-feira passada, quando você dormiu, tomei um avião para Seattle para dar uma espiada num clubinho de luta. Checar o número de recusados, essas coisas. Procurar novos talentos. Temos um Projeto de Ações Violentas também em Seattle.

Tyler passa o dedo na minha sobrancelha inchada. — Temos Projetos de Ações Violentas em Los Angeles, Detroit, um grande Projeto de Ações Violentas acontecendo em Washington, D. C., em Nova York. Temos um Projeto de Ações Violentas em Chicago que você não ia acreditar. Tyler diz:

— Não acredito que você tenha quebrado a sua promessa. A primeira regra do clube da luta é não falar do clube da luta. Ele estava em Seattle na semana passada quando um barman usando um colar cervical contou que a polícia ia invadir os clubes da luta. O comissário de polícia queria que fosse uma batida especial. — O que acontece — disse Tyler — é que temos policiais lutando no clube da luta e gostam muito. Temos repórteres de jornais, escrivães e advogados, e sabemos de tudo antes que as coisas aconteçam. Eles iam fechar.

— Pelo menos em Seattle — diz Tyler.

Eu pergunto o que ele fez.

— O que nós fizemos — diz ele.

Convocamos uma reunião do Comitê de Assalto. — Não somos mais só eu e você — diz Tyler, e belisca a ponta do meu nariz. — Acho que isso você já entendeu. Nós dois usamos o mesmo corpo, mas em horas diferentes. — Nós passamos uma tarefa especial — diz Tyler. — Nós dissemos "tragam os testículos fumegantes do nosso respeitabilíssimo Comissário de Polícia de Seattle".

Não estou sonhando.

— Sim, você está — diz Tyler.

Formamos uma equipe de catorze macacos espaciais, cinco deles policiais, e fomos todos para aquele parque onde sua excelência costuma passear com o cachorro.

— Fique tranqüilo — diz Tyler —, o cachorro está bem. O ataque levou três minutos a menos que o nosso melhor tempo. Nós havíamos planejado doze minutos. Nosso melhor tempo foi nove minutos. Cinco macacos espaciais o seguraram.

Tyler ia me contando essas coisas, mas, de alguma maneira, eu já sabia. Três macacos espaciais ficaram vigiando. Um macaco espacial cuidou do éter.

Um macaco espacial arrancou a respeitável calça molhada do comissário. O cachorro é um cocker spaniel, que fica latindo, latindo.

Latindo, latindo.

Latindo, latindo.

Um macaco espacial deu três voltas bem apertadas na correia de borracha por cima do respeitável saco.

— Um macaco ficou entre as pernas dele com uma faca — sussurra Tyler em meu ouvido, com o rosto estourado. — E eu disse no ouvido do respeitabilíssimo comissário de polícia que era melhor parar de invadir o clube da luta ou todo mundo ia saber que sua excelência respeitabilíssima não tinha mais saco.

Tyler sussurra:

— Até onde o senhor acha que vai, excelência? A tira de borracha o impede de sentir qualquer coisa lá embaixo. — O que o senhor acha que vai conseguir na política, se os eleitores souberem que não tem saco?

Sua excelência já não sentia mais nada.

Cara, o saco dele foi ficando gelado.

E se algum clube da luta fechar, nós vamos mandar um saco para o leste e o outro para o oeste. Um vai para o New York Times e o outro para o Los Angeles Times. Um para cada lado. Uma espécie de press release.

O macaco espacial tirou o éter da boca dele, e o comissário disse não. E Tyler disse:

— Fora o clube da luta, não temos nada a perder. O comissário, sim, tinha tudo a perder.

Para nós sobrara a merda e o lixo do mundo. Tyler fez um sinal de cabeça para o macaco espacial que segurava a faca entre as pernas do comissário.

Tyler perguntou:

— Imagine passar o resto da vida sem ter nada para encher a calça. O comissário disse não.

E não.

Pare.

Por favor.

Oh.

Deus.

Me.

Ajude.

Não.

Me.

Ajude.

Deus.

Faça-os.

Parar.

E o macaco espacial enfiou a faca por dentro e cortou a tira de borracha. Seis minutos, no total, e mais nada a fazer. — Lembre-se disso — disse Tyler. — As pessoas que você quer pisar são as mesmas das quais você depende. Somos as pessoas que lavam a sua roupa,

fazem a sua comida e servem o seu jantar. Nós fazemos a sua cama. Nós

cuidamos do seu sono. Dirigimos as ambulâncias. Passamos as suas ligações. Somos cozinheiros, motoristas de táxi e sabemos tudo a seu respeito. Nós processamos os seus pedidos de seguro e as compras no seu cartão de crédito. Controlamos cada parte de sua vida.

— Somos os filhos do meio da história e fomos ensinados pela televisão a acreditar que um dia seremos milionários, astros de cinema e do rock, mas é mentira. Só que acabamos de saber disso — disse Tyler. — Por isso, não brinque conosco.

O macaco espacial apertou o éter no nariz do comissário que soluçava e o homem saiu do ar.

Outra equipe vestiu a roupa nele e levou-o para casa junto com o cachorro. Depois disso, só dependeria dele guardar o segredo. Não, nós não esperávamos nenhuma outra invasão no clube da luta.

Sua excelência respeitabilíssima voltou para casa assustado, mas intacto. — Cada vez que realizamos essas pequenas tarefas — diz Tyler—, os homens do clube da luta que nada têm a perder acreditam um pouco mais no Projeto de Ações Violentas.

Ajoelhado ao lado da minha cama, Tyler diz: — Feche os olhos e me dê a mão.

Fecho os olhos e Tyler pega na minha mão. Sinto os lábios de Tyler sobre a cicatriz do seu beijo.

— Eu disse que se você falasse de mim pelas costas, nunca mais iria me ver — disse Tyler. — Nós não somos duas pessoas. Resumindo, quando você está acordado, você está no controle, pode chamar a si mesmo do que quiser, mas quando pega no sono, eu assumo, e você se torna Tyler Durden. Mas nós lutamos, eu digo. Na noite que inventamos o clube da luta. — Você não lutou exatamente comigo — diz Tyler. — Foi você mesmo quem disse. Estava lutando com tudo o que odeia na vida. Mas eu vejo você.

— Você está dormindo.

Mas você aluga uma casa. Tem um emprego. Dois empregos. Tyler diz: — Peça os seus cheques cancelados no banco. Eu aluguei a casa em seu nome. Você vai ver que a letra que preencheu os cheques do aluguel é a mesma das regras que você digitou para mim.

Tyler anda gastando o meu dinheiro. Não é a toa que estou sempre no vermelho.

— Quanto aos empregos — continua Tyler—, por que acha que anda tão cansado? Não é pela insônia. Assim que pega no sono, eu assumo e vou trabalhar ou ao clube da luta ou onde for. Você tem sorte de eu não ter aceitado o emprego de domador de serpente.

Eu pergunto: e Marla?

— Marla ama você.

Marla ama você.

— Marla não sabe a diferença entre mim e você. Você deu um nome falso para ela na noite que se conheceram. Nunca deu seu verdadeiro nome num grupo

de apoio, seu merda mentiroso. Desde que salvei a vida dela, Marla acha que seu

nome é Tyler Durden.

Então, agora que sei tudo sobre Tyler, ele vai desaparecer? — Não — diz Tyler, ainda segurando minha mão. — Em primeiro lugar, eu não estaria aqui se você não me quisesse. Vou continuar vivendo a minha vida quando você estiver dormindo, mas se você me sacanear, se amarrar a si mesmo na cama durante a noite ou se tomar muita bola para dormir, então seremos inimigos. E eu pego você por isso.

Ah, que besteira. Isto é um sonho. Tyler é uma projeção. É um distúrbio de personalidade dissociada. Um estado psicogênico de fuga. Tyler Durden é minha alucinação.

— Pare com essa bobagem — diz Tyler. — Talvez você seja a minha alucinação esquizofrênica.

Eu cheguei aqui primeiro. Tyler diz:

— Tá, tá, tá, mas vamos ver quem ficará por último. Isto não é real. Isto é um sonho, e eu vou acordar. — Então acorde.

Então o telefone toca e Tyler some. Logo volta de trás das cortinas. É o meu despertador das 7 horas; quando tiro o fone do gancho, a linha está muda. 23

Rapidamente, tomei um avião e voltei para casa, para Marla, para a Paper Street Soap Company.

Tudo em volta desmoronava.

Em casa, tenho muito medo de olhar dentro da geladeira. Imagine dezenas de saquinhos de sanduíche selados com nomes de cidades como Las Vegas, Chicago e Milwaukee, onde Tyler tinha levado adiante sua ameaça de proteger as sedes do clube da luta. Dentro de cada saco uma porcaria qualquer congelada. Num canto da cozinha, um macaco espacial está sentado no linóleo rachado e se olha num espelho de mão. — Sou a merda deste mundo — diz o macaco espacial para o espelho. — Sou um subproduto do lixo tóxico da criação de Deus.

Outros macacos espaciais andam pelo jardim, colhendo coisas, matando coisas.

Seguro a porta do freezer, respiro fundo e tento me concentrar na minha entidade espiritual iluminada.

Gotas de chuva nas rosas

Felizes animais de Disney

Isso me faz sofrer

Abro a porta um pouquinho, Marla olha por cima do meu ombro e diz: — O que tem para o jantar?

O macaco espacial se olha no espelho. — Sou a merda e o lixo humano





infectado da criação.

Fecha-se o círculo.

Cerca de um mês atrás, tive medo de deixar Marla olhar dentro do freezer. Agora sou eu que tenho medo de olhar dentro do freezer. Oh, Deus. Tyler.

Marla me ama. Marla não sabe a diferença. — Que bom que você voltou — diz. — Precisamos conversar. É sim, digo. Precisamos conversar.

Não estou conseguindo abrir o freezer.

Sou os Testículos Espremidos de Joe.

Digo a Marla, não toque em nada dentro deste freezer. Nem mesmo abra a porta. Se encontrar alguma coisa lá dentro, não coma, não dê para o gato comer, não faça nada. Aquele macaco espacial com o espelho na mão está de olho em nós, então digo a Marla que temos de sair. Precisamos de algum outro lugar para conversar.

Na escada que vai para o porão, um macaco espacial está lendo para outros macacos espaciais "As três maneiras de fazer napalm": — Primeiro, você pode misturar partes iguais de gasolina e suco de laranja concentrado e congelado — lê o macaco espacial. — Segundo, misturar partes iguais de gasolina e coca-cola diet. Terceiro, dissolver alimento granulado para gato em gasolina até obter uma pasta grossa. Marla e eu tomamos um ônibus na Paper Street Soap Company e chegamos a uma mesa discreta no Planet Denny's, o planeta laranja. Uma coisa que Tyler dizia é que a Inglaterra fez suas explorações, construiu colônias e elaborou mapas, e desde então a maioria dos lugares geográficos tem nomes ingleses. O inglês nomeou tudo. Ou quase. Como Irlanda**. New London, na Austrália.

New London, na índia.

New London, em Idaho.

New York, em New York.

Avançar para o futuro.

Dessa maneira, quando a exploração espacial decolar, provavelmente serão as mega-corporações que descobrirão os novos planetas e irão mapeá-los. Esfera Estelar IBM.

Galáxia Philip Morris.

Planet Denny's.

Cada planeta terá a identidade da corporação que chegar primeiro. Mundo Budweiser.

Nosso garçom tem um ovo de ganso enorme na testa, pára ereto, com os calcanhares juntos e diz:

— Senhor! Gostaria de fazer seu pedido agora? Qualquer coisa que pedir não será cobrada. Senhor!

Você já imagina que vai sentir cheiro de urina na sopa. Dois cafés, por favor.

* No original, Ireland, ou “Terra da Ira”.

Marla pergunta:

— Por que ele vai nos dar comida de graça? O garçom pensa que sou Tyler Durden, digo. Nesse caso, Marla aproveita para pedir camarão frito, marisco ensopado, uma cesta de peixe e galinha fritos, uma batata assada com tudo dentro e uma torta chiffon de chocolate. Pela abertura na parede da cozinha, três cozinheiros, um com o lábio superior costurado, observam Marla e eu, e cochicham entre si. Digo ao garçom que nos traga comida limpa, por favor. Por favor, não ponha nenhuma porcaria naquilo que pedimos.

— Nesse caso, senhor — diz o garçom —, não aconselho a moça a comer o marisco ensopado.

Obrigado. Marisco ensopado, não. Marla olha para mim, e eu digo a ela: confie em mim.

O garçom gira sobre os calcanhares e marcha em direção à cozinha com os nossos pedidos.

Através da abertura, os três cozinheiros erguem o polegar para ele. Marla diz:

— Você tem um bocado de mordomias, sendo Tyler Durden. De agora em diante, digo a Marla, ela vai me seguir por toda parte durante a noite, e eu vou anotar todos os lugares em que for. Quem eu vejo. Se castrei alguém importante. Detalhes assim.

Tiro a minha carteira e mostro a Marla a minha licença de motorista com o meu nome verdadeiro.

Não é Tyler Durden.

— Mas todos sabem que você é Tyler Durden — diz Marla. Todos menos eu.

Ninguém no trabalho me chama de Tyler Durden. Meu chefe me chama pelo meu verdadeiro nome. Meus pais sabem quem eu realmente sou. — Mas por que — pergunta Marla — você é Tyler Durden para algumas pessoas, e não para todas?

A primeira vez em que vi Tyler, eu estava dormindo. Vivia cansado, irritado, correndo, e sempre que embarcava num avião, queria que o avião caísse.

Invejava as pessoas que morriam de câncer. Odiava a minha vida. Estava cansado e enjoado do meu trabalho e dos meus móveis, e não sabia como mudar as coisas.

Só acabando com elas.

Sentia-me preso numa armadilha.

Eu era realizado demais.

Era perfeito demais.

Queria me livrar daquela vidinha. Era uma manteiga em porção individual, uma poltrona apertada de avião.

Móvel sueco.

Arte inteligente.

Tirei umas férias. Dormi na praia, e quando acordei lá estava Tyler Durden, nu e suado, sujo de areia, o cabelo molhado caindo no rosto.

Tyler estava puxando os troncos das ondas e arrastando-os para a praia.

Tyler criou a sombra da mão de um gigante e sentou-se na palma da perfeição que ele próprio criara.

Um momento é o máximo que se pode esperar da perfeição. Talvez eu não estivesse acordado naquela praia. Talvez tudo tivesse começado quando mijei na pedra Blarney. Quando pego no sono, não durmo de verdade. Em outras mesas no Planet Denny's, contei um, dois, três, quatro, cinco caras com o queixo amassado ou o nariz dobrado para baixo sorrindo para mim. — Não — diz Marla —, você não dorme.

Tyler Durden é uma personalidade independente criada por mim, e agora está ameaçando tomar conta da minha vida real. — Como a mãe de Tony Perkins em Psicose diz Marla. — Isso é muito legal. Todo mundo tem suas esquisitices. Uma vez, saí com um cara que não tinha mais onde pôr piercings no corpo.

A questão é, digo, que eu durmo e Tyler se apodera do meu corpo e da minha cara esmurrada para cometer seus crimes. De manhã, acordo arrebentado, com a certeza de que não dormi nada.

Na noite seguinte, quero dormir cedo.

Na noite seguinte, Tyler tem mais tempo para assumir o comando. Quando vou para a cama mais cedo, Tyler tem mais tempo para ele. — Mas você é Tyler — diz Marla.

Não, não sou.

Gosto de tudo o que se relaciona com Tyler, sua coragem e sua inteligência. Tyler é engraçado, charmoso, convincente e independente, os homens olham para ele e esperam que a vida deles mude. Tyler é livre e competente. Eu não sou. Eu não sou Tyler Durden.

— Mas você é, Tyler — diz Marla.

Tyler e eu dividimos o mesmo corpo e, até agora, eu não sabia. Sempre que Tyler transava com Marla, eu estava dormindo. Tyler andava e falava enquanto eu achava que estava dormindo.

Todos no clube da luta e no Projeto de Ações Violentas conheciam a mim e a Tyler Durden.

E se eu fosse para a cama mais cedo e dormisse até mais tarde pela manhã, acabava indo do mesmo jeito.

Gostaria de dormir e nunca mais acordar. Marla diz:

— Exatamente como os bichinhos do Controle de Animais. O Vale dos Cães. Mesmo que eles não matem você, mesmo que alguém goste muito de você e o leve para casa, mesmo assim eles o castram. Eu nunca mais acordaria e Tyler assumiria o comando. O garçom traz o café, bate os calcanhares e sai. Cheiro o meu café. Tem cheiro de café.

— Mesmo que eu acreditasse em tudo isso — diz Marla —, o que você quer que eu faça?

Para que Tyler não assuma o controle total, preciso que Marla me mantenha

acordado. O tempo todo.

O círculo se completa.

Na noite em que Tyler salvou sua vida, Marla pediu que ele a mantivesse acordada a noite toda.

No instante em que pego no sono, Tyler assume e alguma coisa terrível acontece.

Se eu pegar no sono, Marla não pode perder Tyler de vista. Aonde ele for. O que ele fizer. Quem sabe durante o dia eu consiga sair correndo e consertar os estragos.

24

O nome dele é Robert Paulson, 48 anos de idade O nome dele é Robert Paulson, e Robert Paulson terá 48 anos para sempre. Num período de tempo mais ou menos longo, a taxa de sobrevivência de todo mundo será zero.

Big Bob.

O grande pão de queijo. O grande alce fora destacado para uma tarefa regulamentar de congelar-e-furar. Foi assim que Tyler conseguiu entrar no meu apartamento e explodi-lo com dinamite caseira. Pegue uma lata de resfriador em spray R-12, se ainda conseguir encontrar, com buraco na camada de ozônio e tudo, ou um R-134a, e espirre dentro do tambor da fechadura para congelar. A tarefa de congelar-e-furar consiste em espirrar o resfriador na fechadura de um telefone público ou de um parquímetro. Depois, com um martelo e uma talhadeira, arrebentar o tambor congelado da fechadura. A tarefa regulamentar de furar-e-encher consiste em furar o telefone ou o caixa automático de banco, depois enroscar o funil de lubrificação e com uma pistola de graxa injetar no alvo graxa de eixo, pudim de baunilha ou cimento plástico.

Não que o Projeto de Ações Violentas tivesse necessidade de roubar uns trocados. A Companhia de Sabão Paper Street contava com uma boa reserva de pedidos. Deus nos ajudava quando os feriados se aproximavam. A tarefa é ter sangue frio. É preciso ter astúcia. Estruturar o seu investimento no Projeto de Ações Violentas.

Em vez da talhadeira, você pode usar furadeira elétrica no tambor congelado da fechadura. Funciona muito bem e não faz tanto barulho. Era uma furadeira elétrica sem fio e a polícia pensou que fosse uma arma quando mandou Big Bob pelos ares.

Não havia onde encaixar Big Bob no Projeto de Ações Violentas, no clube da luta ou no sabão.

Ele tinha no bolso uma foto dele nu em primeiro plano posando para um concurso qualquer. É um jeito estúpido de viver, disse Bob. As luzes do palco o deixam cego, o sistema de som ao fundo o deixa surdo, enquanto o juiz ordena, estenda o quadríceps, flexione e segure. Ponha as mãos onde se possa vê-las.

Estenda o braço esquerdo, flexione o bíceps e segure.

Congele.

Solte a arma.

Isso era melhor que a vida real.

Na mão dele, a cicatriz do meu beijo. Do beijo de Tyler. O cabelo esculpido de Big Bob tinha sido raspado e suas impressões digitais foram queimadas com soda cáustica. Melhor sair ferido do que ir preso, porque se você fosse preso, estaria fora do Projeto de Ações Violentas e nunca mais seria escalado para as tarefas.

Num primeiro momento, Robert Paulson era o centro ao redor do qual girava a vida do mundo, no momento seguinte, Robert Paulson era um objeto. O tiro da polícia e o fantástico milagre da morte. Em todos os clubes da luta, esta noite, o líder da sede anda em círculos no escuro, ao redor do grupo de homens que se encaram de frente no meio do porão vazio, e uma voz grita:

— Seu nome é Robert Paulson. As pessoas repetem: — O nome dele é Robert Paulson. Os líderes gritam: — Ele tem 48 anos.

Ele tem 48 anos e pertencia ao clube da luta. Ele tem 48 anos e pertencia ao Projeto de Ações Violentas. Só a morte conhecerá nossos nomes porque somente morrendo deixaremos de participar dos esforços. Só morrendo seremos heróis. E as pessoas gritam "Robert Paulson". E as pessoas gritam "Robert Paulson". E as pessoas gritam "Robert Paulson". Vou ao clube da luta esta noite para fechá-lo. Paro sob a única lâmpada no meio do porão e dos torcedores. Para todos aqui sou Tyler Durden. Inteligente. Convincente. Valente. Ergo as mãos pedindo silêncio e sugiro, porque todo mundo acha que é só uma noite, que voltem para casa e esqueçam o clube da luta.

O clube da luta já cumpriu sua missão, certo? O Projeto de Ações Violentas está cancelado. Parece que tem um bom jogo de futebol na televisão... Centenas de pares de olhos não se afastam de mim. Um homem morreu, digo. O jogo acabou. Isso deixou de ser brincadeira. Então, do lado de fora do círculo de homens, chega a voz anônima do líder de sede:

— A primeira regra do clube da luta é não falar do clube da luta. Eu grito voltem para suas casas!

— A segunda regra do clube da luta é não falar do clube da luta. O clube da luta está cancelado. O Projeto de Ações Violentas está cancelado.

— A terceira regra é apenas dois caras por luta. Sou Tyler Durden, grito. E estou ordenando que saiam. Ninguém mais está olhando para mim. Os homens se encaram no centro do salão.

A voz do líder de sede arrasta-se pelo salão. Dois homens por luta. Sem

camisa. Sem sapatos.

A luta continua até onde tiver de ir.

Imagine isso acontecendo em centenas de cidades, em meia dúzia de sotaques.

Terminam as regras e eu ainda estou sob a lâmpada. — Luta número 1, vá para o centro — grita a voz da escuridão. — Esvaziem o centro do clube.

Eu não me mexo.

— Esvaziem o centro do clube!

Eu não me mexo.

A única lâmpada está refletida em centenas de pares de olhos voltados para mim, esperando. Tento ver cada homem como Tyler os vê. Escolho os melhores lutadores para treinar no Projeto de Ações Violentas. Qual deles Tyler convidaria para trabalhar na Fábrica de Sabão Paper Street? — Esvaziem o centro do clube! — Este é um procedimento normal no clube da luta. Após três ordens do líder de sede, serei expulso do clube da luta. Mas sou Tyler Durden. Inventei o clube da luta. O clube da luta é meu. Eu escrevi as regras. Ninguém estaria aqui se não fosse por mim. E estou dizendo que parou por aqui!

— Preparar para expulsar o membro em três, dois, um. O círculo de homens avança sobre mim, e duzentas mãos se fecham em meus braços e pernas, erguendo-me em direção à lâmpada. Preparar para abandonar a alma em três, dois, um. Sou passado por cima das cabeças, de mão em mão, o grupo caminha em direção à porta. Estou flutuando. Estou voando. Vou gritando, o clube da luta é meu. O Projeto de Ações Violentas foi idéia minha. Vocês não podem me expulsar. Sou eu que mando aqui. Voltem para casa.

A voz do líder de sede grita:

— Luta número 1, por favor, no centro do salão. Já! Não estou caindo fora. Não estou me entregando. Eu posso vencer. Eu estou no comando.

— Expulsar membro do clube da luta, já!

Abandonar a alma, já.

Saio voando lentamente pela porta para dentro da noite, sob as estrelas e o ar fresco, e aterrisso no asfalto do estacionamento. As mãos se afastam e a porta se fecha atrás de mim. Em centenas de cidades, o clube da luta continua sem mim.

25

Não é de hoje que venho querendo dormir. Dormir mesmo, apagar, mergulhar num sono profundo. Agora, é a última coisa que quero fazer. Estou com Marla no quarto 8G do Regent Hotel. Aqui, com esses velhos e drogados

fechados em seus quartinhos, não sei por que meu desespero me parece normal e

justificado.

— Aqui — Marla está sentada na cama sobre as pernas cruzadas, destacando meia dúzia de comprimidos de anfetamina da embalagem de plástico brilhante. — Era aqui que eu me encontrava com um cara que tinha pesadelos terríveis. Ele também detestava dormir.

O que aconteceu com ele?

— Ah, ele morreu. Ataque cardíaco. Overdose. Muita anfetamina. Ele só tinha dezenove anos — diz Marla.

Obrigado por me contar.

Quando chegamos ao hotel, o recepcionista tinha metade do cabelo arrancado pela raiz. O couro cabeludo coberto com cascas de ferida, ele me cumprimentou. Os velhos que assistiam à televisão na recepção viraram-se para ver quem era quando o sujeito no balcão me chamou de senhor. — Boa noite, senhor.

Neste exato momento, posso imaginá-lo ligando para um quartel do Projeto de Ações Violentas para comunicar a minha localização. Eles devem ter um mapa da cidade na parede e traçam os meus movimentos com tachinhas coloridas. Sinto-me caçado como um ganso migrador do Reino Selvagem. Estou sendo espionado, vigiado.

— Dá para tomar seis destas sem passar mal do estômago — diz Marla —, mas tem de ser pelo cu.

Ah, que coisa mais agradável. Marla diz: — A gente pode conseguir coisa mais forte, mais tarde. Droga de verdade, como cross tops, black beauties ou alligators. Eu não vou enfiar esses comprimidos no meu cu. — Então tome só dois. Aonde é que nós vamos? — Ao boliche. Lá, fica aberto a noite toda e você não vai conseguir dormir. Em qualquer lugar vão achar que sou Tyler Durden. — Foi por isso que o motorista do ônibus não cobrou a nossa passagem? Foi. E foi por isso também que aqueles dois sujeitos no ônibus deram o lugar para a gente sentar.

— E então, tem alguma idéia?

Não acho que resolva a gente ficar se escondendo. Temos de fazer alguma coisa para nos livrarmos de Tyler.

— Uma vez, eu saí com um cara que gostava de usar minhas roupas — diz Marla. — Usar vestidos, sabe. Chapéus com véu. Você podia vestir um vestido e sair disfarçado.

Eu não vou usar vestido e não vou enfiar comprimidos no cu. — Podia ser pior — diz Marla. — Outro cara que conheci queria que eu bancasse a lésbica com sua boneca inflável. Já me vi transformado numa das histórias de Marla. Uma vez saí com um cara que tinha dupla personalidade.

— Saí com outro cara que usava um sistema de alargamento de pênis. Pergunto que horas são.

Quatro da tarde.

Mais três horas e terei de sair para o trabalho.

— Tome os comprimidos — diz Marla. — Sendo Tyler Durden, talvez eles nos deixem jogar boliche de graça. Ei, antes de a gente se livrar de Tyler, que tal fazer umas compras? Podíamos comprar um carro. Umas roupas. Uns CDs. Há um lado bom nessa história toda.

Marla.

— Tudo bem, esquece.

26

O velho ditado que diz que a gente mata a quem mais ama, bom, ele também funciona de outro jeito.

E como funciona.

Esta manhã, fui trabalhar e havia uma barricada policial entre o prédio e o estacionamento, a polícia estava na porta colhendo depoimentos das pessoas que trabalhavam comigo. Todo mundo circulando. Sou o Suor Frio de Joe.

De dentro do ônibus, vejo que as vidraças do teto ao chão da minha sala no terceiro andar foram explodidas, e lá dentro um bombeiro de capa amarela usa o machado numa placa queimada do teto rebaixado. Uma mesa em brasas aparece na vidraça quebrada, empurrada por dois bombeiros, balança, escorrega e despenca três andares na calçada e aterrissa com mais sensação do que barulho. Arrebenta no chão, ainda fumegante.

Sou o Buraco no Estômago de Joe.

É a minha mesa.

Sei que meu chefe está morto.

Há três maneiras de fazer napalm. Eu sabia que Tyler ia matar meu chefe. No momento em que senti cheiro de gasolina nas mãos, quando eu disse que queria abandonar o meu emprego, estava dando permissão a ele. Fique à vontade. Mate meu chefe.

Oh, Tyler.

Sei que um computador explodiu.

Sei disso porque Tyler sabe disso.

Não quero saber, mas se usa uma broca de joalheiro para fazer um buraco na parte superior do monitor do computador. Todos os macacos espaciais sabem disso. Fui eu quem digitei as anotações de Tyler. É uma nova versão da bomba- lâmpada; você faz um orifício na lâmpada e enche de gasolina. Tampa o orifício com cera ou silicone, enrosca a lâmpada num soquete e espera alguém entrar na sala e ligar o interruptor.

No tubo do computador cabe muito mais gasolina do que na lâmpada. Um tubo de raios catódicos, CRT, e aí, ou você remove o plástico que protege o tubo, o que é bem mais fácil de fazer, ou trabalha através dos vãos de ventilação na parte superior do monitor. Primeiro, desligue o monitor da tomada e do computador. Isso também dá certo com televisão.

Mas saiba que se houver uma faísca ou até mesmo eletricidade estática

produzida pelo carpete, você está morto. Morre queimado e gritando. Como um tubo de raios catódicos pode conter 300 volts de armazenagem elétrica passiva, introduza primeiro o cabo da chave de fenda no capacitador de fornecimento de energia. É aqui que você pode morrer se não usar uma chave de fenda com isolamento.

Há vácuo dentro do tubo de raio catódico, então, quando você fizer o buraco, o tubo vai sugar o ar com um leve assobio. Alargue o buraquinho um pouco mais, depois mais um pouquinho, até conseguir enfiar a ponta de um funil. Depois, encha o tubo com o explosivo de sua preferência. Napalm feito em casa é muito bom. Gasolina pura ou misturada a suco de laranja concentrado e congelado ou com alimento granulado para gatos. Dá um ótimo explosivo misturar perman-ganato de potássio com açúcar refinado. A idéia é misturar um ingrediente que queime muito rápido com outro ingrediente que produza o oxigênio necessário para a queima. Queima rápido e explode.

Peróxido de bário e pó de zinco.

Nitrato de amônia e alumínio em pó.

A nouvelle cuisinne da anarquia.

Nitrato de bário em molho de enxofre guarnecido com carvão. Isso é pólvora básica.

Bon appétit.

Encha o monitor do computador e, quando alguém ligar a luz, serão dois ou três quilos de pólvora explodindo na sua cara. O problema é que, de certa maneira, eu gostava do meu chefe. Se você é macho, é cristão e mora nos Estados Unidos, seu pai é o seu modelo de Deus. E às vezes você encontra um pai no seu trabalho. Só que Tyler não gostava do meu chefe.

A polícia está me procurando. Fui a última pessoa a sair do prédio na sexta- feira passada. Acordei na minha mesa com a respiração condensada sobre o tampo e Tyler ao telefone me dizendo:

— Saia. Estamos de carro.

Temos um Cadillac.

O mecânico do clube da luta me perguntou o que eu gostaria de fazer antes de morrer.

Gostaria de sair do emprego. Dei minha permissão para Tyler. Fique à vontade. Mate meu chefe.

Do meu escritório explodido, sigo com o ônibus para a rotatória de cascalho no final da linha. É ai que as subdivisões se perdem de vista nos estacionamentos vazios e nos campos arados. O motorista tira seu lanche e a garrafa térmica e me observa pelo espelho retrovisor.

Pergunto-me até onde posso ir sem que os tiras venham atrás de mim. Sentado no fundo do ônibus, há pelo menos vinte pessoas entre mim e o moto- rista. Conto vinte cabeças.

Vinte cabeças raspadas.

O motorista vira-se para trás e me chama no banco do fundo. — Sr. Durden,

senhor, tenho muita admiração pelo que vem fazendo.

Eu nunca o vi na vida.

— Perdoe-me por isso — diz o motorista. — O comitê diz que a idéia foi sua, senhor.

As cabeças raspadas viram-se, uma atrás da outra. Depois, um por um se levanta. Um deles tem um trapo na mão e dá para sentir o cheiro de éter. O que está mais próximo segura uma faca. Esse com a faca é o mecânico do clube da luta.

— O senhor tem muita coragem — diz o motorista do ônibus — de cumprir uma tarefa pessoalmente.

O mecânico diz ao motorista do ônibus:

— Cale-se. Sentinela não abre a boca.

Você sabe que um dos macacos espaciais está com uma tira de borracha para amarrar os seus testículos. A parte da frente do ônibus está cheia deles. O mecânico diz:

— O senhor conhece a regra, sr. Durden. Foi o senhor mesmo quem a fez. Disse que se alguém tentar um dia fechar o clube, mesmo sendo o senhor, teria de ser capado.

Gônadas. Bolas. Saco. Huevos.

Imagine a sua melhor parte congelada num saco de sanduíche da Fábrica de Sabão Paper Street.

— O senhor sabe que é inútil resistir — diz o mecânico. O motorista mastiga o sanduíche e nos observa pelo espelho retrovisor. Ouço a sirene de um carro de polícia se aproximando. Um trator passa ao longe. Pássaros. A janela no fundo do ônibus está meio aberta. Nuvens. O mato cresce em volta da rotatória de cascalho. Abelhas e moscas voam em círculos. — Só estamos querendo nos garantir — diz o mecânico do clube da luta. — Isto não é só ameaça, sr. Durden. Desta vez vamos ter de cortar mesmo. O motorista do ônibus diz:

— São os tiras.

A sirene ultrapassa o ônibus.

Do que será que vou ter de me defender?

O carro de polícia pára na frente do ônibus, a luz azul e vermelha piscando no pára-brisa, e alguém lá fora grita:

— Pare onde está.

Estou salvo.

Mais ou menos.

Vou contar aos tiras sobre Tyler. Vou contar tudo sobre o clube da luta, talvez eu seja preso e o Projeto de Ações Violentas passe a ser problema deles e eu não tenha mais de ficar olhando para esta faca. Os tiras entram no ônibus e um deles pergunta: — Ainda não terminaram?

O segundo tira diz:

— Andem logo, há um pedido de prisão contra ele. Então ele tira o quepe, vira-se para mim e diz:

— Não é nada pessoal, senhor Durden. É um prazer conhecê-lo finalmente.

Eu digo, vocês estão cometendo um grande erro.

O mecânico diz:

— O senhor nos disse que provavelmente diria isso. Não sou Tyler Durden.

— O senhor nos disse que diria isso também. Estou mudando as regras. Vocês podem ficar com o clube da luta, mas não vão mais castrar ninguém, nunca mais.

— Tá, tá, tá — diz o mecânico. Ele está no meio do corredor segurando a faca na sua frente. — O senhor mesmo disse que diria isso. Está bem, então sou Tyler Durden. Sou. Sou Tyler Durden, sou eu quem dita as regras e estou dizendo, abaixe essa faca. O mecânico olha por cima do ombro e pergunta para os de trás: — Qual foi o nosso melhor tempo para um cortar-e-correr? Alguém responde:

— Quatro minutos. O mecânico diz:

— Alguém está marcando o tempo?

Os tiras estão dentro do ônibus, lá na frente, um deles olha o relógio e diz: — Mais um segundo. O ponteiro menor tem de encostar no 12. O tira diz:

— Nove.

— Oito.

— Sete.

Eu salto pela janela aberta.

Minha barriga raspa no trilho da janela e, às minhas costas, o mecânico do clube da luta grita:

— Sr. Durden! O senhor vai nos atrasar. Pendurado na janela, agarro-me à borracha do pneu traseiro e tento sair. Alguém me segura pelos pés e me puxa para dentro. Começo a gritar para o trator: — Ei. Ei. Ei. — Meu rosto inchado começa a sangrar porque estou de cabeça para baixo. Tento sair. Alguém me puxa pelos tornozelos. A gravata bate no meu rosto. A fivela do cinto de segurança enrosca no trilho da janela. As abelhas, as moscas e o mato estão muito perto do meu rosto, e eu grito: — Ei!

Alguém me segura pela calça e tenta me puxar para dentro. Dentro do ônibus, ouço alguém dizer:

— Um minuto!

Os sapatos escapam dos meus pés.

A fivela do cinto enfia-se no trilho da janela. Alguém junta as minhas pernas. O metal quente do trilho corta a minha pele. Minha camisa branca cobre a cabeça e os ombros, e estou gritando: — Ei!

Minhas pernas são puxadas para trás. A calça escorrega por elas e desaparece. Sinto o sol queimar minha bunda. O sangue lateja em minha cabeça, os olhos estão inchados pela pressão, só vejo a camisa branca em meu rosto. Ouço o motor do trator em algum lugar. As abelhas zunindo. Não sei onde. Tudo está a quilômetros de distância. Em algum

lugar a milhares de quilômetros de mim alguém grita:

— Dois minutos!

Uma mão escorrega por entre minhas pernas e procura alguma coisa. — Não o machuque — diz alguém.

As mãos que seguram meu tornozelo estão a quilômetros de distância. Imagine-as no final de uma longa, longa estrada. Meditação dirigida. Não imagine o trilho da janela como uma lâmina abrindo a sua barriga. Não imagine um bando de homens tentando abrir as suas pernas. A quilômetros de distância, a zilhões e zilhões de quilômetros, uma mão rude passa por baixo da sua perna e puxa você para dentro, e alguma coisa começa a apertar você.

A tira de borracha.

Você está na Irlanda.

Está no clube da luta.

Está no trabalho.

Está em qualquer lugar menos aqui.

— Três minutos!

Alguém grita de muito, muito longe:

— O senhor sabe muito bem, sr. Durden. Não sacaneie o clube da luta. A mão quente está embaixo de você. O toque da lâmina fria. Alguém passa os braços em volta do seu peito. Contato físico terapêutico.

Hora de abraçar.

Alguém encosta éter no seu nariz e na sua boca, e aperta. Depois, o nada, menos que nada. O esquecimento. 27

A cápsula detonada do meu apartamento incendiado é um espaço negro e devastado sobre as luzes da cidade. Sem as janelas, a fita amarela da policia que isola a cena do crime balança ao vento do alto do décimo quinto andar. Eu acordo na laje de concreto. Havia aqui um soalho de madeira. Havia arte nas paredes antes da explosão. Havia móveis suecos. Tudo antes de Tyler. Estou vestido. Enfio a mão no bolso e sinto. Estou inteiro.

Assustado mas intacto.

Vá até a beira da laje, quinze andares sobre o estacionamento, olhe as luzes da cidade e as estrelas e desapareça.

Tudo é tão distante.

Aqui de cima, os quilômetros de noite entre as estrelas e a Terra fazem com que eu me sinta um macaco espacial.

Cachorros.

Macacos.

Homens.

Faça o que você tem de fazer. Puxe uma alavanca. Aperte o botão. Não

precisa entender nada.

Todo mundo enlouqueceu. Meu chefe morreu. Minha casa se foi. Meu trabalho desapareceu. E sou o único responsável por tudo. Não sobrou nada.

Estourei minha conta no banco.

Estou a um passo da beirada.

A fita amarela se agita entre mim e o nada. Só mais um passo.

Lá está Marla.

Salte.

Lá está Marla, ela está no meio de tudo e não sabe. Ela ama você.

Ama Tyler.

Ela não sabe a diferença.

Alguém tem de contar a ela. Saia. Saia. Saia. Salve-se.

Você desce pelo elevador até a portaria e o porteiro que nunca gostou de você lhe sorri sem três dentes na boca e diz: — Boa noite, sr. Durden. Precisa de um táxi? Está se sentindo bem? Quer usar o telefone?

Ligo para Marla no Regent Hotel. O recepcionista do Regent diz: — Imediatamente, sr. Durden. Marla atende. O porteiro fica ouvindo atrás de você. O recepcionista do Regent provavelmente também está ouvindo. Você diz, Marla, precisamos conversar. Marla diz:

— Vá se foder.

Ela pode estar correndo perigo, você diz. Tem de saber o que está acontecendo. Vocês precisam se encontrar. Precisam conversar. — Onde?

Naquele lugar onde nos conhecemos. Lembra-se? — Lembrei — diz. — Chego lá em vinte minutos. Não deixe de ir.

Você desliga, e o porteiro pergunta:

— Quer um táxi, sr. Durden? Vai levá-lo aonde o senhor quiser sem cobrar nada.

Estou sendo seguido pelos rapazes do clube. Não, você diz, a noite está linda, prefiro andar.

É sábado à noite, noite do câncer de bexiga no porão da Primeira Igreja Metodista, e Marla já está lá quando chego. Marla Singer fumando seu cigarro. Marla Singer revirando os olhos. Marla Singer com um olho preto.

Vocês se sentam em lados opostos no círculo de meditação para invocar seus animais de poder; o olho preto de Marla fixo em você. Você fecha os olhos e medita no palácio das sete portas, sempre sentindo o olhar de Marla. E embala sua criança interior.

Marla não desvia o olhar.

Hora de abraçar.

Abram os olhos.

Temos de escolher um parceiro.

Marla cruza a sala em três passos e me dá um tapa na cara. Entregue-se completamente.

— Seu bosta — diz Marla.

A nossa volta, todos param para olhar.

Marla começa a me socar de todos os lados. — Você matou uma pessoa — ela grita. — Chamei a polícia; eles vão chegar a qualquer momento. Seguro-a pelos pulsos e digo, talvez a polícia venha, mas é mais provável que não.

Marla tenta se soltar e diz que a polícia vai me levar para a cadeira elétrica, fritar meus olhos ou me aplicar uma injeção letal. Como o ferrão de um inseto.

Uma dose caprichada de fenorbital de sódio e depois um longo sono. Como no Vale dos Cães.

Marla disse que me viu matar alguém hoje. Se ela se refere ao meu chefe, digo, sim, sim, sim, eu sei, a polícia sabe, estão me procurando para me aplicar uma injeção letal, mas foi Tyler quem o matou.

Por acaso Tyler e eu temos as mesmas impressões digitais, mas isso ninguém vai entender.

— Vá se foder — diz Marla e arregala o olho preto para mim. — Só porque você e os seus os discípulos de merda gostam de bater e apanhar, se encostar a mão em mim mais uma vez, será um homem morto. — Eu vi você atirar num cara esta noite — diz Marla. Não, foi uma bomba, digo, e foi de manhã. Tyler furou o monitor do computador e encheu de gasolina e pólvora. Toda aquela gente que tem um câncer de bexiga verdadeiro parou para nos assistir.

— Não — diz Marla—, eu segui você até o Pressman Hotel, e você era o garçom numa daquelas festas de assassinato misterioso. Nessas festas de assassinato misterioso, os ricos vão para o hotel e participam de um grande jantar, onde representam uma história de Agatha Christie. Em algum momento entre o Boudin de GravJaxe o Saddle de Venison, as luzes se apagam por um minuto e alguém finge ser assassinado. Uma espécie de morte de faz-de-conta.

Ao longo do jantar, os convidados bebem, comem Consommé ao Madeira e tentam encontrar pistas do assassino psicótico que estaria entre eles. Marla grita: — Você matou o convidado especial do prefeito, o encarregado de reciclagem!

Tyler matara o encarregado especial de qualquer coisa do prefeito. Marla continua:

— E você nem tem câncer! Mais cedo do que eu esperava. Estalo os dedos. Todos estão nos olhando.

Eu devolvo, você também não tem!

— Ele vem aqui há dois anos — grita Marla — e não tem nada! Estou tentando salvar sua vida!

— O quê? Por que minha vida precisa ser salva? Porque você tem me seguido. Porque você me seguiu esta noite, porque viu Tyler Durden matar alguém, e Tyler matará quem tentar atrapalhar o Projeto de Ações Violentas.

Todos no salão parecem tirados de suas pequenas tragédias. De seus cancerezinhos. Até os dopados estão de olhos arregalados, alertas. Volto-me para o grupo e peço desculpas. Jamais pretendi prejudicá-los. Nós vamos sair. Podemos conversar lá fora.

Eles dizem:

— Não! Fiquem! O que mais?

Eu não matei ninguém, digo. Não sou Tyler Durden. Ele é o outro lado da minha dupla personalidade. Eu pergunto, alguém assistiu ao filme Sybil? Marla diz:

— Quem é que vai me matar?

Tyler.

— Você?

Tyler, digo, mas eu posso cuidar dele. Você só tem de ficar de olho nos membros do Projeto de Ações Violentas. Tyler pode ter dado ordem de seguir você ou de raptá-la, qualquer coisa.

— Por que eu deveria acreditar nisso?

Foi tudo muito rápido.

Digo: porque acho que gosto de você.

Marla pergunta:

— Amor?

Não é a melhor hora, digo. Não force nada. Todos em volta estão sorrindo.

Preciso ir. Tenho de sair daqui. Fique de olho nos caras de cabeça raspada e nos que parecem ter levado uma surra. Olhos pretos. Dentes faltando. Esse tipo de coisa.

E Marla pergunta:

— Aonde é que você vai?

Vou cuidar de Tyler Durden.

28

Ele se chamava Patrick Madden, e era o encarregado especial de reciclagem do prefeito. Ele se chamava Patrick Madden, e era inimigo do Projeto de Ações Violentas.

Saio da Primeira Metodista, sigo pela noite e tudo começa a voltar. Começo a me lembrar de tudo o que Tyler sabe. Patrick Madden fez uma lista dos bares nos quais o clube da luta se reúne. De repente, sei como operar um projetor de filmes. Sei como quebrar

fechaduras e como Tyler alugou a casa da Paper Street, pouco antes de se revelar

a mim naquela praia.

Sei por que Tyler aconteceu. Tyler amava Marla. Naquela noite em que eu a conheci, Tyler ou parte de mim queria encontrar uma maneira de ficar com Marla.

Não que isso tenha importância. Ao menos agora. Mas todos os detalhes estão voltando enquanto sigo pela noite em direção ao clube da luta mais próximo.

Há um clube da luta no porão do Armory Bar, nas noites de sábado. Provavelmente você vai encontrá-lo na lista que Patrick Maidden estava fazendo, o pobre defunto Patrick Madden.

Esta noite, vou ao Armory Bar e as pessoas se abrem como zíper para me deixar passar. Para todos aqui, sou Tyler Durden, o Grande, o Poderoso. Deus e pai.

— Boa noite, senhor.

— Bem-vindo ao clube da luta, senhor.

— Obrigado por juntar-se a nós, senhor.

Quanto a mim, minha cara de monstro está começando a melhorar. O buraco sorrindo na bochecha. A boca tensa. Porque sou Tyler Durden, e porque você me beija os pés, inscrevo-me para lutar com todos esta noite. São quinze lutas. Uma luta por vez. Sem sapatos. Sem camisa.

As lutas continuam até onde der.

E se Tyler ama Marla.

Eu amo Marla.

E o que acontece não acontece em palavras. Quero asfixiar as praias francesas que nunca verei. Imagine os alces se exibindo nos cânions inundados ao redor do Rockefeller Center.

Na primeira luta, o cara prende meus braços atrás do meu pescoço e soca meu rosto, soca a bochecha, soca o buraco na bochecha no chão de cimento, até que meus dentes se quebram e plantam as raízes pontudas na minha língua. Agora me lembro de Patrick Madden morto no chão, e a mulher dele, uma bonequinha de porcelana, uma menininha de chignon. Ela ria nervosamente e despejava champanhe nos lábios do marido morto. A mulher dizia que o sangue falso era muito, muito vermelho. A sra. Patrick Madden passou dois dedos no sangue empoçado ao lado do marido e pôs os dedos na boca.

Com os dentes cravados na minha língua, sinto gosto de sangue. A sra. Patrick Madden sentiu gosto de sangue. Lembro-me de estar por ali durante uma festa de assassinato misterioso, protegido pelos macacos espaciais garçons que me rodeavam. Marla com seu vestido de rosas escuras de papel de parede me observava do outro lado do salão. Minha segunda luta, o cara aperta o joelho entre meus ombros. Ele puxa meus braços para trás e bate meu peito no chão de cimento. A clavícula de um dos lados, ouço quando estala.

Usaria um machado nos Elgin Marbles e limparia a bunda com a Mona

Lisa.

A sra. Patrick Madden ergue os dois dedos ensanguentados, o sangue se

espalha pelos vãos dos dentes, o sangue escorre pelos dedos dela, desce pelo pulso, atravessa o bracelete de diamantes e chega ao cotovelo, onde começa a pingar.

Luta número três, acordo e é hora da luta número três. Não existem mais nomes no clube da luta.

Você não é seu nome.

Você não é sua família.

O número três parece saber o que preciso e prende a minha cabeça na escuridão e na névoa. Há um golpe que deixa você com ar suficiente para não apagar. O número três prende a minha cabeça na dobra do braço, como se segurasse um bebé ou uma bola de futebol, na dobra do braço, e soca meu rosto com o punho fechado.

Até meus dentes morderem o interior da bochecha. Até o buraco no meu rosto encontrar o canto da boca, duas bordas paralelas desde o nariz até embaixo da orelha.

O número três bate até sentir os dedos machucados. Até eu começar a chorar.

Tudo o que você mais ama o rejeitará ou morrerá. Tudo o que você já criou será jogado fora. Tudo de que você mais se orgulha terminará em lixo. Sou Ozymandias, o rei dos reis.

Mais um soco e meus dentes se fecham na língua. Metade da língua cai no chão e é chutada para longe.

A bonequinha de porcelana da sra. Patrick Madden ajoelhada no chão ao lado do corpo do marido, e os ricos, pessoas consideradas amigas, estão em volta, bêbadas e rindo.

A mulher chama:

— Patrick?

A poça de sangue se espalha e encosta na saia dela. Ela diz:

— Patrick, já basta, chega de morrer.

O sangue sobe pela bainha da saia, ação capilar, fio por fio, subindo pela saia.

Em volta de mim, os homens do Projeto de Ações Violentas estão gritando. E a sra. Patrick Madden está gritando.

E no porão do Armory Bar, Tyler Durden desaba no chão. Tyler Durden, o grande, que foi perfeito por um instante e disse que o instante é o máximo que se pode esperar da perfeição.

A luta continua porque eu quero morrer. Porque só morrendo temos nomes. Só morrendo não fazemos mais parte do Projeto de Ações Violentas. 29

Tyler está ali parado, perfeitamente belo, um anjo em toda a sua loirice.

Minha vontade de viver me surpreende.

Quanto a mim, sou uma amostra de sangue seco sobre o colchão, em meu quarto na Fábrica de Sabão Paper Street. Tudo ali desapareceu.

Meu espelho com a foto do meu pé quando tive câncer por dez minutos. Pior que o câncer. O espelho sumiu. A porta do armário está aberta e minhas seis camisas brancas, as calças pretas, as meias e os sapatos desapareceram. Tyler diz:

— Levante-se.

Por baixo, por trás e dentro de tudo que dou como certo, algo terrível está crescendo.

Tudo está desmoronando.

Os macacos espaciais sumiram. Tudo voltou ao lugar, a gordura lipoaspirada, os beliches, o dinheiro, principalmente o dinheiro. Tyler diz:

— A última coisa que falta fazer é o seu martírio. A sua grande morte. Não a morte como algo triste, deprimente, mas alegre, fortalecedor. Oh, Tyler, estou sofrendo. Acabe comigo agora. — Levante-se.

Mate-me, agora. Mate-me. Mate-me. Mate-me. Mate-me. — Tem de ser grandiosa — diz Tyler. — Imagine só: você no alto do edifício mais alto do mundo, o prédio todo tomado pelo Projeto de Ações Violentas. Rolos de fumaça saindo pelas janelas. As mesas caindo sobre as pessoas na rua. Uma verdadeira ópera da morte, é isso o que vamos fazer. Eu digo, não. Você já me usou demais.

— Se você não cooperar, vou atrás de Marla. Eu digo, vamos em frente. — Então saia dessa porra de cama — diz Tyler — e sente essa bunda naquela porra de carro.

Então, Tyler e eu estamos no alto do Parker-Morris Building com a arma enfiada em minha boca.

Estamos nos nossos dez minutos finais.

Em dez minutos o Parker-Morris Building não estará mais aqui. Sei disso porque Tyler sabe disso.

Com o cano da arma encostado no fundo da minha garganta, Tyler diz: — Ninguém morre verdade.

Empurro com a língua o cano da arma para o lado sobrevivente do rosto e digo, Tyler, você está falando de vampiros. Estamos nos nossos oito minutos finais.

A arma é só para o caso de os helicópteros da polícia aparecerem por aqui. Deus pode achar que é um homem sozinho com uma arma enfiada na boca, mas é Tyler quem está com a arma, e é a minha vida. Pegue vapor de ácido nítrico com 98% de concentração e adicione o ácido a três vezes a mesma quantidade de ácido sulfúrico. Você tem nitroglicerina.

Sete minutos.

Tyler e eu na beira do telhado, o revólver na minha boca, e eu me pergunto

se o revólver estaria limpo.

Três minutos. Então alguém grita.

— Espere — é Marla atravessando o telhado na nossa direção. Marla só vem vindo porque Tyler se foi. Poof. Tyler é minha alucinação, não dela. Rápido como um truque de mágica, Tyler desaparece. E agora sou só um homem com a arma dentro da boca.

— Nós seguimos você — grita Marla. — Todo mundo do grupo de apoio. Não faça isso. Solte essa arma.

Atrás de Marla, todos os cânceres de bexiga, os parasitas de cérebro, o pessoal do melanoma e da tuberculose, vêm andando, mancando, em cadeira de rodas, na minha direção.

Eles dizem:

— Espere.

As vozes chegam a mim através do vento frio: — Pare.

— Podemos ajudar você.

— Deixe-nos ajudar você.

Do céu chega o whop, whop, whop dos helicópteros da polícia. Eu grito, vão embora. Saiam daqui. Este prédio vai explodir. Marla grita: — Nós sabemos.

É um momento de glória total para mim.

Não estou me matando, grito. Estou matando Tyler. Sou a Linha Dura de Joe. Lembro-me de tudo. — Não é amor nem nada disso — grita Marla—, mas acho que gosto de você também.

Um minuto.

Marla gosta de Tyler.

— Não, é de você — grita Marla. — Sei a diferença. E nada.

Nada explode.

Com o cano da arma enfiado na bochecha sobrevivente, digo, Tyler, você misturou a nitro com parafina, não foi?

Parafina nunca funciona.

Preciso fazer isto.

Os helicópteros da polícia.

E aperto o gatilho.

30

Na casa de meu Pai há muitas mansões.

É claro que, ao apertar o gatilho, eu morri. Mentiroso.

E Tyler morreu.

Com os helicópteros da polícia roncando na nossa direção, com Marla e o

pessoal do grupo de apoio que não ia se salvar, mas todos tentando salvar a mim,

eu tinha de apertar o gatilho.

Foi muito melhor que a vida real.

E o seu momento de perfeição não dura para sempre. Tudo no céu é branco no branco.

Fingido.

Tudo no céu é quieto, sapatos de solas de borracha. Consigo dormir no céu.

As pessoas escrevem para o céu para me dizer que se lembram de mim. Que sou o herói delas. Vai ficar ainda melhor. Os anjos daqui são aqueles do Antigo Testamento, legiões e lugares- tenentes, uma hoste celestial que trabalha em turnos, dias, períodos. Cemitério. Eles trazem as suas refeições e os seus medicamentos num copinho descartável. Um kit Vale das Bolinhas.

Conheci Deus na sua longa mesa de nogueira com seus diplomas pendurados na parede, e Ele me pergunta: — Por quê?

Por que causei tanto sofrimento?

Eu não percebia que cada um de nós é sagrado, um floquinho de neve único e especial em sua exclusividade?

Não via que somos todos manifestações do amor? Eu olhava para Deus atrás daquela mesa, tomando notas num bloquinho, mas Deus entendeu tudo errado.

Não somos especiais.

Também não somos merda nem lixo.

Apenas somos.

Apenas somos e o que acontece, acontece. E Deus diz:

— Não, isso não está certo.

É. Bom. Tudo bem. Não se pode ensinar nada a Deus. Deus me pergunta do que eu me lembro.

Eu não me lembro de nada.

A bala que saiu da arma de Tyler saiu pela outra bochecha e me rasgou um sorriso de orelha a orelha. É, como uma moranga de Haloween raivosa. Um demônio japonês. O Dragão da Avareza.

Marla ainda está na Terra e escreve para mim. Algum dia, diz ela, vai me levar de volta.

Se houvesse um telefone no céu, eu ligaria para Marla, e quando ela dissesse "Alô", eu não desligaria. Eu diria "Oi, como andam as coisas? Quero saber tudo, tintim por tintim".

Mas não quero voltar. Ainda não.

Porque não quero.

Porque o tempo todo aparece alguém trazendo meu lanche e meus remédios na bandeja, e esse alguém tem um olho preto, a testa inchada e costurada, e diz: — Sentimos sua falta, sr. Durden.

Ou outro de nariz quebrado passa por mim com um rodinho e sussurra:

— Tudo está de acordo com os planos. Sussurra:

— Vamos acabar com a civilização para construir um mundo melhor. Sussurra:

— Estamos providenciando para levá-lo de volta.



v2- Digitalizado por TailsApnea
`).then(e => console.log(`Código finalizado, ${e} mensagens enviadas`)).catch(console.error)
