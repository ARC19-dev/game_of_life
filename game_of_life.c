#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define w 50
#define h 50

void draw(bool world[w][h]) 
{   
    printf("\033[H");
    for (int x = 0; x < w; x++) {
        for (int y = 0; y < h; y++) 
            printf(world[x][y] ? "#" : " ");
        printf("\n");
    }
}

void evolution(bool world[w][h])
{
    int lives[w][h] = {0};
    for (int x = 0; x < w; x++)
        for (int y = 0; y < h; y++) {
            for (int i = x-1; i <= x+1; i++)
                for (int j = y-1; j <= y+1; y++) 
                    lives[x][y] += world[(i%w > 0) ? i : i%w][(j%h > 0) ? j : j%h];
            lives[x][y] -= world[x][y] ? 1 : 0;
        }

    for (int x = 0; x < w; x++)
        for (int y = 0; y < h; y++)
            world[x][y] = lives[x][y] == 2 || lives[x][y] == 3;
            
}

int main()
{
    system("cls");
    bool world[w][h];
    srand(time(0));
    for (int x = 0; x < w; x++)
        for (int y = 0; y < h; y++)
            world[x][y] = rand() % 2;
    
    while (true)
    {
        draw(world);
        evolution(world);
    }
}
