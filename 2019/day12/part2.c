#include <stdio.h>
#include <string.h>

typedef struct moon {
    int x, y, z;
    int dx, dy, dz;
} moon;

void gravity(moon *m1, moon *m2)
{
    if (m1->x > m2->x) { m1->dx--; m2->dx++; }
    if (m1->x < m2->x) { m1->dx++; m2->dx--; }

    if (m1->y > m2->y) { m1->dy--; m2->dy++; }
    if (m1->y < m2->y) { m1->dy++; m2->dy--; }

    if (m1->z > m2->z) { m1->dz--; m2->dz++; }
    if (m1->z < m2->z) { m1->dz++; m2->dz--; }
}

void velocity(moon *m)
{
    m->x += m->dx;
    m->y += m->dy;
    m->z += m->dz;
}

int main()
{
    moon m1 = { 4,  12,  13};
    moon m2 = {-9,  14, -3};
    moon m3 = {-7, -1,   2};
    moon m4 = {-11, 17, -1};
    //moon m1 = {-8, -10, 0};
    //moon m2 = { 5,  5,  10};
    //moon m3 = { 2, -7,  3};
    //moon m4 = { 9, -8, -3};
    moon m1_bak = m1;
    moon m2_bak = m2;
    moon m3_bak = m3;
    moon m4_bak = m4;

    unsigned long i = 0;
    while (1)
    {
        gravity(&m1, &m2);
        gravity(&m1, &m3);
        gravity(&m1, &m4);
        gravity(&m2, &m3);
        gravity(&m2, &m4);
        gravity(&m3, &m4);
        velocity(&m1);
        velocity(&m2);
        velocity(&m3);
        velocity(&m4);
        i++;

        if (i % 1000000 == 0)
        {
            printf("%lu\n", i);
        }

        if (memcmp(&m1, &m1_bak, sizeof(moon)) == 0 &&
            memcmp(&m2, &m2_bak, sizeof(moon)) == 0 &&
            memcmp(&m3, &m3_bak, sizeof(moon)) == 0 &&
            memcmp(&m4, &m4_bak, sizeof(moon)) == 0)
        {
            printf("Found reoccurence at %lu\n", i);
            break;
        }
    }
    return 1;
}
