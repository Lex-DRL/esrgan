1. ������ ���� "������������" ����, ������� ���� ������ ������ �� �����:
1.1. (optional) CUDA
1.2. Python 3.7 (64-bit!!!)
1.3. PyTorch >= 0.4.0 - https://pytorch.org/get-started/locally/
* Stable
* Windows
* pip
* Python 3.7
* (CUDA?) None

None:
"C:\Python37\python.exe" -m pip install -U pip https://download.pytorch.org/whl/cpu/torch-1.0.0-cp37-cp37m-win_amd64.whl torchvision

CUDA 10:
"C:\Python37\python.exe" -m pip install -U pip https://download.pytorch.org/whl/cu100/torch-1.0.0-cp37-cp37m-win_amd64.whl torchvision

2. �������� �� ���� esrgan, ������ ����� ������ ��� � ������� � � ������������ �����, ������� ��������� � PYTHONPATH (� �������� - ��������� package'�). ���� ���� - ������� ������� � �������� � PYTHONPATH.

3.
"C:\Python37\python.exe" -m pip install -U pip numpy opencv-python

4. Test:
"C:\Python37\python.exe" test.py models/RRDB_ESRGAN_x4.pth
"C:\Python37\python.exe" test.py models/RRDB_PSNR_x4.pth

5. � �������� SendTo �������� ������ �� upscale_ESRGAN.py � upscale_PSNR.py