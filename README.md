# Hướng Dẫn Train & Resume Pipeline trên Kaggle

Dự án này đã được cấu hình sẵn để dễ dàng huấn luyện (training) trên Kaggle. Tất cả các mô hình mạng (`background`, `fusion`, `instance_inpainting`, `instance_style`) đều được cấu hình giới hạn số epoch là 60 (`max_epoch: 60`) và tự động lưu file checkpoint cứng mỗi 10 epoch (`save_epoch_freq: 10`).

## 1. Train từ đầu (Train from scratch)
Chỉ cần chạy file `train.py` với cờ `--config` tương ứng:

```bash
# Ví dụ chạy mạng background
cd background
python train.py --config configs/config.yaml --dataset_name cityscapes512x256
```

Lúc này mô hình sẽ lưu lại các thư mục kết quả trong `outputs/cityscapes512x256/[THỜI_GIAN]/checkpoints/`.

## 2. Train tiếp từ chỗ dang dở (Resuming Training)
Trong trường hợp Kaggle bị hết giờ chạy (timeout) hoặc bạn muốn dừng và train tiếp vào hôm sau, bạn không cần phải train lại từ epoch 0.

Chỉ cần sử dụng hai tham số `--resume` và `--resume_dir`:

```bash
# Ví dụ train tiếp mạng background từ thư mục hôm trước
cd background
python train.py --config configs/config.yaml --dataset_name cityscapes512x256 --resume --resume_dir ./outputs/cityscapes512x256/2026-06-19_02-45-02/
```

**Lưu ý quan trọng khi Resume:**
- Bạn phải đảm bảo đường dẫn `--resume_dir` trỏ đúng vào thư mục cha chứa thư mục con `checkpoints/` (Ví dụ: `.../2026-06-19_02-45-02/`).
- Code sẽ tự động tìm trong đó file model mới nhất (`latest_net_*.pth`) hoặc file checkpoint cứng để chạy tiếp tục từ epoch đang dang dở mà không bỏ lỡ tiến độ.

---
**Lưu ý về Dataset:**
Để train thực tế (Full Pipeline), bạn cần tải bộ dataset đã được **tiền xử lý (Pre-processed)** bởi tác giả (đã được cắt ghép thành các thư mục `images`, `labels`, `inst_map`, `object_datasets`...). Tuyệt đối không dùng dữ liệu RAW của Cityscapes.
