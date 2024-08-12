#include <stdio.h>

int asm4(const char *param_1)
{
    int local_14;
    int local_10;
    int local_c;
  
    local_14 = 0x27a;
    for (local_10 = 0; param_1[local_10] != '\0'; local_10 = local_10 + 1) {
    }
    for (local_c = 1; local_c < local_10 - 1; local_c = local_c + 1) {
        local_14 = ((int)param_1[local_c + 1] - (int)param_1[local_c]) +
                   ((int)param_1[local_c] - (int)param_1[local_c - 1]) +
                   local_14;
    }
    return local_14;
}

int main(void){
    printf("0x%x\n", asm4("picoCTF_f97bb"));
    return 0;
}

