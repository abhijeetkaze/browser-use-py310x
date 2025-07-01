source .venv/bin/activate
uv pip uninstall browser-use-py310x
uv pip install /workspaces/browser-use/dist/browser_use_py310x-0.4.2-py3-none-any.whl --force-reinstall
pip show browser-use-py310x