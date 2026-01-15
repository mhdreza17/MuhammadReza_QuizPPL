# 🚀 QUICK REFERENCE GUIDE
## Login & Register Module Testing

---

## ⚡ QUICK START (5 MENIT)

### Setup Database
```sql
-- Buka phpMyAdmin: http://localhost/phpmyadmin
-- Import: db/quiz_pengupil.sql
-- Done!
```

### Run Manual Test
```
URL: http://localhost/quiz-pengupil-main/login.php
Username: 2221101826
Password: 2221101826
Click "Sign In" → Dashboard ✅
```

### Run Automated Test
```powershell
pip install -r requirements-test.txt
pytest test_selenium_login_register.py -v
```

### Push ke GitHub
```powershell
git init
git add .
git commit -m "Add testing"
git remote add origin https://github.com/YOUR_USERNAME/quiz-pengupil.git
git push -u origin main
```

---

## 📋 FILE REFERENCE

| File | Tujuan | Akses |
|------|--------|-------|
| `login.php` | Login page | `http://localhost/...quiz-pengupil-main/login.php` |
| `register.php` | Register page | `http://localhost/.../register.php` |
| `index.php` | Dashboard (protected) | Hanya setelah login |
| `logout.php` | Logout & clear session | Buka dari dashboard |
| `test_selenium_login_register.py` | Run: `pytest test_selenium_login_register.py -v` | |
| `.github/workflows/selenium-tests.yml` | Auto run saat push | |
| `PANDUAN_TESTING_LENGKAP.md` | Baca ini! | |

---

## ✅ CHECKLIST VERIFIKASI

- [ ] Apache & MySQL running
- [ ] Database imported
- [ ] Test user exists (2221101826 / 2221101826)
- [ ] login.php accessible
- [ ] Manual test berhasil
- [ ] Python dependencies installed
- [ ] Selenium tests pass
- [ ] GitHub repo created
- [ ] GitHub Actions running

---

## 🐛 COMMON ISSUES

### "Connection refused"
```powershell
# Check Apache & MySQL
xampp-control.exe  # Start them
```

### "ModuleNotFoundError: No module named 'selenium'"
```powershell
pip install -r requirements-test.txt
```

### "Test timeout"
```python
# Edit test_selenium_login_register.py
TIMEOUT = 20  # Increase from 10
```

### "Test failed on Windows"
```powershell
# Update WebDriver
pip install --upgrade webdriver-manager
```

---

## 🎯 TEST RESULTS INTERPRETATION

```
21 PASSED          ✅ Semua test pass!
20 PASSED 1 FAILED ❌ 1 test gagal, lihat error message
FAILED ... TimeoutException → Increase TIMEOUT value
FAILED ... NoSuchElementException → Check HTML element
```

---

## 📊 TEST SUMMARY

- **Total:** 21 test cases
- **Passed:** Semua seharusnya pass
- **Duration:** ~2 menit
- **Coverage:** Login, Register, Navigation

---

## 🔧 TROUBLESHOOTING COMMANDS

```powershell
# Check Python version
python --version

# Check Selenium installed
python -c "import selenium; print(selenium.__version__)"

# Check pytest installed
pytest --version

# Run test verbose
pytest test_selenium_login_register.py -vv

# Run test dengan detail error
pytest test_selenium_login_register.py -vv --tb=long

# Check database
mysql -h localhost -u root -p quiz_pengupil -e "SELECT * FROM users;"

# Check server
curl http://localhost/quiz-pengupil-main/login.php
```

---

## 📚 DOKUMENTASI LINKS

| Doc | Isi | Read |
|-----|-----|------|
| PANDUAN_TESTING_LENGKAP.md | **WAJIB BACA** - Step-by-step guide | 📖 |
| TEST_CASE_DOCUMENTATION.md | Detail 21 test cases | 📋 |
| README_TESTING.md | Project overview | 📝 |
| RINGKASAN_PENGERJAAN.md | Summary pengerjaan | 📊 |
| Ini | Quick reference | ⚡ |

---

## 💡 TIPS

1. **Baca PANDUAN_TESTING_LENGKAP.md dulu sebelum mulai**
2. **Jalankan manual test dulu sebelum automated test**
3. **Check database di phpMyAdmin untuk verify**
4. **Lihat error message untuk debugging**
5. **Update GitHub Actions log jika ada issue**

---

## 🎓 REPOSITORY LINKS

Setelah push ke GitHub, akses di:

```
Repository: https://github.com/YOUR_USERNAME/quiz-pengupil
Actions: https://github.com/YOUR_USERNAME/quiz-pengupil/actions
Commits: https://github.com/YOUR_USERNAME/quiz-pengupil/commits
Pull Requests: https://github.com/YOUR_USERNAME/quiz-pengupil/pulls
```

---

## ✨ KEY FEATURES

✅ 21 Test Cases  
✅ Selenium Automation  
✅ GitHub Actions CI/CD  
✅ Complete Documentation  
✅ 4 Bugs Fixed  
✅ Production Ready  

---

## 📞 SUPPORT

**Bingung?** → Baca `PANDUAN_TESTING_LENGKAP.md`  
**Troubleshooting?** → Lihat bagian "Troubleshooting" di panduan  
**Error saat test?** → Check GitHub Actions logs  
**Database issue?** → Use phpMyAdmin  

---

**Happy Testing! 🚀**
