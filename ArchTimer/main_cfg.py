from view.guiWin import callUI
from models.filesfncs import getConfigSets

cfgSets = getConfigSets()
callUI(cfgSets)
