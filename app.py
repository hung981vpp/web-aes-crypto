from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from werkzeug.utils import secure_filename
from aes.encryption import encrypt_file
from aes.decryption import decrypt_file
from aes.utils import process_key  # Đã bỏ validate_key vì không cần kiểm tra độ dài nữa
import binascii
import hashlib  # Thêm thư viện để băm khóa

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = os.urandom(24)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def derive_key(user_key, key_size):
    """Hàm băm khóa người dùng nhập vào để tạo khóa có độ dài phù hợp"""
    # Chuyển key_size từ string sang số
    key_size_bits = int(key_size)
    key_size_bytes = key_size_bits // 8
    
    # Sử dụng SHA-256 để tạo khóa có độ dài cố định (32 bytes)
    hashed = hashlib.sha256(user_key.encode()).digest()
    
    # Cắt hoặc mở rộng (nếu cần) để phù hợp với key_size
    if len(hashed) > key_size_bytes:
        return hashed[:key_size_bytes]
    else:
        # Nếu khóa ngắn hơn, lặp lại cho đủ độ dài (không lý tưởng nhưng đảm bảo hoạt động)
        return (hashed * (key_size_bytes // len(hashed) + 1))[:key_size_bytes]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Vui lòng chọn file', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('Không có file được chọn', 'error')
            return redirect(request.url)
            
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            operation = request.form.get('operation')
            key = request.form.get('key')
            key_size = request.form.get('key_size', '128')
            
            if not key:
                flash('Vui lòng nhập khóa', 'error')
                return redirect(request.url)
            
            try:
                # Bỏ qua validate_key và sử dụng hàm derive_key mới
                processed_key = derive_key(key, key_size)
                
                if operation == 'encrypt':
                    output_filename = f"data.enc"
                    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                    
                    if encrypt_file(filepath, output_path, processed_key, key_size):
                        with open(output_path, 'rb') as f:
                            result_content = f.read().hex()
                        
                        return render_template('result.html',
                                             operation=f'Mã hóa AES-{key_size}',
                                             original_file=filename,
                                             result_file=output_filename,
                                             result_content=result_content)
                
                elif operation == 'decrypt':
                    if not filename.endswith('.enc'):
                        flash('File giải mã phải có đuôi .enc', 'error')
                        return redirect(request.url)
                    
                    output_filename = f"output.txt"
                    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                    
                    try:
                        if decrypt_file(filepath, output_path, processed_key, key_size):
                            with open(output_path, 'rb') as f:
                                result_content = f.read().decode('utf-8', errors='replace')
                            
                            return render_template('result.html',
                                                 operation=f'Giải mã AES-{key_size}',
                                                 original_file=filename,
                                                 result_file=output_filename,
                                                 result_content=result_content)
                    
                    except Exception as e:
                        flash('Giải mã thất bại - Khóa không đúng hoặc file bị hỏng', 'error')
                        return redirect(request.url)
            
            except Exception as e:
                flash(f'Lỗi xử lý: {str(e)}', 'error')
                return redirect(request.url)
    
    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.errorhandler(413)
def request_entity_too_large(error):
    return render_template('error.html', message='File quá lớn (tối đa 16MB)'), 413

if __name__ == '__main__':
    app.run(debug=True)