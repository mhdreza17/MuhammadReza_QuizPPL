# 🔄 GITHUB ACTIONS WORKFLOW GUIDE

**File:** `.github/workflows/selenium-tests.yml`

---

## 📋 WORKFLOW OVERVIEW

Workflow ini secara otomatis menjalankan 21 Selenium test cases setiap kali ada push atau pull request ke GitHub.

---

## 🎯 TRIGGER EVENTS

Workflow akan otomatis trigger pada:

✅ **Push ke branch:**
```yaml
branches: [ main, develop ]
```

✅ **Pull Request ke branch:**
```yaml
branches: [ main, develop ]
```

✅ **Schedule (Daily):**
```yaml
cron: '0 2 * * *'  # Setiap hari pukul 02:00 UTC
```

✅ **Manual trigger:**
- Klik tombol "Run workflow" di GitHub Actions tab

---

## 🔧 WORKFLOW STRUCTURE (13 STEPS)

### STEP 1: 📥 CHECKOUT CODE
```
Mengambil code dari repository
Workspace: /github/workspace
```

### STEP 2: 🔧 SETUP ENVIRONMENT
```
- Setup PHP 8.1
- Setup Python 3.11
- Load cache dari pip
```

### STEP 3: 📦 INSTALL DEPENDENCIES
```
- Upgrade pip
- Install: selenium, pytest, python-dotenv, webdriver-manager
- Install Apache packages
- Enable Apache rewrite module
```

### STEP 4: 📂 COPY PROJECT FILES
```
- Copy project ke /var/www/html
- Set permissions untuk www-data
- Status: ✅ Project files copied
```

### STEP 5: 🔌 DATABASE SETUP
```
- Tunggu MySQL siap (max 60 detik)
- Import database schema: quiz_pengupil.sql
- Verifikasi table dengan: SHOW TABLES
- Status: ✅ Database schema imported
```

### STEP 6: ⏳ APPLICATION READY CHECK
```
- Tunggu Apache siap (max 60 detik)
- Health check: curl login.php
- Verifikasi "Sign-In" text ada
- Status: ✅ Application is healthy
```

### STEP 7: 🔐 CONFIGURATION
```
- Create .env file
- Set: BASE_URL, TEST_TIMEOUT
- Status: ✅ Environment file created
```

### STEP 8: 🧪 RUN SELENIUM TESTS
```
- Run: pytest test_selenium_login_register.py
- Output: junit.xml (test report)
- Output: report.html (detailed report)
- Expected: 21 PASSED
```

### STEP 9: 📊 PARSE TEST RESULTS
```
- Parse junit.xml
- Extract: Total Tests, Failures, Errors
- Create summary di GitHub Actions summary
- Display: ✅ All Tests PASSED! atau ❌ Some Tests FAILED!
```

### STEP 10: 📤 UPLOAD ARTIFACTS
```
- Upload: junit.xml (30 hari retention)
- Upload: report.html (30 hari retention)
- Download dari GitHub Actions UI
```

### STEP 11: 📈 UPLOAD COVERAGE
```
- Upload: htmlcov/ coverage report (7 hari retention)
```

### STEP 12: 📋 PUBLISH TEST REPORT
```
- Publish ke GitHub Actions checks
- Automatic comment di PR (jika PR)
- Title: 🧪 Selenium Test Results
```

### STEP 13: ✅ STATUS & SUCCESS
```
- Fail jika ada test yang failed
- Success message: ✅ All 21 test cases PASSED!
- Link ke run details
```

---

## ✅ EXPECTED OUTPUT

### Saat Semua Test PASSED:

```
=== WORKFLOW SUMMARY ===

✅ STEP 1: Checkout code                          [PASSED]
✅ STEP 2: Setup environment                      [PASSED]
✅ STEP 3: Install dependencies                   [PASSED]
✅ STEP 4: Copy project files                     [PASSED]
✅ STEP 5: Database setup                         [PASSED]
✅ STEP 6: Application ready check                [PASSED]
✅ STEP 7: Configuration                          [PASSED]
✅ STEP 8: Run Selenium Tests                     [PASSED]
  ├── test_FT_001_login_with_valid_credentials   [PASSED]
  ├── test_FT_002_login_with_empty_password      [PASSED]
  ├── ... (19 more test cases)
  └── test_FT_021_logout_button_functionality    [PASSED]
✅ STEP 9: Parse test results                     [PASSED]
✅ STEP 10: Upload artifacts                      [PASSED]
✅ STEP 11: Publish test report                   [PASSED]
✅ STEP 13: Tests completed successfully          [PASSED]

=== TEST EXECUTION SUMMARY ===
| Metric | Count |
|--------|-------|
| Total Tests | 21 |
| Failures | 0 |
| Errors | 0 |

✅ All Tests PASSED!
```

### Saat Ada Test yang FAILED:

```
=== WORKFLOW SUMMARY ===

✅ STEP 1-7: Setup                                [PASSED]
✅ STEP 8: Run Selenium Tests                     [FAILED]
  ├── test_FT_001_login_with_valid_credentials   [PASSED]
  ├── test_FT_009_register_with_valid_data       [PASSED]
  ├── test_FT_018_register_redirect_to_login     [FAILED]
  └── ... (18 more test cases)
❌ STEP 12: Fail if tests failed                  [FAILED]

=== TEST EXECUTION SUMMARY ===
| Metric | Count |
|--------|-------|
| Total Tests | 21 |
| Failures | 1 |
| Errors | 0 |

❌ Some Tests FAILED!
```

---

## 📊 HOW TO READ GITHUB ACTIONS LOGS

### 1. Buka GitHub Actions
```
https://github.com/YOUR_USERNAME/quiz-pengupil/actions
```

### 2. Klik Workflow Run
```
Pilih run terbaru (paling atas)
```

### 3. Klik Job "Selenium Tests"
```
Buka detail job untuk melihat semua steps
```

### 4. Expand Each Step
```
Click dropdown panah untuk melihat detail output
```

### 5. Search untuk Test Results
```
Cari di: STEP 9: Parse test results
Akan menampilkan summary table
```

---

## 🔍 ARTIFACTS & REPORTS

### Test Report Download

1. **Buka GitHub Actions run**
2. **Scroll ke bawah → Artifacts section**
3. **Download:**
   - `test-results-linux-XXXX.zip` (junit.xml + report.html)
   - `coverage-report-XXXX.zip` (htmlcov/)

### View Report Locally

```powershell
# Extract
Expand-Archive test-results-linux-XXXX.zip

# Open HTML report
Start-Process report.html
```

---

## 🚨 TROUBLESHOOTING

### ❌ Error: "Deprecated version of actions/upload-artifact"
**Solution:** Workflow sudah di-update ke v4 ✅

### ❌ Error: "MySQL not ready"
**Solution:** Workflow menunggu max 60 detik (increased from 30)

### ❌ Error: "Apache not responding"
**Solution:** Workflow menunggu max 60 detik + health check

### ❌ Error: "Database import failed"
**Check:**
- File `db/quiz_pengupil.sql` exists
- File tidak corrupted
- MySQL running

### ❌ Tests timing out
**Solution:** Increase timeout di pytest.ini
```ini
timeout = 600  # 10 minutes
```

---

## 📈 WORKFLOW CONFIGURATION

### Concurrency (Cancel in-progress)
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```
**Meaning:** Jika ada run baru, run yang lama akan di-cancel

### Timeout
```yaml
timeout-minutes: 30
```
**Meaning:** Jika workflow > 30 menit, akan auto-fail

### Services
```yaml
services:
  mysql:      # MySQL 8.0
  apache:     # PHP 8.1-Apache
```
**Meaning:** Automatically started & available

---

## 🎯 KEY FEATURES

✅ **13 Clear Steps** dengan emoji untuk easy tracking
✅ **Comprehensive Health Checks** - database, apache, app
✅ **Detailed Logging** - ✅ status di setiap step
✅ **Test Results Summary** - table format di GitHub Actions
✅ **Artifact Upload** - junit.xml + HTML report (v4)
✅ **Auto Reports** - Published ke GitHub checks
✅ **Error Handling** - continue-on-error for test run
✅ **Success Notification** - ✅ All 21 test cases PASSED!

---

## 📝 RECOMMENDED PRACTICES

1. **Monitor Workflow**
   - Klik Actions tab regularly
   - Check untuk ❌ failures

2. **Download Reports**
   - Simpan reports untuk dokumentasi
   - Review failed tests detail

3. **Fix Failed Tests**
   - Read error message
   - Fix code locally
   - Push & verify in workflow

4. **Schedule Tests**
   - Daily tests recommended
   - Detect regression early

5. **PR Requirements**
   - Set workflow sebagai required check
   - Block merge jika tests fail

---

## ⚙️ HOW TO SET PR REQUIREMENTS

1. **Go to Repository Settings**
2. **Branches → Branch protection rules**
3. **Add rule untuk "main" branch**
4. **Require:**
   - ✅ Require status checks to pass
   - ✅ Select "Selenium Test Results" check
5. **Save**

Sekarang PR hanya bisa di-merge jika tests PASSED ✅

---

## 🔗 WORKFLOW FILE LOCATION

```
.github/workflows/selenium-tests.yml
```

**Edit jika:**
- Butuh tambah/kurang trigger event
- Butuh ubah test framework
- Butuh tambah/kurang steps

**Do NOT edit jika:**
- Hanya ingin run test (push to trigger)
- Ingin download report (artifacts sudah ada)

---

## ✅ WORKFLOW VERIFICATION CHECKLIST

- [x] Version bump: `@v3` → `@v4` ✅
- [x] Deprecation fixed: upload-artifact updated
- [x] 13 clear steps dengan emoji
- [x] Health checks comprehensive
- [x] Test result parsing
- [x] Artifact upload (30 days)
- [x] Coverage upload (7 days)
- [x] Report publishing
- [x] Error handling
- [x] Success notification

---

**Workflow Status:** ✅ **UPDATED & PRODUCTION READY**

**Last Updated:** 15 Januari 2026  
**Version:** 2.0 (dengan 13 steps)
