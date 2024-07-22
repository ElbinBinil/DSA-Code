#include <stdio.h>

int main() {
    // Write C code here
    int a[] = {1, 1, 1, 2, 2, 3,3,4,4,4};
    int count = 1, curr = a[0];
    int n = 10;
    for(int i = 1; i<n; i++){
        if(curr == a[i]){
            count++;
        }else{
            printf("%d:%d\n",curr, count);
            curr = a[i];
            count = 1;
        }
    }
    printf("%d:%d",curr, count);
}