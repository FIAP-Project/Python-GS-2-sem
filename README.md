# Projeto de Monitoramento de Energia

Este projeto é uma API Flask em Python que registra informações de energia gerada e calcula as médias de diferentes parâmetros energéticos. Os dados são armazenados em um arquivo JSON local e também podem ser acessados remotamente através de um servidor Railway e visualizados em um website dedicado.

## Sumário

- [Descrição do Projeto](#descrição-do-projeto)
- [Requisitos e Dependências](#requisitos-e-dependências)
- [Instruções de Instalação](#instruções-de-instalação)
- [Como Clonar o Projeto no PyCharm](#como-clonar-o-projeto-no-pycharm)
- [Executando e Testando a Aplicação Localmente](#executando-e-testando-a-aplicação-localmente)
- [Acessando o Projeto em Produção](#acessando-o-projeto-em-produção)
- [Autores](#autores)

## Descrição do Projeto

A API possui dois endpoints principais:

- **POST `/post_energy_info`**: Recebe dados de energia no formato JSON e os armazena no arquivo `energy_data.json`.
- **GET `/get_average_energy_generated`**: Calcula e retorna as médias dos parâmetros energéticos registrados.

Os parâmetros energéticos incluem:

- Força (`forca`)
- Pressão (`pressao`)
- Tensão (`tensao`)
- Energia (`energia`)

**Nota:** O projeto está atualmente rodando em um servidor Railway, permitindo acesso remoto contínuo à API. Os dados registrados estão sendo enviados e exibidos em um website dedicado, facilitando a visualização e análise.

- **Link da API no Railway**: https://python-gs-2-sem-production.up.railway.app
- **Link do Website**: https://gs-bice.vercel.app/

## Requisitos e Dependências

- **Python 3.6+**
- **Flask**
- **ngrok** (para exposição da API em rede pública, opcional)
- **Postman** (para testes de API, opcional)

## Instruções de Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/usuario/projeto-monitoramento-energia.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd projeto-monitoramento-energia
   ```

3. **Crie um ambiente virtual (opcional, mas recomendado)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   ```

4. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

   > **Nota**: Certifique-se de que o arquivo `requirements.txt` contém as dependências necessárias, como `Flask`.

## Como Clonar o Projeto no PyCharm

1. **Abra o PyCharm**.
2. **Selecione** `Get from Version Control` na tela inicial.
3. **Insira a URL do repositório**:

   ```
   https://github.com/usuario/projeto-monitoramento-energia.git
   ```

4. **Escolha o diretório de destino** e clique em `Clone`.
5. **Configure o interpretador Python**:
   
   - Vá em `File` > `Settings` > `Project` > `Python Interpreter`.
   - Selecione o ambiente virtual ou o interpretador Python desejado.

## Executando e Testando a Aplicação Localmente

### Executando a Aplicação

1. **No PyCharm ou terminal**, execute o aplicativo Flask:

   ```bash
   python app.py
   ```

2. **A aplicação estará disponível em** `http://127.0.0.1:5000/`.

### Testando com o Postman e Expondo com ngrok

Esta seção unifica as instruções para testar a aplicação localmente usando o Postman e expor a API para acesso remoto utilizando o ngrok.

#### Passo 1: Configurando o ngrok

O ngrok permite expor a aplicação local na internet.

1. **Baixe e instale o ngrok**:
   
   - Acesse [ngrok.com/download](https://ngrok.com/download) e siga as instruções de instalação para o seu sistema operacional.

2. **Inicie o ngrok** apontando para a porta da aplicação Flask (por padrão, 5000):

   ```bash
   ngrok http 5000
   ```

3. **Copie a URL fornecida pelo ngrok**, que será algo como `http://abcdef1234.ngrok.io`.

#### Passo 2: Testando os Endpoints com o Postman

##### Enviando Dados (POST)

1. **Abra o Postman**.
2. **Crie uma nova requisição** com o método `POST`.
3. **Defina a URL**:

   ```
   http://127.0.0.1:5000/post_energy_info
   ```

   - **Ou**, se estiver usando o ngrok para acesso remoto, substitua pela URL do ngrok:

     ```
     http://abcdef1234.ngrok.io/post_energy_info
     ```

4. **No corpo da requisição**, selecione `raw` e o tipo `JSON`.
5. **Insira o JSON com os dados**:

   ```json
   {
     "forca": 10.5,
     "pressao": 5.2,
     "tensao": 220,
     "energia": 50
   }
   ```

6. **Envie a requisição** e verifique a resposta. Deve retornar uma resposta JSON indicando sucesso:

   ```json
   {
     "status": "success",
     "data": {
       "forca": 10.5,
       "pressao": 5.2,
       "tensao": 220,
       "energia": 50
     }
   }
   ```

##### Obtendo as Médias (GET)

1. **Crie uma nova requisição** com o método `GET`.
2. **Defina a URL**:

   ```
   http://127.0.0.1:5000/get_average_energy_generated
   ```

   - **Ou**, se estiver usando o ngrok:

     ```
     http://abcdef1234.ngrok.io/get_average_energy_generated
     ```

3. **Envie a requisição** e verifique as médias retornadas. Deve retornar algo como:

   ```json
   {
     "forca_average": 10.5,
     "pressao_average": 5.2,
     "tensao_average": 220.0,
     "energia_average": 50.0
   }
   ```

> **Dica:** Utilize o ngrok se desejar testar a API a partir de dispositivos externos ou compartilhar o endpoint para testes colaborativos.

## Acessando o Projeto em Produção

O projeto está em execução em um servidor **Railway**, permitindo acesso à API e ao website de qualquer lugar, sem a necessidade de executar o aplicativo localmente.

### Endpoints no Railway

- **API Base URL**: https://python-gs-2-sem-production.up.railway.app

#### Enviando Dados para a API no Railway

1. **No Postman**, crie uma nova requisição `POST`.
2. **Defina a URL**:

   ```
   https://python-gs-2-sem-production.up.railway.app/post_energy_info
   ```

3. **Configure o corpo da requisição** conforme as instruções anteriores.
4. **Envie a requisição** e verifique a resposta.

#### Obtendo Médias da API no Railway

1. **No Postman**, crie uma nova requisição `GET`.
2. **Defina a URL**:

   ```
   https://python-gs-2-sem-production.up.railway.app/get_average_energy_generated
   ```

3. **Envie a requisição** e verifique as médias retornadas.

### Visualizando os Dados no Website

Os dados coletados pela API são exibidos em um website dedicado.

- **Link do Website**: https://gs-bice.vercel.app/

No website, você pode:

- Visualizar parte dos dados coletados.

## Autores

- **Felipe Cerboncini Cordeiro** - RM: 554909
- **Pedro Henrique Martins Alves dos Santos** - RM: 558107
- **Victor de Almeida Gonçalves** -  RM: 558799

---

Qualquer dúvida ou problema, sinta-se à vontade para entrar em contato com os autores.