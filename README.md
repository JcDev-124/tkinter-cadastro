# Cadastro de Usuários - Projeto de Interface Gráfica

Este projeto consiste em uma interface gráfica de cadastro de usuários utilizando a biblioteca `tkinter` para o design da interface e `PIL` (Python Imaging Library) para manipulação de imagens.

## Justificativa das Decisões Tomadas

### 1. **Uso do Tkinter**
O `tkinter` foi escolhido para a construção da interface gráfica devido à sua simplicidade e popularidade para o desenvolvimento rápido de GUIs em Python. Ele é uma das bibliotecas mais utilizadas para aplicações desktop, sendo nativa do Python e fácil de integrar com outras bibliotecas, como o `PIL` para manipulação de imagens.

### 2. **Uso da Biblioteca PIL (Pillow)**
A biblioteca `PIL` foi escolhida para carregar e exibir imagens na interface, como o ícone da janela. A versão `Pillow` do `PIL` foi utilizada devido à sua compatibilidade com versões recentes do Python e maior suporte a formatos de imagem.

- A função `Image.open("img.png")` abre o ícone da janela.
- O `ImageTk.PhotoImage(icon)` converte a imagem para um formato que pode ser exibido no `tkinter`.

### 3. **Design da Janela**
A janela foi projetada com os seguintes aspectos:
- **Título da janela:** Definido como "Cadastro", o que deixa claro o propósito da aplicação. A cor de fundo verde foi escolhida por ser uma cor associada ao conceito de aprovação ou sucesso.
- **Tamanho fixo e desabilitação de redimensionamento:** Para evitar que o usuário altere o tamanho da janela, a interface é projetada para um tamanho fixo de 400x250 pixels, proporcionando uma experiência de usuário controlada.
- **Icone da janela:** Um ícone (`img.png`) foi adicionado à janela para melhorar a identificação visual da aplicação.

### 4. **Layout da Interface**
O layout foi pensado para ser limpo, simples e intuitivo. A interface é composta por:
- **Campos de entrada:** O nome, e-mail, senha e confirmação de senha são entradas de dados fundamentais para o cadastro.
- **Layout dos campos:** Cada campo foi colocado dentro de um `Frame` para garantir uma estrutura organizada. Os campos de entrada são centralizados e ajustados para uma experiência visual agradável.

### 5. **Botão Cadastrar**
- O botão de cadastro possui uma cor de fundo verde e letras brancas, seguindo a estética geral da interface. Além disso, foi escolhido um tamanho e fonte de fácil leitura para garantir uma boa interação do usuário com o sistema.

### 6. **Escolha das Cores**
A escolha da cor verde para o fundo do título e o botão visa transmitir uma sensação de positividade e ação bem-sucedida. O texto em branco cria um contraste eficiente, tornando a leitura fácil e rápida.

## Como Usar
1. Ao rodar o código, a janela será aberta automaticamente com os campos necessários para o cadastro.
2. O usuário deverá preencher os campos de nome, e-mail, senha e confirmar a senha.
3. Após preencher, o usuário pode clicar no botão **Cadastrar** para enviar as informações.

## Dependências
- `tkinter`: Biblioteca nativa do Python para a criação de interfaces gráficas.
- `Pillow`: Biblioteca para processamento de imagens.

Instale o Pillow com o seguinte comando:
```
pip install pillow
```

## Possíveis Melhorias
- Adicionar validação de dados para garantir que os campos de nome e e-mail sejam preenchidos corretamente e que as senhas coincidam.
- Implementar funcionalidade de armazenamento de dados do usuário, como um banco de dados simples.
- Melhorar o layout com recursos como `pack()` ou `grid()` para um controle mais refinado de posicionamento e dimensionamento dos elementos.

Este projeto é uma base simples que pode ser expandida para criar um sistema completo de cadastro de usuários com funcionalidades avançadas.
