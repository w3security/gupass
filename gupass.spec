# -*- mode: python -*-

'''
PyInstaller build specification for building a stand-alone application
on the current platform
'''

import sys

block_cipher = None


a = Analysis(['pyinstaller_stub.py'],
             pathex=['.'],
             binaries=[],
             datas=[ ('gupass/data/*.txt', 'gupass/data' ),
                     ('gupass/data/*.psv', 'gupass/data' ),
                     ('gupass/icons/*.gif', 'gupass/icons') ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gupass' + ('.exe' if sys.platform == 'win32' else ''),
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='gupass/icons/gupass_icon.ico' )

if sys.platform == 'darwin':
    app = BUNDLE(exe,
                 name='gupass.app',
                 icon='gupass/icons/gupass-Icon-mac.icns',
                 info_plist={'NSHighResolutionCapable': 'True'},
                 bundle_identifier=None)