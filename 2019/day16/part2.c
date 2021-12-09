#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//unsigned char input[] = "12345678";
//unsigned char input[] = "80871224585914546619083218645595";
//unsigned char input[] = "03036732577212944063491565474664";
unsigned char input[] = "59719811742386712072322509550573967421647565332667367184388997335292349852954113343804787102604664096288440135472284308373326245877593956199225516071210882728614292871131765110416999817460140955856338830118060988497097324334962543389288979535054141495171461720836525090700092901849537843081841755954360811618153200442803197286399570023355821961989595705705045742262477597293974158696594795118783767300148414702347570064139665680516053143032825288231685962359393267461932384683218413483205671636464298057303588424278653449749781937014234119757220011471950196190313903906218080178644004164122665292870495547666700781057929319060171363468213087408071790";
//unsigned int offset = 303673;
unsigned int offset = 5971981;
unsigned char* signal;
unsigned int signal_len;
unsigned char phases = 100;
//unsigned short repeat = 1;
unsigned short repeat = 10000;

void repeat_input()
{
    signal = malloc(sizeof(unsigned char) * signal_len * repeat);
    for (unsigned short i; i<repeat; i++)
    {
        memcpy(&signal[i * signal_len], input, sizeof(input));
    }
    signal_len = signal_len * repeat;
}

unsigned int string_to_char(unsigned char string[])
{
    unsigned int i = 0;
    while (1)
    {
        if (string[i] == 0)
        {
            return i;
        }
        string[i] -= 0x30;
        i++;
    }
}

void phase()
{
    unsigned char res[signal_len-offset];
    unsigned int i, j, res_i;
    for (i=offset; i<signal_len; i++)
    {
        res_i = 0;
        for (j = i; j < signal_len; j++)
        {
            res_i += signal[j];
        }
        res[i-offset] = res_i % 10;
    }
    memcpy(&signal[offset], res, sizeof(res));
}

void print_arr(unsigned char arr[], unsigned short len)
{
    for (unsigned short i=0; i<len; i++)
    {
        printf("%hhu", arr[offset+i]);
    }
    printf("\n");
}

int main()
{
    signal_len = string_to_char(input);
    repeat_input();
    for (unsigned char i; i < phases; i++)
    {
        phase();
        printf("PHASE %hhu\n", i+1);
    }
    print_arr(signal, 8);
    return 0;
}

