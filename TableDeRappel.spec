# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec pour Table de Rappel — génère un .app macOS

import re

block_cipher = None

# Lire VERSION depuis le code source
with open('quiz_rappel_gui.py', encoding='utf-8') as f:
    _v = re.search(r'VERSION\s*=\s*"([^"]+)"', f.read())
    APP_VERSION = _v.group(1) if _v else '0.0.0'

a = Analysis(
    ['quiz_rappel_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('TableDeRappel_icon.png', '.')],
    hiddenimports=['PIL', 'PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Table de Rappel',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Table de Rappel',
)

# Bundle macOS avec version dans Info.plist (CFBundleShortVersionString)
app = BUNDLE(
    coll,
    name='Table de Rappel.app',
    icon='TableDeRappel.icns',
    bundle_identifier='com.TableDeRappel.app',
    version=APP_VERSION,
    info_plist={
        'CFBundleShortVersionString': APP_VERSION,
        'CFBundleVersion': APP_VERSION,
        'NSPrincipalClass': 'NSApplication',
        'NSHighResolutionCapable': True,
    },
)
