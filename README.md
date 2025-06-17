# Hướng Dẫn Thiết Lập Môi Trường Ảo Python (venv)

Hướng dẫn này giải thích cách tạo và sử dụng môi trường ảo (`venv`) để chạy script Python 3.

## 1. Kiểm Tra Phiên Bản Python
Đảm bảo Python 3 đã được cài đặt bằng cách chạy lệnh:

```bash
python3 --version
```

hoặc

```bash
python --version
```

## 2. Tạo Môi Trường Ảo
Để tạo một môi trường ảo có tên là `venv`, chạy lệnh sau:

```bash
python3 -m venv venv
```

Lệnh này sẽ tạo một thư mục `venv` chứa tất cả các file cần thiết cho môi trường ảo.

## 3. Kích Hoạt Môi Trường Ảo

- **Trên macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Trên Windows (Command Prompt):**
  ```cmd
  venv\Scripts\activate
  ```
- **Trên Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

Sau khi kích hoạt, bạn sẽ thấy `(venv)` xuất hiện ở đầu dòng lệnh.

## 4. Cài Đặt Các Gói Phụ Thuộc
Nếu dự án của bạn yêu cầu các thư viện Python bổ sung, cài đặt chúng bằng lệnh:

```bash
pip install <tên_gói>
```

Để cài đặt nhiều gói từ file `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 5. Chạy Script Python
Để chạy một script Python trong môi trường ảo:

```bash
python script.py
```

## 6. Tắt Môi Trường Ảo
Để thoát khỏi môi trường ảo, chạy lệnh:

```bash
deactivate
```