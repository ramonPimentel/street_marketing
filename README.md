### Projeto de Feira Livres.

Esse serviço tem a responsabilidade de gerenciar as feiras livres via api. Aonde quem irá consumir esse sistema poderá buscar uma feira livre pelo os campos (distrito, regiao5, nome_feira, bairro) e também será possível editar, remover e criar.

### Tecnologias utilizadas

Para essa aplicação usamos as seguintes tecnologias:

- **Docker**
- **Python:** Linguagem
- **FastApi:** Framework web
- **Mongo:** Banco de Dados

### Dependências para rodar o projeto

Esse projeto utiliza o docker para preparar o ambiente de desenvolvimento, por isso é importante ter o Docker e o Docker Compose instalados na sua máquina. Caso não os tenha, confira a documentação a seguir:

 - [Como instalar o Docker](https://docs.docker.com/engine/install/)
 - [Como instalar o Docker Compose](https://docs.docker.com/compose/install/)

### Rodar o projeto localmente

Com ambas as dependências mencionadas já instaladas, basta rodar o comando `docker-compose build` para que as dependências do projeto sejam instaladas e o ambiente seja montado. Esse procedimento só precisa ser feito na primeira vez que o projeto é clonado do repositório ou quando outro desenvolvedor incluiu uma nova dependência que ainda não foi instalada no seu ambiente virtual do Docker.

Finalizado o processo de build, basta rodar o comando `docker-compose up server` todas as vezes que precisar rodar o projeto localmente.

 O comando `docker-compose up` levantará os serviços do Mongo, FastApi através do endereço http://localhost:9000.

