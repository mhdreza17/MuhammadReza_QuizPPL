"""
Test Suite untuk Login & Register Module - Aplikasi Quiz Pengupil
Menggunakan Selenium untuk automated testing

Requirement: pip install selenium pytest python-dotenv
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_URL = os.getenv('BASE_URL', 'http://localhost/quiz-pengupil-main')
LOGIN_URL = f'{BASE_URL}/login.php'
REGISTER_URL = f'{BASE_URL}/register.php'
INDEX_URL = f'{BASE_URL}/index.php'
TIMEOUT = 10

# Test Data
VALID_USER = {
    'username': '2221101826',
    'password': '2221101826'
}

NEW_USER = {
    'name': 'Test User',
    'email': f'testuser{int(time.time())}@example.com',
    'username': f'testuser{int(time.time())}',
    'password': 'test123456',
    'repassword': 'test123456'
}


class TestLoginModule:
    """Test Suite untuk Login Module"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup WebDriver sebelum setiap test"""
        options = webdriver.ChromeOptions()
        # Headless mode untuk GitHub Actions (tidak perlu display)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        
        yield
        
        # Cleanup setelah test
        self.driver.quit()
    
    def clear_session(self):
        """Clear session dengan logout"""
        try:
            self.driver.get(f'{BASE_URL}/logout.php')
            time.sleep(2)
        except:
            pass
    
    # ===== TEST CASE FT_001 =====
    def test_FT_001_login_with_valid_credentials(self):
        """TEST CASE FT_001: Login dengan Kredensial Valid"""
        print("\n=== TEST CASE FT_001: Login dengan Kredensial Valid ===")
        
        self.clear_session()
        self.driver.get(LOGIN_URL)
        
        # Step 1: Verify login form ditampilkan
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        assert username_field.is_displayed(), "Username field tidak terlihat"
        assert password_field.is_displayed(), "Password field tidak terlihat"
        print("✓ Step 1: Login form ditampilkan")
        
        # Step 2-3: Isi username dan password
        username_field.clear()
        username_field.send_keys(VALID_USER['username'])
        password_field.clear()
        password_field.send_keys(VALID_USER['password'])
        print("✓ Step 2-3: Username dan password diisi")
        
        # Step 4: Klik tombol Sign In
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        
        # Tunggu redirect
        time.sleep(3)
        
        # Verifikasi berhasil redirect ke index.php
        assert 'index.php' in self.driver.current_url, f"Expected URL contain 'index.php', got {self.driver.current_url}"
        print("✓ Step 4: Login berhasil, redirect ke index.php")
        
        # Step 5: Verifikasi session
        page_text = self.driver.page_source
        assert VALID_USER['username'] in page_text or 'Selamat Datang' in page_text, "Username tidak ditemukan di dashboard"
        print("✓ Step 5: Session berhasil tersimpan")
        print("✅ TEST PASSED: FT_001\n")
    
    # ===== TEST CASE FT_002 =====
    def test_FT_002_login_with_empty_password(self):
        """TEST CASE FT_002: Login dengan Password Kosong"""
        print("\n=== TEST CASE FT_002: Login dengan Password Kosong ===")
        
        self.clear_session()
        self.driver.get(LOGIN_URL)
        
        # Isi username saja
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        username_field.send_keys(VALID_USER['username'])
        print("✓ Username diisi")
        
        # Biarkan password kosong dan submit
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(2)
        
        # Verifikasi error message
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger'))
            )
            assert 'Data tidak boleh kosong' in error_element.text, f"Expected error message, got: {error_element.text}"
            print("✓ Error message: 'Data tidak boleh kosong' ditampilkan")
        except:
            pytest.fail("Error message tidak ditemukan")
        
        # Verifikasi tetap di halaman login
        assert 'login.php' in self.driver.current_url, "Harus tetap di login.php"
        print("✓ User tetap di halaman login")
        print("✅ TEST PASSED: FT_002\n")
    
    # ===== TEST CASE FT_003 =====
    def test_FT_003_login_with_empty_username(self):
        """TEST CASE FT_003: Login dengan Username Kosong"""
        print("\n=== TEST CASE FT_003: Login dengan Username Kosong ===")
        
        self.clear_session()
        self.driver.get(LOGIN_URL)
        
        # Isi password saja, biarkan username kosong
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, 'InputPassword')))
        password_field.send_keys(VALID_USER['password'])
        print("✓ Password diisi")
        
        # Submit
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(2)
        
        # Verifikasi error message
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger'))
            )
            assert 'Data tidak boleh kosong' in error_element.text
            print("✓ Error message ditampilkan")
        except:
            pytest.fail("Error message tidak ditemukan")
        
        assert 'login.php' in self.driver.current_url
        print("✓ User tetap di login.php")
        print("✅ TEST PASSED: FT_003\n")
    
    # ===== TEST CASE FT_004 =====
    def test_FT_004_login_with_nonexistent_username(self):
        """TEST CASE FT_004: Login dengan Username yang Tidak Terdaftar"""
        print("\n=== TEST CASE FT_004: Login dengan Username Tidak Terdaftar ===")
        
        self.clear_session()
        self.driver.get(LOGIN_URL)
        
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        
        username_field.send_keys('usertidakada12345')
        password_field.send_keys('anypassword')
        print("✓ Username & password diisi")
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(2)
        
        # Verifikasi error message
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger'))
            )
            assert 'Register User Gagal' in error_element.text or 'Gagal' in error_element.text
            print("✓ Error message: User tidak ditemukan")
        except:
            pytest.fail("Error message tidak ditemukan")
        
        assert 'login.php' in self.driver.current_url
        print("✓ Tetap di login.php")
        print("✅ TEST PASSED: FT_004\n")
    
    # ===== TEST CASE FT_006 =====
    def test_FT_006_login_with_wrong_password(self):
        """TEST CASE FT_006: Login dengan Password Salah"""
        print("\n=== TEST CASE FT_006: Login dengan Password Salah ===")
        
        self.clear_session()
        self.driver.get(LOGIN_URL)
        
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        
        username_field.send_keys(VALID_USER['username'])
        password_field.send_keys('passwordsalah123')
        print("✓ Username valid, password salah diisi")
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(2)
        
        # Verifikasi tetap di login (password tidak cocok)
        # Note: Sistem tidak menampilkan pesan khusus untuk password salah
        assert 'login.php' in self.driver.current_url, "Harus tetap di login.php"
        print("✓ Login ditolak, tetap di login.php")
        print("✅ TEST PASSED: FT_006\n")


class TestRegisterModule:
    """Test Suite untuk Register Module"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup WebDriver sebelum setiap test"""
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        
        yield
        
        self.driver.quit()
    
    def clear_session(self):
        """Clear session"""
        try:
            self.driver.get(f'{BASE_URL}/logout.php')
            time.sleep(2)
        except:
            pass
    
    # ===== TEST CASE FT_009 =====
    def test_FT_009_register_with_valid_data(self):
        """TEST CASE FT_009: Register dengan Data Lengkap dan Valid"""
        print("\n=== TEST CASE FT_009: Register dengan Data Valid ===")
        
        self.clear_session()
        self.driver.get(REGISTER_URL)
        
        # Step 1: Verify register form ditampilkan
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, 'InputEmail')))
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        repass_field = self.driver.find_element(By.ID, 'InputRePassword')
        
        assert all([email_field.is_displayed(), username_field.is_displayed(),
                   password_field.is_displayed(), repass_field.is_displayed()]), \
            "Semua field harus terlihat"
        print("✓ Step 1: Register form ditampilkan")
        
        # Step 2-6: Isi semua field
        email_field.send_keys(NEW_USER['email'])
        username_field.send_keys(NEW_USER['username'])
        password_field.send_keys(NEW_USER['password'])
        repass_field.send_keys(NEW_USER['repassword'])
        print(f"✓ Step 2-6: Data diisi (username: {NEW_USER['username']})")
        
        # Step 7: Klik Register
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(3)
        
        # Step 7-8: Verifikasi redirect ke login.php
        assert 'login.php' in self.driver.current_url, f"Expected login.php, got {self.driver.current_url}"
        print("✓ Step 7: Register berhasil, redirect ke login.php")
        
        # Step 9: Login dengan user baru
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        
        username_field.send_keys(NEW_USER['username'])
        password_field.send_keys(NEW_USER['password'])
        print("✓ Login dengan user baru")
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(3)
        
        # Verifikasi login berhasil
        assert 'index.php' in self.driver.current_url, "Login dengan user baru harus berhasil"
        print("✓ Step 9: Login dengan user baru berhasil")
        print("✅ TEST PASSED: FT_009\n")
    
    # ===== TEST CASE FT_010 =====
    def test_FT_010_register_with_empty_email(self):
        """TEST CASE FT_010: Register dengan Email Kosong"""
        print("\n=== TEST CASE FT_010: Register dengan Email Kosong ===")
        
        self.clear_session()
        self.driver.get(REGISTER_URL)
        
        # Isi field kecuali email
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        repass_field = self.driver.find_element(By.ID, 'InputRePassword')
        
        username_field.send_keys(f'testuser{int(time.time())}')
        password_field.send_keys('test123456')
        repass_field.send_keys('test123456')
        print("✓ Semua field diisi kecuali email (kosong)")
        
        # Submit
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(2)
        
        # Verifikasi error
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger'))
            )
            assert 'Data tidak boleh kosong' in error_element.text
            print("✓ Error message ditampilkan")
        except:
            pytest.fail("Error message tidak ditemukan")
        
        assert 'register.php' in self.driver.current_url
        print("✓ Tetap di register.php")
        print("✅ TEST PASSED: FT_010\n")
    
    # ===== TEST CASE FT_012 =====
    def test_FT_012_register_with_existing_username(self):
        """TEST CASE FT_012: Register dengan Username Sudah Terdaftar"""
        print("\n=== TEST CASE FT_012: Register dengan Username Sudah Ada ===")
        
        self.clear_session()
        self.driver.get(REGISTER_URL)
        
        # Coba register dengan username yang sudah ada
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, 'InputEmail')))
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        repass_field = self.driver.find_element(By.ID, 'InputRePassword')
        
        email_field.send_keys(f'newemail{int(time.time())}@example.com')
        username_field.send_keys(VALID_USER['username'])  # Username yang sudah ada
        password_field.send_keys('test123456')
        repass_field.send_keys('test123456')
        print(f"✓ Coba register dengan username existing: {VALID_USER['username']}")
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(2)
        
        # Verifikasi error
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger'))
            )
            assert 'sudah terdaftar' in error_element.text.lower()
            print("✓ Error: Username sudah terdaftar ditampilkan")
        except:
            pytest.fail("Error message tidak ditemukan")
        
        assert 'register.php' in self.driver.current_url
        print("✓ Tetap di register.php")
        print("✅ TEST PASSED: FT_012\n")
    
    # ===== TEST CASE FT_013 =====
    def test_FT_013_register_password_mismatch(self):
        """TEST CASE FT_013: Register dengan Password dan Re-Password Tidak Sama"""
        print("\n=== TEST CASE FT_013: Register Password Tidak Sama ===")
        
        self.clear_session()
        self.driver.get(REGISTER_URL)
        
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, 'InputEmail')))
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        repass_field = self.driver.find_element(By.ID, 'InputRePassword')
        
        email_field.send_keys(f'test{int(time.time())}@example.com')
        username_field.send_keys(f'testuser{int(time.time())}')
        password_field.send_keys('password123456')
        repass_field.send_keys('passwordberbeda')  # Berbeda!
        print("✓ Password dan Re-Password tidak sama")
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(2)
        
        # Verifikasi error
        try:
            error_element = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'text-danger'))
            )
            assert 'tidak sama' in error_element.text.lower()
            print("✓ Error: Password tidak sama ditampilkan")
        except:
            pytest.fail("Error message tidak ditemukan")
        
        assert 'register.php' in self.driver.current_url
        print("✓ Tetap di register.php")
        print("✅ TEST PASSED: FT_013\n")
    
    # ===== TEST CASE FT_018 =====
    def test_FT_018_register_redirect_to_login(self):
        """TEST CASE FT_018: Register Redirect ke Login (New Flow)"""
        print("\n=== TEST CASE FT_018: Register Redirect ke Login (NEW FLOW) ===")
        
        self.clear_session()
        self.driver.get(REGISTER_URL)
        
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, 'InputEmail')))
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        repass_field = self.driver.find_element(By.ID, 'InputRePassword')
        
        test_username = f'newuser{int(time.time())}'
        test_email = f'newuser{int(time.time())}@2025.com'
        test_password = 'secure123456'
        
        email_field.send_keys(test_email)
        username_field.send_keys(test_username)
        password_field.send_keys(test_password)
        repass_field.send_keys(test_password)
        print(f"✓ Data register diisi (user: {test_username})")
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(3)
        
        # CRITICAL: Verifikasi redirect ke login.php (bukan index.php)
        assert 'login.php' in self.driver.current_url, \
            f"CRITICAL: Register harus redirect ke login.php, bukan index.php! URL: {self.driver.current_url}"
        print("✓ CRITICAL: Redirect ke login.php (bukan index.php)")
        
        # Login dengan user baru
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        
        username_field.send_keys(test_username)
        password_field.send_keys(test_password)
        print("✓ Login dengan user baru")
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(3)
        
        # Verifikasi login berhasil
        assert 'index.php' in self.driver.current_url, "User harus bisa login dengan credential baru"
        print("✓ Login berhasil setelah register")
        print("✅ TEST PASSED: FT_018 (CRITICAL TEST)\n")


class TestNavigationFlow:
    """Test Suite untuk Navigation Flow"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup WebDriver"""
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        
        yield
        
        self.driver.quit()
    
    # ===== TEST CASE FT_019 =====
    def test_FT_019_register_link_in_login_page(self):
        """TEST CASE FT_019: Register Link di Login Page"""
        print("\n=== TEST CASE FT_019: Register Link di Login Page ===")
        
        self.driver.get(LOGIN_URL)
        
        # Cari link register
        register_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'register.php')]"))
        )
        assert register_link.is_displayed(), "Register link tidak terlihat"
        print("✓ Register link ditemukan dan terlihat")
        
        # Klik link
        register_link.click()
        time.sleep(2)
        
        # Verifikasi navigate ke register.php
        assert 'register.php' in self.driver.current_url
        print("✓ Navigate ke register.php berhasil")
        print("✅ TEST PASSED: FT_019\n")
    
    # ===== TEST CASE FT_020 =====
    def test_FT_020_login_link_in_register_page(self):
        """TEST CASE FT_020: Login Link di Register Page"""
        print("\n=== TEST CASE FT_020: Login Link di Register Page ===")
        
        self.driver.get(REGISTER_URL)
        
        # Cari link login
        login_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'login.php')]"))
        )
        assert login_link.is_displayed(), "Login link tidak terlihat"
        print("✓ Login link ditemukan")
        
        # Klik link
        login_link.click()
        time.sleep(2)
        
        # Verifikasi navigate ke login.php
        assert 'login.php' in self.driver.current_url
        print("✓ Navigate ke login.php berhasil")
        print("✅ TEST PASSED: FT_020\n")
    
    # ===== TEST CASE FT_021 =====
    def test_FT_021_logout_button_functionality(self):
        """TEST CASE FT_021: Logout Button di Dashboard"""
        print("\n=== TEST CASE FT_021: Logout Button Functionality ===")
        
        # Login dulu
        self.driver.get(LOGIN_URL)
        username_field = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_field = self.driver.find_element(By.ID, 'InputPassword')
        
        username_field.send_keys(VALID_USER['username'])
        password_field.send_keys(VALID_USER['password'])
        
        submit_btn = self.driver.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(3)
        
        assert 'index.php' in self.driver.current_url, "Login harus berhasil"
        print("✓ User berhasil login ke index.php")
        
        # Cari logout button
        logout_btn = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'logout.php')]"))
        )
        assert logout_btn.is_displayed(), "Logout button tidak terlihat"
        print("✓ Logout button ditemukan")
        
        # Klik logout
        logout_btn.click()
        time.sleep(2)
        
        # Verifikasi redirect ke login.php
        assert 'login.php' in self.driver.current_url, "Harus redirect ke login.php setelah logout"
        print("✓ Logout berhasil, redirect ke login.php")
        
        # Coba akses index.php langsung
        self.driver.get(INDEX_URL)
        time.sleep(2)
        assert 'login.php' in self.driver.current_url, "Tidak bisa akses index tanpa login"
        print("✓ Tidak bisa akses index.php tanpa login (session dihapus)")
        print("✅ TEST PASSED: FT_021\n")


if __name__ == '__main__':
    # Jalankan tests dengan pytest
    # Command: pytest test_selenium_login_register.py -v
    pytest.main([__file__, '-v', '--tb=short'])
