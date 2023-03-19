/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sishin <sishin@student.42seoul.kr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/03/14 13:33:34 by sishin            #+#    #+#             */
/*   Updated: 2023/03/16 12:51:00 by sishin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

void *ft_memmove(void *dst, const void *src, size_t len)
{
    char *temp;
    const char *s;

    if (dst <= src)
    {
        temp = dst;
        s = src;
        while (len--)
            *temp++ = *s++;
    }
    else
    {
        temp = dst;
        temp += len;
        s = src;
        s += len;
        while (len--)
            *--temp = *--s;
    }
    return (dst);
}

#include <stdio.h>

int main()
{
    char src[] = "BlockDMask";
    char dest1[] = "fffffdddddzzzzz";
    char dest2[] = "fffffdddddzzzzz";
    char dest3[] = "fffffdddddzzzzz";

    ft_memmove(dest1, src, sizeof(char) * 10);
    ft_memmove(dest2, src, sizeof(char) * 10 + 1);
    ft_memmove(dest3 + 10, src, sizeof(char) * 3);

    printf("src : %s\n", src);

    printf("dest1 : %s\n", dest1);
    printf("dest2 : %s\n", dest2);
    printf("dest3 : %s\n", dest3);

    return 0;
}