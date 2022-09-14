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

### Para rodar os testes

Temos 2 formas no qual podemos rodar os testes, foi implementado uma action no github no qual rodamos os testes e mostramos o coverage [link dos builds dos tests](https://github.com/ramonPimentel/street_marketing/actions).

Para rodar localmente basta executar o seguinte comendo `docker-compose run server bash -c "make coverage"`, no qual rodamos os testes e geramos o coverage no arquivo `coverage.xml` e também um output no terminal.

```
Name                                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------------------
app/exceptions/aplication_exception.py            15      1    93%   34
app/models/street_marketing_model.py              29      2    93%   29-30
app/repositories/base_repository.py               14      0   100%
app/repositories/street_market_repository.py      25      3    88%   25, 40-52
app/use_cases/create_street_marketing.py          19      0   100%
app/use_cases/delete_street_marketing.py          19      0   100%
app/use_cases/search_street_marketing.py          25     25     0%   1-40
app/use_cases/update_sreet_marketing.py           20      0   100%
app/utils/logger.py                               13      0   100%
----------------------------------------------------------------------------
TOTAL                                            179     31    83%
```

### Documentação

- Swagger

  No projetos usamos o swagger para a documentação da api no qual podemos ver os endpoint(schemas e responses) e interagir com eles.

  Para rodar bastar seguir o passo `Rodar o projeto localmente` e acessar as docs no seguinte endpoint `http://localhost:9000/docs`.

- Postman

  Podemos usar o postman para fazer os testes via api. No link abaixo explica como importamos o schema.

  [Como importar o schema](https://learning.postman.com/docs/designing-and-developing-your-api/importing-an-api/#importing-api-schemas)

  ```
  {"openapi":"3.0.2","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/street_marketing":{"get":{"summary":"Index","operationId":"index_street_marketing_get","parameters":[{"required":false,"schema":{"title":"District","type":"string"},"name":"district","in":"query"},{"required":false,"schema":{"title":"Region5","type":"string"},"name":"region5","in":"query"},{"required":false,"schema":{"title":"Name","type":"string"},"name":"name","in":"query"},{"required":false,"schema":{"title":"Neighborhood","type":"string"},"name":"neighborhood","in":"query"},{"required":false,"schema":{"title":"Next Page","type":"string"},"name":"next_page","in":"query"},{"required":false,"schema":{"title":"Prev Page","type":"string"},"name":"prev_page","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}},"post":{"summary":"Create","operationId":"create_street_marketing_post","requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}},"required":true},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/street_marketing/{id}":{"get":{"summary":"Show","operationId":"show_street_marketing__id__get","parameters":[{"required":true,"schema":{"title":"Id","type":"string"},"name":"id","in":"path"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}},"put":{"summary":"Index","operationId":"index_street_marketing__id__put","parameters":[{"required":true,"schema":{"title":"Id","type":"integer"},"name":"id","in":"path"}],"requestBody":{"content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}},"required":true},"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/StreetMarketing"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}},"delete":{"summary":"Delete","operationId":"delete_street_marketing__id__delete","parameters":[{"required":true,"schema":{"title":"Id","type":"integer"},"name":"id","in":"path"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"HTTPValidationError":{"title":"HTTPValidationError","type":"object","properties":{"detail":{"title":"Detail","type":"array","items":{"$ref":"#/components/schemas/ValidationError"}}}},"StreetMarketing":{"title":"StreetMarketing","type":"object","properties":{"_id":{"title":" Id","type":"string"},"codigo":{"title":"Codigo","type":"integer"},"long":{"title":"Long","type":"integer"},"lat":{"title":"Lat","type":"integer"},"setcens":{"title":"Setcens","type":"integer"},"areap":{"title":"Areap","type":"integer"},"cod_dist":{"title":"Cod Dist","type":"integer"},"distrito":{"title":"Distrito","type":"string"},"cod_subpref":{"title":"Cod Subpref","type":"integer"},"regiao5":{"title":"Regiao5","type":"string"},"regiao8":{"title":"Regiao8","type":"string"},"nome_feira":{"title":"Nome Feira","type":"string"},"registro":{"title":"Registro","type":"string"},"logradouro":{"title":"Logradouro","type":"string"},"bairro":{"title":"Bairro","type":"string"},"referencia":{"title":"Referencia","type":"string"}}},"ValidationError":{"title":"ValidationError","required":["loc","msg","type"],"type":"object","properties":{"loc":{"title":"Location","type":"array","items":{"anyOf":[{"type":"string"},{"type":"integer"}]}},"msg":{"title":"Message","type":"string"},"type":{"title":"Error Type","type":"string"}}}}}}
```

### Logs

Os logs da aplicação ficam armazenados no arquivo logger.txt na raiz do projeto. Todo o log da aplicação é escrito nesse arquivo.

### Melhorias

- Separar os modelos de Distrito, Endereço e Subprefe da entidade de FeiraLivres.
- Implementar cache no endpoint de busca.
- Implementar autenticação nos endpoints da api.
- Colocar um engine de busca.