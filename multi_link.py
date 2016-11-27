import MaxPlus

sel = MaxPlus.SelectionManager.GetNodes()
last = sel[len(sel)-1]
sel.Remove(last)
for node in sel:
    node.SetParent(last)
