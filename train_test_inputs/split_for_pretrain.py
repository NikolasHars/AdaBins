import os
import os.path as osp

split = 'test'


input_path = f"./kitti_eigen_distance_{split}_files_with_gt.txt"
output_path = f"./kitti_eigen_distance_{split}_files_pretrain.txt"

output_path_orig = f"./kitti_eigen_{split}_files.txt"

with open(input_path, 'r') as f:
    lines = f.readlines()

additional_lines = [line for line in lines if "additional" in line]
non_additional_lines = [line for line in lines if "additional" not in line]

print(f"New split length:  {len(additional_lines)}. \nEigen Split length (Verification): {len(lines) - len(additional_lines)}")

with open(output_path, 'w') as f:
    for line in additional_lines:
        f.write(line)

with open(output_path_orig, 'w') as f:
    for line in non_additional_lines:
        f.write(line)
