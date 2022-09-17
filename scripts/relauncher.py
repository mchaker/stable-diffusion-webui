import argparse, os, time

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, help="port to run the webUI on", default=7860)
parser.add_argument("--no-half", action='store_true', help="do not switch the model to 16-bit floats", default=False)
parser.add_argument("--precision", type=str, help="evaluate at this precision", choices=["full", "autocast"], default="autocast")
parser.add_argument("--no-progressbar-hiding", action='store_true', help="do not hide progressbar in gradio UI (we hide it because it slows down ML if you have hardware accleration in browser)", default=False)
parser.add_argument("--gpu", type=int, help="choose which GPU to use if you have multiple", default=int(os.environ.get('CUDA_VISIBLE_DEVICES', 0)))
parser.add_argument("--max-jobs", type=int, help="Maximum number of concurrent 'generate' commands", default=1)

opt = parser.parse_args()

# declare and empty boolean flags
opt_no_half = ""
opt_no_progress_bar_hiding = ""

# fill boolean flags
if opt.no_half:
    opt_no_half = "--no-half"

if opt.no_progressbar_hiding:
    opt_no_progress_bar_hiding = "--no-progressbar-hiding"

# USER CHANGABLE ARGUMENTS

# Change to `True` if you wish to enable these common arguments

# Run upscaling models on the CPU
extra_models_cpu = False

# Automatically open a new browser window or tab on first launch
open_in_browser = False

# Run Stable Diffusion in Optimized Mode - Only requires 4Gb of VRAM, but is significantly slower
optimized = False

# Run in Optimized Turbo Mode - Needs more VRAM than regular optimized mode, but is faster
optimized_turbo = False

# Creates a public xxxxx.gradio.app share link to allow others to use your interface (requires properly forwarded ports to work correctly)
share = False


# Enter other `--arguments` you wish to use - Must be entered as a `--argument ` syntax
additional_arguments = ""





# BEGIN RELAUNCHER PYTHON CODE

common_arguments = ""

if extra_models_cpu == True:
    common_arguments += "--extra-models-cpu "
if optimized_turbo == True:
    common_arguments += "--optimized-turbo "
if optimized == True:
    common_arguments += "--optimized "
if share == True:
    common_arguments += "--share "

if open_in_browser == True:
    inbrowser_argument = "--inbrowser "
else:
    inbrowser_argument = ""

n = 0
while True:
    print('Relauncher: Launching...')
    #os.system(f"python scripts/webui.py {common_arguments} {inbrowser_argument} {additional_arguments}")
    os.system("python3 scripts/webui.py {opt_nohalf} --precision={opt_precision} {opt_noprogressbarhiding} --max-jobs {opt_maxjobs} --gpu {opt_gpu} --port {opt_port}".format(opt_nohalf=opt_no_half, opt_precision=str(opt.precision), opt_noprogressbarhiding=opt_no_progress_bar_hiding, opt_maxjobs=int(opt.max_jobs), opt_gpu=str(opt.gpu), opt_port=str(opt.port)))
        
    print(f'\tRelaunch count: {n}')
    print('Relauncher: Process is ending. Relaunching in 60s...')
    n += 1
    time.sleep(60)

