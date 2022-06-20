# 如何让项目跑起来

1. ```bash
   pip install -r requirements.txt
   ```

​	安装所需包

2. 通过python get/hide_info -h查看命令解析
3. 运行完hide_info.py后，会弹出几个窗口，关掉即可，会输出index_start_pixel，这是get_info的一个重要参数
4. 需要特别注意的是，需要安装matlab2021，因为回升隐藏部分是用matlab编写的代码，只是用python的matlab引擎调用
