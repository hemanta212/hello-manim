import os
import importlib
import sys

script = str(sys.argv[1])

os.system('poetry run python -m manim {script}.py --write_all --video_output_dir=./videos/ --low_quality'.format(script=script))

with open("file.txt", "w") as wf:
    classes = importlib.import_module(script).SCENES_IN_ORDER
    wf.writelines([f"file './videos/{i.__name__}.mp4'\n" for i in classes])

os.system("ffmpeg -f concat -safe 0 -i file.txt -c copy ./videos/Test.mp4")
os.remove('file.txt')
