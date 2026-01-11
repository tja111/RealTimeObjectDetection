# Real-Time Object Detection with TensorFlow

A beginner-friendly project for implementing real-time object detection using TensorFlow Object Detection API.

## 🚀 Quick Start

### New to this project? Start here:

1. **[Setup Guide](SETUP.md)** - Complete step-by-step instructions for setting up your environment
   - ✅ Windows 11 + WSL2 + NVIDIA GPU support
   - ✅ Cleanup instructions for existing installations
   - ✅ Beginner-friendly with detailed explanations
   - ✅ Troubleshooting tips included

2. **Install Dependencies** - After completing the setup guide:
   ```bash
   # Activate your virtual environment first!
   source ~/tf_object_detection/bin/activate  # or conda activate tf_obj_detect
   
   # Install Python packages
   pip install -r requirements.txt
   ```

3. **Run the Tutorial** - Learn by doing:
   ```bash
   jupyter notebook Tutorial.ipynb
   ```

## 📋 What You'll Need

- **Operating System**: Windows 11 with WSL2 (Ubuntu) or native Ubuntu/Linux
- **GPU**: NVIDIA GPU (e.g., RTX series) - optional but recommended
- **Python**: 3.7 or 3.8
- **Storage**: At least 10GB free space for models and dependencies
- **Time**: About 1-2 hours for complete setup

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
- **Tutorial.ipynb**: Interactive notebook with complete workflow
- **SETUP.md**: Detailed environment setup instructions

### External Resources
- [TensorFlow Object Detection API Documentation](https://tensorflow-object-detection-api-tutorial.readthedocs.io/)
- [TensorFlow Official Docs](https://www.tensorflow.org/)
- [OpenCV Documentation](https://docs.opencv.org/)

## 🆘 Getting Help

1. **Setup Issues**: Check the [Troubleshooting section](SETUP.md#troubleshooting) in SETUP.md
2. **TensorFlow Issues**: See [TensorFlow GPU Support Guide](https://www.tensorflow.org/install/gpu)
3. **WSL2 Issues**: Check [WSL2 CUDA Guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
4. **General Questions**: Open an issue on GitHub

## ⚠️ Important Notes

- **WSL2 Users**: Do NOT install CUDA inside WSL2 manually - follow the SETUP.md guide
- **Windows Users**: Install NVIDIA drivers on Windows, not inside WSL2
- **Virtual Environments**: Always use virtual environments to avoid package conflicts
- **GPU Memory**: Monitor GPU usage with `nvidia-smi -l 1` to prevent out-of-memory errors

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

**Ready to get started?** Head over to [SETUP.md](SETUP.md) and begin your journey into real-time object detection! 🚀
