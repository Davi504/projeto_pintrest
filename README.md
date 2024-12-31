# Fake Pinterest

## Descrição
O Fake Pinterest é uma plataforma inovadora de compartilhamento de imagens inspirada no famoso Pinterest. Este projeto foi criado com o intuito de fornecer aos usuários um espaço virtual onde possam expressar suas inspirações visuais e compartilhar suas fotos com uma comunidade diversificada.

### Objetivo
O principal objetivo do Fake Pinterest é criar uma interface amigável e intuitiva que permita aos usuários fazer upload de imagens facilmente, criar perfis personalizados e interagir com outros membros da comunidade. A plataforma visa ser um local de criatividade e inspiração, onde pessoas de todas as idades e interesses podem explorar e compartilhar suas paixões visuais.

### Público-alvo
O Fake Pinterest é destinado a qualquer pessoa interessada em descobrir e compartilhar conteúdo visual. Desde artistas e fotógrafos até pessoas em busca de novas ideias para projetos pessoais, a plataforma oferece algo para todos.

### Diferenciais
O que diferencia o Fake Pinterest de outras plataformas similares é a sua simplicidade e foco na experiência do usuário. Utilizando o framework Flask, o projeto é desenvolvido de forma modular e leve, permitindo atualizações e melhorias contínuas sem complicações. Além disso, a interface responsiva garante que os usuários tenham uma experiência fluida, independentemente do dispositivo que estejam utilizando.

### Futuras Melhorias
Planejamos continuar expandindo as funcionalidades do Fake Pinterest, incluindo a possibilidade de criar álbuns temáticos, realizar buscas avançadas por imagens e implementar um sistema de curadoria de conteúdo para destacar as melhores fotos da comunidade. Nosso compromisso é sempre ouvir o feedback dos usuários e evoluir a plataforma para atender às suas necessidades e expectativas.

## Processo de Desenvolvimento
O desenvolvimento deste projeto foi dividido em várias etapas:
1. **Planejamento e design do banco de dados**: Estruturação das tabelas e relações.
2. **Implementação do backend usando Flask**: Desenvolvimento das APIs e lógica do servidor.
3. **Desenvolvimento do frontend com HTML, CSS e JavaScript**: Criação da interface do usuário.
4. **Integração do frontend e backend**: Conexão das funcionalidades entre cliente e servidor.
5. **Testes e depuração**: Garantia de qualidade e correção de bugs.
6. **Implantação do projeto em um servidor**: Configuração para produção.

## Funcionalidades
- Upload de imagens.
- Sistema de login e registro de usuários.
- Interface responsiva.
- Capacidade de curtir e comentar nas fotos (nova funcionalidade).

## Problemas e Soluções
### Problema:
Tive dificuldade para entender o Flask por ser um framework novo para mim. Embora ele seja simples, foi um desafio inicial. Além disso, descobri que o Flask é fragmentado, diferente do Django que oferece uma estrutura mais pronta.

### Solução:
A simplicidade do Flask facilitou a resolução dos problemas iniciais. Investi tempo em estudar a documentação e as melhores práticas para organizar o projeto de forma eficiente.

## Tecnologias Utilizadas
[![My Skills](https://skillicons.dev/icons?i=html,css,javascript,react,nodejs,npm)](https://skillicons.dev)

## Como Rodar o Projeto na Sua Máquina
1. Clone este repositório:
    ```bash
    git clone https://github.com/Davi504/projeto_pintrest.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd projeto_pintrest
    ```
3. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # No Windows use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Crie o banco de dados executando o arquivo `criar_banco.py`:
    ```bash
    python criar_banco.py
    ```
6. Configure as variáveis de ambiente necessárias.
7. Execute o servidor Flask rodando o arquivo `main.py`:
    ```bash
    python main.py
    ```
8. Acesse o projeto no seu navegador em `http://127.0.0.1:5000`.

## Licença
Este projeto é licenciado sob os termos da licença MIT.
