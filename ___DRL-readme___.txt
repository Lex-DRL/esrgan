0. Python 3.7 (64-bit!!!)
0.1. (optional) CUDA

1. PyTorch >= 0.4.0 - https://pytorch.org/get-started/locally/
* Stable
* Windows
* pip
* Python 3.7
* (CUDA?) None

None:
"C:\Python37\python.exe" -m pip install -U pip https://download.pytorch.org/whl/cpu/torch-1.0.0-cp37-cp37m-win_amd64.whl torchvision

2.
"C:\Python37\python.exe" -m pip install -U pip numpy opencv-python

3. Test:
"C:\Python37\python.exe" test.py models/RRDB_ESRGAN_x4.pth
"C:\Python37\python.exe" test.py models/RRDB_PSNR_x4.pth