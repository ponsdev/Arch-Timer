from views.guiWin import callUI
from models.filesfncs import getConfigSets

cfgSets = getConfigSets()
callUI(cfgSets)
