# Frequently Asked Questions (FAQ)

## General Questions

### Q: Do I need a GPU to run this project?
**A:** No, but it's highly recommended. TensorFlow will work on CPU, but training and inference will be much slower. Real-time object detection is challenging without a GPU.

### Q: Can I use this on native Windows (not WSL2)?
**A:** Yes, but the setup is different. You'll need to:
- Install CUDA and cuDNN for Windows
- Install Visual Studio C++ 2015 or later
- Use Windows paths instead of Linux paths
- See the original problem statement for Windows-specific setup

### Q: What if I have a different NVIDIA GPU (not RTX 5060)?
**A:** The setup works for any NVIDIA GPU with compute capability 3.5 or higher. Check your GPU's compute capability at [NVIDIA's website](https://developer.nvidia.com/cuda-gpus).

### Q: Can I use a different Python version?
**A:** TensorFlow 2.3.1 supports Python 3.5-3.8. Using Python 3.9+ may cause compatibility issues. Stick to Python 3.7 or 3.8 for best results.

---

## Installation Issues

### Q: nvidia-smi shows "command not found" in WSL2
**A:** This means:
1. Your NVIDIA drivers aren't installed on Windows, OR
2. Your WSL2 version doesn't support GPU passthrough

**Fix:**
- Update Windows to the latest version
- Install/update NVIDIA drivers on Windows (not in WSL2!)
- Update WSL2: `wsl --update` (run in Windows PowerShell)
- Restart your computer

### Q: TensorFlow installs but doesn't see my GPU
**A:** Common causes:
1. CUDA/cuDNN versions don't match TensorFlow requirements
2. CUDA not in PATH or LD_LIBRARY_PATH
3. Using CPU-only TensorFlow version

**Fix:**
```bash
# Check TensorFlow sees GPU
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# Reinstall TensorFlow
pip uninstall tensorflow
pip install tensorflow==2.3.1

# Check CUDA paths
echo $LD_LIBRARY_PATH
```

### Q: "protoc: command not found" when installing Object Detection API
**A:** Protocol Buffers compiler isn't installed or not in PATH.

**Fix:**
```bash
# Install via apt
sudo apt install -y protobuf-compiler

# OR install manually (as in SETUP.md)
# Then verify
protoc --version
which protoc
```

### Q: "No module named 'object_detection'" error
**A:** The Object Detection API isn't installed or not in PYTHONPATH.

**Fix:**
```bash
# Add to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:~/models/research:~/models/research/slim

# Make permanent
echo 'export PYTHONPATH=$PYTHONPATH:~/models/research:~/models/research/slim' >> ~/.bashrc
source ~/.bashrc

# Reinstall Object Detection API
cd ~/models/research
python -m pip install .
```

### Q: cuDNN library not found
**A:** cuDNN isn't installed correctly or CUDA can't find it.

**Fix:**
```bash
# Check if cuDNN files exist
ls /usr/local/cuda-11.2/lib64/libcudnn*
ls /usr/local/cuda-11.2/include/cudnn*

# If missing, reinstall cuDNN following SETUP.md
# Ensure LD_LIBRARY_PATH includes CUDA lib64
export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64:$LD_LIBRARY_PATH
```

---

## Training and Runtime Issues

### Q: "Out of memory" error during training
**A:** Your GPU doesn't have enough VRAM for the current batch size.

**Fix:**
- Reduce batch size in your training configuration
- Use a smaller model (e.g., SSD MobileNet instead of Faster R-CNN)
- Reduce image resolution
- Monitor GPU memory: `nvidia-smi -l 1`

### Q: Training is very slow
**A:** Possible causes:
1. Running on CPU instead of GPU
2. Batch size too small
3. Data loading bottleneck

**Fix:**
```bash
# Verify GPU is being used
nvidia-smi -l 1  # Watch GPU utilization

# Check TensorFlow GPU usage in your script
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
```

### Q: Camera not detected for real-time detection
**A:** OpenCV can't access your camera.

**Fix:**
```bash
# Test camera access
python -c "import cv2; cap = cv2.VideoCapture(0); print('Camera OK' if cap.isOpened() else 'Camera FAILED'); cap.release()"

# Try different camera indices (0, 1, 2...)
# On WSL2, camera access can be tricky - consider using Windows for webcam testing
```

---

## WSL2-Specific Questions

### Q: Can I access Windows files from WSL2?
**A:** Yes! Windows drives are mounted at `/mnt/`:
- `C:\` → `/mnt/c/`
- `D:\` → `/mnt/d/`

Example: `/mnt/c/Users/YourName/Downloads`

### Q: Can I run Jupyter Notebook and access it from Windows browser?
**A:** Yes! Start Jupyter in WSL2:
```bash
jupyter notebook --no-browser
```
Then open the provided URL in your Windows browser.

### Q: How do I copy files between Windows and WSL2?
**A:** 
```bash
# From WSL2 to Windows
cp file.txt /mnt/c/Users/YourName/Desktop/

# From Windows to WSL2
cp /mnt/c/Users/YourName/Downloads/file.txt ~/

# Or use Windows Explorer: \\wsl$\Ubuntu\home\yourname\
```

### Q: Should I install everything in WSL2 or Windows?
**A:** For this project:
- **WSL2**: Python, TensorFlow, CUDA toolkit, all development tools
- **Windows**: NVIDIA GPU drivers ONLY

Benefits of WSL2:
- Better package management
- More compatible with Linux-based tutorials
- Easier CUDA setup
- Better terminal experience

---

## Version Compatibility

### Q: Which versions work together?
**A:** Tested combinations:

**Option 1 (Original):**
- Python 3.7.4
- TensorFlow 2.3.1
- CUDA 10.1
- cuDNN 7.6.5
- OpenCV 4.4.0

**Option 2 (Recommended for WSL2):**
- Python 3.8.x
- TensorFlow 2.3.1
- CUDA 11.2
- cuDNN 8.1.0
- OpenCV 4.4.0

### Q: Can I use newer versions of TensorFlow?
**A:** Yes, but you may need to update:
- CUDA version (TensorFlow 2.10+ needs CUDA 11.2+)
- cuDNN version
- Python version
- Code changes may be needed

Check [TensorFlow GPU support](https://www.tensorflow.org/install/source#gpu) for version compatibility.

---

## Development Questions

### Q: How do I train on custom objects?
**A:** Follow these steps:
1. Collect and label images using tools like LabelImg
2. Split data into train/test sets
3. Convert to TFRecord format
4. Update label map
5. Configure pipeline.config
6. Start training

The Tutorial.ipynb in this repo walks through this process.

### Q: How long does training take?
**A:** Depends on:
- Model complexity
- Dataset size
- GPU power
- Number of training steps

Rough estimates on RTX 5060:
- Small model (SSD MobileNet): 1-3 hours for basic training
- Large model (Faster R-CNN): 6-12+ hours

### Q: Can I use pre-trained models?
**A:** Yes! TensorFlow provides many pre-trained models at the [Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md). Transfer learning from these models is faster than training from scratch.

### Q: How do I improve detection accuracy?
**A:** Tips:
1. More training data (especially diverse examples)
2. Better quality labels
3. More training steps
4. Data augmentation
5. Use a larger model (if GPU memory allows)
6. Fine-tune hyperparameters

---

## Getting More Help

### Q: Where can I get more help?
**A:** Resources:
1. **This Repository**: Open an issue on GitHub
2. **TensorFlow Forums**: https://discuss.tensorflow.org/
3. **Stack Overflow**: Tag questions with `tensorflow`, `object-detection`
4. **NVIDIA Forums**: https://forums.developer.nvidia.com/ (for GPU issues)
5. **WSL2 Documentation**: https://docs.microsoft.com/en-us/windows/wsl/

### Q: How do I report a bug in this setup guide?
**A:** Please open an issue on GitHub with:
- Your operating system and version
- GPU model
- Steps you followed
- Error message or unexpected behavior
- Output of `verify_installation.py`

---

## Best Practices

### Q: Should I use virtual environments?
**A:** **YES!** Always use virtual environments (venv or conda) to:
- Avoid package conflicts
- Keep projects isolated
- Make it easy to reproduce environments
- Switch between different TensorFlow versions

### Q: How do I keep my setup maintained?
**A:** Tips:
1. Document your working configuration
2. Use version pinning in requirements.txt
3. Backup your trained models
4. Keep NVIDIA drivers updated
5. Don't mix pip and conda (choose one)

### Q: Should I update packages regularly?
**A:** Be cautious:
- ✅ Update security patches
- ✅ Update minor versions when needed
- ⚠️ Test major updates in a separate environment first
- ❌ Don't update if everything works (especially CUDA/cuDNN)

---

## Quick Tips

💡 **Use `nvidia-smi -l 1`** to monitor GPU usage in real-time

💡 **Save your work frequently** - training can take hours

💡 **Start with small models** to verify setup before training large ones

💡 **Use TensorBoard** to visualize training progress

💡 **Keep a backup** of working configurations

💡 **Test on a single image** before running on video/camera

💡 **Check disk space** - models and datasets can be large

---

*Last updated: January 2026*
