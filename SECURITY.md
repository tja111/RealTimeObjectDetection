# Security Advisory

## ✅ UPDATED: Using Secure Versions

**As of the latest update, this project now uses patched, secure versions by default:**
- TensorFlow 2.12.1 (all 150+ CVEs fixed)
- OpenCV 4.8.1.78 (CVE-2023-4863 fixed)

The legacy vulnerable versions (TensorFlow 2.3.1, OpenCV 4.4.0.46) are still documented below for users following older tutorials.

## 🔒 Current Configuration (DEFAULT - SECURE)

This project now uses secure, patched versions by default:

```bash
# Install current default versions (SECURE)
pip install -r requirements.txt

# This will install:
# - tensorflow==2.12.1 (all CVEs patched)
# - opencv-python==4.8.1.78 (CVE-2023-4863 patched)
```

**Requirements:**
- Python 3.8-3.11 (not 3.7)
- CUDA 11.8 or later (if using GPU)
- cuDNN 8.6 or later (if using GPU)

---

## ⚠️ Legacy Versions (FOR COMPATIBILITY WITH OLD TUTORIALS)

### Vulnerability Summary

If you need to use the older versions for compatibility with existing tutorials:

#### TensorFlow 2.3.1
- **150+ known CVEs** affecting version 2.3.1
- Vulnerabilities include:
  - Code injection in `saved_model_cli`
  - Multiple heap buffer overflows
  - NULL pointer dereferences
  - Integer overflows
  - Out-of-bounds read/write vulnerabilities
  - Segmentation faults in various operations
- **Recommended minimum version**: TensorFlow 2.12.1 (all CVEs patched)

#### OpenCV 4.4.0.46
- **CVE-2023-4863**: Bundled libwebp binaries vulnerability
- **Recommended minimum version**: OpenCV 4.8.1.78 (patched)

---

## 🔄 Using Legacy Versions (If Needed)

### For New Projects (RECOMMENDED - Already Default)

The secure versions are now the default. Just use:

```bash
pip install -r requirements.txt
```

### For Legacy/Educational Projects with Old Tutorials

If you **must** use TensorFlow 2.3.1 for compatibility, see the commented section in `requirements.txt`:

1. **Understand the risks**:
   - These versions have known security vulnerabilities
   - Use ONLY in isolated, non-production environments
   - Do NOT process untrusted input
   - Do NOT expose to network/internet

2. **Mitigation strategies**:
   - Run in isolated VM or container
   - Use WSL2 sandbox on Windows
   - Never run with elevated privileges
   - Don't process user-uploaded files
   - Keep systems updated and monitor for exploitation

3. **Add to your setup**:
   ```bash
   # After installing vulnerable versions, acknowledge risks
   echo "# SECURITY WARNING: Using vulnerable TensorFlow 2.3.1" >> ~/SECURITY_NOTICE.txt
   ```

---

## 📋 Detailed Vulnerability List

### OpenCV 4.4.0.46

| CVE | Severity | Description | Fixed In |
|-----|----------|-------------|----------|
| CVE-2023-4863 | HIGH | libwebp vulnerability in bundled binaries | 4.8.1.78 |

### TensorFlow 2.3.1 (Summary - 150+ CVEs)

**Categories of vulnerabilities:**

1. **Code Injection** (High Risk)
   - Code injection in `saved_model_cli`
   - Fixed in: 2.6.4, 2.7.2, 2.8.1

2. **Memory Corruption** (High Risk)
   - Heap buffer overflows in multiple ops
   - Out-of-bounds read/write
   - Double free vulnerabilities
   - Fixed in: 2.8.4, 2.9.3, 2.10.1, 2.11.1

3. **Denial of Service** (Medium Risk)
   - NULL pointer dereferences
   - Division by zero
   - Segmentation faults
   - Fixed in: 2.5.3, 2.6.3, 2.7.1, 2.11.1

4. **Integer Overflows** (Medium Risk)
   - Integer overflow in EditDistance
   - Multiple integer handling issues
   - Fixed in: 2.5.3, 2.6.3, 2.7.1, 2.11.1

**All vulnerabilities are fixed in TensorFlow 2.12.1+**

---

---

## 📚 Additional Resources

- [TensorFlow Security Advisories](https://github.com/tensorflow/tensorflow/security/advisories)
- [NIST National Vulnerability Database](https://nvd.nist.gov/)
- [GitHub Advisory Database](https://github.com/advisories)
- [TensorFlow Migration Guide](https://www.tensorflow.org/guide/migrate)

---

## ✅ Conclusion

**This project now uses secure versions by default:**

1. **🔒 Default Configuration** (Current)
   - TensorFlow 2.12.1 (all CVEs patched)
   - OpenCV 4.8.1.78 (CVE-2023-4863 patched)
   - Suitable for all use cases including production
   - Python 3.8-3.11 required

2. **📚 Legacy Configuration** (Optional - for old tutorials)
   - TensorFlow 2.3.1 and OpenCV 4.4.0.46
   - Contains known vulnerabilities - see comments in requirements.txt
   - Only for educational purposes
   - Isolated environment required
   - Never use in production

**Stay informed. Stay secure.** 🛡️

---

*Last updated: January 2026*
*CVE information sourced from GitHub Advisory Database*
