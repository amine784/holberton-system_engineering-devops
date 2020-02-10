#include <stdio.h
#include <stdlib.h>
/**
* infinite_while-infinite while
*Return: always success
**/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}
/**
* main-main programm
*Return: always success
**/
int main(void)
{
return (infinite_while());
}
