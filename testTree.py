import random


class tt(tuple):
    def __str__(self):
        pass

empty = None
red, black = range(2)
color, left, root, right = range(4)

node = lambda l, t, r: {left: l, root: t, right: r}
rbnode = lambda c, l, t, r: {color: c, left: l, root: t, right: r}


def insert(x, tree):
    if tree == empty:
        return node(empty, x, empty)

    if x < tree[root]:
        return node(insert(x, tree[left]), tree[root], tree[right])
    elif  tree[root] < x:
        return node(tree[left], tree[root], insert(x, tree[right]))
    else:
        return tree


def balanced(ll, lt, lr, t, rl, rt, rr):
    lsub = rbnode(black, ll, lt, lr)
    rsub = rbnode(black, rl, rt, rr)
    return rbnode(red, lsub, t, rsub)


def balance(tree):
    if tree[color] == black and tree[left] and tree[left][color] == red:
        if tree[left][left] and tree[left][left][color] == red:
            return balanced(
                tree[left][left][left], tree[left][left][root], tree[left][left][right],
                tree[left][root], tree[left][right],
                tree[root], tree[right])
        elif tree[left][right] and tree[left][right][color] == red:
            return balanced(
                tree[left][left], tree[left][root],
                tree[left][right][left], tree[left][right][root], tree[left][right][right],
                tree[root], tree[right])

    if tree[color] == black and tree[right]  and tree[right][color] == red:
        if tree[right][left] and tree[right][left][color] == red:
            return balanced(
                tree[left], tree[root],
                tree[right][left][left], tree[right][left][root], tree[right][left][right],
                tree[right][root], tree[right][right])
        elif tree[right][right] and tree[right][right][color] == red:
            return balanced(
                tree[left], tree[root],
                tree[right][left], tree[right][root],
                tree[right][right][left], tree[right][right][root], tree[right][right][right])

    return tree


def rb_insert(x, tree):
    def ins(t):
        if t == empty:
            return rbnode(red, empty, x, empty)
        if x < t[root]:
            return balance(rbnode(t[color], ins(t[left]), t[root], t[right]))
        elif t[root] < x:
            return balance(rbnode(t[color], t[left], t[root], ins(t[right])))
        else:
            return t

    bal_tree = ins(tree)
    bal_tree[color] = black
    return bal_tree


def print_tree(tree):
    if tree[left] != empty:
        print(tree[root], ' -> ', tree[left][root], ';')
        print_tree(tree[left])
    if tree[right] != empty:
        print(tree[root], ' -> ', tree[right][root], ';')
        print_tree(tree[right])


def graphviz_printer(tree):
    print("digraph tree {")
    print_tree(tree)
    print("}")


t = empty
things = range(20)
# random.shuffle(things)  # tree should not be a list
for x in things:
    t = rb_insert(x, t)

graphviz_printer(t)