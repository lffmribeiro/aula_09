# Aula 09

## Aula sobre Funções

As funções são responsáveis por processar informações com base em três componentes principais: entrada (input), processamento e saída (output).

### Principais Vantagens de Usar Funções em Programação

1. **Reutilização de Código**: Funções permitem que o mesmo bloco de código seja usado diversas vezes em diferentes partes do programa, evitando duplicação e facilitando a manutenção.

2. **Modularidade**: Dividir um programa em funções torna o código mais organizado e modular. Cada função pode ser desenvolvida, testada e depurada separadamente, o que simplifica o processo de desenvolvimento.

3. **Legibilidade e Manutenção**: Funções ajudam a estruturar o código de maneira clara e lógica, tornando-o mais fácil de ler e entender. Isso facilita a manutenção e a colaboração entre desenvolvedores.

4. **Abstração**: Funções permitem esconder a complexidade dos detalhes de implementação, oferecendo uma interface simples para os usuários. Isso promove a abstração e o encapsulamento.

5. **Facilidade de Depuração e Testes**: Testar e depurar código em funções individuais é mais fácil do que em programas grandes e monolíticos. Isso permite a detecção e correção de erros de forma mais eficiente.

6. **Escalabilidade**: Funções facilitam a extensão e modificação do código. Novas funcionalidades podem ser adicionadas como novas funções, sem impactar outras partes do programa.

### Estrutura de uma Função

As funções em programação possuem uma estrutura que inclui:

- **Nome da Função**: Um identificador único que descreve o propósito da função.
- **Parâmetros**: Variáveis listadas na definição da função. Elas representam os dados que a função espera receber.
- **Argumentos**: Valores reais passados para a função quando ela é chamada. Eles substituem os parâmetros definidos.
- **Retorno (return)**: O valor que a função devolve após executar seu código.

### Diferença entre Parâmetros e Argumentos

- **Parâmetros**: São variáveis declaradas na definição da função. Eles servem como marcadores de posição que a função espera receber quando chamada.
  ```python
  def soma(a, b):  # a e b são parâmetros
      return a + b
