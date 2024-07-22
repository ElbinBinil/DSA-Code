// Online C compiler to run C program online
#include <stdio.h>

void insertDigitsToArray(int number, int *array, int length) {
    for (int i = length - 1; i >= 0; i--) {
        array[i] = number % 10;
        number /= 10;
    }
}
int main() {
    // Write C code here
    int num;
    printf("Enter an Integer: ");
    scanf("%d", &num);
    int originalNum = num;
    int count = 0;
    while (num > 0) {
        count++;
        num /= 10; 
    }
    int array[count];
    insertDigitsToArray(originalNum, array, count);
    printf("%d", array[2] + array[3]);
    
}