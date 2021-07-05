# -*- mode: python -*-

block_cipher = None


a = Analysis(['/media/maddocks/usb3tb/vial-gui/src/main/python/main.py'],
             pathex=['/media/maddocks/usb3tb/vial-gui/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/usr/local/lib/python3.8/dist-packages/fbs/freeze/hooks'],
             runtime_hooks=['/media/maddocks/usb3tb/vial-gui/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Vial',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Vial')
