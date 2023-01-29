import os
import moviepy.editor as mp
import argparse

# taking arguments
parser = argparse.ArgumentParser("python webm_convert.py")
parser.add_argument(
    "--input",
    default="skins",
    help="The root input directory for gifs to be converted",
    type=str,
)
parser.add_argument(
    "--output",
    default="webm",
    help="The root output directory for webm videos to be saved",
    type=str,
)
parser.add_argument(
    "--rem",
    default=False,
    action="store_true",
    help="delete converted gifs",
)
args = parser.parse_args()

input_folder = args.input
output_folder = args.output
delete_on_completion = args.rem

# getting files
filenames = [
    os.path.join(dirpath, f)
    for (dirpath, dirnames, filenames) in os.walk(input_folder)
    for f in filenames
    if f.endswith(".gif")
]

# converting
for file in filenames:
    print(f"\n Processing [{file.split(',')[-1]}] ... \n")

    output_file = f"{output_folder}\{file.replace('.gif','.webm')}"
    try:
        clip = mp.VideoFileClip(file)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        clip.write_videofile(output_file)
        if delete_on_completion:
            os.remove(file)
    except:
        print("Failed to create or save file! skipping")
