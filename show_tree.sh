#!/bin/bash

# Carpeta desde donde se ejecuta
BASE_DIR="."
# Archivo de salida (puedes cambiar .txt por .md si prefieres)
OUTPUT_FILE="estructura.md"

# Vaciar archivo de salida antes de escribir
echo "# 📁 Estructura de directorios en: $(pwd)" > "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Función recursiva para generar el árbol
print_tree() {
  local dir="$1"
  local prefix="$2"

  local items=("$dir"/*)
  local count=${#items[@]}
  local i=0

  for item in "${items[@]}"; do
    ((i++))
    local connector="├──"
    [ "$i" -eq "$count" ] && connector="└──"

    local name=$(basename "$item")
    echo "${prefix}${connector} $name" | tee -a "$OUTPUT_FILE"

    if [ -d "$item" ]; then
      local new_prefix="${prefix}"
      [ "$i" -eq "$count" ] && new_prefix+="    " || new_prefix+="│   "
      print_tree "$item" "$new_prefix"
    fi
  done
}

print_tree "$BASE_DIR"
echo -e "\n✅ Árbol exportado a: $OUTPUT_FILE"
