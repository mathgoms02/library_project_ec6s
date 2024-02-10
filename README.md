# Projeto Literapice - Loja Virtual de Livros

## Descrição

O Projeto Literapice é uma loja virtual de livros desenvolvida em Python, utilizando a biblioteca Tkinter para a interface gráfica e o MySQL para o armazenamento de dados. O objetivo é oferecer uma experiência interativa ao usuário, permitindo a navegação pela lista de livros disponíveis, a adição de itens ao carrinho, a visualização do carrinho e a análise estatística dos gastos.

## Funcionalidades

### Tela Inicial (`tela_home`)

- **Conexão com Banco de Dados:** Conecta-se ao banco de dados para recuperar os livros disponíveis para o usuário logado.
  
- **Interface Gráfica:** Exibe uma janela principal com informações de boas-vindas e uma tabela mostrando os livros disponíveis.
  
- **Botões de Navegação:** Fornece botões para navegar até a loja de livros (`to_loja`), visualizar estatísticas de gastos (`to_estatistica`), e restaurar a tabela de livros disponíveis.

### Loja de Livros (`tela_livros`)

- **Conexão com Banco de Dados:** Conecta-se ao banco de dados para recuperar todos os livros disponíveis.
  
- **Interface Gráfica:** Exibe uma janela com uma tabela dos livros, permitindo a pesquisa por título e a adição de livros ao carrinho.
  
- **Botões de Ação:** Oferece botões para pesquisar livros (`botao_pesquisar`), adicionar livros ao carrinho (`add_carrinho`), e visualizar o carrinho (`to_carrinho`).

### Carrinho (`tela_carrinho`)

- **Interface Gráfica:** Mostra os itens no carrinho do usuário.
  
- **Ações no Carrinho:** Permite remover itens do carrinho (`tirar_carrinho`), adquirir os itens no carrinho (`adquirir`), e voltar à lista de livros disponíveis (`voltar_lista`).

### Estatísticas (`tela_estatistica`)

- **Conexão com Banco de Dados:** Conecta-se ao banco de dados para calcular estatísticas de gastos do usuário.
  
- **Interface Gráfica:** Exibe as estatísticas, incluindo total gasto, média de gastos, moda, mediana e desvio padrão.

## Uso

1. **Pré-requisitos:**
   - Instale o Python.
   - Configure um servidor MySQL e ajuste as credenciais no código.

2. **Execução:**
   - Execute o script principal `main.py` para iniciar a aplicação.

3. **Funcionalidades:**
   - Navegue pela lista de livros, adicione itens ao carrinho, visualize o carrinho e analise as estatísticas de gastos.

## OBS

- **Para vizualizar o código, basta entrar na branding master.
