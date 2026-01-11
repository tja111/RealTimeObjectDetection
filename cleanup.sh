#!/bin/bash

# Cleanup Script for Real-Time Object Detection Environment
# This script removes existing installations to start fresh
# Use with caution - it will remove TensorFlow, CUDA, and related packages

echo "================================================"
echo "Environment Cleanup Script"
echo "================================================"
echo ""
echo "This script will remove:"
echo "  - TensorFlow installations"
echo "  - CUDA toolkit"
echo "  - cuDNN"
echo "  - Related Python packages"
echo ""
echo "⚠️  WARNING: This is destructive! Make sure you want to proceed."
echo ""
read -p "Do you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Cleanup cancelled."
    exit 0
fi

echo ""
echo "Starting cleanup..."
echo ""

# Step 1: Remove TensorFlow
echo "🧹 Removing TensorFlow installations..."
pip uninstall tensorflow tensorflow-gpu -y 2>/dev/null
pip3 uninstall tensorflow tensorflow-gpu -y 2>/dev/null
echo "✅ TensorFlow removed"

# Step 2: Remove OpenCV
echo "🧹 Removing OpenCV..."
pip uninstall opencv-python opencv-contrib-python -y 2>/dev/null
pip3 uninstall opencv-python opencv-contrib-python -y 2>/dev/null
echo "✅ OpenCV removed"

# Step 3: Remove CUDA packages (apt)
echo "🧹 Removing CUDA packages..."
echo "⚠️  This will remove packages matching CUDA patterns..."
echo "Showing some packages that will be removed:"
dpkg -l | grep -E "cuda|cublas|cufft|nvidia" | awk '{print $2}' | head -20
echo ""
echo "Note: There may be more packages than shown above."
read -p "Proceed with CUDA package removal? (yes/no): " confirm_cuda

if [ "$confirm_cuda" = "yes" ]; then
    sudo apt-get --purge remove "*cuda*" "*cublas*" "*cufft*" "*cufile*" "*curand*" "*cusolver*" "*cusparse*" "*gds-tools*" "*npp*" "*nvjpeg*" "nsight*" "*nvvm*" -y 2>/dev/null
    sudo apt-get --purge remove "*nvidia*" -y 2>/dev/null
    sudo apt-get autoremove -y
    sudo apt-get autoclean -y
    echo "✅ CUDA packages removed"
else
    echo "ℹ️  Skipped CUDA package removal"
fi

# Step 4: Remove CUDA directories
echo "🧹 Removing CUDA directories..."
if [ -d "/usr/local/cuda" ] || [ -L "/usr/local/cuda" ]; then
    sudo rm -rf /usr/local/cuda*
    echo "✅ CUDA directories removed"
else
    echo "ℹ️  No CUDA directories found"
fi

# Step 5: Clean pip cache
echo "🧹 Cleaning pip cache..."
pip cache purge 2>/dev/null
pip3 cache purge 2>/dev/null
echo "✅ Pip cache cleaned"

# Step 6: Remove TensorFlow models (optional)
echo ""
read -p "Do you want to remove ~/models directory (TensorFlow Object Detection API)? (yes/no): " remove_models
if [ "$remove_models" = "yes" ]; then
    if [ -d "$HOME/models" ]; then
        rm -rf $HOME/models
        echo "✅ ~/models directory removed"
    else
        echo "ℹ️  ~/models directory not found"
    fi
fi

# Step 7: Remove virtual environments (optional)
echo ""
read -p "Do you want to remove ~/tf_object_detection virtual environment? (yes/no): " remove_venv
if [ "$remove_venv" = "yes" ]; then
    if [ -d "$HOME/tf_object_detection" ]; then
        rm -rf $HOME/tf_object_detection
        echo "✅ Virtual environment removed"
    else
        echo "ℹ️  Virtual environment not found"
    fi
fi

# Step 8: Clean up .bashrc entries (backup first)
echo ""
echo "🧹 Backing up ~/.bashrc..."
cp ~/.bashrc ~/.bashrc.backup
echo "✅ Backup created at ~/.bashrc.backup"

echo ""
echo "================================================"
echo "Cleanup Complete! ✨"
echo "================================================"
echo ""
echo "Next steps:"
echo "  1. Review the SETUP.md guide"
echo "  2. Follow the installation steps"
echo "  3. Set up your environment fresh"
echo ""
echo "Your ~/.bashrc has been backed up to ~/.bashrc.backup"
echo "You may want to manually remove CUDA/PYTHONPATH entries from ~/.bashrc"
echo ""
echo "Run: nano ~/.bashrc"
echo "Remove lines containing: CUDA, LD_LIBRARY_PATH, PYTHONPATH"
echo "Then run: source ~/.bashrc"
echo ""
