# 🚀 Getting Started - New User Guide

Welcome! This guide will help you get started with Real-Time Object Detection step by step.

## ⚠️ IMPORTANT: Security Notice

**Before you begin, please be aware:**

This project uses **TensorFlow 2.3.1** and **OpenCV 4.4.0.46**, which contain **150+ known security vulnerabilities**.

### Should I continue?

**✅ YES, if you are:**
- Learning object detection for educational purposes
- Following tutorials that require these specific versions  
- Using an isolated environment (WSL2 provides sandboxing)
- NOT processing untrusted or sensitive data
- NOT deploying to production

**❌ NO, if you are:**
- Building production applications
- Processing user-uploaded content
- Handling sensitive data
- Deploying to network-accessible systems

**📖 Read [SECURITY.md](SECURITY.md) first** to understand:
- What vulnerabilities exist
- How to use safely for learning
- How to upgrade to secure versions (TensorFlow 2.12.1+)
- Migration guide for production use

---

## 📖 First Time Here?

If you're new to this project, **START HERE** and follow these steps in order:

### Step 1: Understand What You'll Build (5 minutes)
- Read: [README.md](README.md) for project overview
- What you'll learn: Train a custom object detection model that works in real-time

### Step 2: Set Up Your Environment (1-2 hours)
- **Primary Guide**: [SETUP.md](SETUP.md) - Follow this carefully!
- For quick commands: [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- Having issues? Check [FAQ.md](FAQ.md)

**Key points:**
- ✅ You have Windows 11 with WSL2 ← Perfect for this setup
- ✅ You have an NVIDIA RTX 5060 ← Great GPU for training
- ⚠️ You have existing CUDA/TensorFlow installed ← We'll clean this first

### Step 3: Clean Your Existing Setup (15 minutes)
Since you mentioned having existing installations:

```bash
# Option 1: Use our cleanup script (recommended)
bash cleanup.sh

# Option 2: Follow manual cleanup in SETUP.md Section 2
```

### Step 4: Fresh Installation (1 hour)
Follow [SETUP.md](SETUP.md) from "Installation Steps" section:
1. Update WSL2 and Ubuntu
2. Install Python 3.8
3. Install CUDA 11.2 (WSL2 version)
4. Install cuDNN 8.1
5. Install Protocol Buffers 3.13
6. Install Python packages
7. Install TensorFlow Object Detection API

### Step 5: Verify Everything Works (10 minutes)
```bash
# Run our verification script
python verify_installation.py

# All checks should pass ✅
```

If any checks fail:
1. Read the error message
2. Check [FAQ.md](FAQ.md) for solutions
3. Re-run verify_installation.py after fixing

### Step 6: Clone This Repository (5 minutes)
```bash
cd ~
git clone https://github.com/tja111/RealTimeObjectDetection.git
cd RealTimeObjectDetection

# Activate your virtual environment
source ~/tf_object_detection/bin/activate

# Install project requirements
pip install -r requirements.txt
```

### Step 7: Start Learning! (Variable time)
```bash
# Launch Jupyter Notebook
jupyter notebook Tutorial.ipynb

# Follow the tutorial step by step
```

---

## 📋 Quick Start Checklist

Print this or keep it handy:

- [ ] Read README.md
- [ ] Run `bash cleanup.sh`
- [ ] Install Python 3.8
- [ ] Install CUDA 11.2 for WSL2
- [ ] Install cuDNN 8.1
- [ ] Install protoc 3.13
- [ ] Create virtual environment
- [ ] Install TensorFlow 2.3.1
- [ ] Install OpenCV 4.4.0
- [ ] Install Object Detection API
- [ ] Run `python verify_installation.py` (all pass)
- [ ] Clone this repository
- [ ] Install `requirements.txt`
- [ ] Open `Tutorial.ipynb`

---

## 🎯 What Files Do What?

### Documentation (Read These)
- **README.md** ← Start here for overview
- **SETUP.md** ← Complete setup guide (your main reference)
- **FAQ.md** ← Troubleshooting and common questions
- **WORKFLOW.md** ← Complete project workflow with diagrams
- **QUICK_REFERENCE.md** ← Quick command reference
- **GETTING_STARTED.md** ← This file!

### Scripts (Run These)
- **cleanup.sh** ← Cleans existing installations
- **verify_installation.py** ← Checks if setup is correct
- **requirements.txt** ← Python dependencies

### Tutorial (Learn From This)
- **Tutorial.ipynb** ← Step-by-step training tutorial

### Configuration
- **.gitignore** ← Prevents committing unnecessary files

---

## 🆘 Having Problems?

### Problem: I'm completely lost
**Solution**: Start with README.md, then SETUP.md. Follow exactly as written.

### Problem: Something isn't working
**Solution**: 
1. Read the error message
2. Check [FAQ.md](FAQ.md)
3. Run `python verify_installation.py`
4. Search for your error online

### Problem: Setup is taking forever
**Solution**: This is normal! Environment setup takes 1-2 hours. Don't rush.

### Problem: I'm on Windows, not WSL2
**Solution**: SETUP.md is for WSL2. For native Windows:
- Install CUDA for Windows
- Install Visual Studio C++ 2015+
- Follow Windows-specific TensorFlow installation

### Problem: No GPU or different GPU
**Solution**: 
- Most steps are the same
- Training will be slower without GPU
- Skip GPU-specific verification

---

## 💡 Pro Tips for Beginners

1. **Don't skip the cleanup**: Starting fresh prevents mysterious errors
2. **Use virtual environments**: Always! Avoid "works on my machine" issues
3. **Read error messages**: They usually tell you what's wrong
4. **One step at a time**: Complete each phase before moving to next
5. **Take notes**: Document what works for you
6. **Ask for help**: If stuck, open a GitHub issue with details
7. **Be patient**: ML setup is complex but worth it!

---

## 📚 Learning Path

```
You are here → Environment Setup (SETUP.md)
                      ↓
              Verify Installation (verify_installation.py)
                      ↓
              Clone Repository
                      ↓
              Tutorial (Tutorial.ipynb)
                      ↓
              Collect Your Data
                      ↓
              Train Your Model (WORKFLOW.md)
                      ↓
              Deploy Real-time Detection
                      ↓
              🎉 Success!
```

---

## 🎓 What You'll Learn

By completing this project, you'll learn:

1. **Environment Setup**: CUDA, cuDNN, TensorFlow on WSL2
2. **Deep Learning**: How object detection models work
3. **TensorFlow**: Training and deploying models
4. **Computer Vision**: Image processing with OpenCV
5. **Real-time AI**: Running models on live video
6. **MLOps**: Managing ML projects and dependencies

---

## ⏱️ Time Expectations

- **Environment Setup**: 1-2 hours (one-time)
- **Tutorial Completion**: 2-3 hours
- **Data Collection**: 1-2 hours (depends on your project)
- **Model Training**: 2-8 hours (depends on dataset and GPU)
- **Testing & Deployment**: 1-2 hours

**Total**: ~10-20 hours for complete project

---

## 🎯 Your Next Action

**Right now, do this:**

```bash
# 1. Open your WSL2 Ubuntu terminal
# 2. Run the cleanup script
cd /path/to/RealTimeObjectDetection
bash cleanup.sh

# 3. Open SETUP.md and start following it
# 4. When done, run verify_installation.py
```

---

## 📞 Need Help?

- **Setup Issues**: Check [SETUP.md](SETUP.md) troubleshooting section
- **General Questions**: Read [FAQ.md](FAQ.md)
- **Command Reference**: See [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **Workflow Questions**: Read [WORKFLOW.md](WORKFLOW.md)
- **Still stuck?**: Open a GitHub issue

---

## ✅ How to Know You're Ready

You're ready to move forward when:
- ✅ `python verify_installation.py` shows all checks passing
- ✅ `nvidia-smi` shows your RTX 5060
- ✅ TensorFlow detects your GPU
- ✅ You can import TensorFlow without errors
- ✅ Object Detection API is installed

If all above are true: **Congratulations! Start the Tutorial.ipynb** 🎉

---

## 🚀 Ready? Let's Go!

1. **Bookmark this page** for reference
2. **Open SETUP.md** in another window
3. **Follow step by step**
4. **Don't skip steps!**
5. **Have fun learning!** 🎓

---

*Remember: Everyone struggles with environment setup at first. It's normal! Take your time and follow the guides. You've got this! 💪*

**Good luck, and happy detecting!** 🎯
