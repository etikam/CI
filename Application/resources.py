from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User
from .models import Etudiant, Departement, Licence

class EtudiantResource(resources.ModelResource):
    username = fields.Field(
        column_name='username',
        attribute='user',
        widget=ForeignKeyWidget(User, 'username')
    )

    class Meta:
        model = Etudiant
        fields = ('ine', 'pv', 'username', 'pere', 'mere', 'date_naissance', 
                  'lieu_naissance', 'ecole_origine', 'genre', 'departement', 'licence')
        import_id_fields = ('ine',)  # Assurez-vous d'utiliser un champ unique pour identifier les enregistrements
        exclude = ('id',)  # Exclure le champ ID

    def before_import_row(self, row, **kwargs):
        username = row.get('username')
        first_name = row.get('first_name')
        last_name = row.get('last_name')
        
        if username:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=False,
                )
                user.set_password('CI2023@2024')
                user.save()
            row['user'] = user.pk

    def dehydrate_genre(self, obj):
        return 'Homme' if obj.genre else 'Femme'
