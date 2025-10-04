# Example 7: Todos os tipos da linguagem Minipar

/* Este exemplo demonstra TODOS os 7 tipos básicos:
   1. number  - Números inteiros e reais
   2. string  - Sequência de caracteres
   3. bool    - Booleano (true ou false)
   4. void    - Retorno vazio
   5. func    - Tipo função
   6. c_channel - Canal socket cliente (declaração)
   7. s_channel - Canal socket servidor (declaração)
*/

# ========== Tipo NUMBER ==========
number inteiro = 42;
number real = 3.14159;
number negativo = -10;
number operacao = inteiro + real * 2;

# ========== Tipo STRING ==========
string nome = "Alice";
string mensagem = "Hello, World!";
string caminho = "/usr/local/bin";
string vazio = "";

# ========== Tipo BOOL ==========
bool verdadeiro = true;
bool falso = false;
bool comparacao = inteiro > 0;
bool logico = verdadeiro && !falso;

# ========== Tipo FUNC (funções) ==========

func number calcular(number x, number y) {
    /* Função que retorna number */
    return x * y + 10;
}

func bool verificar(number valor) {
    /* Função que retorna bool */
    return valor > 0 && valor < 100;
}

func string formatar(string texto, number codigo) {
    /* Função que retorna string */
    return "Formatted";
}

func void processar(number n) {
    /* Função com retorno void (sem retorno) */
    number temp = n * 2;
}

# ========== Tipos de CHANNELS ==========

/* Nota: c_channel e s_channel são tipos para comunicação
   socket cliente e servidor. Aqui apenas demonstramos
   a declaração do tipo. */

func void conectarCliente(c_channel canal) {
    /* Função que aceita um canal cliente */
    number status = 1;
}

func void iniciarServidor(s_channel servidor) {
    /* Função que aceita um canal servidor */
    number porta = 8080;
}

# ========== MAIN com todos os tipos ==========

func void main() {
    /* Demonstração de uso integrado de todos os tipos */
    
    # Numbers
    number contador = 0;
    number pi = 3.14;
    number resultado = calcular(10, 5);
    
    # Strings
    string usuario = "Bob";
    string senha = "secret123";
    string formatado = formatar(usuario, 200);
    
    # Booleans
    bool ativo = true;
    bool valido = verificar(resultado);
    bool autorizado = ativo && valido;
    
    # Void functions
    processar(contador);
    
    # Condicionais com múltiplos tipos
    if (autorizado && contador >= 0) {
        string status = "Success";
        number codigo = 200;
        bool ok = true;
    } else {
        string status = "Failed";
        number codigo = 404;
        bool ok = false;
    }
    
    # Loops com múltiplos tipos
    number i = 0;
    while (i < 10) {
        bool isEven = i % 2 == 0;
        
        if (isEven) {
            string tipo = "even";
        } else {
            string tipo = "odd";
        }
        
        i = i + 1;
    }
}
