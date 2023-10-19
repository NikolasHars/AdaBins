"""
Check if all sequences in the render split are in the eigen split
"""

eigen_path = "./kitti_eigen_train_files_with_gt.txt"
render_path = "./kitti_eigen_angled_train_files_pretrain.txt"

# Get index of _drive_ element from both files
# ---------------------------------------------------------------
# Eigen
# ---------------------------------------------------------------
with open(eigen_path, 'r') as f:
    eigen_lines = f.readlines()

eigen_elements = [line.split(" ")[0] for line in eigen_lines]

element_0 = eigen_elements[0]

for eigen_idx, el in enumerate(element_0.split("/")):
    if "drive" in el:
        break

# ---------------------------------------------------------------
# Render
# ---------------------------------------------------------------
with open(render_path, 'r') as f:
    render_lines = f.readlines()

render_elements = [line.split(" ")[0] for line in render_lines]

element_0 = render_elements[0]

for render_idx, el in enumerate(element_0.split("/")):
    if "drive" in el:
        break

# ---------------------------------------------------------------
# Collect all drives from both files
# ---------------------------------------------------------------
eigen_set = {el.split("/")[eigen_idx].removesuffix("_sync") for el in eigen_elements}
render_set = {el.split("/")[render_idx] for el in render_elements}

# ---------------------------------------------------------------
# Check if drives in render_set are in eigen_set
# ---------------------------------------------------------------
not_in_eigen = [drive for drive in render_set if drive not in eigen_set]

print(f"Drives in render_set but not in eigen_set: {not_in_eigen}")

# Write all eigen sequences to a file
with open("eigen_sequences.txt", 'w') as f:
    for el in eigen_set:
        f.write(el + "\n")