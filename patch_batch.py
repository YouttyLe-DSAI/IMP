import glob, yaml

for cfg_path in glob.glob('*/configs/config.yaml'):
    with open(cfg_path, 'r') as f:
        content = f.read()
    
    # We use regex to replace batch_size and worker to keep the original formatting
    import re
    content = re.sub(r'batch_size:\s*\d+', 'batch_size: 4', content)
    content = re.sub(r'worker:\s*\d+', 'worker: 2', content)
    
    with open(cfg_path, 'w') as f:
        f.write(content)
