from rest_framework import serializers

class TextEntrySerializer(serializers.Serializer):
     entry = serializers.CharField(
        required=True,          # obliga a que siempre venga en la petición
        allow_blank=False,      # no se acepta cadena vacía
        min_length=5,           # longitud mínima automática
        max_length=500,         # longitud máxima automática
        trim_whitespace=True,   # recorta espacios al inicio/fin
    )

     def validate(self, attrs):
        text = attrs.get('entry', '')
        # Verifica que haya al menos 3 palabras (2 espacios)
        if text.count(' ') < 2:
        # Retorna error asociado al campo 'entry'
            raise serializers.ValidationError({ 
                'entry': 'Debe contener al menos 3 palabras.' 
            })
        return attrs