#include <stdio.h>
//funcao q verifica se o retangulo de lados a e b
//cabe dentro do retangulo de lados x e y
int test(int a,int b,int x,int y)
{
	if(a<=x && b<=y)	return 1;
	if(a<=y && b<=x)	return 1;
	return 0;
}
int main()
{
	int h1,b1;
	int h2,b2;
	int h,b;
	scanf("%d %d %d %d %d %d",&h1,&b1,&h2,&b2,&b,&h);
	//verificador
	int ver=0;
	
	//verificando se o retangulo de lados h e b 
	//cabe dentro do retangulo de lados h1 e b1
	
	if(test(h,b,h1,b1))	ver=1;
	
	//verificando se o retangulo de lados h e b 
	//cabe dentro do retangulo de lados h1 e b1
	
	if(test(h,b,h2,b2))	ver=1;
	
	for(int i=0;i<=h;i++)
	{
		//costura paralela ao lado b e separando o 
		//lado h em i e h-i
		if(test(b,i,h1,b1)&&test(b,h-i,h2,b2)) ver=1;
		if(test(b,i,h2,b2)&&test(b,h-i,h1,b1)) ver=1;
	}
	for(int i=0;i<=b;i++)
	{
		//costura paralela ao lado h e separando o 
		//lado b em i e b-i
		if(test(h,i,h1,b1)&&test(h,b-i,h2,b2)) ver=1;
		if(test(h,i,h2,b2)&&test(h,b-i,h1,b1)) ver=1;
	}
	if(ver)	printf("S\n");
	else printf("N\n");
	return 0;
}