# Quick Reference Guide

Quick commands for common tasks. See [SETUP.md](SETUP.md) for detailed instructions.

## Environment Activation

### Using venv
```bash
source ~/tf_object_detection/bin/activate
```

### Using Conda
```bash
conda activate tf_obj_detect
```

## Verification Commands

```bash
# Check Python version
python --version

# Check TensorFlow version and GPU support
python -c "import tensorflow as tf; print(f'TensorFlow: {tf.__version__}'); print(f'GPU Available: {tf.config.list_physical_devices(\"GPU\")}')"

# Check OpenCV version
python -c "import cv2; print(f'OpenCV: {cv2.__version__}')"

# Check CUDA version
nvcc --version

# Check GPU status
nvidia-smi

# Check protoc version
protoc --version
```

## Starting Jupyter Notebook

```bash
# Activate your environment first!
jupyter notebook
```

## Cleaning and Reinstalling

### Clean Python packages
```bash
pip cache purge
pip uninstall tensorflow opencv-python -y
pip install -r requirements.txt
```

### Clean CUDA (WSL2)
```bash
sudo apt-get --purge remove "*cuda*" "*nvidia*" -y
sudo apt-get autoremove -y
sudo rm -rf /usr/local/cuda*
# Then reinstall following SETUP.md
```

## Environment Variables

Add these to your `~/.bashrc` file:

```bash
# CUDA paths
export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

# TensorFlow Object Detection API
export PYTHONPATH=$PYTHONPATH:~/models/research:~/models/research/slim
```

Apply changes:
```bash
source ~/.bashrc
```

## Common Issues Quick Fix

### GPU not detected
```bash
# Check if GPU is visible to system
nvidia-smi

# Reinstall TensorFlow with GPU support
pip install --upgrade --force-reinstall tensorflow==2.3.1
```

### Module not found
```bash
# Add to PYTHONPATH
export PYTHONPATH=$PYTHONPATH:~/models/research:~/models/research/slim
```

### protoc errors
```bash
sudo apt install -y protobuf-compiler
protoc --version
```

## Training Commands

From the TensorFlow Object Detection API:

```bash
# Navigate to models/research
cd ~/models/research

# Test Object Detection API
python object_detection/builders/model_builder_tf2_test.py

# Training (example)
python object_detection/model_main_tf2.py \
    --model_dir=path/to/model_dir \
    --pipeline_config_path=path/to/pipeline.config
```

## File Locations

- **CUDA**: `/usr/local/cuda-11.2/`
- **Models**: `~/models/research/`
- **Project**: `~/RealTimeObjectDetection/`
- **Virtual Env**: `~/tf_object_detection/`
- **Windows Files** (from WSL2): `/mnt/c/Users/YOUR_USERNAME/`

## Monitoring GPU Usage

```bash
# Real-time GPU monitoring (updates every 1 second)
nvidia-smi -l 1

# Check specific process
nvidia-smi pmon
```

---

For detailed explanations and troubleshooting, see [SETUP.md](SETUP.md).
