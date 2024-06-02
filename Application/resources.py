from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Etudiant, Departement, Licence
from django.contrib.auth.models import User

class EtudiantResource(resources.ModelResource):
    matricule = fields.Field(attribute='user__username', column_name='matricule')
    nom = fields.Field(attribute='user__last_name', column_name='nom')
    prenom = fields.Field(attribute='user__first_name', column_name='prenom')
    departement = fields.Field(
        column_name='departement',
        attribute='departement',
        widget=ForeignKeyWidget(Departement, 'id')
    )
    licence = fields.Field(
        column_name='licence',
        attribute='licence',
        widget=ForeignKeyWidget(Licence, 'id')
    )

    class Meta:
        model = Etudiant
        exclude = ('id', 'user')  # Exclure le champ 'id' et 'user' de l'import/export
        import_id_fields = ('matricule',)
        fields = ('ine', 'pv', 'pere', 'mere', 'date_naissance', 'lieu_naissance', 'ecole_origine', 'departement', 'licence', 'genre', 'matricule', 'nom', 'prenom')

    def before_import_row(self, row, **kwargs):
        # Si vous avez besoin de prétraiter les lignes avant importation
        pass

    def save_instance(self, instance, using_transactions=True, dry_run=False):
        # Créer l'utilisateur associé
        user, created = User.objects.get_or_create(
            username=instance.user.username,
            defaults={
                'first_name': instance.user.first_name,
                'last_name': instance.user.last_name,
                'is_active': False,
                'password': 'CI2023@2024',
            }
        )
        if created:
            user.set_password('CI2023@2024')
            user.save()
        instance.user = user