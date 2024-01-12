#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int num1, num2;
	scanf("%d %d", &num1, &num2);
	
	if (num1 > 0 && num1 < 10 && num2 > 0 && num2 < 10)
	{
		printf("%d", (num1 + num2));
	}

		return 0;
	
}