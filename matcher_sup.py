import MaxPlus
from PySide import QtGui

#creation du separator
class HSeparator(QtGui.QFrame):
    def __init__(self):
        super(HSeparator, self).__init__()
        self.setFrameShape(QtGui.QFrame.HLine)
        self.setFrameShadow(QtGui.QFrame.Sunken)

#creation de notre fenetre avec pyside
class MatcherUI(QtGui.QWidget):
    def __init__(self):
        super(MatcherUI, self).__init__()
        self.setWindowTitle("Matcher")
        self.resize(230, 180)
        self.layout = QtGui.QVBoxLayout(self)
        label = QtGui.QLabel("Match attributes\nbetween objects")
        separator = HSeparator()
        self.name = QtGui.QCheckBox("Name")
        self.color = QtGui.QCheckBox("Color")
        self.position = QtGui.QCheckBox("Position")
        self.rotation = QtGui.QCheckBox("Rotation")
        self.ref = QtGui.QCheckBox("Ref")
        separator2 = HSeparator()
        self.button = QtGui.QPushButton("Apply")

        self.layout.addWidget(label)
        self.layout.addWidget(separator)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.color)
        self.layout.addWidget(self.position)
        self.layout.addWidget(self.rotation)
        self.layout.addWidget(self.ref)
        self.layout.addWidget(separator2)
        self.layout.addWidget(self.button)

class Matcher(object):
    ui = None
    objects = None
    def __init__(self, objects):
        self.ui = MatcherUI()
        self.objects = objects

        self.ui.button.clicked.connect(self.apply)

    def apply(self):
        self.objects = [n for n in MaxPlus.SelectionManager.GetNodes()]
        if len(self.objects)%2:
            print "La selection doit etre paire"
            return
        else:
            mid = len(self.objects) / 2
            right = self.objects[:mid]
            left = self.objects[mid:]
            for n in left:
                target = right[left.index(n)]
                if self.ui.ref.checkState():
                    self.match_ref(n, target)
                if self.ui.name.checkState():
                    self.match_name(n, target)
                if self.ui.color.checkState():
                    self.match_color(n, target)
                if self.ui.position.checkState():
                    self.match_position(n, target)
                if self.ui.rotation.checkState():
                    self.match_rotation(n, target)

    def match_name(self, obj, trg):
        obj.SetName(trg.Name)

    def match_color(self, obj, trg):
        obj.SetWireColor(trg.GetWireColor())

    def match_position(self, obj, trg):
        obj.SetWorldPosition(trg.GetWorldPosition())

    def match_rotation(self, obj, trg):
        pos = obj.GetWorldPosition()
        obj.SetWorldTM(trg.GetWorldTM())
        obj.SetWorldPosition(pos)

    def match_ref(self, obj, trg):
        obj.SetObjectRef(trg.GetObjectRef())

fenetre = Matcher([n for n in MaxPlus.SelectionManager.GetNodes()])
MaxPlus.AttachQWidgetToMax(fenetre.ui)

fenetre.ui.show()