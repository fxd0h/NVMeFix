#!/usr/bin/env python3
"""
Script para actualizar el config.plist de OpenCore con la nueva versión de NVMeFix
"""

import plistlib
import sys
import os

def update_config_plist(config_path):
    """Actualiza el config.plist con la nueva versión de NVMeFix"""
    
    # Leer el config.plist actual
    with open(config_path, 'rb') as f:
        config = plistlib.load(f)
    
    # Buscar NVMeFix en la sección Kernel > Add
    if 'Kernel' in config and 'Add' in config['Kernel']:
        for i, kext in enumerate(config['Kernel']['Add']):
            if kext.get('BundlePath') == 'NVMeFix.kext':
                # Actualizar la versión y comentario
                kext['Comment'] = 'V1.1.4 | NVMe Power Management Fix - WD SN750 Support'
                print(f"✅ Actualizado NVMeFix en posición {i}")
                break
    
    # Buscar Lilu en la sección Kernel > Add
    if 'Kernel' in config and 'Add' in config['Kernel']:
        for i, kext in enumerate(config['Kernel']['Add']):
            if kext.get('BundlePath') == 'Lilu.kext':
                # Actualizar la versión y comentario
                kext['Comment'] = 'V1.7.0 | Patching Engine - Updated'
                print(f"✅ Actualizado Lilu en posición {i}")
                break
    
    # Crear backup del config original
    backup_path = config_path + '.backup'
    with open(backup_path, 'wb') as f:
        plistlib.dump(config, f)
    print(f"📁 Backup creado: {backup_path}")
    
    # Escribir el config actualizado
    with open(config_path, 'wb') as f:
        plistlib.dump(config, f)
    
    print(f"✅ Config.plist actualizado: {config_path}")

if __name__ == '__main__':
    config_path = '/Volumes/EFI/EFI/OC/config.plist'
    
    if not os.path.exists(config_path):
        print(f"❌ Error: No se encontró {config_path}")
        sys.exit(1)
    
    try:
        update_config_plist(config_path)
        print("🎉 ¡Config.plist actualizado exitosamente!")
    except Exception as e:
        print(f"❌ Error actualizando config.plist: {e}")
        sys.exit(1)
