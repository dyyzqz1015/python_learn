# python_learn


1.如何通过串口通信访问硬件
COM=serial.Serial("COM3".115200,parity=serial.PARITY_SPACE,timeout=10)
Vision=b"5a5a0000200800000000"
n=COM3.write(binascii.a2b_hex(Vision))
ASC=COM3.read(n)
showVision=binascii.b2a_hex(ASC)
print(showVision)

2.如何通过开始频率、结束频率、点数，生成频率点

startFreq=10
stopFreq=100
points=10
freq_points=np.linspace(startFreq,stopFreq,points)

3.如何配置pycharm将QtDesigner的ui转换为.py

File->Settings->Tools->External Tools
1.配置QtDesigner
点+，然后配置如下
Name:QtDesigner
Program:D:\Anaconda3\Library\bin\desagner.exe
Parameters:
Working directory:$FileDir$

2.配置Qt uic
Name:Qt uic
Program:D:\Anaconda3\Scripts\pyuic5.exe
Parameters:"FileName" -o $FileNameWithoutExtension$.py
Working directory:$FileDir$


4.在QT当中显示和隐藏工具栏

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()
 
5. skrf列子中找不到ring slot.s2p如何解决

增加绝对路径

lib_path=r"D:\Aanconda3_win32\Lib\site-packages\skrf\data"
os.chdir(lib_path)

ring_slot=rf.Network('ring slot.s2p')
ring_slot.plot_s_smith()
plt.show()





