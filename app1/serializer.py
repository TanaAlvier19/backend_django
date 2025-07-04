from rest_framework import serializers
class FieldDefinitionSerializer(serializers.Serializer):
    name = serializers.RegexField(
        regex=r'^[a-zA-Z_][a-zA-Z0-9_]*$',
        max_length=64,
        error_messages={
            'invalid': 'Field names must start with a letter or underscore and contain only letters, numbers and underscores'
        }
    )

    type = serializers.ChoiceField(choices=[
        'serial', 'integer','int', 'bigint', 'varchar', 'text',
        'numeric', 'decimal', 'float', 'double precision',
        'boolean', 'date', 'timestamp', 'json', 'jsonb'
    ])

    length = serializers.IntegerField(required=False, min_value=1, max_value=65535)
    constraints = serializers.CharField(required=False, max_length=255, allow_blank=True)

class CreateTableSerializer(serializers.Serializer):
    table_name = serializers.RegexField(
        regex=r'^[a-zA-Z_][a-zA-Z0-9_]*$',
        max_length=64,
        error_messages={
            'invalid': 'Table names must start with a letter or underscore and contain only letters, numbers and underscores'
        }
    )

    fields = serializers.ListField(
        child=FieldDefinitionSerializer(),
        min_length=1
    )

    def validate_fields(self, value):
        has_primary = any(
            'PRIMARY KEY' in field.get('constraints', '').upper()
            for field in value
        )
        if not has_primary:
            raise serializers.ValidationError("The table must have at least one PRIMARY KEY field")
        return value
