from esrgan import upscale

if __name__ == "__main__":
	import sys
	args = sys.argv[1:]
	upscale.upscale_from_cmd_args(sys.argv[1:], '/models/RRDB_PSNR_x4.pth', 'psnr')
