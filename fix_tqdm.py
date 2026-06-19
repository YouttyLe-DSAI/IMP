import glob

for train_path in glob.glob('code/*/train.py'):
    with open(train_path, 'r') as f:
        content = f.read()

    # Find the line "for epoch in range(cur_epoch, cfg['max_epoch']):"
    lines = content.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        if line.strip() == "for epoch in range(cur_epoch, cfg['max_epoch']):":
            new_lines.append(line)
            # Add pbar definition on the next line
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(indent + "    pbar = tqdm(train_loader, desc=f\"Epoch {epoch}/{cfg['max_epoch']}\", dynamic_ncols=True)")
        elif line.strip() == "for i, data in enumerate(train_loader):  # inner loop within one epoch":
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(indent + "for i, data in enumerate(pbar):  # inner loop within one epoch")
        elif line.strip() == "for i, data in enumerate(train_loader):":
            indent = line[:len(line) - len(line.lstrip())]
            new_lines.append(indent + "for i, data in enumerate(pbar):")
        else:
            new_lines.append(line)
    
    with open(train_path, 'w') as f:
        f.write('\n'.join(new_lines))
