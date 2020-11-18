# Docker + ELK
---------
Esse módulo do repositório tem por objetivo oferecer as configurações necessárias para o elastic rodar junto do kibana e logstash. Neste repositório as pastas **data**, **pipeline** e **eslasticsearch** são pastas que serão lincadas aos containers do **logstash** e **elasticsearch**, respectivamente.

- Na pasta **data** devem estar os dados que serão lidos pelo **logstash** que ficaram disponíveis no **kibana**;
- Na pasta **pipeline** ficam os arquivos de configuração que manipulam os dados da pasta **data**;
- Na pasta **elasticsearch** é uma pasta de persistência para guardar todas as alterações que foram feitas dentro do **kibana**
---------
## Para executar esse projeto

### Requisitos
* [Docker](https://docs.docker.com/get-docker/);
* [Docker-compose](https://docs.docker.com/compose/install/);

### Executando
Antes de executar o projeto crie as pastas **data** e **eslasticsearch**, caso não existam. Após isso, basta executar os comando a seguir:
```sh
# Assumindo que já esteja na pasta onde está o `docker-compose.yml´
$ docker-compose up
```
e para desativar basta usar o comando:
```sh
$ docker-compose down
```
