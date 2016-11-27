#description de MaxPlus

#import du module MaxPlus
import MaxPlus
#recuperation de la selection
selection = MaxPlus.SelectionManager.GetNodes()

#retourne un tableau INodeTab compose de INode
#presentation du INode

#creation dune liste a partir du INodeTab
selection = [node for node in selection]

#exemple d'utilisation de la selection dans une boucle
for node in selection:
    print node.GetName()
    node.SetPositionX(0.0)
    node.SetPositionY(0.0)
    node.SetPositionZ(0.0)

#rappel de ce que cest un attribut
#une methode, une fonction