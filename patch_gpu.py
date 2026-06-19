import glob, re

for train_path in glob.glob('*/train.py'):
    with open(train_path, 'r') as f:
        content = f.read()

    # Remove the hardcoded os.environ["CUDA_VISIBLE_DEVICES"] = '0'
    content = re.sub(r'os\.environ\["CUDA_VISIBLE_DEVICES"\]\s*=\s*[\'"]0[\'"]', '# removed hardcoded GPU', content)
    
    with open(train_path, 'w') as f:
        f.write(content)
