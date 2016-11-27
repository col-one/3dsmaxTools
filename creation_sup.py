import MaxPlus
#creation dune primitive
#bien differencier le mesh du node.
mesh = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
node = MaxPlus.Factory.CreateNode(mesh)
node.SetName("Ma Sphere")

#creation d'une instance de ma sphere
node2 = MaxPlus.Factory.CreateNode(mesh)
node2.SetName("Mon Instance")

#creation en boucle
for i in range(100):
    node = node2 = MaxPlus.Factory.CreateNode(mesh)
    node.SetName("Mon Instance "+str(i))