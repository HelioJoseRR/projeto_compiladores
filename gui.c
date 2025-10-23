#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Global variables
int entrada;  // Global variable
int ret;  // Global variable

int main() {
    // Temporary variables
    int t0 = 0;
    int t1 = 0;
    int t2 = 0;
    int t3 = 0;
    int t4 = 0;

    // Channel client created (c_channel)
L0:
    if (!true) goto L1;
    // input() call - not implemented
    t0 = 0;
    entrada = t0;
    t1 = entrada == "exit";
    if (!t1) goto L2;
    goto L1;
L2:
    // Method call: client.send()
    t2 = 0;  // Method result
    ret = t2;
    printf("%d\n", ret);
    goto L0;
L1:
    // Method call: client.close()
    t4 = 0;  // Method result

    return 0;
}