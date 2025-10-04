# Example 5: Tipo string e manipulação

/* Este exemplo demonstra:
   - Tipo string
   - Declaração de strings
   - Passagem de strings como parâmetros
   - Múltiplos tipos em um programa
   - Funções void com strings
*/

func void greet(string name) {
    string greeting = "Hello, ";
    string exclamation = "!";
    /* Em uma implementação completa, concatenaria as strings */
}

func void displayMessage(string msg, number code) {
    /* Função que aceita múltiplos tipos */
    string status = "Status: ";
}

func string getWelcomeMessage() {
    return "Welcome to Minipar!";
}

func void processUser(string username, number userId, bool active) {
    /* Demonstra função com múltiplos tipos de parâmetros */
    string userType = "User";
    
    if (active) {
        string status = "Active";
    } else {
        string status = "Inactive";
    }
}

func void main() {
    string name = "World";
    string language = "Minipar";
    string version = "1.0";
    
    greet(name);
    
    number errorCode = 404;
    string errorMsg = "Not Found";
    displayMessage(errorMsg, errorCode);
    
    # Múltiplos tipos juntos
    number count = 42;
    bool flag = true;
    string label = "Count";
    
    # Uso de string com outros tipos
    string userName = "Alice";
    number userAge = 25;
    bool userActive = true;
    
    processUser(userName, userAge, userActive);
    
    string welcome = getWelcomeMessage();
}
