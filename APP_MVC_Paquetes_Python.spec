# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import copy_metadata

datas = [('resources', 'resources')]
binaries = []
hiddenimports = ['PIL._tkinter_finder', 'platformdirs', 'jaraco.text', 'importlib_resources', 'importlib_metadata', 'pkg_resources']
datas += copy_metadata('customtkinter')
datas += copy_metadata('packaging')
datas += copy_metadata('platformdirs')
hiddenimports += collect_submodules('pkg_resources')
tmp_ret = collect_all('customtkinter')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('PIL')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='APP_MVC_Paquetes_Python',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version_info.txt',
    icon=['C:\\Users\\Gonzalo\\Desktop\\2º DAM\\Sistemas de Gestión Empresarial\\Python\\InstitutoTKinter\\resources\\icons\\icono_exe.ico'],
)
