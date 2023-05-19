# CRUD de Agenda de Contatos

Este é um programa em Python que permite gerenciar uma agenda de contatos através de operações de criação, leitura, atualização e exclusão (CRUD). Os contatos são armazenados em um arquivo JSON chamado "agenda.json".

## Funcionalidades

O programa oferece as seguintes funcionalidades:

1. **Adicionar Contato:** Permite adicionar um novo contato à agenda, solicitando informações como nome, telefone, e-mail, conta do Twitter e @ do Instagram.

2. **Listar Contatos:** Exibe todos os contatos presentes na agenda, mostrando as informações de cada contato.

3. **Excluir Contato:** Permite remover um contato da agenda, informando o nome do contato a ser excluído.

4. **Atualizar Contato:** Permite atualizar as informações de um contato existente na agenda, solicitando o nome do contato a ser atualizado e as novas informações como telefone, e-mail, Twitter e Instagram.

5. **Pesquisar Contato:** Permite pesquisar um contato específico na agenda, informando o nome do contato. Exibe as informações do contato se encontrado, caso contrário, exibe uma mensagem informando que o contato não foi encontrado.

6. **Pesquisar Todos os Contatos:** Exibe todos os contatos presentes na agenda, mostrando as informações de cada contato.

7. **Sair:** Encerra o programa.

## Utilização

1. Certifique-se de ter o Python instalado em seu sistema.

2. Faça o download do código-fonte e abra o terminal na pasta do projeto.

3. Execute o seguinte comando para iniciar o programa:

4. Será exibido um menu com as opções disponíveis. Escolha uma opção digitando o número correspondente e siga as instruções exibidas no terminal.

5. Após realizar uma ação, o menu será exibido novamente para que você possa escolher uma nova opção. Para sair do programa, escolha a opção "7. Sair".

## Requisitos

- Python 3.x
- Arquivo "agenda.json" (será criado automaticamente se não existir)

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para fazer sugestões, relatar problemas ou enviar pull requests para aprimorar este programa.

### Sugestões para melhorias


- Validação de entrada: Adicione validações de entrada para garantir que os campos obrigatórios sejam preenchidos adequadamente. Por exemplo, verifique se o nome do contato não está em branco antes de adicionar ou atualizar um contato.

- Tratamento de exceções: Adicione tratamento de exceções para lidar com possíveis erros durante a leitura, gravação e manipulação do arquivo JSON. Isso ajudará a evitar que o programa seja interrompido abruptamente em caso de problemas.

- Organização do código: Considere dividir o código em funções mais específicas e bem definidas para facilitar a leitura, manutenção e reutilização do código. Isso também ajudará a separar as responsabilidades de cada função.

- Melhorias na apresentação dos dados: Explore diferentes formas de exibir as informações dos contatos, como formatar a exibição dos números de telefone ou datas de uma maneira mais amigável.

- Opções adicionais: Se desejar expandir a funcionalidade do programa, você pode considerar adicionar recursos como pesquisa avançada por critérios específicos, ordenação dos contatos, filtragem por campos, entre outros.

- Testes unitários: Implemente testes unitários para verificar se as funções do programa estão funcionando corretamente. Isso ajudará a identificar e corrigir erros mais rapidamente.

Essas são apenas algumas sugestões para melhorar o código existente. Você pode adaptar e implementar as melhorias de acordo com suas necessidades e preferências.







## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
