import re

# Patch instance_inpainting
path1 = '/home/tuan/workspace/IMP/code/instance_inpainting/trainer.py'
with open(path1, 'r') as f:
    content1 = f.read()

old_get_loss_str = """    def get_loss_str(self):
        log = []
        for name in self.Losses_name:
            for k,v in getattr(self, name).items():
                log.append(f"{k}: {v.item():.3f}")
        return " | ".join(log)"""

new_get_loss_str1 = """    def get_loss_str(self):
        log = []
        for k,v in self.G_losses.items():
            log.append(f"{k}: {v.item():.3f}")
        for k,v in self.D_inp_losses.items():
            log.append(f"{k}: {v.item():.3f}")
        return " | ".join(log)"""

content1 = content1.replace(old_get_loss_str, new_get_loss_str1)
with open(path1, 'w') as f:
    f.write(content1)

# Patch instance_style
path2 = '/home/tuan/workspace/IMP/code/instance_style/trainer.py'
with open(path2, 'r') as f:
    content2 = f.read()

new_get_loss_str2 = """    def get_loss_str(self):
        log = []
        for k,v in self.G_losses.items():
            log.append(f"{k}: {v.item():.3f}")
        for k,v in self.D_losses.items():
            log.append(f"{k}: {v.item():.3f}")
        return " | ".join(log)"""

content2 = content2.replace(old_get_loss_str, new_get_loss_str2)
with open(path2, 'w') as f:
    f.write(content2)

