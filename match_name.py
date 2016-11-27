import MaxPlus

sel = MaxPlus.SelectionManager.GetNodes()
ls_node = [i for i in sel]
if len(ls_node) % 2:
    print "Selection must be even : exit()"
    exit()
mid = len(ls_node) / 2
right = ls_node[:mid]
left = ls_node[mid:]

for n in left:
    print n.Name + "   >   " + right[left.index(n)].Name
    n.SetName(right[left.index(n)].Name)