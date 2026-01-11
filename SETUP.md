# Real-Time Object Detection Environment Setup Guide

## For Windows 11 + WSL2 + RTX GPU (Beginner-Friendly)

This guide will walk you through setting up your development environment for real-time object detection using TensorFlow. If you have existing installations, we'll start by cleaning everything up to ensure a fresh, working setup.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Cleaning Existing Installations](#cleaning-existing-installations)
3. [Installation Steps](#installation-steps)
4. [Verification](#verification)
5. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- **Operating System**: Windows 11 with WSL2 (Ubuntu)
- **GPU**: NVIDIA RTX 5060 (or any compatible NVIDIA GPU)
- **Internet Connection**: Required for downloading packages
- **Administrator Access**: Required for some installations

---

## Cleaning Existing Installations

Since you mentioned you already have CUDA, cuDNN, and TensorFlow installed, let's clean them up first to start fresh.

### Step 1: Clean WSL2 Ubuntu Environment

Open your WSL2 Ubuntu terminal and run:

```bash
# Remove existing TensorFlow installations
pip uninstall tensorflow tensorflow-gpu -y
pip3 uninstall tensorflow tensorflow-gpu -y

# Remove existing CUDA toolkit (if installed via apt)
sudo apt-get --purge remove "*cuda*" "*cublas*" "*cufft*" "*cufile*" "*curand*" "*cusolver*" "*cusparse*" "*gds-tools*" "*npp*" "*nvjpeg*" "nsight*" "*nvvm*" -y
sudo apt-get --purge remove "*nvidia*" -y
sudo apt-get autoremove -y
sudo apt-get autoclean -y

# Remove CUDA directories
sudo rm -rf /usr/local/cuda*

# Clean pip cache
pip cache purge
pip3 cache purge

# Remove any conda environments if you have them
# conda env remove -n your_env_name
```

### Step 2: Clean Windows NVIDIA Drivers (Keep These!)

**IMPORTANT**: Do NOT uninstall your NVIDIA GPU drivers from Windows. WSL2 uses the Windows NVIDIA drivers directly. Only uninstall if you're having driver issues, then reinstall the latest drivers from [NVIDIA's website](https://www.nvidia.com/download/index.aspx).

---

## Installation Steps

### Step 1: Update WSL2 and Ubuntu

```bash
# Update package lists
sudo apt update

# Upgrade existing packages
sudo apt upgrade -y

# Install essential build tools
sudo apt install -y build-essential
```

### Step 2: Install Python 3.8 or 3.9

For TensorFlow 2.3.1, Python 3.7-3.8 is recommended. However, for better compatibility with modern packages, we'll use Python 3.8:

```bash
# Check current Python version
python3 --version

# If you need Python 3.8, install it:
sudo apt install -y python3.8 python3.8-venv python3.8-dev python3-pip

# Set Python 3.8 as default (optional)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Upgrade pip
python3 -m pip install --upgrade pip
```

### Step 3: Install CUDA Toolkit 11.2 for WSL2

**Note**: WSL2 uses a special version of CUDA. Do NOT use the Windows CUDA installer!

```bash
# Download and install CUDA 11.2 for WSL-Ubuntu
wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda-repo-wsl-ubuntu-11-2-local_11.2.0-1_amd64.deb
sudo dpkg -i cuda-repo-wsl-ubuntu-11-2-local_11.2.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-wsl-ubuntu-11-2-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda-toolkit-11-2

# Add CUDA to PATH
echo 'export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc
```

### Step 4: Install cuDNN 8.1

```bash
# Download cuDNN (you'll need to create an NVIDIA Developer account)
# Go to: https://developer.nvidia.com/rdp/cudnn-archive
# Download: cuDNN v8.1.0 for CUDA 11.2

# After downloading, copy the file to WSL2 (assuming it's in your Downloads folder):
# From WSL2 terminal:
cd ~
# Replace YOUR_USERNAME with your actual Windows username
# You can also use: echo $USER to see your WSL username
cp /mnt/c/Users/YOUR_USERNAME/Downloads/cudnn-11.2-linux-x64-v8.1.0.77.tgz .

# If you're unsure of your username, list the Users directory:
# ls /mnt/c/Users/

# Extract and install
tar -xzvf cudnn-11.2-linux-x64-v8.1.0.77.tgz
sudo cp cuda/include/cudnn*.h /usr/local/cuda-11.2/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-11.2/lib64
sudo chmod a+r /usr/local/cuda-11.2/include/cudnn*.h /usr/local/cuda-11.2/lib64/libcudnn*

# Clean up
rm -rf cuda
rm cudnn-11.2-linux-x64-v8.1.0.77.tgz
```

### Step 5: Install Protocol Buffers (protoc) 3.13

```bash
# Install protobuf compiler
cd ~
wget https://github.com/protocolbuffers/protobuf/releases/download/v3.13.0/protoc-3.13.0-linux-x86_64.zip
sudo apt install -y unzip
unzip protoc-3.13.0-linux-x86_64.zip -d protoc3
sudo mv protoc3/bin/* /usr/local/bin/
sudo mv protoc3/include/* /usr/local/include/
sudo chmod +x /usr/local/bin/protoc
rm -rf protoc3 protoc-3.13.0-linux-x86_64.zip

# Verify installation
protoc --version
```

### Step 6: Install Python Packages

```bash
# Create a virtual environment (recommended)
cd ~/
python3 -m venv tf_object_detection
source tf_object_detection/bin/activate

# Upgrade pip in virtual environment
pip install --upgrade pip

# Install TensorFlow with GPU support
pip install tensorflow==2.3.1

# Install OpenCV (NOTE: Fixed typo from original instructions)
pip install opencv-python==4.4.0.46

# Install other common dependencies
pip install numpy matplotlib pillow lxml jupyter
```

### Step 7: Install TensorFlow Object Detection API

```bash
# Navigate to your project directory or home
cd ~

# Clone TensorFlow models repository
git clone https://github.com/tensorflow/models.git
cd models/research

# Compile protobuf files
protoc object_detection/protos/*.proto --python_out=.

# Install the Object Detection API
cp object_detection/packages/tf2/setup.py .
python -m pip install .

# Install additional dependencies
pip install pycocotools

# Set PYTHONPATH (add to ~/.bashrc for persistence)
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
echo "export PYTHONPATH=\$PYTHONPATH:~/models/research:~/models/research/slim" >> ~/.bashrc
```

---

## Verification

### Step 1: Verify CUDA Installation

```bash
nvcc --version
nvidia-smi  # This should show your RTX 5060
```

### Step 2: Verify TensorFlow GPU Support

Create a test script:

```bash
cd ~
cat > test_tf_gpu.py << 'EOF'
import tensorflow as tf
print("TensorFlow version:", tf.__version__)
print("GPU Available:", tf.config.list_physical_devices('GPU'))
print("Built with CUDA:", tf.test.is_built_with_cuda())
print("GPU Support:", tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))
EOF

python test_tf_gpu.py
```

**Expected Output**: You should see your GPU listed and "GPU Available: True"

### Step 3: Verify Object Detection API

```bash
cd ~/models/research
python object_detection/builders/model_builder_tf2_test.py
```

**Expected Output**: All tests should pass (OK or PASSED status)

### Step 4: Verify OpenCV

```bash
python -c "import cv2; print('OpenCV version:', cv2.__version__)"
```

---

## Troubleshooting

### Issue: `nvidia-smi` not working in WSL2

**Solution**: 
1. Update Windows to the latest version
2. Install the latest NVIDIA drivers for Windows (not WSL2)
3. Update WSL2 kernel: `wsl --update`

### Issue: TensorFlow doesn't detect GPU

**Solutions**:
1. Ensure CUDA and cuDNN versions match TensorFlow requirements
2. Check if GPU is visible: `nvidia-smi`
3. Verify CUDA path: `echo $LD_LIBRARY_PATH`
4. Reinstall TensorFlow: `pip install --upgrade --force-reinstall tensorflow==2.3.1`

### Issue: protoc command not found

**Solution**:
```bash
sudo apt install -y protobuf-compiler
# OR ensure /usr/local/bin is in your PATH
echo 'export PATH=/usr/local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Issue: Module not found errors for Object Detection API

**Solution**:
```bash
# Ensure PYTHONPATH is set correctly
export PYTHONPATH=$PYTHONPATH:~/models/research:~/models/research/slim
# Add to ~/.bashrc for persistence
echo "export PYTHONPATH=\$PYTHONPATH:~/models/research:~/models/research/slim" >> ~/.bashrc
source ~/.bashrc
```

### Issue: Out of memory errors

**Solution**:
1. Reduce batch size in training configuration
2. Use a smaller model architecture
3. Monitor GPU memory: `nvidia-smi -l 1`

---

## Alternative Setup: Using Conda (Easier Package Management)

If you prefer using Anaconda/Miniconda (which many find easier for managing Python environments):

```bash
# Install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Create environment with Python 3.8
conda create -n tf_obj_detect python=3.8

# Activate environment
conda activate tf_obj_detect

# Install packages
pip install tensorflow==2.3.1
pip install opencv-python==4.4.0.46
pip install numpy matplotlib pillow lxml jupyter pycocotools

# Then continue with CUDA, cuDNN, and Object Detection API installation as above
```

---

## Important Notes

1. **WSL2 vs Windows**: This guide is for WSL2 Ubuntu. If you want to use native Windows, the CUDA/cuDNN installation steps will be different.

2. **Version Compatibility**: TensorFlow 2.3.1 requires:
   - CUDA 10.1 or 11.2
   - cuDNN 7.6 or 8.1
   - Python 3.5-3.8

3. **Virtual Environments**: Always use virtual environments (venv or conda) to avoid conflicts between projects.

4. **WSL2 File Access**: Your Windows files are accessible in WSL2 at `/mnt/c/`, `/mnt/d/`, etc.

5. **GPU Driver**: Only install NVIDIA drivers on Windows, not inside WSL2. WSL2 automatically uses the Windows drivers.

---

## Next Steps

After completing this setup:

1. Clone this repository: `git clone https://github.com/tja111/RealTimeObjectDetection.git`
2. Navigate to the project: `cd RealTimeObjectDetection`
3. Open the Tutorial.ipynb: `jupyter notebook Tutorial.ipynb`
4. Follow the tutorial to train your object detection model!

---

## Additional Resources

- [TensorFlow Object Detection API Tutorial](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html)
- [TensorFlow GPU Support](https://www.tensorflow.org/install/gpu)
- [WSL2 CUDA Support](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
- [NVIDIA Developer Forums](https://forums.developer.nvidia.com/)

---

## Credits

Original setup instructions by the repository author. Enhanced and adapted for Windows 11 + WSL2 + RTX GPU setup with cleanup procedures.

**Last Updated**: January 2026
