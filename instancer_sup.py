import MaxPlus

#recuperation de ma selection
sel = MaxPlus.SelectionManager.GetNodes()
#transformation en liste python
sel = [n for n in sel]
#recup master object
master = sel[0]
#recup ref du master
ref = master.GetObjectRef()
#pop le master de la list
sel.pop(0)
#Parse les autres objet a instancier
for node in sel:
    #Cahgement de son object ref
    node.SetObjectRef(ref)
