import pandas as pd
from treelib import Node, Tree
from collections.abc import Iterable

dict_components = [{'parent': 'part1', 'child': 'part2', 'ghost': 'y', 'qty': 1},
                   {'parent': 'part1', 'child': 'part3', 'ghost': 'y', 'qty': 1},
                   {'parent': 'part1', 'child': 'part4', 'ghost': 'n', 'qty': 1},
                   {'parent': 'part2', 'child': 'part5', 'ghost': 'n', 'qty': 2},
                   {'parent': 'part3', 'child': 'part6', 'ghost': 'n', 'qty': 3},
                   {'parent': 'part3', 'child': 'part7', 'ghost': 'y', 'qty': 1},
                   {'parent': 'part7', 'child': 'part8', 'ghost': 'n', 'qty': 4},
                   {'parent': 'part7', 'child': 'part9', 'ghost': 'n', 'qty': 2},
                   {'parent': 'part7', 'child': 'part10', 'ghost': 'n', 'qty': 1},
                   {'parent': 'part7', 'child': 'part11', 'ghost': 'y', 'qty': 1},
                   {'parent': 'part11', 'child': 'part12', 'ghost': 'n', 'qty': 3},
                   {'parent': 'part11', 'child': 'part13', 'ghost': 'n', 'qty': 2},
                   {'parent': 'part11', 'child': 'part14', 'ghost': 'n', 'qty': 2},
                   {'parent': 'part1', 'child': 'part15', 'ghost': 'y', 'qty': 1},
                   {'parent': 'part15', 'child': 'part16', 'ghost': 'n', 'qty': 2},
                   {'parent': 'part15', 'child': 'part17', 'ghost': 'n', 'qty': 1},
                   {'parent': 'part15', 'child': 'part18', 'ghost': 'y', 'qty': 1},
                   {'parent': 'part18', 'child': 'part19', 'ghost': 'n', 'qty': 5},
                   {'parent': 'part18', 'child': 'part20', 'ghost': 'n', 'qty': 2}]

df_components = pd.DataFrame.from_dict(dict_components)

dict_items = [{'item': 'part1', 'description': 'part1 description'},
              {'item': 'part2', 'description': 'part2 description'},
              {'item': 'part3', 'description': 'part3 description'},
              {'item': 'part4', 'description': 'part4 description'},
              {'item': 'part5', 'description': 'part5 description'},
              {'item': 'part6', 'description': 'part6 description'},
              {'item': 'part7', 'description': 'part7 description'},
              {'item': 'part8', 'description': 'part8 description'},
              {'item': 'part9', 'description': 'part9 description'},
              {'item': 'part10', 'description': 'part10 description'},
              {'item': 'part11', 'description': 'part11 description'},
              {'item': 'part12', 'description': 'part12 description'},
              {'item': 'part13', 'description': 'part13 description'},
              {'item': 'part14', 'description': 'part14 description'},
              {'item': 'part15', 'description': 'part15 description'},
              {'item': 'part16', 'description': 'part16 description'},
              {'item': 'part17', 'description': 'part17 description'},
              {'item': 'part18', 'description': 'part18 description'},
              {'item': 'part19', 'description': 'part19 description'},
              {'item': 'part20', 'description': 'part20 description'}]

df_items = pd.DataFrame.from_dict(dict_items)


def get_tree_children(item_number, version=""):
    used = [item_number]  # work arround to not duplicate parent nodes
    item_filter = df_components["parent"].str.strip() == item_number
    children = df_components.loc[item_filter]  # Filter from thousand of data only the needed item
    for x in children.itertuples(index=True, name="Pandas"):
        if isinstance(x, Iterable):  # received an Error message without this
            if x.child in used:
                pass
            else:
                used.append(x.child)
                child_item = df_items.loc[df_items['item'] == x.child]  # to get the child description on df_items
                tree.create_node(
                    f"{x.child} - {child_item.description.item()} - G:{x.ghost}\t\t\t\t qty: {x.qty}",
                    f"{x.child}",
                    parent=f"{x.parent}",
                )
                get_tree_children(x.child, version="")
    return tree


item_to_tree = "part3"  # interested part
tree = Tree()  # create a tree named tree
tree.create_node("这是显示","这是描述", data="hulala")  # create tree root
get_tree_children(item_to_tree)  # call to get_tree_children function passing interested part
tree.show()
tree.to_json()

# tree.update_node(nid="part3",data="2hao")
# data_num = tree.get_node('part3').data
# print(data_num)