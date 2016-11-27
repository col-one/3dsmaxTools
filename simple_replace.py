import MaxPlus

sel = MaxPlus.SelectionManager.GetNodes()
target = sel[1]
obj = sel[0]
target_name = target.Name
target_parent = target.Parent
MaxPlus.CoordinateSystem.SetReferenceSystem(3)
obj.Position = target.Position
obj.Rotation = target.Rotation
obj.Scale = target.Scale
for child in target.Children:
    child.SetParent(obj)
obj.SetParent(target_parent)
obj.SetName(target_name)
MaxPlus.INode.Delete(target)
