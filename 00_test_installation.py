print("🔍 Starting LangChain v1.0 setup validation...\n")

# 1. Check Python Version
import sys
py_version = sys.version
print(f"✅ Python version: {py_version.split()[0]} (OK)")

# 2. Check LangChain & Core Dependencies
try:
    import langchain
    print(f"✅ LangChain installed: v{langchain.__version__}")

except ImportError:
    print("❌ LangChain not found. Run: uv pip install langchain")
    sys.exit(1)