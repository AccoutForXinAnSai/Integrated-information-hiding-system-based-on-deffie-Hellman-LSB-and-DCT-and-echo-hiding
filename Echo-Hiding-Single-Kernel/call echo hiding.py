import matlab
import matlab.engine


eng = matlab.engine.start_matlab()
audio = eng.data_embedding(nargout=0)
print('隐藏信息成功')
eng.data_extracting(nargout=0)
print('解密信息成功')