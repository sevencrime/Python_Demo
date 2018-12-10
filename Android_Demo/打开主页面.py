# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
#device.installPackage('/sdcard/qq.apk')

# sets a variable with the package's internal name
package = 'com.android.calculator2'

# sets a variable with the name of an Activity in the package
activity = 'com.android.calculator2.Calculator'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
device.startActivity(component=runComponent)







# Presses the Menu button
MonkeyRunner.sleep(2)
device.press('KEYCODE_BACK ', MonkeyDevice.DOWN_AND_UP)

# Takes a screenshot
MonkeyRunner.sleep(2)
result = device.takeSnapshot()

# Writes the screenshot to a file
MonkeyRunner.sleep(2)
result.writeToFile('e:\shot1.png','png')

