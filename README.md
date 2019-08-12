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
