# 🔐 Web AES Crypto

Một ứng dụng web bảo mật dựa trên Python và Flask để mã hóa và giải mã dữ liệu sử dụng thuật toán AES (Advanced Encryption Standard).

## 📋 Tổng quan

Web AES Crypto là một ứng dụng web cho phép người dùng mã hóa và giải mã dữ liệu bằng cách sử dụng thuật toán AES. Được xây dựng với Python, Flask và Bootstrap, ứng dụng cung cấp giao diện trực quan, dễ sử dụng, và thực hiện các thao tác mã hóa an toàn.

## ✨ Tính năng

- 🔒 Mã hóa văn bản bằng thuật toán AES-128, AES-192, hoặc AES-256
- 🔓 Giải mã văn bản đã được mã hóa
- 🔄 Hỗ trợ nhiều chế độ mã hóa khác nhau (CBC, CFB, OFB, CTR)
- 🔑 Cho phép người dùng tự nhập khóa bảo mật
- 🧩 Tùy chọn sử dụng vector khởi tạo (IV) tùy chỉnh
- 💻 Giao diện thân thiện với người dùng
- 🛡️ Xử lý bảo mật dữ liệu người dùng

## 🚀 Cài đặt

1. Clone repository:
   ```
   git clone https://github.com/hung981vpp/web-aes-crypto.git
   ```

2. Di chuyển vào thư mục dự án:
   ```
   cd web-aes-crypto
   ```

3. Tạo và kích hoạt môi trường ảo (khuyến nghị):
   ```
   python -m venv venv
   # Trên Windows
   venv\Scripts\activate
   # Trên macOS/Linux
   source venv/bin/activate
   ```

4. Cài đặt các dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Chạy ứng dụng:
   ```
   flask run
   ```
   hoặc
   ```
   python app.py
   ```

## 📝 Cách sử dụng

1. 🌐 Truy cập ứng dụng thông qua trình duyệt web (mặc định: http://127.0.0.1:5000)
2. 🔄 Chọn chế độ mã hóa hoặc giải mã
3. ✏️ Nhập văn bản cần xử lý
4. 🔑 Nhập khóa bảo mật (secret key)
5. ⚙️ Tùy chọn: Cấu hình thêm các tham số khác như chế độ mã hóa, vector khởi tạo
6. 🖱️ Nhấn nút "Mã hóa" hoặc "Giải mã" để thực hiện thao tác
7. ✅ Kết quả sẽ được hiển thị trên giao diện

## 🛠️ Công nghệ sử dụng

- 🐍 Python: Ngôn ngữ lập trình back-end
- 🌶️ Flask: Framework web để xây dựng ứng dụng
- 🎨 Bootstrap: Tạo giao diện responsive
- 📜 JavaScript: Xử lý mã hóa/giải mã phía client

## 🔒 Bảo mật

- 🔐 Quá trình mã hóa/giải mã có thể được thực hiện ở phía server hoặc phía client tùy vào cấu hình
- 🚫 Không lưu trữ dữ liệu người dùng hoặc khóa mã hóa sau khi xử lý
- 🔐 Sử dụng HTTPS để bảo vệ dữ liệu trong quá trình truyền tải (khi triển khai)
- 👁️ Mã nguồn mở, có thể kiểm tra tính toàn vẹn của ứng dụng

## 🤝 Đóng góp

Mọi đóng góp đều được hoan nghênh! Nếu bạn muốn cải thiện dự án, vui lòng:

1. 🔱 Fork repository
2. 🌿 Tạo branch mới (`git checkout -b feature/amazing-feature`)
3. ✅ Commit các thay đổi (`git commit -m 'Add some amazing feature'`)
4. 📤 Push lên branch (`git push origin feature/amazing-feature`)
5. 🔃 Mở Pull Request

## 📜 Giấy phép

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 📞 Liên hệ

Hung Nguyen - [@hung981vpp](https://github.com/hung981vpp)

Link dự án: [https://github.com/hung981vpp/web-aes-crypto](https://github.com/hung981vpp/web-aes-crypto)

## 🙏 Lời cảm ơn

- 🌶️ [Flask](https://flask.palletsprojects.com/)
- 🎨 [Bootstrap](https://getbootstrap.com/)
- 🔐 [PyCryptodome](https://pycryptodome.readthedocs.io/) (nếu được sử dụng)
- 🛡️ [Python Cryptography](https://cryptography.io/) (nếu được sử dụng)

## 📂 Cấu trúc dự án

```
web-aes-crypto/
│
├── app.py                # Entry point của ứng dụng Flask
├── templates/            # Thư mục chứa các template HTML
│   ├── index.html        # Trang chính
│   ├── encrypt.html      # Trang mã hóa
│   └── decrypt.html      # Trang giải mã
│
├── static/               # Thư mục chứa các file tĩnh
│   ├── css/              # Stylesheet và Bootstrap
│   └── js/               # JavaScript và xử lý mã hóa
│
├── modules/              # Các module chức năng
│   └── crypto.py         # Module xử lý mã hóa/giải mã AES
│
├── requirements.txt      # Danh sách các dependency
└── README.md             # Tài liệu hướng dẫn
```
