# Commands used in Docker
    DOCKER HUB: Repositório onde ficam armazenados as imagens.

    - docker ps: Comando para listar os containers rodando;
    - docker ps -a: Comando para listar os containers rodando;
    - docker images: Comando para exibir as imagens que estão rodando;
    - docker volume ls: Comando para visulizar os volumes;
    - docker rm + ID do container: Comando para deletar um container com o ID informado;
    - docker rmi: Comando para deletar uma imagem;
    - docker run + nome_do_arquivo: Comando para dar o start;
    - docker build --tag + nome da imagem . : Comando para criar uma imagem;
    - docker inspect + id_container: Comando para visualizar as informações detalhadas do container;
    - docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=passwor -p 3306:3306 -v mysqlVolume:/var/lib/mysql -d mysql:version: Comando para criar um volume do mysql pareando a porta 3306;

# Commands used in Python/ Framework
    - python -m venv venv: Comando para instalar ambiente virtual;
    - pip install Flask: Comando para Instalar o Flask;
    - pip freeze > requirements.txt: Comando para criar o arquivo com as dependências;
    - pip install -r requirements.txt: Comando para instalar as dependências contidas no arquivo "requirements.txt";
    - pip install pre-commit: Comando para instalar a ferramenta de "pre-commit";
    - pip install SQLAlchemy: Comando para instalar o SQLAlchemy;
    - pre-commit install: Comando para instalar o pre-commit;
    - pip install PyMySQL: Comando para instalar a biblioteca do MySQL;
    - pip install cryptography: Comando para instalar a biblioteca de criptografia;
