# Real-Time Object Detection with TensorFlow

A beginner-friendly project for implementing real-time object detection using TensorFlow Object Detection API.

## 🚀 Quick Start

### 👋 New to this project? Start here:

1. **[Getting Started Guide](GETTING_STARTED.md)** - Complete beginner's roadmap (START HERE!)
2. **[Setup Guide](SETUP.md)** - Detailed step-by-step environment setup instructions
   - ✅ Windows 11 + WSL2 + NVIDIA GPU support
   - ✅ Cleanup instructions for existing installations
   - ✅ Beginner-friendly with detailed explanations
   - ✅ Troubleshooting tips included
3. **[FAQ](FAQ.md)** - Answers to common questions and issues
4. **[Workflow Guide](WORKFLOW.md)** - Complete project workflow with visual diagrams

2. **Install Dependencies** - After completing the setup guide:
   ```bash
   # Clone this repository
   git clone https://github.com/tja111/RealTimeObjectDetection.git
   cd RealTimeObjectDetection
   
   # Activate your virtual environment first!
   source ~/tf_object_detection/bin/activate  # or conda activate tf_obj_detect
   
   # Install Python packages
   pip install -r requirements.txt
   ```

3. **Verify Installation** - Make sure everything works:
   ```bash
   python verify_installation.py
   ```

4. **Run the Tutorial** - Learn by doing:
   ```bash
   jupyter notebook Tutorial.ipynb
   ```

## 📋 What You'll Need

- **Operating System**: Windows 11 with WSL2 (Ubuntu) or native Ubuntu/Linux
- **GPU**: NVIDIA GPU (e.g., RTX series) - optional but recommended
- **Python**: 3.8, 3.9, 3.10, or 3.11 (3.9 recommended)
- **Storage**: At least 10GB free space for models and dependencies
- **Time**: About 1-2 hours for complete setup

**Note**: For the current secure versions (TensorFlow 2.12.1+), Python 3.8-3.11 is required. If following older tutorials with TensorFlow 2.3.1, see `SECURITY.md` for legacy version information.

## 📁 Project Structure

```
RealTimeObjectDetection/
├── SETUP.md              # Comprehensive setup guide
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── Tutorial.ipynb        # Step-by-step tutorial notebook
└── Tensorflow/
    ├── scripts/          # Helper scripts
    └── workspace/        # Your working directory
        ├── annotations/  # Label maps and TFRecord files
        ├── images/       # Training and test images
        ├── models/       # Your trained models
        └── pre-trained-models/  # Downloaded pre-trained models
```

## 🎯 Features

- Real-time object detection using TensorFlow 2.x
- Support for custom object detection models
- Easy-to-follow Jupyter notebook tutorial
- Pre-configured workspace structure
- GPU acceleration support

## 📚 Learning Resources

### Included in This Repository
- **[GETTING_STARTED.md](GETTING_STARTED.md)**: Complete beginner's roadmap
- **[SETUP.md](SETUP.md)**: Detailed environment setup instructions
- **[Tutorial.ipynb](Tutorial.ipynb)**: Interactive notebook with complete workflow
- **[FAQ.md](FAQ.md)**: Frequently asked questions and troubleshooting
- **[WORKFLOW.md](WORKFLOW.md)**: Visual workflow guide with diagrams
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)**: Quick command reference

### External Resources
- [TensorFlow Object Detection API Documentation](https://tensorflow-object-detection-api-tutorial.readthedocs.io/)
- [TensorFlow Official Docs](https://www.tensorflow.org/)
- [OpenCV Documentation](https://docs.opencv.org/)

## 🆘 Getting Help

1. **Security Concerns**: Read [SECURITY.md](SECURITY.md) about known vulnerabilities
2. **Setup Issues**: Check the [Troubleshooting section](SETUP.md#troubleshooting) in SETUP.md
3. **Common Questions**: See [FAQ.md](FAQ.md) for answers
4. **Quick Commands**: Reference [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
5. **TensorFlow Issues**: See [TensorFlow GPU Support Guide](https://www.tensorflow.org/install/gpu)
6. **WSL2 Issues**: Check [WSL2 CUDA Guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
7. **General Questions**: Open an issue on GitHub with:
   - Your OS and GPU details
   - Output of `verify_installation.py`
   - Error messages and steps to reproduce

## ⚠️ Important Notes

- **🔒 SECURITY WARNING**: The pinned versions (TensorFlow 2.3.1, OpenCV 4.4.0.46) contain known vulnerabilities. See [SECURITY.md](SECURITY.md) for details and mitigation strategies.
- **WSL2 Users**: Do NOT install CUDA inside WSL2 manually - follow the SETUP.md guide
- **Windows Users**: Install NVIDIA drivers on Windows, not inside WSL2
- **Virtual Environments**: Always use virtual environments to avoid package conflicts
- **GPU Memory**: Monitor GPU usage with `nvidia-smi -l 1` to prevent out-of-memory errors
- **Use Case**: These vulnerable versions are acceptable ONLY for isolated educational use. For production, upgrade to TensorFlow 2.12.1+ and OpenCV 4.8.1.78+

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest improvements
- Share your trained models
- Improve documentation

## 📝 License

This project is provided as-is for educational purposes.

## 🙏 Acknowledgments

- TensorFlow team for the Object Detection API
- The open-source community for tutorials and guides

---

**Ready to get started?** 

👉 Head over to [GETTING_STARTED.md](GETTING_STARTED.md) for a complete beginner's roadmap!

🚀 Already set up? Jump straight to [Tutorial.ipynb](Tutorial.ipynb) to start training!
