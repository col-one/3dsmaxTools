from PySide.QtGui import *
import MaxPlus
import random


def make_wall(longueur, hauteur, bricks):
    lwall = longueur
    hwall = hauteur
    offset = 0
    offseth = 0
    lenght = 0
    for l in range(1, lwall):
        for h in range(1, hwall):
            #recup une brick aleatoirement dans ma selection
            r = random.randint(0, len(bricks)-1)
            randBricks = bricks[r]
            #recup lobjet referent et l'assigne a un nouveau node
            mesh = randBricks.GetObjectRef()
            node = MaxPlus.Factory.CreateNode(mesh)
            #je recup la bouding box de mon object referent et la convertie
            #en un objet TriObject
            mesh = MaxPlus.TriObject._CastFrom(mesh).GetMesh()
            bb = mesh.GetBoundingBox()
            #je calcule la longeure largeur
            lenght = bb.GetMax().GetY() - bb.GetMin().GetY()
            height = bb.GetMax().GetZ() - bb.GetMin().GetZ()
            #une brique sur deux sera deplace de moitiee
            if h % 2:
                decay = lenght / 2.0
            else:
                decay = 0
            #je deplace ma brique sur Y longeure avec un decay ou pas (0 pour la permiere)
            node.SetPositionY(offset - decay)
            #je monte ma brique d'une hauteur (0 pour la premiere)
            node.SetPositionZ(offseth)
            #pour faire une colone jincremente ma valeur de offset hauteur
            offseth += height
        #pour faire une nouvelle colone jincremente ma longueure
        offset += lenght
        #je reset les valeur qui sont lie a une colone
        decay = 0
        offseth = 0

class _GCProtector(object):
    widgets = []

class WallWidget(QDialog):
    def __init__(self):
        super(WallWidget, self).__init__()
        lay = QVBoxLayout(self)
        but_add = QPushButton("Add bricks")
        lab_h = QLabel("Height")
        self.haut = QSpinBox()
        lab_l = QLabel("Length")
        self.longu = QSpinBox()
        but_create = QPushButton("Create a Wall")

        lay.addWidget(but_add)
        lay.addWidget(lab_h)
        lay.addWidget(self.haut)
        lay.addWidget(lab_l)
        lay.addWidget(self.longu)
        lay.addWidget(but_create)

        self.bricks = []

        but_add.clicked.connect(self.add_bricks)
        but_create.clicked.connect(self.create_wall)

    def add_bricks(self):
        select = list(MaxPlus.SelectionManager.GetNodes())
        self.bricks += select

    def create_wall(self):
        make_wall(self.longu.value(), self.haut.value(), self.bricks)

app = QApplication.instance()
if not app:
    app = QApplication([])
w = WallWidget()
_GCProtector.widgets.append( w )
w.show()