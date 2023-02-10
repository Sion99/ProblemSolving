#include <stdio.h>
#include <stdlib.h>

typedef struct treeNode
{
    struct treeNode *left;
    struct treeNode *right;
} treeNode;

int main()
{
    int n;
    treeNode **tree;

    scanf("%d", &n);
    tree = (treeNode **)malloc(sizeof(treeNode *));
    for (int i = 0; i < n; i++)
    {
        tree[i] = (treeNode *)malloc(sizeof(treeNode));
        scanf("%c %c %c", );
    }
}