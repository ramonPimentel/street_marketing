### Projeto de Feira Livres.

Esse serviço tem a responsabilidade de gerenciar as feiras livres via api. Aonde quem irá consumir esse sistema poderá buscar uma feira livre pelo os campos (distrito, regiao5, nome_feira, bairro) e também será possível editar, remover e criar.

O banco da aplicação segue a mesma nomenclatura da planilha, com o nome da tabela e os campo em português. Visando que a aplicação continue falando na mesma linguagem do sistema que fez a geração da planilha.

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

Com ambas as dependências mencionadas já instaladas, basta rodar o comando `docker-compose build server` para que as dependências do projeto sejam instaladas e o ambiente seja montado. Esse procedimento só precisa ser feito na primeira vez que o projeto é clonado do repositório ou quando outro desenvolvedor incluiu uma nova dependência que ainda não foi instalada no seu ambiente virtual do Docker.

Finalizado o processo de build, basta rodar o comando `docker-compose up server` todas as vezes que precisar rodar o projeto localmente.

 O comando `docker-compose up` levantará os serviços do Mongo, FastApi através do endereço http://localhost:9000.

### Para rodar o import do csv

Para rodar o import do csv basta fazer o passo anterior e rodar o seguinte comando: `docker-compose run server bash -c "make run-import"`

### Para rodar os testes

Temos 2 formas no qual podemos rodar os testes:

- Github Action
Foi implementado uma action no github no qual rodamos os testes e mostramos o coverage [link dos builds dos tests](https://github.com/ramonPimentel/street_marketing/actions).

- Rodar localmente:
Com ambas as dependências mencionadas já instaladas, basta rodar o comando `docker-compose build test` para que as dependências do projeto sejam instaladas e o ambiente seja montado. Esse procedimento só precisa ser feito na primeira vez que o projeto é clonado do repositório ou quando outro desenvolvedor incluiu uma nova dependência que ainda não foi instalada no seu ambiente virtual do Docker.

Finalizado o processo de build, basta rodar o comando `docker-compose up test` todas as vezes que precisar rodar os testes.

No qual rodamos os testes e geramos o coverage no arquivo `coverage.xml` e também um output no terminal.

```
Name                                                Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------------
app/models/street_marketing_model.py                   27      0   100%
app/repositories/base_repository.py                    18      0   100%
app/repositories/street_market_repository.py           18      0   100%
app/routes/street_marketing_router.py                  51      0   100%
app/schemas/update_street_marketing_schema.py          25      0   100%
app/use_cases/create_street_marketing.py               19      0   100%
app/use_cases/delete_street_marketing.py               19      0   100%
app/use_cases/find_street_marketing.py                 14      0   100%
app/use_cases/import_street_marketing_from_csv.py      35      0   100%
app/use_cases/search_street_marketing.py               25      0   100%
app/use_cases/update_sreet_marketing.py                21      0   100%
app/utils/logger.py                                    12      0   100%
---------------------------------------------------------------------------------
TOTAL                                                 284      0   100%
Coverage XML written to file coverage.xml
```

### Documentação

- Swagger

  No projetos usamos o swagger para a documentação da api no qual podemos ver os endpoint(schemas e responses) e interagir com eles.

  Para rodar bastar seguir o passo `Rodar o projeto localmente` e acessar as docs no seguinte endpoint `http://localhost:9000/docs`.

- Postman

  Podemos usar o postman para fazer os testes via api. No link abaixo explica como importamos o schema.

  [Como importar o schema](https://learning.postman.com/docs/designing-and-developing-your-api/importing-an-api/#importing-api-schemas)

  ```
{"openapi":"3.0.2","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/feira_livres":{"get":{"tags":["feira livres"],"summary":"Index","operationId":"index_feira_livres_get","parameters":[{"required":false,"schema":{"title":"Distrito","type":"string"},"name":"distrito","in":"query"},{"required":false,"schema":{"title":"Regiao5","type":"string"},"name":"regiao5","in":"query"},{"required":false,"schema":{"title":"Nome Feira","type":"string"},"name":"nome_feira","in":"query"},{"required":false,"schema":{"title":"Bairro","type":"string"},"name":"bairro","in":"query"},{"required":false,"schema":{"title":"Pagina Proxima","type":"string"},"name":"pagina_proxima","in":"query"},{"required":false,"schema":{"title":"Pagina Anterior","type":"string"},"name":"pagina_anterior","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}},"post":{"tags":["feira livres"],"summary":"Create","operationId":"create_feira_livres_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}},"required":true},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/feira_livres/{registro}":{"get":{"tags":["feira livres"],"summary":"Show","operationId":"show_feira_livres__registro__get","parameters":[{"required":true,"schema":{"title":"Registro","type":"string"},"name":"registro","in":"path"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}},"put":{"tags":["feira livres"],"summary":"Update","operationId":"update_feira_livres__registro__put","parameters":[{"required":true,"schema":{"title":"Registro","type":"string"},"name":"registro","in":"path"}],"requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/UpdateStreetMarketingSchema"}}},"required":true},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}},"delete":{"tags":["feira livres"],"summary":"Delete","operationId":"delete_feira_livres__registro__delete","parameters":[{"required":true,"schema":{"title":"Registro","type":"string"},"name":"registro","in":"path"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"HTTPValidationError":{"title":"HTTPValidationError","type":"object","properties":{"detail":{"title":"Detail","type":"array","items":{"$ref":"#/components/schemas/ValidationError"}}}},"StreetMarketing":{"title":"StreetMarketing","required":["long","lat","setcens","areap","cod_dist","distrito","cod_subpref","subpref","regiao5","regiao8","nome_feira","registro","logradouro","numero","bairro","referencia"],"type":"object","properties":{"_id":{"title":" Id","type":"string"},"long":{"title":"Long","type":"integer"},"lat":{"title":"Lat","type":"integer"},"setcens":{"title":"Setcens","type":"integer"},"areap":{"title":"Areap","type":"integer"},"cod_dist":{"title":"Cod Dist","type":"integer"},"distrito":{"title":"Distrito","type":"string"},"cod_subpref":{"title":"Cod Subpref","type":"integer"},"subpref":{"title":"Subpref","type":"string"},"regiao5":{"title":"Regiao5","type":"string"},"regiao8":{"title":"Regiao8","type":"string"},"nome_feira":{"title":"Nome Feira","type":"string"},"registro":{"title":"Registro","type":"string"},"logradouro":{"title":"Logradouro","type":"string"},"numero":{"title":"Numero","type":"string"},"bairro":{"title":"Bairro","type":"string"},"referencia":{"title":"Referencia","type":"string"}}},"UpdateStreetMarketingSchema":{"title":"UpdateStreetMarketingSchema","type":"object","properties":{"long":{"title":"Long","type":"integer"},"lat":{"title":"Lat","type":"integer"},"setcens":{"title":"Setcens","type":"integer"},"areap":{"title":"Areap","type":"integer"},"cod_dist":{"title":"Cod Dist","type":"integer"},"distrito":{"title":"Distrito","type":"string"},"cod_subpref":{"title":"Cod Subpref","type":"integer"},"subpref":{"title":"Subpref","type":"string"},"regiao5":{"title":"Regiao5","type":"string"},"regiao8":{"title":"Regiao8","type":"string"},"nome_feira":{"title":"Nome Feira","type":"string"},"logradouro":{"title":"Logradouro","type":"string"},"bairro":{"title":"Bairro","type":"string"},"numero":{"title":"Numero","type":"string"},"referencia":{"title":"Referencia","type":"string"}}},"ValidationError":{"title":"ValidationError","required":["loc","msg","type"],"type":"object","properties":{"loc":{"title":"Location","type":"array","items":{"anyOf":[{"type":"string"},{"type":"integer"}]}},"msg":{"title":"Message","type":"string"},"type":{"title":"Error Type","type":"string"}}}}}}
```

### Logs

Os logs da aplicação ficam armazenados no arquivo logger.txt na raiz do projeto. Todo o log da aplicação é escrito nesse arquivo.

### Melhorias

- Separar os modelos de Distrito, Endereço e Subprefe da entidade de FeiraLivres.
- Implementar cache no endpoint de busca.
- Implementar autenticação nos endpoints da api.
- Colocar um engine de busca.