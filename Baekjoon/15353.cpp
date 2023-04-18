#include <iostream>

using namespace std;

char a[10002];
char b[10002];

int ft_strlen(char *s)
{
	int i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

int main()
{

	int alen, blen;
	int temp = 0;

	cin >> a >> b;
	alen = ft_strlen(a);
	blen = ft_strlen(b);
	int c[10002];
	
	if (alen >= blen)
	{
		for (int i = alen - 1; i >= 0, i--;)
		{
			c[i] += temp;
			if (b[i] == 0)
			{
				c[i] = a[i] - '0';
			}
			else
			{
				if ((a[i] - '0') + (b[i] - '0') >= 10)
				{
					temp = 1;
					c[i] += (a[i] - '0' + b[i] - '0') - 10;
				}
				else
				{
					temp = 0;
					c[i] += (a[i] - '0' + b[i] - '0');
				}
			}
		}
	}
	else
	{
		for (int i = blen - 1; i >= 0, i--;)
		{
			c[i] += temp;
			if (a[i] == 0)
			{
				c[i] = b[i] - '0';
			}
			else
			{
				if ((a[i] - '0') + (b[i] - '0') >= 10)
				{
					temp = 1;
					c[i] += (a[i] - '0' + b[i] - '0') - 10;
				}
				else
				{
					temp = 0;
					c[i] += (a[i] - '0' + b[i] - '0');
				}
			}
		}
	}
	cout << a << "\n" << b << "\n";
	cout << c;
}