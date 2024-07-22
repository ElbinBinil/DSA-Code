#include <stdio.h>

int main(){
    int a[] = {3,8,6,7,5};
    int n = 5, greatest = a[0], sec = a[0];
    for(int i =1; i<n; i++){
        if(a[i] > greatest){
            sec = greatest;
            greatest = a[i];
        }else if(a[i] > sec){
            sec = a[i];
        }
    }
    printf("%d", sec);
}