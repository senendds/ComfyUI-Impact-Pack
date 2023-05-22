import sys
import subprocess


def ensure_onnx_package():
    try:
        import onnxruntime
    except Exception:
        if "python_embeded" in sys.executable or "python_embedded" in sys.executable:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', 'onnxruntime'])
        else:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'onnxruntime'])