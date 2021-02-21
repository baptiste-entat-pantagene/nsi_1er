"""
Baptiste
Entat
"""

from AppWindow import *
from DataManagement import *


application = AppWindow()
dataMag = DataManagement("default-project")
dataMag.getIndex()

application.mainloop()