1. Ставим весь "родительский" софт, который надо руками качать из инета:
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

2. Затянуть из гита esrgan, назвав папку именно так и положив её в родительскую папку, которая добавлена в PYTHONPATH (её подпапки - питонские package'и). Если надо - создать таковую и добавить в PYTHONPATH.

3.
"C:\Python37\python.exe" -m pip install -U pip numpy opencv-python

4. Test:
"C:\Python37\python.exe" test.py models/RRDB_ESRGAN_x4.pth
"C:\Python37\python.exe" test.py models/RRDB_PSNR_x4.pth

5. В Виндовый SendTo добавить ярлыки на upscale_ESRGAN.py и upscale_PSNR.py