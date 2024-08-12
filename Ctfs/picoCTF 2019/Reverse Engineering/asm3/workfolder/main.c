#include <stdint.h>
#include <stdio.h>

uint16_t asm3(uint32_t param_1, uint32_t param_2, uint32_t param_3) {
    uint8_t byte1 = (uint8_t)param_2;
    uint8_t byte2 = -(param_2 >> 8);
    uint16_t result = (byte1 << 8) | byte2;
    return result ^ (param_3 >> 16);
}

int main(int argc, char* argv[])
{
    printf("0x%x\n", asm3(0xba6c5a02,0xd101e3dd,0xbb86a173));
    return 0;
}
