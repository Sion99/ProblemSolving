#include <iostream>
#include <vector>

using namespace std;

struct node
{
    char left;
    char right;
};

vector<node> tree(26);
// 벡터로 트리를 구현하였음

void preorder(char node)
{
    if (node == '.')
        return;
    cout << node;
    preorder(tree[node].left);
    preorder(tree[node].right);
}

void inorder(char node)
{
    if (node == '.')
        return;
    inorder(tree[node].left);
    cout << node;
    inorder(tree[node].right);
}

void postorder(char node)
{
    if (node == '.')
        return;
    postorder(tree[node].left);
    postorder(tree[node].right);
    cout << node;
}

int main()
{
    int n;
    char self, l, r;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> self >> l >> r;
        tree[self].left = l;
        tree[self].right = r;
    }
    preorder('A');
    cout << endl;
    inorder('A');
    cout << endl;
    postorder('A');
    cout << endl;

    return 0;
}