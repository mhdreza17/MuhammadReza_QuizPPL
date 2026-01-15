# TEST CASE DOKUMENTASI
## Aplikasi: Quiz Pengupil - Login & Register Module

**Project Name:** Aplikasi Bimbingan Belajar  
**Modul yang Ditest:** Login dan Register  
**Dibuat oleh:** Muhammad Reza  
**NPM:** 2221101826  
**Tanggal:** 15 Januari 2026  

---

## A. FUNCTIONAL TEST PLAN ASSUMPTIONS

| No. | Assumptions |
|-----|-------------|
| 1 | Developers memiliki pemahaman mendalam tentang aplikasi yang ditest |
| 2 | Tester mengetahui Business Requirements |
| 3 | Semua defects akan diperbaiki melalui snapshot/JPEG format |
| 4 | Test team akan disediakan akses ke test environment via VPN connectivity |
| 5 | Server web, middleware tier, dan database servers fully deployed, installed, dan configured |
| 6 | Tidak ada downtime environment selama test due to outages atau defect fixes |
| 7 | System akan diperlakukan sebagai blackbox |
| 8 | Testing team akan menggunakan preloaded data yang tersedia di sistem |
| 9 | SQL Injection dan XSS characters tidak akan diperhatikan di test cycle ini |
| 10 | Database 'name' field sengaja tidak diisi sebagai bagian dari testing strategy |

---

## B. TEST CASE LENGKAP

### TEST SUITE 1: USER AUTHENTICATION & AUTHORIZATION

#### TEST CASE TC_AUTH_001: Login dengan Kredensial Valid
**Test Case ID:** FT_001  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** Critical  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: 2221101826, Password: 2221101826 |
| Prerequisites | 1. Akun Peserta sudah terdaftar dan aktif |
| Expected Result | Login berhasil, redirect ke index.php (Dashboard) |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login pada URL `http://localhost/quiz-pengupil-main/login.php` | Login form ditampilkan dengan field Username, Password, dan tombol Sign In | | |
| 2 | Masukkan username yang valid: `2221101826` | Input diterima dengan benar | | |
| 3 | Masukkan password yang valid: `2221101826` | Input diterima dengan benar | | |
| 4 | Klik tombol "Sign In" | Login berhasil dan redirect ke index.php (Dashboard) dengan pesan selamat datang | | |
| 5 | Verifikasi session username tersimpan | Session `$_SESSION['username']` = `2221101826` | | |

---

#### TEST CASE TC_AUTH_002: Login dengan Password Kosong
**Test Case ID:** FT_002  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: 2221101826, Password: (kosong) |
| Prerequisites | 1. Akun Peserta sudah terdaftar |
| Expected Result | Validation error: "Data tidak boleh kosong !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login | Login form ditampilkan | | |
| 2 | Masukkan username: `2221101826` | Input diterima | | |
| 3 | Biarkan password kosong | Field password tetap kosong | | |
| 4 | Klik tombol "Sign In" | Menampilkan error message: "Data tidak boleh kosong !!" | | |
| 5 | User tetap di halaman login | Halaman login masih ditampilkan, tidak ada redirect | | |

---

#### TEST CASE TC_AUTH_003: Login dengan Username Kosong
**Test Case ID:** FT_003  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: (kosong), Password: 2221101826 |
| Prerequisites | 1. Akun Peserta sudah terdaftar |
| Expected Result | Validation error: "Data tidak boleh kosong !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login | Login form ditampilkan | | |
| 2 | Biarkan username kosong | Field username tetap kosong | | |
| 3 | Masukkan password: `2221101826` | Input diterima | | |
| 4 | Klik tombol "Sign In" | Menampilkan error message: "Data tidak boleh kosong !!" | | |
| 5 | User tetap di halaman login | Tidak ada redirect, form tetap ditampilkan | | |

---

#### TEST CASE TC_AUTH_004: Login dengan Username yang Tidak Terdaftar
**Test Case ID:** FT_004  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: usertidakada, Password: password123 |
| Prerequisites | 1. Username tidak terdaftar di database |
| Expected Result | Error: "Register User Gagal !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login | Login form ditampilkan | | |
| 2 | Masukkan username tidak terdaftar: `usertidakada` | Input diterima | | |
| 3 | Masukkan password: `password123` | Input diterima | | |
| 4 | Klik tombol "Sign In" | Error message: "Register User Gagal !!" ditampilkan | | |
| 5 | User tetap di halaman login | Tidak ada redirect | | |

---

#### TEST CASE TC_AUTH_005: Login dengan Password Benar dan Username Salah
**Test Case ID:** FT_005  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: usersalah, Password: 2221101826 (valid password) |
| Prerequisites | 1. Username tidak ada di database, tapi password benar untuk user lain |
| Expected Result | Login gagal: "Register User Gagal !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login | Login form ditampilkan | | |
| 2 | Masukkan username salah: `usersalah` | Input diterima | | |
| 3 | Masukkan password valid: `2221101826` | Input diterima | | |
| 4 | Klik tombol "Sign In" | Error: "Register User Gagal !!" ditampilkan | | |
| 5 | Verifikasi session tidak terbuat | `$_SESSION['username']` tidak ada | | |

---

#### TEST CASE TC_AUTH_006: Login dengan Username Benar dan Password Salah
**Test Case ID:** FT_006  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: 2221101826, Password: passwordsalah |
| Prerequisites | 1. Username ada di database, password tidak sesuai |
| Expected Result | Login gagal, password tidak cocok |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login | Login form ditampilkan | | |
| 2 | Masukkan username valid: `2221101826` | Input diterima | | |
| 3 | Masukkan password salah: `passwordsalah` | Input diterima | | |
| 4 | Klik tombol "Sign In" | Login gagal, user tetap di halaman login (password tidak terverifikasi) | | |
| 5 | Verifikasi tidak ada error message yang menunjukkan tipe error | Page tidak menampilkan pesan error spesifik | | |

---

#### TEST CASE TC_AUTH_007: Login Rate Limiting (Multiple Failed Attempts)
**Test Case ID:** FT_007  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** Medium  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: 2221101826, Password: berbagai password salah |
| Prerequisites | 1. Account terdaftar, user melakukan banyak login gagal |
| Expected Result | Sistem menerapkan rate limiting setelah beberapa kali gagal |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login | Login form ditampilkan | | |
| 2 | Coba login dengan password salah 5 kali berturut-turut | Setiap percobaan ditolak | | |
| 3 | Pada percobaan ke 6 | Sistem seharusnya menerapkan rate limiting atau menampilkan warning | | |
| 4 | Tunggu beberapa menit | Rate limiting reset (jika ada) | | |
| 5 | Coba login lagi dengan password benar | Login berhasil setelah reset periode | | |

---

#### TEST CASE TC_AUTH_008: Login dengan Token/Session yang Expired
**Test Case ID:** FT_008  
**Test Scenario:** User Authentication & Authorization  
**Requirement:** S1  
**Priority:** Medium  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Session ID yang sudah kadaluarsa |
| Prerequisites | 1. User sudah login sebelumnya, session sudah expired |
| Expected Result | Session dihapus, redirect ke login.php |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | User login dengan sukses | Session `$_SESSION['username']` tersimpan | | |
| 2 | Tunggu sampai session timeout (default 24 menit atau sesuai config) | Session expire | | |
| 3 | Coba akses halaman protected (index.php) | Redirect ke login.php | | |
| 4 | Verifikasi session sudah dihapus | `$_SESSION['username']` tidak ada | | |

---

### TEST SUITE 2: USER REGISTRATION

#### TEST CASE TC_REG_001: Register dengan Data Lengkap dan Valid
**Test Case ID:** FT_009  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** Critical  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Name: (optional/kosong), Username: testuser123, Email: test@example.com, Password: test123456, Re-Password: test123456 |
| Prerequisites | 1. Username belum terdaftar di database |
| Expected Result | Register berhasil, redirect ke login.php, user dapat login dengan credential baru |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register pada URL `http://localhost/quiz-pengupil-main/register.php` | Register form ditampilkan dengan field Nama, Email, Username, Password, Re-Password | | |
| 2 | (Optional) Masukkan nama: (kosong, karena field name tidak required) | Boleh kosong | | |
| 3 | Masukkan email valid: `test@example.com` | Input diterima | | |
| 4 | Masukkan username: `testuser123` | Input diterima | | |
| 5 | Masukkan password: `test123456` | Input diterima (masked) | | |
| 6 | Masukkan re-password: `test123456` | Input diterima (masked) | | |
| 7 | Klik tombol "Register" | Register berhasil, redirect ke login.php | | |
| 8 | Verifikasi data di database | Username `testuser123` sudah tersimpan di table users dengan password ter-hash | | |
| 9 | Login dengan credential baru | Username: testuser123, Password: test123456 harus berhasil | | |

---

#### TEST CASE TC_REG_002: Register dengan Email Kosong
**Test Case ID:** FT_010  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Name: Test User, Username: testuser456, Email: (kosong), Password: test123456, Re-Password: test123456 |
| Prerequisites | 1. Username belum terdaftar |
| Expected Result | Validation error: "Data tidak boleh kosong !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Masukkan nama: `Test User` | Input diterima | | |
| 3 | Biarkan email kosong | Field email tetap kosong | | |
| 4 | Masukkan username: `testuser456` | Input diterima | | |
| 5 | Masukkan password dan re-password | Input diterima | | |
| 6 | Klik tombol "Register" | Error: "Data tidak boleh kosong !!" ditampilkan | | |
| 7 | Verifikasi user tidak tersimpan di database | Username `testuser456` tidak ada di table users | | |

---

#### TEST CASE TC_REG_003: Register dengan Username Kosong
**Test Case ID:** FT_011  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Name: Test User, Username: (kosong), Email: test@example.com, Password: test123456, Re-Password: test123456 |
| Prerequisites | 1. Data lainnya valid |
| Expected Result | Validation error: "Data tidak boleh kosong !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Masukkan nama dan email | Input diterima | | |
| 3 | Biarkan username kosong | Field username tetap kosong | | |
| 4 | Masukkan password dan re-password | Input diterima | | |
| 5 | Klik tombol "Register" | Error: "Data tidak boleh kosong !!" ditampilkan | | |
| 6 | Verifikasi tidak ada user baru | Database tidak berubah | | |

---

#### TEST CASE TC_REG_004: Register dengan Username Sudah Terdaftar
**Test Case ID:** FT_012  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Name: User Baru, Username: 2221101826 (sudah ada), Email: newuser@example.com, Password: pass123456, Re-Password: pass123456 |
| Prerequisites | 1. Username 2221101826 sudah terdaftar di database |
| Expected Result | Duplicate error: "Username sudah terdaftar !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Isi semua field dengan data valid | Input diterima | | |
| 3 | Masukkan username yang sudah ada: `2221101826` | Input diterima | | |
| 4 | Klik tombol "Register" | Error: "Username sudah terdaftar !!" ditampilkan | | |
| 5 | Verifikasi email tidak duplikasi | Data email baru tidak tersimpan | | |

---

#### TEST CASE TC_REG_005: Register dengan Password dan Re-Password Tidak Sama
**Test Case ID:** FT_013  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Name: Test User, Username: testuser789, Email: test@example.com, Password: test123456, Re-Password: test654321 |
| Prerequisites | 1. Username belum terdaftar |
| Expected Result | Validation error: "Password tidak sama !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Isi semua field kecuali re-password | Input diterima | | |
| 3 | Masukkan password: `test123456` | Input diterima (masked) | | |
| 4 | Masukkan re-password berbeda: `test654321` | Input diterima (masked) | | |
| 5 | Klik tombol "Register" | Error: "Password tidak sama !!" ditampilkan di bawah field Re-Password | | |
| 6 | Verifikasi user tidak tersimpan | Username `testuser789` tidak ada di database | | |

---

#### TEST CASE TC_REG_006: Register dengan Password Kosong
**Test Case ID:** FT_014  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** High  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Name: Test User, Username: testuser999, Email: test@example.com, Password: (kosong), Re-Password: (kosong) |
| Prerequisites | 1. Email belum digunakan |
| Expected Result | Validation error: "Data tidak boleh kosong !!" |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Isi field name, email, username | Input diterima | | |
| 3 | Biarkan password kosong | Field password tetap kosong | | |
| 4 | Biarkan re-password kosong | Field re-password tetap kosong | | |
| 5 | Klik tombol "Register" | Error: "Data tidak boleh kosong !!" ditampilkan | | |
| 6 | Verifikasi database | Tidak ada user baru | | |

---

#### TEST CASE TC_REG_007: Register dengan Format Email Invalid
**Test Case ID:** FT_015  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** Medium  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Name: Test User, Username: testuser001, Email: invalidemail, Password: test123456, Re-Password: test123456 |
| Prerequisites | 1. Email format tidak valid (tidak ada @) |
| Expected Result | Browser validation atau server-side validation error |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Isi field lain dengan valid | Input diterima | | |
| 3 | Masukkan email invalid: `invalidemail` | Input diterima oleh form |  | |
| 4 | Klik tombol "Register" | Browser validation menampilkan error "Please include an '@' in the email address" ATAU server menolak | | |
| 5 | Verifikasi email tidak tersimpan | Database tidak berubah | | |

---

#### TEST CASE TC_REG_008: Register dengan Password Panjang (Edge Case)
**Test Case ID:** FT_016  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** Low  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Password dengan 100+ karakter, kombinasi spesial karakter |
| Prerequisites | 1. Password sangat panjang |
| Expected Result | Register berhasil (password di-hash dengan aman) |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Isi field name, email, username | Input diterima | | |
| 3 | Masukkan password sangat panjang: `aA1!aA1!aA1!aA1!aA1!aA1!...` (100 karakter) | Input diterima (masked) | | |
| 4 | Masukkan re-password sama | Input diterima | | |
| 5 | Klik tombol "Register" | Register berhasil | | |
| 6 | Login dengan password panjang | Login berhasil dengan password tersebut | | |

---

#### TEST CASE TC_REG_009: Register dengan Karakter Spesial di Username
**Test Case ID:** FT_017  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** Medium  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: user@name#123, Password: test123456 |
| Prerequisites | 1. Username dengan karakter spesial |
| Expected Result | Register berhasil (username di-escape dengan aman) atau error validation |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Isi field lainnya valid | Input diterima | | |
| 3 | Masukkan username dengan spesial char: `user@name#123` | Input diterima | | |
| 4 | Isi password dan re-password | Input diterima | | |
| 5 | Klik tombol "Register" | Register berhasil (username di-escape via mysqli_real_escape_string) | | |
| 6 | Verifikasi di database | Username tersimpan dengan aman (escaped) | | |
| 7 | Login dengan username tersebut | Login berhasil | | |

---

#### TEST CASE TC_REG_010: Register Redirect ke Login (New Flow)
**Test Case ID:** FT_018  
**Test Scenario:** User Registration  
**Requirement:** S2  
**Priority:** Critical  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Test Data | Username: newuser2025, Email: newuser@2025.com, Password: secure123456 |
| Prerequisites | 1. Username belum ada di database |
| Expected Result | Register berhasil → Redirect ke login.php (bukan index.php) |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register form ditampilkan | | |
| 2 | Isi semua field dengan valid data | Input diterima | | |
| 3 | Klik tombol "Register" | Data tersimpan di database | | |
| 4 | Verifikasi redirect | Browser redirect ke login.php (bukan index.php) | | |
| 5 | Periksa URL | URL berubah menjadi `http://localhost/quiz-pengupil-main/login.php` | | |
| 6 | Login dengan user baru | Login dengan newuser2025 / secure123456 berhasil | | |
| 7 | Verifikasi session | Session `$_SESSION['username']` = newuser2025 | | |
| 8 | Akses dashboard | Dapat mengakses index.php setelah login berhasil | | |

---

### TEST SUITE 3: NAVIGATION & UI FLOW

#### TEST CASE TC_NAV_001: Register Link di Login Page
**Test Case ID:** FT_019  
**Test Scenario:** Navigation  
**Requirement:** UI Flow  
**Priority:** Medium  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Prerequisites | 1. User berada di halaman login |
| Expected Result | Link "Register" navigate ke register.php |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman login | Login page ditampilkan | | |
| 2 | Lihat text "Belum punya account? Register" | Link tersedia | | |
| 3 | Klik link "Register" | Navigate ke register.php | | |
| 4 | Verifikasi URL | URL = `http://localhost/quiz-pengupil-main/register.php` | | |

---

#### TEST CASE TC_NAV_002: Login Link di Register Page
**Test Case ID:** FT_020  
**Test Scenario:** Navigation  
**Requirement:** UI Flow  
**Priority:** Medium  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Prerequisites | 1. User berada di halaman register |
| Expected Result | Link "Login" navigate ke login.php |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Buka halaman register | Register page ditampilkan | | |
| 2 | Lihat text "Sudah punya account? Login" | Link tersedia | | |
| 3 | Klik link "Login" | Navigate ke login.php | | |
| 4 | Verifikasi URL | URL = `http://localhost/quiz-pengupil-main/login.php` | | |

---

#### TEST CASE TC_NAV_003: Logout Button di Dashboard
**Test Case ID:** FT_021  
**Test Scenario:** Navigation  
**Requirement:** UI Flow  
**Priority:** Medium  

| Element | Detail |
|---------|--------|
| Created By | Tester |
| Reviewed By | Reza |
| Prerequisites | 1. User sudah login dan berada di index.php |
| Expected Result | Logout button menghapus session dan redirect ke login.php |

**Test Steps:**

| Step # | Step Details | Expected Results | Actual Results | Pass/Fail |
|--------|-------------|------------------|----------------|-----------|
| 1 | Login dengan user valid | Redirect ke index.php berhasil | | |
| 2 | Verifikasi Logout button ada | Tombol "Logout" terlihat di dashboard | | |
| 3 | Klik tombol "Logout" | Session dihapus dan redirect ke login.php | | |
| 4 | Verifikasi URL | URL = `http://localhost/quiz-pengupil-main/login.php` | | |
| 5 | Coba akses index.php langsung | Redirect ke login.php (tidak bisa akses tanpa login) | | |

---

## C. TEST SUMMARY

| Test Suite | Total Test Cases | Test Case IDs |
|-----------|------------------|---------------|
| User Authentication & Authorization | 8 | FT_001 - FT_008 |
| User Registration | 10 | FT_009 - FT_018 |
| Navigation & UI Flow | 3 | FT_019 - FT_021 |
| **TOTAL** | **21** | |

---

## D. ENTRY & EXIT CRITERIA

### Entry Criteria:
- [ ] Semua code sudah di-review dan diapprove
- [ ] Environment sudah siap (local/staging/production)
- [ ] Database sudah terinisialisasi dengan schema yang benar
- [ ] Test data sudah disiapkan
- [ ] Test tools (Selenium) sudah terinstall

### Exit Criteria:
- [ ] Semua 21 test cases sudah diexecute
- [ ] Critical bugs sudah diperbaiki
- [ ] High priority bugs diperbaiki atau documented
- [ ] Test report dibuat dan diserahkan
- [ ] Sign-off dari stakeholder diterima

---

## E. DEFECT SEVERITY LEVELS

| Severity | Description |
|----------|-------------|
| **Critical** | Modul tidak bisa digunakan, menghalangi user melakukan action utama |
| **High** | Modul berfungsi tapi ada issue signifikan yang mengganggu user experience |
| **Medium** | Modul berfungsi, issue minor yang tidak terlalu mengganggu |
| **Low** | Cosmetic issue atau edge case yang jarang terjadi |

---

**Dokumen ini dibuat untuk keperluan functional testing Login & Register Module**  
**Tanggal Update: 15 Januari 2026**
