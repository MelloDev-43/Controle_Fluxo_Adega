Sistema de Controle de Estoque

Descrição

Este repositório contém o código de um sistema de controle de estoque desenvolvido como parte de um projeto acadêmico. O objetivo principal foi criar uma aplicação com interface gráfica intuitiva para gerenciar o fluxo de inventário, utilizando Python e SQLite. O sistema é ideal para pequenas e médias empresas que buscam uma solução acessível para controle de estoque.

Funcionalidades

- Cadastro de produtos com campos como nome, categoria, quantidade e preço.
- Atualização de estoque em tempo real.
- Relatórios detalhados sobre o status do inventário.
- Interface gráfica desenvolvida com Tkinter.
- Banco de dados relacional utilizando SQLite.

Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Interface Gráfica:** Tkinter
- **Banco de Dados:** SQLite
- **Controle de Versão:** Git

Requisitos de Instalação

Certifique-se de ter o Python instalado em sua máquina. Você pode instalar as dependências necessárias utilizando o arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/sistema-controle-estoque.git
```

2. Acesse o diretório do projeto:

```bash
cd sistema-controle-estoque
```

3. Execute o script principal:

```bash
python main.py
```

A interface gráfica será aberta, permitindo que você comece a usar o sistema.

Estrutura do Projeto

```
sistema-controle-estoque/
├── main.py
├── database/
│   └── estoque.db
├── gui/
│   └── interface.py
├── models/
│   └── produto.py
├── README.md
└── requirements.txt
```

- **main.py:** Arquivo principal para executar a aplicação.
- **database/estoque.db:** Banco de dados SQLite utilizado pelo sistema.
- **gui/interface.py:** Arquivo que gerencia a interface gráfica.
- **models/produto.py:** Modelo de dados para o produto.

Contribuições

Contribuições são bem-vindas! Siga os passos abaixo para colaborar:

1. Realize um fork deste repositório.
2. Crie uma branch para sua feature ou correção de bug:

```bash
git checkout -b minha-feature
```

3. Faça commit das suas alterações:

```bash
git commit -m "Adicionar minha feature"
```

4. Envie para o repositório remoto:

```bash
git push origin minha-feature
```

5. Abra um pull request.

Autor

Desenvolvido por Cauan Mello. Para mais informações, visite meu [LinkedIn](http://www.linkedin.com/in/cauandev).

Licença

Este projeto está licenciado sob os termos da MIT License. Consulte o arquivo `LICENSE` para mais detalhes.


