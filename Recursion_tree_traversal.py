tree = {
    'value': 'A',

    'left': {
        'value': 'B',
        'left': None,
        'right': None
    },
    'right': {
        'value': 'C',
        'left': None,
        'right': None
    }
}

def traverse(node):
    if node is None:
        return

    print(node['value'])
    traverse(node['left'])
    traverse(node['right'])


traverse(tree)