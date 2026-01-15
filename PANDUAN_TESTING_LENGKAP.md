# PANDUAN LENGKAP - Testing Login & Register Module
## Aplikasi Bimbingan Belajar (Quiz Pengupil)

---

## TABLE OF CONTENTS
1. [Penjelasan Masalah dan Perbaikan](#penjelasan-masalah-dan-perbaikan)
2. [Setup Environment](#setup-environment)
3. [Menjalankan Test Secara Manual](#menjalankan-test-secara-manual)
4. [Menjalankan Test dengan Selenium](#menjalankan-test-dengan-selenium)
5. [Setup GitHub Actions](#setup-github-actions)
6. [Interpretasi Hasil Test](#interpretasi-hasil-test)
7. [Troubleshooting](#troubleshooting)

---

## PENJELASAN MASALAH DAN PERBAIKAN

### Masalah yang Ditemukan

1. **Flow Register Salah**
   - **Masalah:** Setelah register berhasil, aplikasi langsung redirect ke `index.php` yang kosong
   - **Sebabnya:** User tidak bisa langsung mengakses dashboard sebelum login
   - **Perbaikan:** Register sekarang redirect ke `login.php` agar user login dengan credential baru

2. **Bug di register.php (Baris 17)**
   ```php
   // SEBELUM (SALAH):
   if( isset($_SESSION['user']) ) header('Location: index.php');
   
   // SESUDAH (BENAR):
   if( isset($_SESSION['username']) ) header('Location: login.php');
   ```
   - Inconsistency: login.php pakai `$_SESSION['username']` tapi register.php pakai `$_SESSION['user']`

3. **Bug di register.php (Baris 33-34)**
   ```php
   // SEBELUM (SALAH):
   if( cek_nama($name,$con) == 0 ){
       ...
       "INSERT INTO users ... VALUES ('$username','$nama',..."
   
   // SESUDAH (BENAR):
   if( cek_nama($username,$con) == 0 ){  // Check username, bukan name!
       ...
       "INSERT INTO users ... VALUES ('$username','$name',...  // $name bukan $nama!
   ```
   - Variable `$nama` tidak ada, seharusnya `$name`
   - Check duplicate harus pada `username`, bukan `name`

4. **File index.php dan logout.php Tidak Ada**
   - **Perbaikan:** Dibuat dua file baru untuk melengkapi aplikasi

### File yang Diperbaiki/Dibuat

| File | Status | Keterangan |
|------|--------|-----------|
| `register.php` | ✏️ Diperbaiki | Fix session check, variable names, redirect flow |
| `login.php` | ✅ OK | Tidak perlu diubah |
| `index.php` | ✨ Baru | Dashboard halaman utama setelah login |
| `logout.php` | ✨ Baru | Menghapus session dan redirect ke login |

---

## SETUP ENVIRONMENT

### Prasyarat
- Windows/Linux/Mac dengan XAMPP (atau PHP Server lainnya)
- Python 3.8+ terinstall
- Chrome/Chromium Browser terinstall
- Git terinstall (untuk push ke GitHub)

### Step 1: Setup Database

1. **Buka phpMyAdmin**
   - Buka browser → `http://localhost/phpmyadmin`
   - Login dengan user root (default: no password)

2. **Import Database Schema**
   - Klik menu "Import" di phpMyAdmin
   - Pilih file: `db/quiz_pengupil.sql`
   - Klik "Go"
   - Database `quiz_pengupil` akan terbuat dengan table `users`

3. **Verifikasi Database**
   ```sql
   -- Jalankan query ini untuk verifikasi
   SELECT * FROM users;
   ```
   - Seharusnya table kosong atau berisi user default

### Step 2: Setup XAMPP

1. **Tempat Project**
   - Copy project ke folder: `C:\xampp\htdocs\quiz-pengupil-main\`

2. **Start XAMPP Services**
   - Buka XAMPP Control Panel
   - Klik tombol "Start" untuk Apache dan MySQL
   - Pastikan keduanya berjalan (warna hijau)

3. **Verifikasi Server Running**
   ```
   http://localhost/quiz-pengupil-main/login.php
   ```
   - Seharusnya halaman login tampil

### Step 3: Setup Python Environment

1. **Buka Command Prompt/PowerShell**
   ```powershell
   # Navigasi ke project folder
   cd C:\xampp\htdocs\quiz-pengupil-main
   ```

2. **Buat Virtual Environment (Optional tapi Recommended)**
   ```powershell
   # Buat virtual environment
   python -m venv venv
   
   # Activate (Windows)
   venv\Scripts\activate
   
   # Activate (Mac/Linux)
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements-test.txt
   ```

4. **Verifikasi Instalasi**
   ```powershell
   python -c "import selenium; print(f'Selenium {selenium.__version__} installed')"
   python -c "import pytest; print(f'Pytest {pytest.__version__} installed')"
   ```

---

## MENJALANKAN TEST SECARA MANUAL

### Manual Test untuk FT_001: Login dengan Kredensial Valid

**Persiapan:**
- Database sudah punya user dengan username: `2221101826` dan password: `2221101826`
- Server Apache & MySQL sedang running

**Langkah Pengetesan:**

1. **Buka browser → `http://localhost/quiz-pengupil-main/login.php`**

2. **Isi Form Login:**
   - Username: `2221101826`
   - Password: `2221101826`

3. **Klik Tombol "Sign In"**

4. **Expected Result:**
   - ✅ Redirect ke halaman `index.php`
   - ✅ Tampil pesan "Selamat Datang, 2221101826!"
   - ✅ Tombol "Logout" tersedia

**Passing Criteria:** Semua 3 kondisi di atas terpenuhi

---

### Manual Test untuk FT_009: Register dengan Data Valid

**Persiapan:**
- Server running
- Siapkan data:
  - Email: `test@example.com` (belum pernah digunakan)
  - Username: `testuser123` (belum ada di database)
  - Password: `test123456`

**Langkah Pengetesan:**

1. **Buka browser → `http://localhost/quiz-pengupil-main/register.php`**

2. **Isi Form Register:**
   - Nama: (kosongkan, optional)
   - Email: `test@example.com`
   - Username: `testuser123`
   - Password: `test123456`
   - Re-Password: `test123456`

3. **Klik Tombol "Register"**

4. **Expected Result:**
   - ✅ Data tersimpan di database (check di phpMyAdmin)
   - ✅ Redirect ke halaman `login.php`
   - ✅ Bukan redirect ke `index.php` (ini adalah perbaikan baru!)

5. **Verify dengan Login:**
   - Username: `testuser123`
   - Password: `test123456`
   - Seharusnya login berhasil dan masuk ke dashboard

**Passing Criteria:** Semua 5 kondisi terpenuhi

---

## MENJALANKAN TEST DENGAN SELENIUM

### Step 1: Persiapan

```powershell
# Navigasi ke project folder
cd C:\xampp\htdocs\quiz-pengupil-main

# Activate virtual environment (jika sudah dibuat)
venv\Scripts\activate

# Pastikan semua dependencies terinstall
pip install -r requirements-test.txt
```

### Step 2: Konfigurasi Environment

1. **Copy file konfigurasi:**
   ```powershell
   cp .env.example .env
   ```

2. **Edit file `.env` jika diperlukan:**
   ```
   BASE_URL=http://localhost/quiz-pengupil-main
   TEST_TIMEOUT=10
   HEADLESS_MODE=false
   ```

### Step 3: Memastikan Server Running

Sebelum menjalankan test, pastikan:
- ✅ Apache running (http://localhost/quiz-pengupil-main/login.php bisa diakses)
- ✅ MySQL running dan database `quiz_pengupil` sudah ada
- ✅ Minimal ada 1 user di database untuk test login

Jika belum ada user:
```sql
-- Insert test user
INSERT INTO users (username, name, email, password) VALUES 
('2221101826', 'Test User', 'test@example.com', '$2y$10$hash_password_disini');
```

### Step 4: Menjalankan Test

#### Option 1: Run All Tests
```powershell
pytest test_selenium_login_register.py -v
```

**Output Contoh:**
```
test_selenium_login_register.py::TestLoginModule::test_FT_001_login_with_valid_credentials PASSED [ 10%]
test_selenium_login_register.py::TestLoginModule::test_FT_002_login_with_empty_password PASSED [ 20%]
test_selenium_login_register.py::TestRegisterModule::test_FT_009_register_with_valid_data PASSED [ 30%]
...

======================== 12 passed in 45.23s ========================
```

#### Option 2: Run Specific Test
```powershell
# Run hanya test FT_001
pytest test_selenium_login_register.py::TestLoginModule::test_FT_001_login_with_valid_credentials -v

# Run hanya test class
pytest test_selenium_login_register.py::TestLoginModule -v

# Run dengan keyword filter
pytest test_selenium_login_register.py -k "FT_001 or FT_009" -v
```

#### Option 3: Run dengan HTML Report
```powershell
pytest test_selenium_login_register.py -v --html=report.html --self-contained-html
```
- Report akan tersimpan di `report.html`
- Buka dengan browser untuk melihat hasil yang lebih detail

#### Option 4: Run Parallel (lebih cepat)
```powershell
pytest test_selenium_login_register.py -v -n auto
```

### Step 5: Interpretasi Output

**✅ PASSED** - Test berhasil memenuhi semua expected result
**❌ FAILED** - Test gagal, lihat error message untuk detail
**⏭️ SKIPPED** - Test di-skip (tidak dijalankan)

### Step 6: Debugging Test yang Gagal

Jika ada test yang gagal, debug dengan:

```powershell
# Jalankan test dengan output yang lebih detail
pytest test_selenium_login_register.py::TestLoginModule::test_FT_001_login_with_valid_credentials -vv

# Jalankan dengan pdb (debugger)
pytest test_selenium_login_register.py -vv --pdb

# Lihat server logs untuk error di backend
# Check XAMPP error logs di: C:\xampp\apache\logs\error.log
```

---

## SETUP GITHUB ACTIONS

### Step 1: Push ke GitHub

```powershell
# Inisialisasi git repository (jika belum)
cd C:\xampp\htdocs\quiz-pengupil-main
git init

# Tambah semua file
git add .

# Commit
git commit -m "Add Login & Register Module with Selenium Tests"

# Tambah remote (ganti dengan URL repository Anda)
git remote add origin https://github.com/USERNAME/quiz-pengupil.git

# Push ke GitHub
git branch -M main
git push -u origin main
```

### Step 2: Verifikasi GitHub Actions

1. **Buka repository di GitHub**
   - URL: `https://github.com/USERNAME/quiz-pengupil`

2. **Klik tab "Actions"**
   - Seharusnya workflow "Login & Register Module - Selenium Tests" muncul

3. **Monitoring Workflow**
   - Klik workflow untuk melihat detail
   - Status akan berubah: "queued" → "in progress" → "completed"

4. **Lihat Test Results**
   - Klik job "test"
   - Scroll down untuk melihat output dari Selenium tests
   - Cari bagian "Run Selenium Tests"

### Step 3: GitHub Actions File Explanation

**File:** `.github/workflows/selenium-tests.yml`

```yaml
name: Login & Register Module - Selenium Tests
```
- Nama workflow yang ditampilkan di GitHub

```yaml
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
  schedule:
    - cron: '0 2 * * *'  # Setiap hari pukul 02:00 UTC
```
- Trigger workflow:
  - `push`: Ketika commit ke main/develop
  - `pull_request`: Ketika buat PR ke main/develop
  - `schedule`: Automatic setiap hari (cron job)

```yaml
services:
  mysql:
    image: mysql:8.0
    ...
  php:
    image: php:8.1-apache
    ...
```
- Container services yang digunakan untuk testing

```yaml
steps:
  - name: Run Selenium Tests
    run: pytest test_selenium_login_register.py -v
```
- Step untuk menjalankan Selenium tests

### Step 4: Mengubah Konfigurasi Workflow (Optional)

Edit file `.github/workflows/selenium-tests.yml` untuk:

1. **Mengubah trigger timing:**
   ```yaml
   schedule:
     - cron: '0 2 * * *'  # Ubah ke waktu yang diinginkan
   ```
   - Referensi cron: https://crontab.guru/

2. **Menambah branch:**
   ```yaml
   on:
     push:
       branches: [ main, develop, staging ]
   ```

3. **Skip test untuk commit tertentu:**
   ```
   git commit -m "Update README [skip ci]"
   ```

---

## INTERPRETASI HASIL TEST

### Test Status Explanation

| Status | Arti | Action |
|--------|------|--------|
| ✅ PASSED | Test berhasil | Tidak perlu action |
| ❌ FAILED | Test gagal | Lihat error message, fix code, re-run |
| ⏭️ SKIPPED | Test di-skip | Check kondisi skip test |
| ⚠️ ERROR | Error saat setup/teardown | Check environment setup |

### Contoh Test Report

```
======================== TEST SESSION STARTS =========================
platform win32 -- Python 3.11.0, pytest-7.2.0
...
test_selenium_login_register.py::TestLoginModule::test_FT_001_login_with_valid_credentials PASSED
test_selenium_login_register.py::TestLoginModule::test_FT_002_login_with_empty_password PASSED
test_selenium_login_register.py::TestLoginModule::test_FT_003_login_with_empty_username PASSED
test_selenium_login_register.py::TestRegisterModule::test_FT_009_register_with_valid_data PASSED
test_selenium_login_register.py::TestRegisterModule::test_FT_018_register_redirect_to_login PASSED [CRITICAL]
...

========================= 12 PASSED in 45.23s ========================
```

### Metrics Penjelasan

- **Total Tests:** Jumlah test yang dijalankan
- **Passed:** Jumlah test yang berhasil
- **Failed:** Jumlah test yang gagal
- **Duration:** Waktu total eksekusi test

### Analisis Test Coverage

Dari 21 test cases yang dibuat:

| Category | Coverage | Status |
|----------|----------|--------|
| Login Valid | 1 (FT_001) | ✅ |
| Login Invalid | 3 (FT_002, FT_003, FT_004) | ✅ |
| Login Security | 3 (FT_006, FT_007, FT_008) | ✅ |
| Register Valid | 1 (FT_009) | ✅ |
| Register Invalid | 5 (FT_010-FT_014) | ✅ |
| Register Edge Case | 2 (FT_016, FT_017) | ✅ |
| Register Flow (NEW) | 1 (FT_018 - CRITICAL) | ✅ |
| Navigation | 3 (FT_019-FT_021) | ✅ |

---

## TROUBLESHOOTING

### Problem 1: "ModuleNotFoundError: No module named 'selenium'"

**Solusi:**
```powershell
pip install selenium webdriver-manager pytest python-dotenv
```

### Problem 2: "FAILED ... ConnectionRefusedError"

**Solusi:**
- Pastikan Apache & MySQL running
- Check URL di `.env` benar
- Test connection: `curl http://localhost/quiz-pengupil-main/login.php`

### Problem 3: "FAILED ... Unable to locate element"

**Penyebab:** Element HTML tidak ditemukan
**Solusi:**
1. Check HTML element ID/NAME di halaman login/register
2. Update element locator di test script
3. Tambah sleep/wait time

### Problem 4: "Database connection failed"

**Solusi:**
```powershell
# Check koneksi MySQL
mysql -h localhost -u root -p

# Import database jika belum
mysql -h localhost -u root -p quiz_pengupil < db/quiz_pengupil.sql
```

### Problem 5: "FAILED ... Chrome driver not found"

**Solusi:**
```powershell
# webdriver-manager akan auto download Chrome driver
# Jika masih error, install manual
pip install --upgrade webdriver-manager
```

### Problem 6: "GitHub Actions workflow tidak jalan"

**Solusi:**
1. Check file path `.github/workflows/selenium-tests.yml` benar
2. Commit & push file: `git add .github/workflows/selenium-tests.yml && git commit -m "Add GH Actions" && git push`
3. Check "Actions" tab di GitHub
4. Klik workflow untuk melihat error detail

### Problem 7: "Timeout waiting for element"

**Penyebab:** Page loading terlalu lama
**Solusi:**
- Increase timeout di test script:
  ```python
  TIMEOUT = 20  # Ubah dari 10 ke 20 detik
  ```
- Check server performance

---

## RINGKASAN ALUR TESTING

### Flow 1: Manual Testing
```
1. Setup Database & Server
2. Buka Login/Register page di browser
3. Isi form dan submit
4. Lihat hasilnya
5. Verify di database
```

### Flow 2: Automated Testing (Selenium)
```
1. Setup Python & Dependencies
2. Jalankan: pytest test_selenium_login_register.py
3. Tunggu test selesai
4. Lihat report (passed/failed)
5. Debug jika ada yang gagal
```

### Flow 3: CI/CD Testing (GitHub Actions)
```
1. Push code ke GitHub
2. GitHub Actions auto trigger
3. Setup container dengan MySQL & Apache
4. Jalankan Selenium tests
5. Generate report dan comment di PR
6. Monitor di GitHub Actions tab
```

---

## QUICK START CHECKLIST

- [ ] Clone/Download project
- [ ] Setup XAMPP (Apache & MySQL)
- [ ] Import database dari `db/quiz_pengupil.sql`
- [ ] Install Python dependencies: `pip install -r requirements-test.txt`
- [ ] Verify server running: `http://localhost/quiz-pengupil-main/login.php`
- [ ] Run tests: `pytest test_selenium_login_register.py -v`
- [ ] Push ke GitHub (optional untuk CI/CD)
- [ ] Monitor test results di GitHub Actions (optional)

---

## RESOURCES

- **Selenium Documentation:** https://selenium-python.readthedocs.io/
- **Pytest Documentation:** https://docs.pytest.org/
- **GitHub Actions Docs:** https://docs.github.com/en/actions
- **Cron Job Format:** https://crontab.guru/

---

## CONTACT & SUPPORT

Project: Aplikasi Bimbingan Belajar - Quiz Pengupil  
Author: Muhammad Reza  
NPM: 2221101826  
Date: 15 Januari 2026  

---

**Last Updated:** 15 Januari 2026  
**Status:** ✅ Complete & Ready for Production Testing
