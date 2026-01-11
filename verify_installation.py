#!/usr/bin/env python3
"""
Environment Verification Script for Real-Time Object Detection
This script checks if all required components are installed correctly.
"""

import sys
import subprocess

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_status(check_name, status, message=""):
    """Print check status with emoji"""
    emoji = "✅" if status else "❌"
    print(f"{emoji} {check_name}: ", end="")
    if message:
        print(message)
    else:
        print("OK" if status else "FAILED")

def check_python_version():
    """Check Python version"""
    print_header("Python Version")
    version = sys.version.split()[0]
    major, minor = sys.version_info[:2]
    print(f"Python version: {version}")
    
    is_valid = (3, 7) <= (major, minor) <= (3, 8)
    print_status("Python 3.7-3.8", is_valid)
    return is_valid

def check_tensorflow():
    """Check TensorFlow installation and GPU support"""
    print_header("TensorFlow")
    try:
        import tensorflow as tf
        print(f"TensorFlow version: {tf.__version__}")
        print_status("TensorFlow installed", True)
        
        # Check GPU support
        gpus = tf.config.list_physical_devices('GPU')
        if gpus:
            print(f"GPU(s) detected: {len(gpus)}")
            for gpu in gpus:
                print(f"  - {gpu.name}")
            print_status("GPU support", True)
        else:
            print("No GPUs detected")
            print_status("GPU support", False, "No GPU found (CPU mode)")
        
        return True
    except ImportError:
        print_status("TensorFlow installed", False, "Not installed")
        return False
    except Exception as e:
        print_status("TensorFlow check", False, str(e))
        return False

def check_opencv():
    """Check OpenCV installation"""
    print_header("OpenCV")
    try:
        import cv2
        print(f"OpenCV version: {cv2.__version__}")
        print_status("OpenCV installed", True)
        return True
    except ImportError:
        print_status("OpenCV installed", False, "Not installed")
        return False
    except Exception as e:
        print_status("OpenCV check", False, str(e))
        return False

def check_cuda():
    """Check CUDA installation"""
    print_header("CUDA")
    try:
        result = subprocess.run(
            ['nvcc', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            # Extract version from output
            for line in result.stdout.split('\n'):
                if 'release' in line.lower():
                    print(line.strip())
            print_status("CUDA compiler (nvcc)", True)
            return True
        else:
            print_status("CUDA compiler (nvcc)", False, "Command failed")
            return False
    except FileNotFoundError:
        print_status("CUDA compiler (nvcc)", False, "Not found in PATH")
        return False
    except Exception as e:
        print_status("CUDA check", False, str(e))
        return False

def check_nvidia_gpu():
    """Check NVIDIA GPU with nvidia-smi"""
    print_header("NVIDIA GPU")
    try:
        result = subprocess.run(
            ['nvidia-smi'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            # Print first few lines of nvidia-smi output
            lines = result.stdout.split('\n')[:10]
            for line in lines:
                if line.strip():
                    print(line)
            print_status("NVIDIA GPU detected", True)
            return True
        else:
            print_status("NVIDIA GPU detected", False, "nvidia-smi failed")
            return False
    except FileNotFoundError:
        print_status("NVIDIA GPU detected", False, "nvidia-smi not found")
        return False
    except Exception as e:
        print_status("GPU check", False, str(e))
        return False

def check_protoc():
    """Check Protocol Buffers compiler"""
    print_header("Protocol Buffers")
    try:
        result = subprocess.run(
            ['protoc', '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(result.stdout.strip())
            print_status("protoc installed", True)
            return True
        else:
            print_status("protoc installed", False, "Command failed")
            return False
    except FileNotFoundError:
        print_status("protoc installed", False, "Not found in PATH")
        return False
    except Exception as e:
        print_status("protoc check", False, str(e))
        return False

def check_required_packages():
    """Check other required Python packages"""
    print_header("Required Python Packages")
    packages = {
        'numpy': 'numpy',
        'matplotlib': 'matplotlib',
        'pillow': 'PIL',
        'lxml': 'lxml',
        'jupyter': 'jupyter',
    }
    
    all_ok = True
    for name, import_name in packages.items():
        try:
            import importlib
            module = importlib.import_module(import_name)
            version = getattr(module, '__version__', 'unknown')
            print_status(f"{name}", True, f"v{version}")
        except ImportError:
            print_status(f"{name}", False, "Not installed")
            all_ok = False
    
    return all_ok

def check_object_detection_api():
    """Check TensorFlow Object Detection API"""
    print_header("TensorFlow Object Detection API")
    try:
        # Try to import from object_detection
        from object_detection.utils import label_map_util
        print_status("Object Detection API", True)
        return True
    except ImportError:
        print_status("Object Detection API", False, "Not installed or not in PYTHONPATH")
        print("\nTo install:")
        print("  1. git clone https://github.com/tensorflow/models")
        print("  2. cd models/research")
        print("  3. protoc object_detection/protos/*.proto --python_out=.")
        print("  4. cp object_detection/packages/tf2/setup.py .")
        print("  5. python -m pip install .")
        return False
    except Exception as e:
        print_status("Object Detection API", False, str(e))
        return False

def main():
    """Run all checks"""
    print("\n")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   Real-Time Object Detection Environment Verification   ║")
    print("╚══════════════════════════════════════════════════════════╝")
    
    checks = [
        ("Python", check_python_version),
        ("TensorFlow", check_tensorflow),
        ("OpenCV", check_opencv),
        ("CUDA", check_cuda),
        ("NVIDIA GPU", check_nvidia_gpu),
        ("Protocol Buffers", check_protoc),
        ("Python Packages", check_required_packages),
        ("Object Detection API", check_object_detection_api),
    ]
    
    results = {}
    for name, check_func in checks:
        try:
            results[name] = check_func()
        except Exception as e:
            print(f"\n❌ Error checking {name}: {e}")
            results[name] = False
    
    # Summary
    print_header("Summary")
    passed = sum(results.values())
    total = len(results)
    
    print(f"\nPassed: {passed}/{total} checks")
    print()
    
    if passed == total:
        print("🎉 All checks passed! Your environment is ready.")
        print("\nNext steps:")
        print("  1. Clone the repository: git clone https://github.com/tja111/RealTimeObjectDetection")
        print("  2. Navigate to the project: cd RealTimeObjectDetection")
        print("  3. Run the tutorial: jupyter notebook Tutorial.ipynb")
    else:
        print("⚠️  Some checks failed. Please review the output above.")
        print("\nFailed checks:")
        for name, status in results.items():
            if not status:
                print(f"  - {name}")
        print("\nRefer to SETUP.md for installation instructions.")
    
    print()
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
