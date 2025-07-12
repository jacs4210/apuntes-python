# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al Curso de Python! Este documento te guiará a través del proceso de contribución.

## 📋 Tabla de Contenidos

- [Cómo Contribuir](#cómo-contribuir)
- [Tipos de Contribuciones](#tipos-de-contribuciones)
- [Estándares de Código](#estándares-de-código)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Reportar Bugs](#reportar-bugs)
- [Solicitar Features](#solicitar-features)

## 🚀 Cómo Contribuir

### 1. **Fork del Repositorio**
```bash
# Clona tu fork
git clone https://github.com/tu-usuario/curso-python.git
cd curso-python

# Agrega el repositorio original como upstream
git remote add upstream https://github.com/original-usuario/curso-python.git
```

### 2. **Crea una Rama**
```bash
# Crea una rama para tu contribución
git checkout -b feature/nueva-leccion
# o
git checkout -b fix/correccion-bug
```

### 3. **Haz tus Cambios**
- Sigue los estándares de código
- Agrega comentarios explicativos
- Incluye ejemplos prácticos
- Actualiza la documentación si es necesario

### 4. **Commit y Push**
```bash
git add .
git commit -m "feat: agregar nueva lección sobre decoradores"
git push origin feature/nueva-leccion
```

### 5. **Abre un Pull Request**
- Ve a GitHub y abre un Pull Request
- Describe claramente tus cambios
- Incluye ejemplos de uso si aplica

## 📝 Tipos de Contribuciones

### **🆕 Nuevas Lecciones**
- Conceptos que falten en el curso
- Ejemplos más claros de temas existentes
- Temas avanzados para estudiantes avanzados

### **🔧 Mejoras de Código**
- Optimización de ejemplos existentes
- Corrección de errores
- Mejora de la legibilidad

### **📚 Documentación**
- Mejorar comentarios en el código
- Actualizar README.md
- Agregar explicaciones teóricas

### **🎯 Ejercicios**
- Nuevos ejercicios prácticos
- Mejorar ejercicios existentes
- Agregar soluciones detalladas

### **🌍 Traducciones**
- Traducir contenido a otros idiomas
- Mejorar traducciones existentes

## 📏 Estándares de Código

### **Convenciones de Nomenclatura**
```python
# Variables y funciones: snake_case
nombre_variable = "valor"
def mi_funcion():
    pass

# Clases: PascalCase
class MiClase:
    pass

# Constantes: UPPER_SNAKE_CASE
PI = 3.14159
MAX_INTENTOS = 3
```

### **Comentarios**
```python
# Comentarios de una línea
def calcular_area(radio):
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): El radio del círculo
        
    Returns:
        float: El área del círculo
    """
    return PI * radio ** 2
```

### **Estructura de Archivos**
```python
"""
Título de la Lección

Descripción breve de lo que se aprenderá en esta lección.

Objetivos:
- Objetivo 1
- Objetivo 2
- Objetivo 3

Autor: Tu Nombre
Fecha: YYYY-MM-DD
"""

# Imports
import math

# Variables globales
CONSTANTE = 10

# Funciones
def ejemplo_funcion():
    """Ejemplo de función bien documentada."""
    pass

# Clases
class EjemploClase:
    """Ejemplo de clase bien documentada."""
    pass

# Código principal
if __name__ == "__main__":
    # Ejemplos de uso
    pass
```

## 🔄 Proceso de Pull Request

### **Antes de Abrir un PR**
- [ ] Tu código sigue los estándares
- [ ] Has probado tu código
- [ ] Has actualizado la documentación
- [ ] Has agregado tests si aplica

### **Template de Pull Request**
```markdown
## Descripción
Breve descripción de los cambios realizados.

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva lección
- [ ] Mejora de documentación
- [ ] Nuevo ejercicio
- [ ] Otro (especificar)

## Cambios Realizados
- Lista de cambios específicos

## Cómo Probar
1. Instrucciones para probar los cambios
2. Comandos a ejecutar
3. Resultados esperados

## Capturas de Pantalla (si aplica)
Agregar capturas si hay cambios visuales

## Checklist
- [ ] He leído y sigo las guías de contribución
- [ ] Mi código sigue los estándares del proyecto
- [ ] He probado mi código
- [ ] He actualizado la documentación
- [ ] Mis cambios no introducen nuevos bugs
```

## 🐛 Reportar Bugs

### **Antes de Reportar**
1. Busca en issues existentes
2. Verifica que el bug no haya sido reportado
3. Intenta reproducir el bug

### **Template de Bug Report**
```markdown
## Descripción del Bug
Descripción clara y concisa del bug.

## Pasos para Reproducir
1. Ve a '...'
2. Haz clic en '...'
3. Desplázate hacia abajo hasta '...'
4. Ve el error

## Comportamiento Esperado
Descripción de lo que debería pasar.

## Comportamiento Actual
Descripción de lo que está pasando.

## Capturas de Pantalla
Si aplica, agrega capturas.

## Información del Sistema
- OS: [ej. Windows 10, macOS, Ubuntu]
- Python Version: [ej. 3.8.5]
- Navegador: [ej. Chrome, Firefox]

## Información Adicional
Cualquier otra información relevante.
```

## 💡 Solicitar Features

### **Template de Feature Request**
```markdown
## Descripción del Feature
Descripción clara del feature que quieres.

## Problema que Resuelve
Explica qué problema resuelve este feature.

## Solución Propuesta
Describe la solución que propones.

## Alternativas Consideradas
Describe alternativas que consideraste.

## Información Adicional
Cualquier otra información relevante.
```

## 🏷️ Convenciones de Commits

Usa el formato de commits convencionales:

```bash
# Tipos de commits
feat: nueva lección sobre decoradores
fix: corregir error en ejercicio 15
docs: actualizar README con nueva información
style: mejorar formato del código
refactor: refactorizar función de cálculo
test: agregar tests para nueva lección
chore: actualizar dependencias
```

## 📞 Contacto

Si tienes preguntas sobre cómo contribuir:

- Abre un issue en GitHub
- Contacta al mantenedor del proyecto
- Únete a las discusiones en GitHub

## 🙏 Agradecimientos

¡Gracias por contribuir al Curso de Python! Tu ayuda hace que este recurso sea mejor para todos los estudiantes.

---

**Recuerda**: Cada contribución, sin importar qué tan pequeña sea, es valiosa para la comunidad. ¡Gracias por tu tiempo y esfuerzo! 