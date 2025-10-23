#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Forward declarations
int count(int n);

// Global variables
int num;  // Global variable

int count(int n) {
    // Temporary variables
    int t0 = 0;
    int t1 = 0;
    int t2 = 0;

L0:
    t0 = n >= 0;
    if (!t0) goto L1;
    printf("%d\n", n);
    t2 = n - 1;
    n = t2;
    goto L0;
L1:
    ;  // Empty statement after label
}

int main() {
    // Temporary variables
    int t3 = 0;

    num = 10;
    t3 = count(num);

    return 0;
}