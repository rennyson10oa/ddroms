<p align="center">
  <img src="assets/ddroms icon.png">
<br>
<a href="#Linux"><img src="https://img.shields.io/badge/os-linux-brightgreen">
<a href="#Windows"><img src="https://img.shields.io/badge/os-windows-yellowgreen">
<br>
<a href="https://github.com/sweetbbak"><img src="https://img.shields.io/badge/creator-sweet-green"></a>
<br>
</p>

<p align="center">
<a href="#python"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<a href="#linux"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<a href="windows"><img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">
</p>

<h3 align="center">
DDroms e a ferramenta perfeita para baixar seus jogos
</h3>

Com o `ddroms`, é possível baixar roms de diversos consoles disponíveis em nosso catálogo, além de ter um funcionamento simples e eficiente, facilitando sua vida quando quiser jogar alguns jogos. Os arquivos são obtidos da página no-intro rom sets (2024) https://archive.org/details/ni-romsets

## Tabela de conteudos

- [Instalacao](#Instalacao)
- [Como usar](#Exemplos)
- [Bugs e mais avisos bacanas](#bugs-e-mais-avisos-bacanas)

## Instalação

Primeiro de tudo certifique-se de ter a versão mais recente do python instalada em sua máquina, baixe pelo site oficial do python:

```sh
https://www.python.org/downloads/
```

Após isso baixe o arquivo zip na página de `realeses`:

<a href="https://github.com/rennyson10oa/ddroms/releases">Página de releases</a>

 
Quando baixar, apenas descompacte o arquivo zip que conterá dois arquivos: `ddroms.py, requirements.txt`

abra um terminal nessa pasta e siga as instruções de acordo com seu sistema operacional:

`Windows`

```sh
pip install requirements.txt
python ddroms.py
```

`Linux`

```sh
pip3 install requirements.txt
python3 ddroms.py
```
Na realidade o primeiro comando é apenas para baixar as bibliotecas e o segundo é para rodar o programa em si

## Exemplos

Dentro da tela do app, você será apresentado a 2 opções. Na primeira, você irá baixar TODAS as roms de TODOS os consoles disponíveis. Na segunda, poderá escolher um console específico. Caso escolha a 1ª opção, esteja preparado para ter uma grande quantidade de espaço do seu PC tomado, além de esse processo demorar bastante.

![Página inicial do DDRoms](assets/inicial.png)

Caso escolha a segunda opção, lhe será mostrada uma lista de todos os consoles, e você deve digitar o número correspondente ao console escolhido.

![Escolha de console](assets/escolha%20de%20console.png)

dica: `caso queira rolar para cima no windows ou linux usando as teclas do teclado, segure shift + seta pra cima ou seta para baixo :)`

Após escolher o console voce podera escolher uma das 4 opções abaixo, onde:

`1 - você baixa tudo desse console, simples assim`

`2 - você ve as roms que o console oferece e decide se quer baixa-las`

`3 - escolhe outro console`

`4 - é possivel baixar uma porcentagem do total de roms, por exemplo, se um console tem 70 mb no total de roms vocé pode baixar apenas 20% disso, ou 50%, 2%, vocé decide`

![Escolha de console](assets/escolha%20de%20download.png)

Tambem é possivel ver quanto GB/MB um console tem:

![Tamanho das roms](assets/roms.png)

> [!AVISO]\
> Atualmente, eu ainda estou desenvolvendo essa bagaça (sozinho), então podem acontecer bugs e 
> outras coisas estranhas que eu vou listar aqui embaixo, além de que no futuro tenho o desejo de 
> adicionar outras funções, como buscar roms de jogos específicos, ou recomendar alguns 
> emuladores de outras plataformas, ou até baixar tais emuladores no seu PC de forma automática.

## Bugs e mais avisos bacanas

Como disse antes, eu estou desenvolvendo isso sozinho, então obviamente alguns bugs podem ocorrer, e se ocorrerem, seria de grande ajuda se você me mandasse uma mensagem avisando sobre isso.

Não tenho nenhum servidor onde eu poderia estar hospedando essas roms, e atualmente esse programa faz web scraping da página do archive.org. Essa página em si é um pouco lenta, então coisas como: downloads falhando e demora para baixar alguma rom podem ser recorrentes.

Outra coisa interessante de se lembrar é que no meio dessas roms tem algumas bios, então ao baixar as roms de algum console, você leva de brinde as bios (mas não posso garantir que elas funcionam, já que nem eu testei todas).
