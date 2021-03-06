import sys
import math
reload(sys)
sys.setdefaultencoding("utf-8")

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

#connect device
print('connect device!')
device = MonkeyRunner.waitForConnection()

#start activity
print('start activity')
package = 'com.android.calculator2' 
activity = 'com.android.calculator2.Calculator'
runComponent = package + '/' + activity
device.startActivity(component=runComponent)
MonkeyRunner.sleep(5)

#init easymonkeydevice object ,this is init method
print('init easymonkeydevice')

easy_device = EasyMonkeyDevice(device)  
print('Tap 8')
easy_device.touch(By.id('id/digit_8'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1.0)
print('Tap *')
easy_device.touch(By.id('id/op_mul'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1.0)
print('Tap 9')
easy_device.touch(By.id('id/digit_9'),MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(1.0)
#print('Tap =')
#easy_device.touch(By.id('id/eq'),MonkeyDevice.DOWN_AND_UP)

MonkeyRunner.sleep(1.0)
pic = device.takeSnapshot()
pic.writeToFile('F:\Python_Demo\Android_Demo\image/result.png','png')
print('test finished!')