# Desafio de Software

# Instruções para executar a aplicação
## Clone o repositório
git clone 'git@github.com:JoaoPauloAntunes/desafio-software.git'

## Executar os comandos na pasta raiz do repositório
`pip install pipenv
pipenv install fastapi
pipenv install --python 3.6 fastapi
pipenv run software`

# Tarefas
- [x] usar o framework FastAPI no servidor
- [x] coletar >= 50 cores aleatórias da API Random Color
- [x] usar os objetos de cores coletados para fazer um gráfico de ID da cor em função da posição da cor na lista
- [ ] configurar a aplicação para salvar arquivo no servidor listando cores da lista que não repetiram
	- [x] obter cores exclusivas filtrando as cores
	- [ ] enviar via POST string cores exclusivas para o servidor
	- [x] processar a string enviada e criar arquivo de cores exclusivas
- [x] exibir no gráfico as cores que tem pelo menos 50% de vermelho
- [ ] salvar a listagem de cores não repetidas no banco SQL
