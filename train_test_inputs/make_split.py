import os

original_file = "/cluster/project/infk/courses/252-0579-00L/group26/nihars_tests/AdaBins/train_test_inputs/kitti_eigen_train_files.txt"
extra_paths_to_include = ["/cluster/project/infk/courses/252-0579-00L/group26/nihars_tests/renders_translated_0.15"] #"/cluster/project/infk/courses/252-0579-00L/group26/nihars_tests/renders_angled_15", 

name = "kitti_eigen_train_partial"

for path in extra_paths_to_include:
    name += "_plus-" + os.path.basename(path)

name += ".txt"

lines = ""
# renders_... 
for path in extra_paths_to_include:
    # scene_...
    for scene in os.listdir(path):
        # pose_neg...
        for subdir in os.listdir(os.path.join(path, scene)):
            # 00000_rgb.png 00000_depth.png 0.0 00000_mask.png
            files = os.listdir(os.path.join(path, scene, subdir))
            idxs = [int(f.split("_")[0]) for f in files if f.endswith("_rgb.png")]
            idxs.sort()
            for idx in idxs:
                if os.path.isfile(os.path.join(path, scene, subdir, f"{idx:05d}_mask.png")):
                    lines += os.path.join(path, scene, subdir, f"{idx:05d}_rgb.png") + " "
                    lines += os.path.join(path, scene, subdir, f"{idx:05d}_depth.png") + " "
                    lines += "0.0"
                    lines += " " + os.path.join(path, scene, subdir, f"{idx:05d}_mask.png")
                    lines += "\n"

with open(name, "w") as f:
    f.write(lines)

    with open(original_file) as f2:
        for line in f2.readlines():
            f.write(line)