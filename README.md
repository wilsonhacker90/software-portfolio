cat > README.md << 'EOF'
# Software de Portafolio PYQT6
## Sistema Avanzado de RFID

### Descripción
Este es un sistema que permite el acceso de personas y registro mediante un módulo RFID que se comunica con el software a través de puerto RS232.

### 🚀 Características
- Control de acceso por RFID
- Sistema de autenticación de usuarios
- Registro de eventos y accesos
- Interfaz desarrollada con PYQT6

### 📋 Requisitos
- Módulo RFID con interfaz RS232
- Python 3.x
- Librerías: PYQT6, pyserial

### 🔧 Instalación y Uso
1. **Conexión Hardware**: Conectar el módulo RFID via RS232-USB
2. **Configuración**: El software detecta automáticamente el puerto
3. **Autenticación**: 
   - Usuario por defecto: `wilson`
   - Contraseña por defecto: `1234`
4. **Seguridad**: Cambiar la contraseña después del primer acceso

### ⚠️ Importante
- Cambiar las credenciales por defecto después de la instalación
- Verificar la conexión del módulo RFID antes de usar
- El sistema reconoce automáticamente la llave RFID configurada
Autor wilsonhacker90
